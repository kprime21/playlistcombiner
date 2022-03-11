import requests
from bs4 import BeautifulSoup
import re

import spotipy
from spotipy.oauth2 import SpotifyOAuth


#test youtube links

link = 'https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020'
link2 = 'https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1'

#check if it is link to playlist or link to playlist in videos and get id for playlist
playlistResult = re.findall(r'www.youtube.com\/(.*?)[\?|&]list=([^&\v]*)',link)



#youtube

data2 = requests.get('https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020')
soup2 = BeautifulSoup(data2.text, 'html.parser')

#titles of youtube videos
youtubetitles = re.findall(r'"playlistVideoRenderer":.*?"text":"(.*?)"}]', str(soup2))
#get video id
youtubelinks = re.findall(r'"playlistVideoRenderer":.*?"videoId":"(.*?)"', str(soup2))
#get link to thumbnail image
youtubeidcovers = re.findall(r'{"playlistVideoRenderer":{"videoId":"(.*?)","thumbnail":{"thumbnails":\[{"url":"(.*?)"',str(soup2))

for i in range(len(youtubetitles)):
    print(youtubetitles[i])
    linkInsert = 'https://www.youtube.com/watch?v=' + str(youtubelinks[i]) + '&list=' + playlistResult[0][1] + '&index=' + str(i+1) 
    print("link: " + linkInsert + "\n" + "cover: " + str(youtubeidcovers[i][1]))





#spotify music ( spotify only limits to 100 so changes need to be made)

data = requests.get('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')
soup = BeautifulSoup(data.text, 'html.parser')

#hold results
artists = []
artistsForSong = []
songIndex = -1
songs = []
covers = []
spotifyLink = []

#scrape html and get all <a> tags of songs and artists
for values in soup.find_all('a'):
    if(bool(re.search(r'<a class="EntityRowV2__Link-sc-ayafop-8 eWYxOj"', str(values)))): #match songs to the correct artists
        songs.append(values.text)
        if(songIndex>=0):
            artists.append(artistsForSong)
            artistsForSong = []
        songIndex+=1
        
    elif(bool(re.search(r'<a href="\/artist\/', str(values)))):
        artistsForSong.append(values.text)
        
#scrape html and get href of spotify links
for value in soup.find_all('a', {'href': re.compile(r'(https:\/\/open.spotify.com\/track\/\w*)')}):
    spotifyLink.append(value['href'])

#use spotipy API to get images 
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'

#spotipy auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth('a620a32c5e2644edb56292724f8711f0','e9152986f5644c6d8acefd8002e236c8','https://open.spotify.com/', scope=SCOPE, cache_path=CACHE))

#spotify api to get playlist
results = sp.playlist_items('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')

#get album covers
for idx, item in enumerate(results['items']):
    covers.append('cover: ' + item['track']['album']['images'][0]['url'])

#print values
for x in range(songIndex):
    a = ""
    for j in artists[x]:
        a+= j + " "
    print(a + " - " + songs[x] + "\n"+covers[x] + "\n"+spotifyLink[x])




    


    