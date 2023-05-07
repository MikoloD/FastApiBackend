import json

class Song:
    def __init__(self, artist, name):
        self.artist = artist
        self.name = name

def obj_dict(obj):
    return obj.__dict__

def getSongsData():
    with open("song_info.json", 'r') as f:
        songs = json.load(f)
    songs = {int(k): v for k, v in songs.items()}
    return songs

def getSongsProps(songs):
    songsResult = []
    for id in songs:
        track_name = songs[id]['track_name']
        artist_name = songs[id]['artist_name']
        songsResult.append(Song(artist_name,track_name))
    return songsResult

def getSongsForSeachBar():
    songs = getSongsData()
    return getSongsProps(songs)