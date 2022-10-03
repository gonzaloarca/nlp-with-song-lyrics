import argparse
from concurrent.futures import ThreadPoolExecutor
from threading import Lock
from time import sleep

import pandas as pd

from .lyrics_getter.lyrics_getter import get_lyrics_for_charts
from .charts_getter.charts_getter import get_chart_in_range

csv_lock = Lock()


def parse_args():
    parser = argparse.ArgumentParser(
        description='Scrape Billboard charts together with their lyrics within a given date range.')
    parser.add_argument('--chart', help='Chart to scrape',
                        type=str, default='hot-100')
    parser.add_argument(
        '--trim', help='Trim chart to top N entries', type=int, default=100)
    parser.add_argument('--start', help='Start date of the range', type=str)
    parser.add_argument('--end', help='End date of the range', type=str)
    parser.add_argument(
        '--freq', help='Frequency of the date range', type=str)
    parser.add_argument('--output', help='Output file',
                        type=str, default='charts.csv')
    parser.add_argument(
        '--billboard_cooldown', help='Cooldown between Billboard API calls', type=float, default=1)
    parser.add_argument(
        '--lyrics_cooldown', help='Cooldown between Lyrics API calls', type=float, default=0)
    parser.add_argument(
        '--thread_count', help='Number of threads to use', type=int, default=10)

    return parser.parse_args()


def validate_args(args):
    # exactly three of start, end, periods, freq must be specified
    if args.start is None:
        raise ValueError('Start date must be specified')
    if args.end is None:
        raise ValueError('End date must be specified')
    if args.freq is None:
        raise ValueError('Frequency must be specified')


def write_header(output):
    with open(output, 'w') as f:
        f.write(
            'rank,title,artist,weeks,is_new,date,lyrics,matched_title,matched_artist,timeout\n')


def get_data(charts, output, lyrics_cooldown, thread_id=0):

    print(f'Got {len(charts)} songs')

    charts_with_lyrics = get_lyrics_for_charts(
        charts, lyrics_cooldown, thread_id)

    with csv_lock:
        print(
            f'Writing {len(charts_with_lyrics)} songs to {output} from thread {thread_id}')
        charts_with_lyrics.to_csv(
            output, index=False, mode='a', header=False)


def set_up_scraping_threads(chart, output, start, end, freq, billboard_cooldown, lyrics_cooldown, trim, thread_count):
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        thread_dates = pd.date_range(start, end, periods=thread_count+1)

        for i in range(thread_count):
            start_date = thread_dates[i].strftime('%Y-%m-%d')
            end_date = thread_dates[i+1].strftime('%Y-%m-%d')

            # get chart data sequentially
            charts = get_chart_in_range(
                chart, start_date, end_date, freq, billboard_cooldown, trim)

            print(
                f'Starting thread {i} with start date {start_date} and end date {end_date}')

            executor.submit(get_data, charts, output, lyrics_cooldown, i)

            sleep(billboard_cooldown)


if __name__ == '__main__':
    args = parse_args()
    print(args)

    validate_args(args)

    write_header(args.output)

    set_up_scraping_threads(args.chart, args.output, args.start, args.end,
                            args.freq, args.billboard_cooldown, args.lyrics_cooldown, args.trim, args.thread_count)

    # get_data(args.chart, args.output, args.start, args.end, args.periods,
    #  args.freq, args.billboard_cooldown, args.lyrics_cooldown, args.trim)
