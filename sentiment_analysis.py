import nltk
nltk.download()
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import config
import pandas as pd
artists = config.artists
df = pd.DataFrame(columns = ('artist', 'positive', 'neautral', 'negative'))
sid = SentimentIntensityAnalyzer()
i=0
for artist in artists:
    pos = 0
    neg = 0
    neu = 0

    f = open('lyrics/' + artist + '-cleaned', 'rb')
    for sentence in f.readlines():
        this_sentence = sentence.decode('utf-8')
        comp = sid.polarity_scores(this_sentence)
        comp = comp['compound']
        if comp >= 0.5:
            pos += 1
        elif comp > -0.5 and comp < 0.5:
            neu += 1
        else:
            neg += 1

    num_total = po + neu + neg
    percent_negative = (neg / float(num_total)) * 100
    percent_neutral = (neu / float(num_total)) * 100
    percent_positive = (pos / float(num_total)) * 100
    df.loc[i] = (artist, percent_positive, percent_neutral, percent_negative)
    i+=1

df.plot.bar(x='artist', stacked=True)
plt.show()
