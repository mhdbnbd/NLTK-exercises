# NLTK-exercises

Exercise sheets

I. Accessing Text Corpora and Lexical Resources

Plot the conditional frequency distribution of how the usage of the words “men”, “women”,
and “people” has changed over time in the Inaugural Address Corpus.
  Solution => cfd_IAC.py
 
Plot a conditional frequency distribution over the Names Corpus that allows you to see
which initial letters are more frequent for males vs. females.
  Solution => cfd_NC.py
  
Define a function supergloss(s) that takes a synset s as its argument and returns a
string consisting of the concatenation of the definition of s, and the definitions of all the
hypernyms and hyponyms of s. Apply the function to the synset “car.n.01”.
  Solution => synsets_definitions.py
  
Define a function to find all words that occur at least n times in the Brown Corpus. Call
the function with the value n = 200.
  Solution => word_frequency.py
  
Write a program that lists the lexical diversity scores for all Brown Corpus genres, one
per line.
  Solution => lds.py
  
Write a function word freq() that takes a word and the name of a Brown Corpus genre
as arguments, and computes the frequency of the word in that section of the corpus. Use
the function to compute the frequency of “love” in “news” vs. “romance” genre.
  Solution => word_freq_genre.py
  
  
II. Learning to Classify Text

Write a name gender classifier using the Names Corpus, the apply_features function,
shuffling, and a test set of 500 instances. Use the following features:
a) first letter;
b) last letter;
c) last two letters;
d) length;
e) for each letter one feature, which is true if the name contains the letter.
Use the NaiveBayesClassifier, calculate the accuracy, and display the 10 most informative features.
  Solution => gender_classifer.py
