import re
import os, config

artists = config.artists

for artist in artists:
    f = open('lyrics/' + artist, 'rb')
    words = ''
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        words += this_sentence
    f.close()

    # remove "chorus," "verse," "..."
    words = re.sub(r'[\(\[].*? [\)\)]', '', words)

    words = os.linesep.join([s for s in words.splitlines() if s])

    f = open('lyrics/' + artist + '-cleaned', 'wb')
    f.write(words, encode('utf-8'))
    f.close()
