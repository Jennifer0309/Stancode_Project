#!/usr/bin/python

import math
import random
from collections import defaultdict
from util import *
from typing import Any, Dict, Tuple, List, Callable

d = defaultdict(int)  # int() 會生成 0，所以這個 defaultdict 會對不存在的鍵返回 0
FeatureVector = Dict[str, int]
WeightVector = Dict[str, float]
Example = Tuple[FeatureVector, int]


############################################################
# Milestone 3a: feature extraction

def extractWordFeatures(x: str) -> FeatureVector:
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
    # Use defaultdict to automatically handle words that have not appeared before, with an initial count of 0
    features = defaultdict(int)
    for word in x.split():
        features[word] += 1
    return dict(features)
    # END_YOUR_CODE


############################################################
# Milestone 4: Sentiment Classification

def learnPredictor(trainExamples: List[Tuple[Any, int]], validationExamples: List[Tuple[Any, int]],
                   featureExtractor: Callable[[str], FeatureVector], numEpochs: int, alpha: float) -> WeightVector:
    """
    Given |trainExamples| and |validationExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of epochs to
    train |numEpochs|, the step size |eta|, return the weight vector (sparse
    feature vector) learned.

    You should implement gradient descent.
    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and validationExamples
    to see how you're doing as you learn after each epoch. Note also that the
    identity function may be used as the featureExtractor function during testing.
    """
    weights = {}  # the weight vector

    # BEGIN_YOUR_CODE (our solution is 12 lines of code, but don't worry if you deviate from this)
    def sigmoid(k):
        """ Sigmoid activation function. """
        return 1 / (1 + math.exp(-k))

    def predictor(review):
        """ Predicts the class for a given review. """
        phi_vector = featureExtractor(review)
        score = dotProduct(phi_vector, weights)
        return 1 if score >= 0 else -1

    for epoch in range(numEpochs):
        for x, y in trainExamples:
            y = 0 if y < 0 else 1  # Convert y to binary
            phi_x = featureExtractor(x)
            h = sigmoid(dotProduct(weights, phi_x))
            increment(weights, -alpha * (h - y), phi_x)  # Update weights

        # Evaluate the model on training and validation sets
        train_error = evaluatePredictor(trainExamples, predictor)
        validation_error = evaluatePredictor(validationExamples, predictor)
        print(f'Training Error (Epoch {epoch}): {train_error}')
        print(f'Validation Error (Epoch {epoch}): {validation_error}')

    # END_YOUR_CODE
    return weights


############################################################
# Milestone 5a: generate test case

def generateDataset(numExamples: int, weights: WeightVector) -> List[Example]:
    """
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    """
    random.seed(42)

    def generateExample() -> Tuple[Dict[str, int], int]:
        """
        Return a single example (phi(x), y).
        phi(x) should be a dict whose keys are a subset of the keys in weights
        and values are their word occurrence.
        y should be 1 or -1 as classified by the weight vector.
        Note that the weight vector can be arbitrary during testing.
        """
        # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)
        phi = {}
        # Select a random subset of features from weights
        chosen_features = random.sample(weights.keys(), min(len(weights), 10))  # choose up to 10 features
        # Randomly assign counts to these features
        phi = {feature: random.randint(1, 5) for feature in chosen_features}
        # Calculate the dot product to determine the label
        dot_product = sum(weights[feature] * phi[feature] for feature in phi)
        y = 1 if dot_product >= 0 else -1
        return phi, y
        # END_YOUR_CODE

    return [generateExample() for _ in range(numExamples)]


############################################################
# Milestone 5b: character features

def extractCharacterFeatures(n: int) -> Callable[[str], FeatureVector]:
    """
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces mapped to their n-gram counts.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    """

    def extract(x: str) -> Dict[str, int]:
        # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
        x = x.replace(" ", "")  # Remove spaces
        ngrams = [x[i:i + n] for i in range(len(x) - n + 1)]
        feature_vector = {}
        for ngram in ngrams:
            if ngram in feature_vector:
                feature_vector[ngram] += 1
            else:
                feature_vector[ngram] = 1
        return feature_vector

        # END_YOUR_CODE
    return extract


############################################################
# Problem 3f: 
def testValuesOfN(n: int):
    """
    Use this code to test different values of n for extractCharacterFeatures
    This code is exclusively for testing.
    Your full written solution for this problem must be in sentiment.pdf.
    """
    trainExamples = readExamples('polarity.train')
    validationExamples = readExamples('polarity.dev')
    featureExtractor = extractCharacterFeatures(n)
    weights = learnPredictor(trainExamples, validationExamples, featureExtractor, numEpochs=20, alpha=0.01)
    outputWeights(weights, 'weights')
    outputErrorAnalysis(validationExamples, featureExtractor, weights, 'error-analysis')  # Use this to debug
    trainError = evaluatePredictor(trainExamples,
                                   lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    validationError = evaluatePredictor(validationExamples,
                                        lambda x: (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
    print(("Official: train error = %s, validation error = %s" % (trainError, validationError)))
