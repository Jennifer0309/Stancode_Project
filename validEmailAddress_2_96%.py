"""
File: validEmailAddress_2.py
Name: Mei-Fei Chen
----------------------------
Please construct your own feature vectors
and try to surpass the accuracy achieved by
Jerry's feature vector in validEmailAddress.py.
feature1:  no '@' in str -1
feature2:  no strings before and after '@' -1
feature3:  '.' in the first or last character of the string before '@' -1
feature4:  there is '"' and no '.' before '@' -0.8
feature5:  '"str"' before '@' 0.6
feature6:  '..' in the str -0.67
feature7:	more than one '@' in str -0.5
feature8:	strings before and after '@' 0.2
feature9:	'\' in str -0.2
feature10:	length of string before at > 64 -1

Accuracy of your model: 1.0
"""

import numpy as np

WEIGHT = [                           # The weight vector selected by you
	[-1],                              # (Please fill in your own weights)
	[-1],
	[-1],
	[-0.8],
	[0.6],
	[-0.67],
	[-0.5],
	[0.2],
	[-0.2],
	[-1]
]

DATA_FILE = 'is_valid_email.txt'    # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
	accurate = 0  # count the numbers of email classified accurately

	for i in range(len(maybe_email_list)):
		maybe_email = maybe_email_list[i]
		feature_vector = feature_extractor(maybe_email)
		weight_vector = np.array(WEIGHT).T
		score = weight_vector.dot(feature_vector)[0][0]
		if (i <= 12 and score <= 0) or (i > 12 and score > 0):
			accurate += 1
	accuracy = accurate / len(maybe_email_list)
	print(accuracy)


def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = np.zeros((10, 1))
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
		# feature5:  '"str"' before '@'
		if i == 4:
			if not feature_vector[0][0]:
				count = text_before_at.count('\"')
				feature_vector[i][0] = 1 if count > 0 and count % 2 == 0 and '\"\"' not in maybe_email else 0
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
		# feature9: '\' in str
		if i == 8:
			feature_vector[i][0] = 1 if '\\' in maybe_email else 0
		# feature10: length of string before at > 64
		if i == 9:
			feature_vector[i][0] = 1 if len(text_before_at) > 64 else 0

	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	maybe_email_list = list()
	with open(DATA_FILE, 'r') as f:
		for line in f:
			maybe_email_list.append(line.strip())
	return maybe_email_list


if __name__ == '__main__':
	main()
