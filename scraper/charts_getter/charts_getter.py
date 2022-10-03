import json
from time import sleep
import billboard
from datetime import datetime
import pandas as pd
from ..utils import normalize_string

DATE_FORMAT = '%Y-%m-%d'
TIMEOUT = 20


def normalize_chart_entry(chart_entry: dict):
    normalized_entry = {}

    for key in chart_entry.keys():
        if type(chart_entry[key]) == str:
            normalized_entry[key] = normalize_string(chart_entry[key])
        else:
            normalized_entry[key] = chart_entry[key]

    return normalized_entry


def get_chart(chart, date):
    print(f'Getting chart for {date}')

    try:
        chart_data = billboard.ChartData(
            chart, date=date, timeout=TIMEOUT).entries
    except:
        print(f'Error getting chart for {date}')
        return []

    print(f'Got {len(chart_data)} entries for {date}')

    norm_data = [normalize_chart_entry(
        json.loads(entry.json())) for entry in chart_data]

    # add date column to each entry
    for entry in norm_data:
        entry['date'] = date

    return norm_data


def get_chart_in_range(chart: str, start_date: str, end_date: str, periods: int, freq: str, cooldown: float, trim: int):
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)

    date_range = pd.date_range(
        start_date, end_date, periods=periods, freq=freq, inclusive="left")

    charts = pd.DataFrame()

    for date in date_range:
        date_str = date.strftime(DATE_FORMAT)
        chart_data = get_chart(chart, date_str)
        chart_df = pd.DataFrame(chart_data)

        # trim chart to top n entries
        chart_df = chart_df.head(trim)

        charts = pd.concat([charts, chart_df])

        sleep(cooldown)

    return charts
