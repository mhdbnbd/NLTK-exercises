#Write a program that lists the lexical diversity scores for all Brown Corpus genres, one
#per line.

from nltk.corpus import brown

for genre in brown.categories():
    n_words = len(brown.words(categories=genre))
    vocab = len(set(w.lower() for w in brown.words(categories=genre)))
    print(round(n_words/vocab, 2), genre)

