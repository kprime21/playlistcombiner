import requests
from bs4 import BeautifulSoup
import re



# get beautiful soup link
def Soupify(link):
    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'html.parser')
    return soup


# check if it is link to playlist or link to playlist in videos and get id for playlist
def checkYoutubeLink(link):
    playlistResult = re.findall(
        r'www.youtube.com\/(playlist|watch).*?[\?|&]list=([^&\v]*)', link)

    if(playlistResult[0][0] == 'watch'):
        link = 'https://www.youtube.com/playlist?list=' + playlistResult[0][1]
    return link


# titles of youtube videos
def youtubeGetSongs(soup):
    youtubeSongs = re.findall(
        r'"playlistVideoRenderer":.*?"text":"(.*?)"}]', str(soup))
    return youtubeSongs

def youtubeGetLinks(soup,link):
    youtubeLinks = []
    # get video id
    youtubeId = re.findall(
        r'"playlistVideoRenderer":.*?"videoId":"(.*?)"', str(soup))

    #use to check if it is playlist or video
    playlistResult = re.findall(
        r'www.youtube.com\/(playlist|watch).*?[\?|&]list=([^&\v]*)', link)

    index = 0
    for i in youtubeId:
        index+=1
        linkInsert = 'https://www.youtube.com/watch?v=' + \
            str(i) + '&list=' + \
            playlistResult[0][1] + '&index=' + str(index)    
        youtubeLinks.append(linkInsert)
    return youtubeLinks

        




# spotify - get songs  ( spotify only limits to 100 songs per playlist)


# scrape html and get all artists + songs
def spotifyGetSongs(soup):
    spotifySongs = []
    artists = []
    artistsForSong = []
    songIndex = -1
    songs = []
    for values in soup.find_all('a'):
        # match songs to the correct artists
        if(bool(re.search(r'<a class="EntityRowV2__Link-sc-ayafop-8 eWYxOj"', str(values)))):
            songs.append(values.text)
            if(songIndex >= 0):
                artists.append(artistsForSong)
                artistsForSong = []
            songIndex += 1

        elif(bool(re.search(r'<a href="\/artist\/', str(values)))):
            artistsForSong.append(values.text)
    artists.append(artistsForSong)
    songIndex+=1

    for x in range(songIndex):
        a = ""
        for j in artists[x]:
            a += j + " "
            spotifySongs.append(a + " - " + songs[x])

    return spotifySongs

# scrape html for spotify links

def spotifyGetLinks(soup):
    spotifyLinks = []
    for value in soup.find_all('a', {'href': re.compile(r'(https:\/\/open.spotify.com\/track\/\w*)')}):
        spotifyLinks.append(value['href'])
    return spotifyLinks


def Youtube(link):
    youtubeSongsAndLinks = []
    youtubeLink = checkYoutubeLink(link)
    youtubeSongsAndLinks.append(youtubeGetSongs(youtubeLink))
    youtubeSongsAndLinks.append(youtubeGetLinks(Soupify(youtubeLink),youtubeLink))

    return youtubeSongsAndLinks

def Spotify(link):
    spotifySongsAndLinks = []
    spotifyLink = Soupify(link)
    spotifySongsAndLinks.append(spotifyGetSongs(spotifyLink))
    spotifySongsAndLinks.append(spotifyGetLinks(spotifyLink))

    return spotifySongsAndLinks
    
Youtube('https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1')
Spotify('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')



# test links

#https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020
#https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1
#https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL


# get link to thumbnail image
#youtubeidcovers = re.findall(r'{"playlistVideoRenderer":{"videoId":"(.*?)","thumbnail":{"thumbnails":\[{"url":"(.*?)"',str(soup2))