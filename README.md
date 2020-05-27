# NLTK-exercises

Exercise sheets

I. Accessing Text Corpora and Lexical Resources

Plot the conditional frequency distribution of how the usage of the words “men”, “women”,
and “people” has changed over time in the Inaugural Address Corpus.
    Solution => **cfd_IAC.py**
 
Plot a conditional frequency distribution over the Names Corpus that allows you to see
which initial letters are more frequent for males vs. females.
    Solution => **cfd_NC.py**
  
Define a function supergloss(s) that takes a synset s as its argument and returns a
string consisting of the concatenation of the definition of s, and the definitions of all the
hypernyms and hyponyms of s. Apply the function to the synset “car.n.01”.
    Solution => **synsets_definitions.py**
  
Define a function to find all words that occur at least n times in the Brown Corpus. Call
the function with the value n = 200.
    Solution => **word_frequency.py**
  
Write a program that lists the lexical diversity scores for all Brown Corpus genres, one
per line.
    Solution => **lds.py**
  
Write a function word freq() that takes a word and the name of a Brown Corpus genre
as arguments, and computes the frequency of the word in that section of the corpus. Use
the function to compute the frequency of “love” in “news” vs. “romance” genre.
    Solution => **word_freq_genre.py**
    
II. Learning to Classify Text

Write a name gender classifier using the Names Corpus, the apply_features function,
shuffling, and a test set of 500 instances. Use the following features:
a) first letter;
b) last letter;
c) last two letters;
d) length;
e) for each letter one feature, which is true if the name contains the letter.
Use the NaiveBayesClassifier, calculate the accuracy, and display the 10 most informative features.
    Solution => **gender_classifer.py**

Based on the Movie Reviews document classifier, build a new
NaiveBayesClassifier. Tag first the Movie Reviews Corpus using the combined tagger stored in t2.pkl. Filter the tagged words to contain only
words for the tags [’JJ’, ’JJR’, ’JJS’, ’RB’, ’NN’, ’NNS’, ’VB’, ’VBN’, ’VBG’, ’VBZ’,
’VBD’, ’QL’] as well as only alphabetic tokens with at least three characters. Convert the
words to lowercase. Use the most common 5000 words as word_features in the function
document_features.
Run 10 iterations by reshuffling the instances and printing the accuracy and 5 most
informative features for each iteration. Finally, print the average accuracy.
    Solution => **movie_reviews.py**

The Senseval 2 Corpus contains data intended to train word-sense disambiguation classifiers. Using this dataset, build a NaiveBayesClassifier that predicts the correct sense
tag for a given instance for the word “hard”.
Use the preceding and following word as features. They can be calculated by retrieving the
position of the word “hard” as p=inst.position and then accessing inst.context[p-1]
and inst.context[p+1].
Run 10 iterations by reshuffling the instances and printing the individual accuracies.
Finally, print the average accuracy. 
    Solution => **word_sense.py**

The synonyms “strong” and “powerful” pattern differently. Use the tagged Brown corpus
with the universal tagset to first list the nouns which follow “strong” vs. “powerful”. Write
for this a function next_noun(word, tagged_text) which returns the list of nouns that
follow word in the tagged_text. Build then a NaiveBayesClassifier that predicts when
each word should be used by using the function apply_features and the following noun
as single feature.
Run 10 iterations by reshuffling the instances and printing the individual accuracies.
Finally, print the average accuracy.. 
    Solution => **strong_vs_powerful.py**
    
III. Extracting Information from Text

Extend a chunk grammar to match noun phrases containing plural head nouns. Test your grammar with the following sentences:
("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")<br/>
=: (S (NP many/JJ dogs/NNS) barked/VBD at/IN (NP the/DT cat/NN))<br/>
("two", "CD"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")<br/>
=: (S (NP two/CD dogs/NNS) barked/VBD at/IN (NP the/DT cat/NN))<br/>
("both", "DT"), ("new", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("cat", "NN")<br/>
=: (S (NP both/DT new/JJ dogs/NNS) barked/VBD at/IN (NP the/DT cat/NN))<br/>
    Solution => **chunker_phn.py**

Extend a chunk grammar to match noun phrases containing gerunds. Test your grammar with the following sentences:
("many", "JJ"), ("dogs", "NNS"), ("barked", "VBD"), ("at", "IN"), ("the", "DT"), ("meowing", "VBG"), ("cat", "NN")<br/>
=: (S (NP many/JJ dogs/NNS) barked/VBD at/IN (NP the/DT meowing/VBG cat/NN))<br/>
("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"), ("become", "VB"), ("assistant", "NN"), ("managing", "VBG"), 
("director", "NN")<br/>
=: (S (NP the/DT man/NN) wants/VBZ to/TO become/VB (NP assistant/NN managing/VBG director/NN))<br/>
    Solution => **chunker_gerunds.py**
    
Extend the grammar from **chunker_gerunds.py** to also handle coordinated noun phrases. Test your grammar with
the following sentences and the sentences from **chunker_phn.py** and **chunker_gerunds.py**:
("the", "DT"), ("man", "NN"), ("wants", "VBZ"), ("to", "TO"), ("leave", "VB"), ("in", "IN"), ("July", "NNP"), 
("or", "CC"), ("August", "NNP")<br/>
=: (S (NP the/DT man/NN) wants/VBZ to/TO leave/VB in/IN (NP July/NNP or/CC August/NNP))<br/>
("Donald", "NNP"), ("fired", "VBD"), ("all", "PDT"), ("your", "PRP$"), ("managers", "NNS"), ("and", "CC"), 
("supervisors", "NNS")<br/>
=: (S (NP Donald/NNP) fired/VBD (NP all/PDT your/PRP$ managers/NNS and/CC supervisors/NNS))<br/>
("company", "NN"), ("personnel", "NN"), ("policy", "NN"), ("has", "VBZ"), ("always", "RB"), ("been", "VBN"), 
("the", "DT"), ("law", "NN"), ("that", "WDT"), ("rules", "VBZ"), ("company", "NN"), ("courts", "NN"), ("and", "CC"), 
("adjudicators", "NNS")<br/>
=: (S (NP company/NN personnel/NN policy/NN) has/VBZ always/RB been/VBN (NP the/DT law/NN) that/WDT rules/VBZ 
(NP company/NN courts/NN and/CC adjudicators/NNS))<br/>
    Solution => **chunker_cc.py**