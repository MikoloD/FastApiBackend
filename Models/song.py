
class Model:
    def __init__(self, artist, name, songId, spotifyUri):
        self.artist = artist
        self.name = name
        self.songId = songId
        self.spotifyUri = spotifyUri
    def UriReplace(self):
        self.spotifyUri = self.spotifyUri.replace("spotify", "spotify" + ".com")
        self.spotifyUri = 'https://open.'+ self.spotifyUri.replace(":", "/")

def encode(self):
    return self.__dict__
