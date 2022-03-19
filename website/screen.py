from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from .models import musiclist
from .playlistcombine import Youtube,Spotify
from . import db

screen = Blueprint('screen', __name__)

@screen.route("/view")
def view():
    return render_template("view.html",values=musiclist.query.all())

@screen.route("/", methods=["POST", "GET"])
def home():
    # get the values entered in form
    if request.method == "POST":
        title = request.form["pltl"]
        youtube = request.form["yt"]
        spotify = request.form["sp"]
        

        # check if there exists a combined playlist already
        found_list = musiclist.query.filter_by(
            youtubePlaylist=youtube, spotifyPlaylist=spotify).first()

        if(found_list):
            print("already exists a playlist with " + title)

        else:
            musicl = musiclist(title, youtube, spotify)
            db.session.add(musicl)
            db.session.commit()
        

        youtubeData = Youtube(youtube)
        spotifyData = Spotify(spotify)

        return render_template("music.html", title=title, youtube=youtube, spotify=spotify, \
            youtubeSongs = youtubeData[0], youtubeSongLinks = youtubeData[1], \
            spotifySongs = spotifyData[0], spotifyLinks = spotifyData[1])
    else:
        return render_template("index.html")


