"""
File: boston_housing_competition.py
Name: pei yin Li
--------------------------------
This file demonstrates how to analyze boston
housing dataset. Students will upload their 
results to kaggle.com and compete with people
in class!

You are allowed to use pandas, sklearn, or build the
model from scratch! Go data scientists!
"""

import pandas as pd
from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt
import math


# from sklearn.model_selection import train_test_split, cross_val_score
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeRegressor
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics import mean_squared_error
# import matplotlib.pyplot as plt


def main():
    train_data = pd.read_csv('boston_housing/train.csv')
    print(train_data.count())
    y = train_data.medv
    x_train = np.array(train_data.rm).reshape(-1, 1)
    h = linear_model.LinearRegression()
    regressor = h.fit(x_train, y)
    print(sum(regressor.predict(x_train)) / len(x_train))

# def main():
#     # Load the data
#     train_data = pd.read_csv('train.csv')
#     test_data = pd.read_csv('test.csv')
#
#     # Prepare the data
#     y = train_data['medv']
#     X = train_data.drop(columns=['ID', 'medv'])
#     X_test = test_data.drop(columns=['ID'])
#
#     # Split the data for validation
#     X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
#
#     # Standardize the features
#     scaler = StandardScaler()
#     X_train_scaled = scaler.fit_transform(X_train)
#     X_val_scaled = scaler.transform(X_val)
#     X_test_scaled = scaler.transform(X_test)
#
#     # Define models to train
#     models = {
#         'Linear Regression': LinearRegression(),
#         'Decision Tree': DecisionTreeRegressor(random_state=42),
#         'Random Forest': RandomForestRegressor(random_state=42),
#         'Gradient Boosting': GradientBoostingRegressor(random_state=42)
#     }
#
#     # Train and evaluate each model
#     for name, model in models.items():
#         model.fit(X_train_scaled, y_train)
#         val_predictions = model.predict(X_val_scaled)
#         mse = mean_squared_error(y_val, val_predictions)
#         rmse = np.sqrt(mse)
#         cv_scores = cross_val_score(model, X_train_scaled, y_train, cv=5, scoring='neg_mean_squared_error')
#         cv_rmse = np.sqrt(-cv_scores).mean()
#         print(f"{name} - Validation RMSE: {rmse}, Cross-Validation RMSE: {cv_rmse}")
#
#     # Choose the best model (for simplicity, we'll choose Gradient Boosting)
#     best_model = GradientBoostingRegressor(random_state=42)
#     best_model.fit(scaler.fit_transform(X), y)
#
#     # Predict on the test data
#     test_predictions = best_model.predict(X_test_scaled)

    # Prepare the submission file
    submission = pd.DataFrame({'ID': train_data['ID'], 'medv': train_data})
    submission.to_csv('submission.csv', index=False)
    print("Submission file has been created.")


#
#     # build model my ourselves
#     x_train = train_data.rm
#     # h = wx + b
#     w, b, c = 0, 0, 0.6
#     alpha = 0.01
#     num_epoch = 80
#     history = []
#     for epoch in range(num_epoch):
#         total = 0
#         for i in range(len(x_train)):
#             x = x_train[i]
#             label = y[i]
#             h = w * x + b
#             loss = (h - label) ** 2 * (sign(h - label) - c) ** 2
#             total += loss
#             # G.D
#             w = w - alpha * (2 * (h - label) * x * (sign(h - label) - c) ** 2)
#             b = b - alpha * (2 * (h - label) * 1 * (sign(h - label) - c) ** 2)
#         history.append(total / len(x_train))
#     plt.plot(history)
#     plt.show()
#
#     predictions = []
#     for x in x_train:
#         predictions.append(w * x + b)
#     print(sum(predictions) / len(predictions))
#
#
# def sign(data):
#     if data > 0:
#         return 1
#     elif data == 0:
#         return 0
#     else:
#         return -1


if __name__ == '__main__':
    main()
