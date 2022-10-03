from time import sleep
import pandas as pd
import lyricsgenius
from ..utils import normalize_string
from progress.bar import Bar

genius = lyricsgenius.Genius(verbose=False)
genius.retries = 3


def get_lyrics(artist: str, song: str):
    # print(
    #     f'Getting lyrics for {artist} - {song} ({rank})')

    song = genius.search_song(song, artist)

    if song is None:
        return ""

    return normalize_string(song.lyrics)


def get_lyrics_for_charts(chart: pd.DataFrame, cooldown: float, thread_id=0):
    chart_with_lyrics = chart.copy()

    # drop duplicates to avoid unnecessary API calls
    unique_songs = chart_with_lyrics.drop_duplicates(
        subset=['artist', 'title'])

    bar = Bar(f'Getting lyrics from thread {thread_id}', max=len(unique_songs))

    for _, row in unique_songs.iterrows():
        artist = row['artist']
        song = row['title']

        lyrics = get_lyrics(artist, song)

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == song), 'lyrics'] = lyrics

        bar.next()
        sleep(cooldown)

    return chart_with_lyrics
