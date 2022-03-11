import requests
from bs4 import BeautifulSoup
import re


# test youtube links

#https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020
#https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1
#https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL

link = input("Enter youtube playlist link ex-https://www.youtube.com/playlist?list=PLau9bkm0iK9t1DPKultYqH3q8yWpg-SvR : ")

link2 = input("Enter spotify playlist link ex-https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL : ")

# check if it is link to playlist or link to playlist in videos and get id for playlist
playlistResult = re.findall(
    r'www.youtube.com\/(playlist|watch).*?[\?|&]list=([^&\v]*)', link)

if(playlistResult[0][0] == 'watch'):
    link = 'https://www.youtube.com/playlist?list=' + playlistResult[0][1]




# youtube - get songs and covers

data2 = requests.get(link)
soup2 = BeautifulSoup(data2.text, 'html.parser')

# titles of youtube videos
youtubetitles = re.findall(
    r'"playlistVideoRenderer":.*?"text":"(.*?)"}]', str(soup2))
# get video id
youtubelinks = re.findall(
    r'"playlistVideoRenderer":.*?"videoId":"(.*?)"', str(soup2))
# get link to thumbnail image
#youtubeidcovers = re.findall(r'{"playlistVideoRenderer":{"videoId":"(.*?)","thumbnail":{"thumbnails":\[{"url":"(.*?)"',str(soup2))

for i in range(len(youtubetitles)):
    print(youtubetitles[i])
    linkInsert = 'https://www.youtube.com/watch?v=' + \
        str(youtubelinks[i]) + '&list=' + \
        playlistResult[0][1] + '&index=' + str(i+1)
    print(linkInsert)


# spotify - get songs  ( spotify only limits to 100 songs per playlist)

data = requests.get(link2)
soup = BeautifulSoup(data.text, 'html.parser')

# hold results
artists = []
artistsForSong = []
songIndex = -1
songs = []
covers = []
spotifyLink = []

# scrape html and get all <a> tags of songs and artists
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

# scrape html and get href of spotify links
for value in soup.find_all('a', {'href': re.compile(r'(https:\/\/open.spotify.com\/track\/\w*)')}):
    spotifyLink.append(value['href'])


# print values
for x in range(songIndex):
    a = ""
    for j in artists[x]:
        a += j + " "
    print(a + " - " + songs[x] + "\n"+spotifyLink[x])
