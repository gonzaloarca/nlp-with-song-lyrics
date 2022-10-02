import json
import billboard
from datetime import datetime
import pandas as pd

DATE_FORMAT = '%Y-%m-%d'


def scrape_charts(chart, date):
    chart_data = billboard.ChartData(chart, date=date).entries

    dict_data = [json.loads(entry.json()) for entry in chart_data]

    # add date column to each entry
    for entry in dict_data:
        entry['date'] = date

    return dict_data


def scrape_chart_in_range(chart, start_date, end_date, periods, freq):
    start_date = datetime.strptime(start_date, DATE_FORMAT)
    end_date = datetime.strptime(end_date, DATE_FORMAT)
    date_range = pd.date_range(
        start_date, end_date, periods=periods, freq=freq)

    charts = pd.DataFrame()

    for date in date_range:
        date_str = date.strftime(DATE_FORMAT)
        chart_data = scrape_charts(chart, date_str)

        chart_df = pd.DataFrame(chart_data)
        charts = pd.concat([charts, chart_df])

    return charts