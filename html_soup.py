import re
from BeautifulSoup import BeautifulSoup
import mechanize

br = mechanize.Browser()

br.addheaders = [('User-agent', 'Mozilla/5.0')]

url = ('http://ambarsariya.me/')
br.open(url) 
res = br.response().read()
soup = BeautifulSoup(res)
print (soup.prettify())
