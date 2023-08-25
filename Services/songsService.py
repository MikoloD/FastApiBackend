from Models import song
from Data import dataProvider


def getSongsProps(songs):

    songsResult = []
    for id in songs:
        track_name = songs[id]['track_name']
        artist_name = songs[id]['artist_name']
        spotify_uri = songs[id]['track_uri']
        addedSong = song.Model(artist_name, track_name, id,spotify_uri)
        addedSong.UriReplace()
        songsResult.append(addedSong)
    return songsResult


def getSongsForSeachBar(path):
    songs = dataProvider.getSongsData(path)
    return getSongsProps(songs)
