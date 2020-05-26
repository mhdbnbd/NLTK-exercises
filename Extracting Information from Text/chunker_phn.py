import nltk

sentence1 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence2 = [("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence3 = [("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
             ("cat", "NN")]
grammar = "NP: {<DT>?<CD>?<JJ>*(<NN>|<NNS>)}"
cp = nltk.RegexpParser(grammar)
results = [print(cp.parse(sentence))for sentence in [sentence1, sentence2, sentence3]]
