"""
File: titanic_level1.py
Name: Jennifer Li
----------------------------------
This file builds a machine learning algorithm from scratch 
by Python. We'll be using 'with open' to read in dataset,
store data into a Python dict, and finally train the model and 
test it on kaggle website. This model is the most flexible among all
levels. You should do hyper-parameter tuning to find the best model.
"""

import csv
import math
import pandas as pd
import util

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename: str, data: dict, mode='Train', training_data=None):
    data = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        if mode == "Train":
            data = {key: [] for key in ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']}
        elif mode == "Test":
            data = {key: [] for key in ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']}

        for row in reader:

            if mode == 'Train':
                if row['Age'] != '' and row['Embarked'] != '':
                    data['Survived'].append(int(row['Survived']))
                    data['Pclass'].append(int(row['Pclass']))
                    data['Sex'].append(1 if row['Sex'] == 'male' else 0)
                    data['Age'].append(int(row['Age']))
                    data['SibSp'].append(int(row['SibSp']))  # corrected key frpm 'Sibsp' to 'SibSp'
                    data['Parch'].append(int(row['Parch']))
                    data['Fared'].append(int(row['Fare']))
                    data['Embarkedd'].append({'S': 0, 'C': 1, 'Q': 2}[row['Embarked']])

            elif mode == 'Test':
                if row['Age']:
                    age = float(row['Age'])
                else:
                    age = round(sum(training_data['Age']) / len(training_data['Age']), 3)

                if row['Fare']:
                    fare = float(row['Fare'])
                else:
                    fare = round(sum(training_data['Fare']) / len(training_data['Fare']), 3)

                if row['Embarked']:
                    embarked = {'S': 0, 'C': 1, 'Q': 2}[row['Embarked']]
                else:
                    embarked = round(sum(training_data['Embarked']) / len(training_data['Embarked']), 3)

                data.setdefault('Pclass', []).append(int(row['Pclass']))
                data.setdefault('Sex', []).append(1 if row['Sex'] == 'male' else 0)
                data.setdefault('Age', []).append(age)
                data.setdefault('SibSp', []).append(int(row['SibSp']))
                data.setdefault('Parch', []).append(int(row['Parch']))
                data.setdefault('Fare', []).append(fare)
                data.setdefault('Embarked', []).append(embarked)

    return data


def one_hot_encoding(data: dict, feature: str):
    """
    :param data: dict[str, list], key is the column name, value is its data
    :param feature: str, the column name of interest
    :return data: dict[str, list], remove the feature column and add its one-hot encoding features
    """
    # a ={1,2,3} for i, ele in a: print(i , ele)
    unique_values = set(data[feature])
    for i, value in enumerate(unique_values):
        new_feature_name = f"{feature}_{i}"
        data[new_feature_name] = [1 if item == value else 0 for item in data[feature]]
    data.pop(feature)
    return data


def normalize(data: dict):
    """
    :param data: dict[str, list], key is the column name, value is its data
    :return data: dict[str, list], key is the column name, value is its normalized data
    """

    for key in data:
        min_val = min(data[key])
        max_val = max(data[key])
        data[key] = [(item - min_val) / (max_val - min_val) for item in data[key]]
    return data


def learnPredictor(inputs: dict, labels: list, degree: int, num_epochs: int, alpha: float):
    """
    :param inputs: dict[str, list], key is the column name, value is its data
    :param labels: list[int], indicating the true label for each data
    :param degree: int, degree of polynomial features
    :param num_epochs: int, the number of epochs for training
    :param alpha: float, known as step size or learning rate
    :return weights: dict[str, float], feature name and its weight
    """
    # Step 1 : Initialize weights
    weights = {}  # feature => weight
    keys = list(inputs.keys())
    if degree == 1:
        for i in range(len(keys)):
            weights[keys[i]] = 0
    elif degree == 2:
        for i in range(len(keys)):
            weights[keys[i]] = 0
        for i in range(len(keys)):
            for j in range(i, len(keys)):
                weights[keys[i] + keys[j]] = 0

    def sigmoid(k):
        return 1 / (1 + math.exp(-k))

    for epoch in range(num_epochs):
        if degree == 1:
            for i in range(len(inputs[keys[0]])):
                dot = sum(inputs.get(key)[i] * weights.get(key) for key in weights)
                h = sigmoid(dot)
                for key in weights:
                    weights[key] -= alpha * (h - labels[i]) * inputs[key][i]

        elif degree == 2:
            for key in keys:
                for j in range(key.index(key), len(keys)):
                    new_series = list(inputs[key][k] * inputs[keys[j]][k] for k in range(len(inputs[key])))
                    inputs[key + keys[j]] = new_series
            phi = {}
            for i in range(len(inputs[keys[0]])):
                k = util.dotProduct(weights, phi)
                h = 1 / (1 + math.exp(-k))
                for key in weights.keys():
                    phi[key] = inputs[key][i]
                dot = sum(phi.get(key, 0) * weights.get(key, 0) for key in weights)
                h - sigmoid(dot)
                util.increment(weights, -(h - labels[i] * alpha, phi))
        return weights
