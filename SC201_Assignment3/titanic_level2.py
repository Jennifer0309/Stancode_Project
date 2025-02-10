"""
File: titanic_level2.py
Name: Jennifer Li
----------------------------------
This file builds a machine learning algorithm by pandas and sklearn libraries.
We'll be using pandas to read in dataset, store data into a DataFrame,
standardize the data by sklearn, and finally train the model and
test it on kaggle website. Hyper-parameters tuning are not required due to its
high level of abstraction, which makes it easier to use but less flexible.
You should find a good model that surpasses 77% test accuracy on kaggle.
"""

import math
import pandas as pd
from sklearn import preprocessing, linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

TRAIN_FILE = 'titanic_data/train.csv'
TEST_FILE = 'titanic_data/test.csv'


def data_preprocess(filename, mode='Train', training_data=None):
    """
    :param filename: str, the filename to be read into pandas
    :param mode: str, indicating the mode we are using (either Train or Test)
    :param training_data: DataFrame, a 2D data structure that looks like an excel worksheet
                          (You will only use this when mode == 'Test')
    :return: Tuple(data, labels), if the mode is 'Train'; or return data, if the mode is 'Test'
    """
    data = pd.read_csv(filename)
    data.pop('PassengerId')
    data.pop('Name')
    data.pop('Ticket')
    data.pop('Cabin')

    data.loc[data.Sex == 'male', 'sex'] = 1
    data.loc[data.Sex == 'female', 'sex'] = 0
    data.loc[data.Embarked == 'S', 'Embarked'] = 0
    data.loc[data.Embarked == 'C', 'Embarked'] = 1
    data.loc[data.Embarked == 'Q', 'Embarked'] = 2

    if mode == 'Train':
        data.dropna(inplace=True)
        labels = data.pop('Survived')
        return data, labels

    elif mode == 'Test':
        training_data.loc[training_data.Sex == 'male', 'Sex'] = 1
        training_data.loc[training_data.Sex == 'female', 'Sex'] = 0

        training_data.loc[training_data.Embarked == 'S', 'Embarked'] = 0
        training_data.loc[training_data.Embarked == 'C', 'Embarked'] = 1
        training_data.loc[training_data.Embarked == 'Q', 'Embarked'] = 2

        pclass_medium = training_data.Pclass.mean()
        data.Pclass.fillna(pclass_medium, inplace=True)

        sex_medium = 1 if training_data.Sex.mean() > 0.5 else 0
        data.Sex.fillna(sex_medium, inplace=True)

        age_medium = round(training_data.Age.mean(), 3)
        data.Age.fillna(age_medium, inplace=True)

        sibsp_medium = training_data.SibSp.mean()
        data.SibSp.fillna(sibsp_medium, inplace=True)

        parch_medium = training_data.Parch.mean()
        data.Parch.fillna(parch_medium, inplace=True)

        fare_medium = round(training_data.Fare.mean(), 3)
        data.Fare.fillna(fare_medium, inplace=True)

        embarked_medium = training_data.Embarked.mean()
        data.Embarked.fillna(embarked_medium, inplace=True)

        return data


#
# def one_hot_encoding(data, feature):
#     """
#     :param data: DataFrame, key is the column name, value is its data
#     :param feature: str, the column name of interest
#     :return data: DataFrame, remove the feature column and add its one-hot encoding features
#     """
#     if feature == 'Pclass':
#         one_hot = pd.get_dummies(data[feature], prefix=feature)
#         one_hot.columns = ['Pclass_0', 'Pclass_1', 'Pclass_2']
#     else:
#         one_hot = pd.get_dummies(data[feature], prefix=feature)
#     data = pd.concat([data, one_hot], axis=1)
#     data = data.drop(columns=[feature])
#
#     return data

