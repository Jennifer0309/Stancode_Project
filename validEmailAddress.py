"""
File: validEmailAddress.py
Name: Jennifer Li
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: 10%
"""

WEIGHT = [  # The weight vector selected by Jerry
    [0.4],  # (see assignment handout for more details)
    [0.4],
    [0.2],
    [0.2],
    [0.9],
    [-0.65],
    [0.1],
    [0.1],
    [0.1],
    [-0.7]
]

DATA_FILE = 'is_valid_email.txt'  # This is the file name to be processed


def main():
    maybe_email_list = read_in_data()
    correct_predictions = 0
    for index, maybe_email in enumerate(maybe_email_list):
        feature_vector = feature_extractor(maybe_email)
        score = sum(feature_vector[i] * WEIGHT[i][0] for i in range(len(feature_vector)))

        # The first 13 entries are correct email addresses, so if the score is >0, the prediction is considered correct.
        # The next 13 entries are incorrect email addresses, so if the score is <0, the prediction is considered correct
        if (index < 13 and score < 0) or (index >= 13 and score > 0):
            correct_predictions += 1

    accuracy = (correct_predictions / len(maybe_email_list)) * 100
    print(f"Accuracy of this model: {accuracy}")


# def feature_extractor(maybe_email):
# 	"""
# 	:param maybe_email: str, the string to be processed
# 	:return: list, feature vector with 10 values of 0's or 1's
# 	"""
# 	feature_vector = [0] * len(WEIGHT)
# 	for i in range(len(feature_vector)):
# 		if i == 0:
# 			feature_vector[i] = 1 if '@' in maybe_email else 0
# 		elif i == 1:
# 			if feature_vector[0]:
# 				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
#
# 	return feature_vector

def feature_extractor(maybe_email):
    """
    :param maybe_email: str, the string to be processed
    :return: list, feature vector with 10 values of 0's or 1's
    """
    feature_vector = [0] * len(WEIGHT)
    parts = maybe_email.split('@')
    # Feature 1: Check if '@' is included
    feature_vector[0] = 1 if len(parts) == 2 else 0
    # Feature 2: Check if there is no '.' before '@'
    feature_vector[1] = 1 if feature_vector[0] and '.' not in parts[0] else 0
    # Feature 3: Check if there are some strings before '@'
    feature_vector[2] = 1 if feature_vector[0] and len(parts[0]) > 0 else 0
    # Feature 4: Check if there are some strings after '@'
    feature_vector[3] = 1 if feature_vector[0] and len(parts[1]) > 0 else 0
    # Feature 5: Check if there is a '.' after '@'
    feature_vector[4] = 1 if feature_vector[0] and '.' in parts[1] else 0
    # Feature 6: Check if there is no white space
    feature_vector[5] = 1 if ' ' not in maybe_email else 0
    # Feature 7: Check if it ends with 'com'
    feature_vector[6] = 1 if maybe_email.endswith('com') else 0
    # Feature 8: Check if it ends with 'edu'
    feature_vector[7] = 1 if maybe_email.endswith('edu') else 0
    # Feature 9: Check if it ends with '.tw'
    feature_vector[8] = 1 if maybe_email.endswith('.tw') else 0
    # Feature 10: Check if the length is greater than 10
    feature_vector[9] = 1 if len(maybe_email) > 10 else 0
    return feature_vector


def read_in_data():
    """
    :return: list, containing strings that might be valid email addresses
    """
    l = []
    with open(DATA_FILE, 'r') as f:
        for line in f:
            tokens = line.strip()
            l.append(tokens)
    return l


if __name__ == '__main__':
    main()
