import nltk

sentence1 = [("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence2 = [("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")]
sentence3 = [("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"),
             ("cat", "NN")]

grammar = r"""
  NP: {<DT|CD|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN, CD
  PP: {<IN><NP>}                  # Chunk prepositions followed by NP
  VP: {<VB.*><NP|PP>+$}           # Chunk verbs and their arguments
  {<NP><VP>}                      # Chunk NP, VP
  """
cp = nltk.RegexpParser(grammar)
results = [print(cp.parse(sentence))for sentence in [sentence1, sentence2, sentence3]]

