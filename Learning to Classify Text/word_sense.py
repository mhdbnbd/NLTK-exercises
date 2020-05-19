from nltk.corpus import senseval
from nltk.classify import apply_features
import nltk
import random

instances = senseval.instances('hard.pos')
labeled_instances = [(inst, inst.senses) for inst in instances]
size = int(len(labeled_instances) * 0.1)


def sense_features(instance):
    features = {}
    p = instance.position
    features['preceding_word'] = instance.context[p - 1]
    features['following_word'] = instance.context[p + 1]
    return features


accuracies = []
for i in range(10):
    random.shuffle(labeled_instances)
    train_set = apply_features(sense_features, labeled_instances[size:])
    test_set = apply_features(sense_features, labeled_instances[:size])
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    accuracies.append(accuracy)
print(accuracies)
avg_accuracy = sum(accuracies)/10
print("average accuracy :", avg_accuracy)
