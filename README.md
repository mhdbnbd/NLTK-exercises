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
    Solution => **strong_vs_powerful**
    
The PP Attachment Corpus is a corpus describing prepositional phrase attachment decisions. Each instance in the training corpus is encoded as a PPAttachment object
In the same way, ppattach.attachments(’test’) accesses the test instances. Select
only the instances where inst.attachment is ’N’
Using this sub-corpus, build a NaiveBayesClassifier that attempts to predict which
preposition is used to connect a given pair of nouns. For example, given the pair of nouns
“team” and “researchers”, the classifier should predict the preposition “of”.
Write for this purpose a function prepare_featuresets(subcorpus), where subcorpus
is either the string “training” or “test” to return the training set or the test set.
Print the achieved accuracy as well as the result of classifier.classify({’noun1’:
’team’, ’noun2’: ’researchers’}).
    Solution => 

