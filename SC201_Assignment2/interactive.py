"""
File: interactive.py
Name: pei yin Li
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users on Console. Remember to read the weights
and build a Dict[str: float]
"""

from util import interactivePrompt
from submission import extractWordFeatures


def main():
    weights = load_weights('weights')
    interactivePrompt(extractWordFeatures, weights)


def load_weights(filename: str) -> dict:
    """
    Load weights from a file and return a dictionary with the weights.
    """
    weights = {}
    with open(filename, 'r') as f:
        for line in f:
            key, value = line.split()
            weights[key] = float(value)
    return weights


if __name__ == '__main__':
    main()
