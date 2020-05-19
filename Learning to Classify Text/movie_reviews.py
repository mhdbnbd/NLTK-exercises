import random
import nltk
from nltk.corpus import movie_reviews
from pickle import load

# import tagger
input_tagger = open('t2.pkl', 'rb')
tagger = load(input_tagger)
input_tagger.close()

# pre-processing : filtering tagging
documents = [(movie_reviews.words(fileid), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
filtered_documents = [([word.lower() for word in document if word.isalpha() and len(word) > 2], category)
                      for (document, category) in documents]
tagged_documents = [(tagger.tag(doc), category) for (doc, category) in filtered_documents]
ft_documents = [([(w, tag) for (w, tag) in tagged_doc
                 if tag in ['JJ', 'JJR', 'JJS', 'RB', 'NN', 'NNS', 'VB', 'VBN', 'VBG', 'VBZ', 'VBD', 'QL']], category)
                for (tagged_doc, category) in tagged_documents]

# feature extractor
tokens = nltk.FreqDist(w.lower() for w in movie_reviews.words() if w.isalpha() and len(w) > 2)
word_features = list(tokens)[:5000]
tagged_word_features = tagger.tag(word_features)
ft_word_features = [(w, tag) for (w, tag) in tagged_word_features
                    if tag in ['JJ', 'JJR', 'JJS', 'RB', 'NN', 'NNS', 'VB', 'VBN', 'VBG', 'VBZ', 'VBD', 'QL']]


def document_features(document):
    document_words = set(document)
    features = {}
    for (word, tag) in ft_word_features:
        features['contains({}, {})'.format(word, tag)] = ((word, tag) in document_words)
    return features


# classifier, 10 iterations, reshuffling, average accuracy
accuracies = []
for i in range(10):
    random.shuffle(ft_documents)
    feature_sets = [(document_features(document), category) for (document, category) in ft_documents]
    train_set, test_set = feature_sets[100:], feature_sets[:100]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    print("Accuracy :", accuracy)
    accuracies.append(accuracy)
    classifier.show_most_informative_features(5)
print(accuracies)
avg_accuracy = sum(accuracies)/10
print("average accuracy :", avg_accuracy)
