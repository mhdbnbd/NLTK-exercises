import nltk

sentence1 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence2 = [("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence3 = [("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
             ("cat", "NN")]
sentence21 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
              ("meowing", "VBG"), ("cat", "NN")]
sentence22 = [("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"),
              ("become", "VB"), ("assistant", "NN"), ("managing", "VBG"), ("director", "NN")]

grammar = r"""
  NP: {<DT|CD|JJ|NN.*|VBG>+}     
  PP: {<IN><NP>}           
  VP: {<VB.*>+<PP|INFCL|NP>+$} 
  INFCL: {<TO><VP>}
                       
  """
cp = nltk.RegexpParser(grammar, loop=2)
results = [print(cp.parse(sentence))for sentence in [sentence21, sentence22, sentence1, sentence2, sentence3]]

