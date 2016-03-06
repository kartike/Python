import requests
import urllib2
from bs4 import BeautifulSoup

urll = urllib2.urlopen('https://www.youtube.com/user/ProgrammingKnowledge/videos')
text = urll.read()
urll.close()

soup = BeautifulSoup(text,'html.parser')
ren = soup.find_all("h3","yt-lockup-title")

for item in ren:
    item = item.text
    if 'Mongo' in item:
        print item