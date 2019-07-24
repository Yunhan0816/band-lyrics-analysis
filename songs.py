from search import search
from bs4 import BeautifulSoup
import urllib, os, re
import config

outputfile = "lyrics.csv"
artists = config.artists
client_access_token = ""

def get_lyrics(url):
    request = urllib.request.Request(url)
    request.add_header("Authorization", "Bearer "+ client_access_token)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")
    page = urllib.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_ = "lyrics")
    return lyrics.text

f2 = open('urls', 'wb')

for artist in ["radiohead"]:
    a = search(artist, outputfile, client_access_token)
    urls = map(lambda t: t[3], a)
    print(artist, len(urls))

    f =  open('lyrics/' + artist, 'wb')
    f2. write(artist)
    for url in urls:
        lyrics = get_lyrics(url)
        f2.write(url)
        print(url)
        f.write(lyrics.encode("urf8"))
    f.close()
f2.close()
