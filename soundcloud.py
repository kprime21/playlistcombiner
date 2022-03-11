import requests
from bs4 import BeautifulSoup
import re




data3 = requests.get('https://soundcloud.com/emiya-6343457/sets/doujinx2')
soup3 = BeautifulSoup(data3.text, 'html.parser')

f=open("soundcloud.html", "w")
f.write(str(soup3))
