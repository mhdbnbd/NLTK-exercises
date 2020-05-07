#Define a function to find all words that occur at least n times in the Brown Corpus. Call
#the function with the value n = 200.

import nltk
from nltk.corpus import brown


def reoccur(n):
    text = brown.words()
    fd = nltk.FreqDist(w.lower() for w in text)
    words = []
    for word in fd:
        if fd[word] > n and word.isalpha():
            words.append(word)
    return words


print(reoccur(200))