def one_hot_encoding(data, feature, categories=None):
    """
    Ensure consistent One-Hot Encoding so that `train_data` and `test_data` have the same feature names.
    :param data: DataFrame, the dataset to be one-hot encoded
    :param feature: str, column name to be encoded
    :param categories: list, categories from training data (to maintain consistency in test data)
    :return: DataFrame, the one-hot encoded dataset
    """
    if categories is None:
        categories = sorted(data[feature].dropna().unique())  # Get all unique categories and sort them for consistency

    # Convert to pandas categorical type to ensure all categories are considered
    data[feature] = pd.Categorical(data[feature], categories=categories)

    # Perform One-Hot Encoding
    one_hot = pd.get_dummies(data[feature], prefix=feature)

    # Ensure all expected feature columns exist (fill missing categories with 0)
    for cat in categories:
        col_name = f"{feature}_{cat}"
        if col_name not in one_hot.columns:
            one_hot[col_name] = 0

    # Merge the One-Hot Encoded features and drop the original column
    data = pd.concat([data, one_hot], axis=1)
    data.drop(columns=[feature], inplace=True)

    return data, categories  # Return the encoded dataset and the category list


def standardization(data, mode='Train'):
    """
    :param data: DataFrame, key is the column name, value is its data
    :param mode: str, indicating the mode we are using (either Train or Test)
    :return data: DataFrame, standardized features
    """
    scaler = StandardScaler()
    if mode == 'Train':
        data = scaler.fit_transform(data)
    elif mode == 'Test':
        data = scaler.transform(data)
    return data


def main():
    """
    You should call data_preprocess(), one_hot_encoding(), and
    standardization() on your training data. You should see ~80% accuracy on degree1;
    ~83% on degree2; ~87% on degree3.
    Please write down the accuracy for degree1, 2, and 3 respectively below
    (rounding accuracies to 8 decimal places)
    TODO: real accuracy on degree1 -> ______________________
    TODO: real accuracy on degree2 -> ______________________
    TODO: real accuracy on degree3 -> ______________________
    """

    train_data, labels = data_preprocess(TRAIN_FILE, mode='Train')
    test_data = data_preprocess(TEST_FILE, mode='Test', training_data=train_data)

    # train_data = one_hot_encoding(train_data, 'Sex')
    # train_data = one_hot_encoding(train_data, 'Pclass')
    # train_data = one_hot_encoding(train_data, 'Embarked')
    #
    # test_data = one_hot_encoding(test_data, 'Sex')
    # test_data = one_hot_encoding(test_data, 'Pclass')
    # test_data = one_hot_encoding(test_data, 'Embarked')

    # Apply One-Hot Encoding to `train_data` and store category names
    train_data, sex_categories = one_hot_encoding(train_data, 'Sex')
    train_data, pclass_categories = one_hot_encoding(train_data, 'Pclass')
    train_data, embarked_categories = one_hot_encoding(train_data, 'Embarked')

    # Use the same category names in `test_data` to ensure consistency
    test_data, _ = one_hot_encoding(test_data, 'Sex', categories=sex_categories)
    test_data, _ = one_hot_encoding(test_data, 'Pclass', categories=pclass_categories)
    test_data, _ = one_hot_encoding(test_data, 'Embarked', categories=embarked_categories)

    scaler = StandardScaler()
    train_data = scaler.fit_transform(train_data)
    test_data = scaler.transform(test_data)

    for degree in [1, 2, 3]:
        poly = PolynomialFeatures(degree=degree)
        train_poly = poly.fit_transform(train_data)
        test_poly = poly.transform(test_data)

        X_train, X_val, y_train, y_val = train_test_split(train_poly, labels, test_size=0.2, random_state=42)

        model = LogisticRegression(max_iter=10000)
        model.fit(X_train, y_train)
        predictions = model.predict(X_val)
        accuracy = accuracy_score(y_val, predictions)

        print(f"Accuracy for degree {degree}: {accuracy:}")


if __name__ == '__main__':
    main()
