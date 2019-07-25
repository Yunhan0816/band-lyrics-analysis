import re
import os
import config

artists = config.artists

for artist in artists:
    f = open('lyrics/' + artist, 'rb')
    words = ''
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        words += this_sentence
    f.close()

    # remove "chorus," "verse," using re.sub()
    words = re.sub(r"[\(\(].*? [\)\)]", words)
    #join the lines
    words = os.linesep.join([l for l in words.splitlines() if l])

    # write the cleaned words into file one by one
    f = open('lyrics/' + artist + '_cleaned', 'wb')
    f.write(words, encode('utf-8'))
    f.close()
