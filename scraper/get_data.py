import argparse

from .lyrics_getter.lyrics_getter import get_lyrics_for_charts
from .charts_getter.charts_getter import get_chart_in_range


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
        '--periods', help='Number of periods to generate', type=int)
    parser.add_argument(
        '--freq', help='Frequency of the date range', type=str)
    parser.add_argument('--output', help='Output file',
                        type=str, default='charts.csv')
    parser.add_argument(
        '--billboard_cooldown', help='Cooldown between Billboard API calls', type=float, default=1)
    parser.add_argument(
        '--lyrics_cooldown', help='Cooldown between Lyrics API calls', type=float, default=0)

    return parser.parse_args()


def validate_args(args):
    # exactly three of start, end, periods, freq must be specified
    if sum([args.start is not None, args.end is not None, args.periods is not None, args.freq is not None]) != 3:
        raise ValueError(
            'Exactly three of start, end, periods, freq must be specified')


if __name__ == '__main__':
    args = parse_args()
    print(args)

    validate_args(args)

    charts = get_chart_in_range(
        args.chart, args.start, args.end, args.periods, args.freq, args.billboard_cooldown)

    charts_with_lyrics = get_lyrics_for_charts(charts, args.lyrics_cooldown)

    charts_with_lyrics.to_csv(args.output, index=False)
