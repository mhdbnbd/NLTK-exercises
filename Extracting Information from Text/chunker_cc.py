import nltk

sentence1 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"), ("leave", "VB"), ("in", "IN"),
             ("July", "NNP"), ("or", "CC"), ("August", "NNP")]
sentence2 = [("Donald", "NNP"), ("fired", "VBD"), ("all", "PDT"), ("your", "PRP"),
             ("managers", "NNS"), ("and", "CC"), ("supervisors", "NNS")]
sentence3 = [("company", "NN"), ("personnel", "NN"), ("policy", "NN"), ("has", "VBZ"), ("always", "RB"),
             ("been", "VBN"), ("the", "DT"), ("law", "NN"), ("that", "WDT"), ("rules", "VBZ"),
             ("company", "NN"), ("courts", "NN"), ("and", "CC"), ("adjudicators", "NNS")]
sentence11 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence12 = [("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence13 = [("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
              ("cat", "NN")]
sentence21 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"),
              ("the", "DT"), ("meowing", "VBG"), ("cat", "NN")]
sentence22 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"),
              ("become", "VB"), ("assistant", "NN"), ("managing", "VBG"), ("director", "NN")]

grammar = "NP: {<DT>?<CD>?<JJ>*(<PDT>|<PRP>)*(<NN>|<NNS>|<NNP>)*<CC>?<VBG>?(<NN>|<NNS>|<NNP>)*}"
cp = nltk.RegexpParser(grammar)
results = [print(cp.parse(sentence))for sentence in [sentence1, sentence2, sentence3, sentence11, sentence12, sentence13
                                                     , sentence21, sentence22]]
