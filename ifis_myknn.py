import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class myKNN():
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
    def predict(self, x_test):
        predictions = []
        for row in x_test:
            label = random.choice(self.y_train)
            predictions.append(label)
        return predictions
# 훈련데이터

iris = datasets.load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)

clf = myKNN()
clf.fit(x_train, y_train)
predictions = clf.predict(x_test)

print(accuracy_score(y_test, predictions))