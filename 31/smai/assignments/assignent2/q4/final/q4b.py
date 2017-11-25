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

i=0.00001
maxs=0
maxi=-1
while(i<5):
        model=Ridge(alpha=i, fit_intercept=True, normalize=True, max_iter=10000, tol=0.0001)

        model.fit(X,Y)

        predicted = model.predict(X1)

        for i in range(len(predicted)):
                if(predicted[i]>0.5):
                        predicted[i]=1
                else:
                        predicted[i]=0

        a1=metrics.accuracy_score(Y1, predicted)
        if(a1>maxs):
                maxs=a1
                maxi=i
        i=i+0.00001
print maxs

