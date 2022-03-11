import requests
from bs4 import BeautifulSoup
import re




# link = 'https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020'
# link2 = 'https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1'

# #check if it is link to playlist or link to playlist in videos
# result = re.findall(r'www.youtube.com\/(.*?)\?(list|v)(.*)',link)






data = requests.get('https://open.spotify.com/playlist/4NKQC01pmUYlJqSRQnWTVL')
data2 = requests.get('https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020')





soup = BeautifulSoup(data.text, 'html.parser')
soup2 = BeautifulSoup(data2.text, 'html.parser')

#spotify music ( spotify only limits to 100 so changes need to be made)
artists = []
artistsForSong = []
songIndex = -1
songs = []
for values in soup.find_all('a'):

    if(bool(re.search(r'<a class="EntityRowV2__Link-sc-ayafop-8 eWYxOj"', str(values)))):
        songs.append(values.text)
        if(songIndex>=0):
            artists.append(artistsForSong)
            artistsForSong = []
        songIndex+=1
        
    elif(bool(re.search(r'<a href="\/artist\/', str(values)))):
        artistsForSong.append(values.text)

for x in range(songIndex):
    a = ""
    for j in artists[x]:
        a+= j + " "
    print(a + " - " + songs[x])


    
#youtube

youtubetitles = re.findall(r'"playlistVideoRenderer":.*?"text":"(.*?)"}]', str(soup2))
youtubelinks = re.findall(r'"playlistVideoRenderer":.*?"videoId":"(.*?)"', str(soup2))

for values in youtubetitles:
    print(values)
for values in youtubelinks:
    print("https://www.youtube.com/watch?v=" + values)


