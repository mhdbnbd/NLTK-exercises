#Write a function word freq() that takes a word and the name of a Brown Corpus genre
#as arguments, and computes the frequency of the word in that section of the corpus. Use
#the function to compute the frequency of “love” in “news” vs. “romance” genre.

import nltk
from nltk.corpus import brown


def word_freq(wrd, gnr):
    cfd = nltk.ConditionalFreqDist(
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre))
    genres = [gnr]
    words = [wrd]
    cfd.tabulate(conditions=genres, samples=words)


word_freq('love', 'romance')
word_freq('love', 'news')

