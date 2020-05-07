#Plot a conditional frequency distribution over the Names Corpus that allows you to see
#which initial letters are more frequent for males vs. females.

import nltk
names = nltk.corpus.names
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))
cfd.plot()
