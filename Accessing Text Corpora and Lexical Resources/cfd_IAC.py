#Plot the conditional frequency distribution of how the usage of the words “men”, “women”,
#and “people” has changed over time in the Inaugural Address Corpus.

import nltk
from nltk.corpus import inaugural

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['men', 'women', 'people']
    if w.lower().startswith(target)
)
cfd.plot()

