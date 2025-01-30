"""
File: validEmailAddress_2.py
Name: Jennifer Li
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  Check if no '@' in str
feature2:  Check there is no strings before and after '@'
feature3:  Check '.' in the first or last character of the string before '@'
feature4:  Check there is '"' and no '.' before '@'
feature5:  Check if there is no white space
feature6:  Check if '..' in the str
feature7:  Check if more than one '@' in str
feature8:  strings before and after '@'
feature9:  Whether it contains illegal characters
feature10: Whether it ends with a legal domain

Accuracy of your model: 96.15%
"""
# The weight vector selected by you
# (Please fill in your own weights)
import numpy as np

WEIGHT = [  # The weight vector selected by you
    [-1],
    [-0.8],
    [-0.9],
    [-0.8],
    [0.1],
    [-0.68],
    [-0.5],
    [0.2],
    [0.1],
    [0.2]
]

DATA_FILE = 'is_valid_email.txt'  # This is the file name to be processed


def main():
    maybe_email_list = read_in_data()
    correct_predictions = 0

    for i in range(len(maybe_email_list)):
        maybe_email = maybe_email_list[i]
        feature_vector = feature_extractor(maybe_email)
        weight_vector = np.array(WEIGHT).T
        score = weight_vector.dot(feature_vector)[0][0]
        # The first 12 entries are correct email addresses, so if the score is >0, the prediction is considered correct.
        # The next 12 entries are incorrect email addresses, so if the score is <0, the prediction is considered correct
        if (i <= 12 and score <= 0) or (i > 12 and score > 0):
            correct_predictions += 1
    accuracy = correct_predictions / len(maybe_email_list) * 100
    print(f"Accuracy of this model: {accuracy}")


def feature_extractor(maybe_email):
    """
    :param maybe_email: str, the string to be processed
    :return: list, feature vector with value 0's and 1's
    """
    feature_vector = np.zeros((10, 1))  # initialize an array with 10 rows, 1 col
    # Iterates over each element of the feature vector (from 0 to 9,there are 10 features)
    for i in range(len(feature_vector)):
        # feature1:  no '@' in str
        if i == 0:
            feature_vector[i][0] = 1 if '@' not in maybe_email else 0
        text_before_at = ''.join(maybe_email.split('@')[:-1])
        text_after_at = ''.join(maybe_email.split('@')[1:])
        # feature2:  there is no strings before and after '@'
        if i == 1:
            if not feature_vector[0][0]:
                feature_vector[i][0] = 1 if not text_before_at or not text_after_at else 0
        # feature3:  '.' in the first or last character of the string before '@'
        if i == 2:
            if not feature_vector[0][0] and not feature_vector[1][0]:
                feature_vector[i][0] = 1 if text_before_at[0] == '.' or text_before_at[-1] == '.' else 0
        # feature4:  there is '"' and no '.' before '@'
        if i == 3:
            if not feature_vector[0][0] and not feature_vector[1][0]:
                feature_vector[i][0] = 1 if '\"' in text_before_at and '.' not in text_before_at else 0
        # feature 5: Check if there is no white space
        if i == 4:
            if not feature_vector[0][0]:
                feature_vector[i][0] = 1 if ' ' not in maybe_email else 0
        # feature6:  '..' in the str
        if i == 5:
            feature_vector[i][0] = 1 if '..' in maybe_email else 0
        # feature7:	more than one '@' in str
        if i == 6:
            if not feature_vector[0][0]:
                feature_vector[i][0] = 1 if maybe_email.count('@') > 1 else 0
        # feature8:	strings before and after '@'
        if i == 7:
            feature_vector[i][0] = 1 if text_before_at and text_after_at else 0
        # feature9: Whether it contains illegal characters
        if i == 8:
            invalid_chars = set("!#$%&'*+/=?^`{|}~")
            feature_vector[i][0] = 1 if not any(char in invalid_chars for char in maybe_email) else 0
        # feature10: Whether it ends with a legal domain
        if i == 9:
            feature_vector[i][0] = 1 if maybe_email.endswith(('com', 'org', 'net', 'edu', 'gov', 'tw')) else 0

    return feature_vector


def read_in_data():
    """
    :return: list, containing strings that may be valid email addresses
    """
    l = []
    with open(DATA_FILE, 'r') as f:
        for line in f:
            tokens = line.strip()  # Remove the end of whitespace
            l.append(tokens)
    return l


if __name__ == '__main__':
    main()
