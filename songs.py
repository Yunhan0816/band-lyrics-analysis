from search import search
from bs4 import BeautifulSoup
import urllib, os, re
import config
from urllib.parse import quote
import urllib.request

outputfilename = "lyrics.csv"
artists = config.artists
client_access_token = "your client_access_token"

def get_lyrics(url):
    request = urllib.request.Request(url)
    request.add_header("Authorization", "Bearer "+ client_access_token)
    request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36")
    page = urllib.request.urlopen(request)
    soup = BeautifulSoup(page, "lxml")
    lyrics = soup.find("div", class_ = "lyrics") # web scraping
    #print(lyrics)
    return lyrics.text

f2 = open('urls', 'w+')

for artist in artists:
    a1 = search(artist, outputfilename, client_access_token, 2)
    urls1 = map(lambda t: t[3], a1)
    a2 = search(artist, outputfilename, client_access_token, 3)
    urls2 = map(lambda t: t[3], a2)
    a3 = search(artist, outputfilename, client_access_token, 4)
    urls3 = map(lambda t: t[3], a3)
    f =  open('lyrics/' + artist, 'wb') # write lyrics to folder
    f2.write(artist)
    for url in urls1:
        print(url)
        lyrics = get_lyrics(url)
        f2.write(url)
        f.write(lyrics.encode('utf8'))
    for url in urls2:
        print(url)
        lyrics = get_lyrics(url)
        f2.write(url)
        f.write(lyrics.encode('utf8'))
    for url in urls3:
        print(url)
        lyrics = get_lyrics(url)
        f2.write(url)
        f.write(lyrics.encode('utf8'))
    f.close()
f2.close()
