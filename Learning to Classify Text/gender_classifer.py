import random
import nltk
from nltk.corpus import names
from nltk.classify import apply_features

# features extractor


def gender_features(name):
    features = {'first_letter': name[0].lower(), 'last_letter': name[-1].lower(), 'last_two_letters': name[-2:].lower(),
                'name_length': len(name)}
    name = name.lower()
    a = ord('a')
    alphas = [chr(i) for i in range(a, a + 26)]
    list_features = [0] * len(alphas)
    letters = [name[i] for i in range(len(name))]
    for alpha in alphas:
        if alpha in letters:
            list_features[alphas.index(alpha)] = 1
    features['name_letters'] = ''.join(map(str, list_features))
    return features


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


train(gender_features)
