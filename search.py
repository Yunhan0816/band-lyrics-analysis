import sys
import re
import urllib
import json
import csv
import codecs
import os
import socket
from socket import AF_INET, SOCK_DGRAM
import urllib.parse
import urllib.request
from importlib import reload
from urllib.parse import quote
def load_credentials():
    lines = [line.rstrip('\n') for line in open('credentials.txt')]
    chars_to_strip = " \'\""
    for line in lines:
        if "client_id" in line:
            client_id = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        if "client_secret" in line:
            client_secret = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
        #Currently only need access token to run, the other two perhaps for future implementation
        if "client_access_token" in line:
            client_access_token = re.findall(r'[\"\']([^\"\']*)[\"\']', line)[0]
    return client_id, client_secret, client_access_token

def setup(search_term):
    #reload(sys) #dirty (but quick) way to deal with character encoding issues in Python2; if writing for Python3, should remove
    #sys.setdefaultencoding('utf8')
    if not os.path.exists("output/"):
        os.makedirs("output/")
    outputfilename = "output/output-" + re.sub(r"[^A-Za-z]+", '', search_term) + ".csv"
    with codecs.open(outputfilename, 'ab', encoding='utf8') as outputfile:
        outwriter = csv.writer(outputfile)
        if os.stat(outputfilename).st_size == 0:
            header = ["page","id","title","url","path","header_image_url","annotation_count","pyongs_count","primaryartist_id","primaryartist_name","primaryartist_url","primaryartist_imageurl"]
            outwriter.writerow(header)
            return outputfilename
        else:
            return outputfilename

def search(search_term,outputfilename,client_access_token):
    #page = 1
    #print(search_term)
    with codecs.open(outputfilename, 'ab', encoding='utf8') as outputfile:
        outwriter = csv.writer(outputfile)
        page = 1
        while True:
            querystring = "http://api.genius.com/search?q=" + urllib.parse.quote(search_term,"") + "&page=" + str(page)
            request = urllib.request.Request(querystring)
            request.add_header("Authorization", "Bearer " + client_access_token)
            request.add_header("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36") #Must include user agent of some sort, otherwise 403 returned
            while True:
                try:
                    response = urllib.request.urlopen(request, timeout=10) #timeout set to 10 seconds; automatically retries if times out
                    raw = response.read()
                except socket.timeout:
                    print("Timeout raised and caught")
                    continue
                break
            json_obj = json.loads(raw)
            body = json_obj["response"]["hits"]

            num_hits = len(body)
            if num_hits==0:
                if page==1:
                    print("No results for: " + search_term)
                break
            print("page {0}; num hits {1}".format(page, num_hits))

            results = []
            for result in body:
                result_id = result["result"]["id"]
                title = result["result"]["title"]
                url = result["result"]["url"]
                path = result["result"]["path"]
                header_image_url = result["result"]["header_image_url"]
                annotation_count = result["result"]["annotation_count"]
                pyongs_count = result["result"]["pyongs_count"]
                primaryartist_id = result["result"]["primary_artist"]["id"]
                primaryartist_name = result["result"]["primary_artist"]["name"]
                primaryartist_url = result["result"]["primary_artist"]["url"]
                primaryartist_imageurl = result["result"]["primary_artist"]["image_url"]
                row=[page,result_id,title.encode('utf-8'),url,path,header_image_url,annotation_count,pyongs_count,primaryartist_id,primaryartist_name,primaryartist_url,primaryartist_imageurl]
                print row
                outwriter.writerow(row) #write as CSV
                results.append(row)
            return results
            page+=1

def main():
    arguments = sys.argv[1:] #so you can input searches from command line if you want
    search_term = arguments[0].translate(str.maketrans("","", "\'\""))
    outputfilename = setup(search_term)
    client_id, client_secret, client_access_token = load_credentials()
    search(search_term,outputfilename,client_access_token)

if __name__ == '__main__':
    main()
