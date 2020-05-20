import random
import nltk
from nltk import apply_features
from nltk.corpus import brown

tagged_words = brown.tagged_words(tagset='universal')
tagged_bigrams = list(nltk.bigrams(tagged_words))

# feature function


def next_noun(word):
    next_nouns = [((w1.lower(), t1), (w2.lower(), t2)) for ((w1, t1), (w2, t2)) in tagged_bigrams if t2 == 'NOUN']
    flattened_bigrams = [(w1, w2) for ((w1, t1), (w2, t2)) in next_nouns]
    features = {w2: word for (w1, w2) in flattened_bigrams if w1 == word.lower()}
    return features


# labels
labeled_instances = ([(strong_feature, 'strong') for strong_feature in next_noun('strong')] +
                     [(powerful_feature, 'powerful') for powerful_feature in next_noun('powerful')])

# classifier, 10 iterations, reshuffling, average accuracy
size = int(len(labeled_instances) * 0.1)
accuracies = []
for i in range(10):
    random.shuffle(labeled_instances)
    train_set = apply_features(next_noun, labeled_instances[size:])
    test_set = apply_features(next_noun, labeled_instances[:size])
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    accuracy = nltk.classify.accuracy(classifier, test_set)
    accuracies.append(accuracy)
print(accuracies)
avg_accuracy = sum(accuracies)/10
print("average accuracy :", avg_accuracy)
