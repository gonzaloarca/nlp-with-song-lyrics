import pandas as pd

from .classification.count_vectorizer import get_cv_stats

from .visualizations.artist_histogram import plot_top_20_artist_histogram

from .visualizations.word_clouds import plot_holidays_word_cloud_lyrics, plot_full_word_cloud_lyrics, plot_non_holidays_word_cloud_lyrics, plot_holidays_word_cloud_title, plot_full_word_cloud_title, plot_non_holidays_word_cloud_title


if __name__ == "__main__":
    df = pd.read_csv('data_examples/corpus.csv')

    print(df.head())

    print(df['lyrics'].head())

    # change lyrics and title columns to string types
    df['lyrics'] = df['lyrics'].astype(str)
    df['title'] = df['title'].astype(str)
    df['artist'] = df['artist'].astype(str)

    vocab, vocab_len, feature_names, doc_freq, doc_freq_sum = get_cv_stats(
        df, 'lyrics')

    print(f"Vocabulary: {vocab}")
    print(f"Vocabulary length: {vocab_len}")
    print(f"Feature names: {feature_names}")
    print(f"Document frequency: {doc_freq}")
    print(f"Document frequency sum: {doc_freq_sum}")

    vocab, vocab_len, feature_names, doc_freq, doc_freq_sum = get_cv_stats(
        df, 'title')

    print(f"Vocabulary: {vocab}")
    print(f"Vocabulary length: {vocab_len}")
    print(f"Feature names: {feature_names}")
    print(f"Document frequency: {doc_freq}")
    print(f"Document frequency sum: {doc_freq_sum}")

    plot_top_20_artist_histogram(df)

    # plot_holidays_word_cloud_lyrics(df)
    # plot_full_word_cloud_title(df)
    # plot_full_word_cloud_lyrics(df)
    # plot_non_holidays_word_cloud_lyrics(df)
    # plot_holidays_word_cloud_title(df)
    # plot_non_holidays_word_cloud_title(df)
