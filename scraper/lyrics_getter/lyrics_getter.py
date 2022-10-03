from time import sleep
import pandas as pd
import lyricsgenius
from ..utils import normalize_string
from progress.bar import Bar

genius = lyricsgenius.Genius(verbose=False, remove_section_headers=True)
genius.retries = 3


def get_lyrics_api_match(artist: str, song: str):
    # print(
    #     f'Getting lyrics for {artist} - {song} ({rank})')

    try:
        song = genius.search_song(song, artist, get_full_info=False)
    except:
        print(f'Error getting lyrics for {artist} - {song}')
        return '', '', '', True

    if song is None:
        return '', '', '', False

    return normalize_string(song.lyrics), normalize_string(song.title), normalize_string(song.artist), False


def get_lyrics_for_charts(chart: pd.DataFrame, cooldown: float, thread_id=0):
    chart_with_lyrics = chart.copy()

    # drop duplicates to avoid unnecessary API calls
    unique_songs = chart_with_lyrics.drop_duplicates(
        subset=['artist', 'title'])

    bar = Bar(f'Getting lyrics from thread {thread_id}', max=len(unique_songs))

    for _, row in unique_songs.iterrows():
        artist = row['artist']
        title = row['title']

        lyrics, matched_artist, matched_title, timeout = get_lyrics_api_match(
            artist, title)

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == title), 'lyrics'] = lyrics

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == title), 'matched_artist'] = matched_artist

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == title), 'matched_title'] = matched_title

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == title), 'timeout'] = timeout

        bar.next()
        sleep(cooldown)

    return chart_with_lyrics
