#Define a function supergloss(s) that takes a synset s as its argument and returns a
#string consisting of the concatenation of the definition of s, and the definitions of all the
#hypernyms and hyponyms of s. Apply the function to the synset “car.n.01”.

from nltk.corpus import wordnet as wn


def supergloss(s):
    s = wn.synset(s)
    hyper_s = s.hypernyms()
    hypo_s = s.hyponyms()
    hyp_s = hyper_s + hypo_s
    list_hyp_def = []
    for i in range(len(hyp_s)-1):
        hyp_def = hyp_s[i].definition()
        list_hyp_def.append(hyp_def)
    list_def = [s.definition()] + list_hyp_def
    str_def = '. '.join(list_def)
    return str_def


ex4 = supergloss("car.n.01")
print(ex4)
