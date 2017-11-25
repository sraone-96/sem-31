import numpy as np
import sys
from sklearn import linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

data = np.genfromtxt("train.csv", delimiter=",")
data1 = np.genfromtxt("test.csv", delimiter=",")
X=data[:,0:11]
Y=data[:,11]
X1=data1[:,0:11]
Y1=data1[:,11]

model=LogisticRegression()
model.fit(X,Y)
predicted = model.predict(X1)
#print predicted
a1=metrics.accuracy_score(Y1, predicted)
print a1

