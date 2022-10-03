
from matplotlib import pyplot as plt


def plot_top_20_artist_histogram(df):
    df = df[df['artist'].isin(df['artist'].value_counts().head(20).index)]

    plt.figure(figsize=(20, 10))
    plt.title('Top 20 Artists Histogram', fontsize=20)
    plt.xlabel('Artist', fontsize=15)
    plt.ylabel('Count', fontsize=15)

    plt.xticks(rotation=45)
    plt.bar(df['artist'].value_counts().index,
            df['artist'].value_counts().values)
    plt.show()
