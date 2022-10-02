from time import sleep
import azapi
import pandas as pd
import lyricsgenius

genius = lyricsgenius.Genius()
genius.retries = 3


def get_lyrics(artist: str, song: str):
    print(f'Getting lyrics for {artist} - {song}')

    song = genius.search_song(song, artist)

    if song is None:
        return ""

    return song.lyrics


def get_lyrics_for_charts(chart: pd.DataFrame, cooldown: float):
    chart_with_lyrics = chart.copy()

    # drop duplicates to avoid unnecessary API calls
    unique_songs = chart_with_lyrics[['artist', 'title']].drop_duplicates()

    for _, row in unique_songs.iterrows():
        artist = row['artist']
        song = row['title']

        lyrics = get_lyrics(artist, song)

        chart_with_lyrics.loc[(chart_with_lyrics['artist'] == artist) & (
            chart_with_lyrics['title'] == song), 'lyrics'] = lyrics

        sleep(cooldown)

    # remap lyrics, artist, title to original chart
    chart_with_lyrics = chart_with_lyrics.merge(
        unique_songs, on=['artist', 'title'], how='left')

    return chart_with_lyrics
