import nltk

sentence1 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"),
             ("the", "DT"), ("meowing", "VBG"), ("cat", "NN")]
sentence2 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"),
             ("become", "VB"), ("assistant", "NN"), ("managing", "VBG"), ("director", "NN")]
grammar = "NP: {<DT>?<CD>?<JJ>*(<NN>|<NNS>|<VBG>)*}"
cp = nltk.RegexpParser(grammar)
results = [print(cp.parse(sentence))for sentence in [sentence1, sentence2]]
