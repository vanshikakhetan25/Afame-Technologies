import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
titanic_data=pd.read_csv(r"C:\Users\hp\Desktop\Titanic.csv")
print(titanic_data.head())
print(titanic_data.isnull().sum())
titanic_data = titanic_data.drop(columns='Cabin', axis=1)
print(titanic_data)
print(titanic_data['Age'])
titanic_data['Age'].fillna(titanic_data['Age'].mean(), inplace=True)

print(titanic_data['Age'])
titanic_data['Embarked'].fillna(titanic_data['Embarked'].mode()[0], inplace=True)
print(titanic_data['Embarked'])
print(titanic_data.isnull().sum())
titanic_data.replace({'Sex':{'male':0,'female':1}, 'Embarked':{'S':0,'C':1,'Q':2}}, inplace=True)
titanic_data2= titanic_data.drop(columns = ['PassengerId', 'Name', 'Ticket', 'Survived'], axis=1)
print(titanic_data2)
X = titanic_data2
Y = titanic_data['Survived']
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

model = LogisticRegression(max_iter=100000000)
model.fit(X_train, Y_train)

X_train_prediction = model.predict(X_train)
predictions=model.predict(X_test)

print(classification_report(Y_test, predictions))
print(confusion_matrix(Y_test, predictions))
 
training_data_accuracy = accuracy_score(Y_train, X_train_prediction)
print('Accuracy score of training data : ', training_data_accuracy)
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(Y_test, X_test_prediction)
print('Accuracy score of test data : ', test_data_accuracy)

