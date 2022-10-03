

import itertools
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import string
import nltk
nltk.download('punkt')

stopwords = set(map(lambda s: s.translate(
    s.maketrans('', '', string.punctuation)), STOPWORDS))


def plot_word_cloud(words, title, stopwords_set):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords_set,
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=1
    ).generate(' '.join(words))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    plt.title(title, fontsize=20)
    plt.imshow(wordcloud)
    plt.show()


def tokenize_and_normalize(str):
    str = str.lower()
    str = str.translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(str)

    return [token for token in tokens if token.isalpha()]


def plot_holidays_word_cloud_lyrics(df):
    holiday_df = df[df['date'].str.contains('12-31')]
    print(len(holiday_df))

    lyrics = holiday_df[['lyrics']].values
    plot_title = 'Winter Holidays Word Cloud (Lyrics)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(lyric[0])
                                                for lyric in lyrics]))

    plot_word_cloud(words, plot_title, stopwords)


def plot_full_word_cloud_lyrics(df):
    lyrics = df[['lyrics']].values
    print(len(lyrics))
    plot_title = 'General Word Cloud (Lyrics)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(lyric[0])
                                                for lyric in lyrics]))

    plot_word_cloud(words, plot_title, stopwords)


def plot_non_holidays_word_cloud_lyrics(df):
    df = df[~df['date'].str.contains('12-31')]
    print(len(df))

    lyrics = df[['lyrics']].values
    plot_title = 'Non-Holiday Word Cloud (Lyrics)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(lyric[0])
                                                for lyric in lyrics]))

    plot_word_cloud(words, plot_title, stopwords)


def plot_holidays_word_cloud_title(df):
    holiday_df = df[df['date'].str.contains('12-31')]
    print(len(holiday_df))
    titles = holiday_df[['title']].values
    plot_title = 'Winter Holidays Word Cloud (Title)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(title[0])
                                                for title in titles]))

    plot_word_cloud(words, plot_title, stopwords)


def plot_full_word_cloud_title(df):
    titles = df[['title']].values

    plot_title = 'General Word Cloud (Title)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(title[0])
                                                for title in titles]))

    plot_word_cloud(words, plot_title, stopwords)


def plot_non_holidays_word_cloud_title(df):
    df = df[~df['date'].str.contains('12-31')]
    titles = df[['title']].values
    plot_title = 'Non-Holiday Word Cloud (Title)'

    words = list(itertools.chain.from_iterable([tokenize_and_normalize(title[0])
                                                for title in titles]))

    plot_word_cloud(words, plot_title, stopwords)
