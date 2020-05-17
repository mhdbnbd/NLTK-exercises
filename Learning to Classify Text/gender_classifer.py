import random
import nltk
from nltk.corpus import names
from nltk.classify import apply_features

# features extractor


def a_features(word):
    return {'first_letter': word[0]}


def b_features(word):
    return {'last_letter': word[-1]}


def c_features(word):
    return {'last_two_letters': word[-2:]}


def d_features(word):
    return {'word_length': len(word)}


def e_features(word):
    word = word.lower()
    a = ord('a')
    alphas = [chr(i) for i in range(a, a + 26)]
    list_features = [0] * len(alphas)
    letters = [word[i] for i in range(len(word))]
    for alpha in alphas:
        if alpha in letters:
            list_features[alphas.index(alpha)] = 1
    string_features = ''.join(map(str, list_features))
    return {'word_letters': string_features}


# labels for training/test
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)


def train(features):
    train_set = apply_features(features, labeled_names[500:])
    test_set = apply_features(features, labeled_names[:500])
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    print(accuracy)
    most_informative = classifier.show_most_informative_features(10)
    return {accuracy, most_informative}


for f in [a_features, b_features, c_features, d_features, e_features]:
    train(f)
