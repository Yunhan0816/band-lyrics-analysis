from search import search
from bs4 import BeautifulSoup
import urllib, os, re
import config
from urllib.parse import quote
import urllib.request

outputfilename = "lyrics.csv"
artists = config.artists
client_access_token = "9hWmRE5uhP4A3bAf3rrmvIRuTCJBoJEByP0QMsmpl-jy2SR9K_La-IRvlV1I7mKx"

def get_lyrics(url):
    request = urllib.request(url)
    request.add_header("Authorization", "Bearer "+ client_access_token)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_ = "lyrics")
    #print(lyrics)
    return lyrics.text

f2 = open('urls', 'w')

for artist in artists:
    a = search(artist, outputfilename, client_access_token)
    urls = map(lambda t: t[3], a)
    print(artist, len(list(urls)))
    f =  open('lyrics/' + artist, 'w') # write lyrics to folder
    f2. write(artist)
    for url in urls:
        lyrics = get_lyrics(url)
        f2.write(url)
        print(url)
        f.write(lyrics)
    f.close()
f2.close()
