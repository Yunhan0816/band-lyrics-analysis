from wordcloud import WordCloud
import config
artists = config.artists

for artist in artists:
    f = open('lyrics/' + artist + '_cleaned', 'rb')
    words = ''
    for sentence in f.readlines():
        s = sentence.decode('utf8')
        words += s
    word_cloud = WordCloud(width = 1000, height = 500).generate(words.lower())
    word_cloud.to_file('word_clouds/' + artist + '.png')
    image = word_cloud.to_image()
