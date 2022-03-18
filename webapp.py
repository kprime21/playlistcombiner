from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


# FLASK
app = Flask(__name__)
app.secret_key = "hello"
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///musiclist.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# model for the playlist


class musiclist(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    playlistTitle = db.Column(db.String(100))
    youtubePlaylist = db.Column(db.String(100))
    spotifyPlaylist = db.Column(db.String(100))

    def __init__(self, playlistTitle, youtubePlaylist, spotifyPlaylist):
        self.playlistTitle = playlistTitle
        self.youtubePlaylist = youtubePlaylist
        self.spotifyPlaylist = spotifyPlaylist

@app.route("/view")
def view():
    return render_template("view.html",values=musiclist.query.all())

@app.route("/", methods=["POST", "GET"])
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

        return render_template("music.html", title=title, youtube=youtube, spotify=spotify)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
