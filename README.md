# Band-Lyrics-Analysis
Sentiment analysis on my favorite indie bands' song lyrics

### Data: Genius.com API
1. Used genius.com, a convenient API, to obtain lyrics data. Used and modified this https://github.com/jasonqng/genius-lyrics-search python script for searching and obtaining lyrics from genius.com
2. I decided to analyze song lyrics by Beach Fossils, Beach House, Diiv, Radiohead, and Wild Nothing. For each artist, collected 30 songs to analyze by connecting genius.com and use BeautifulSoup to do data scraping from the website.
3. clean the data by removing [chorus], [verse 1], and other unnecessary words

### Analysis: text analysis, sentiment analysis, and word cloud
1. Used wordcloud library in python to generate each artist's wordclouds.
2. Used NLTK's sentiment analyzer to generate normalized unidimensional metric of sentiment, finding the positivity, negativity, and neutrality of the lyrics by each artist, and illustrated the result by plotting the graph.

### Result
#### Word Cloud
Beach fossils and Diiv have similar word cloud (partially because Zach from Diiv is a former beach fossils member.) They both like to use "lost," "know," and "feel." Wild Nothing's lyrics tend to talk about "love" and "woman," while Beach House's song lyrics seem more gentle, they use "darling," "take care," and love talking about "night." Radiohead's lyrics are shown to talk a lot about "mess, "truth," "rain," and "broken hearts."
#### Sentiment Analysis
Beach Fossils's songs are the most neutral ones comparing to other artists'. Diiv and Radiohead have more negative lyrics than the rest of the artists. Wild Nothing's lyrics are shown to be the most positive ones.
