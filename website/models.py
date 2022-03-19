from . import db
from sqlalchemy.sql import func


class musiclist(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    playlistTitle = db.Column(db.String(100))
    youtubePlaylist = db.Column(db.String(100))
    spotifyPlaylist = db.Column(db.String(100))
    
    def __init__(self, playlistTitle, youtubePlaylist, spotifyPlaylist):
        self.playlistTitle = playlistTitle
        self.youtubePlaylist = youtubePlaylist
        self.spotifyPlaylist = spotifyPlaylist