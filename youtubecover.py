import requests
from bs4 import BeautifulSoup
import re



#youtube

link = 'https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020'
link2 = 'https://www.youtube.com/watch?v=C-hzP3mOBGY&list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020&index=1'

#check if it is link to playlist or link to playlist in videos
result = re.findall(r'www.youtube.com\/(.*?)\?(list|v)(.*)',link)

data2 = requests.get('https://www.youtube.com/playlist?list=PLgEPGvYuVfmpKScw-Gozj6rfbc2edU020')
soup2 = BeautifulSoup(data2.text, 'html.parser')
youtubetitles = re.findall(r'"playlistVideoRenderer":.*?"text":"(.*?)"}]', str(soup2))
youtubelinks = re.findall(r'"playlistVideoRenderer":.*?"videoId":"(.*?)"', str(soup2))
youtubeidcovers = re.findall(r'{"playlistVideoRenderer":{"videoId":"(.*?)","thumbnail":{"thumbnails":\[{"url":"(.*?)"',str(soup2))


for values in youtubecovers:
    print(values)