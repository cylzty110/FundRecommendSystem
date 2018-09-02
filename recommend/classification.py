from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


def SVM(train_x, train_y):
    clf = svm.SVC()
    clf.fit(train_x, train_y)
    return clf


def LR(train_x, train_y):
    clf = LogisticRegression()
    clf.fit(train_x, train_y)
    return clf






