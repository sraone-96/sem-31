import numpy as np
import sys
from sklearn import linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
data=np.genfromtxt(sys.argv[1],delimiter=",")
data1=np.genfromtxt(sys.argv[2],delimiter=",")
#print train[0]

X=data[:,0:11]
Y=data[:,11]
X1=data1[:,0:11]
Y1=data1[:,11]

i=0.00000001
maxs=0
maxi=-1
'''while(i==0.0001):
        model=Ridge(alpha=i, fit_intercept=True, normalize=True, max_iter=10000, tol=0.0001)

        model.fit(X,Y)

        predicted = model.predict(X1)

        for j in range(len(predicted)):
                if(predicted[j]>0.5):
                        predicted[j]=1
                else:
                        predicted[j]=0

        a1=metrics.accuracy_score(Y1, predicted)
        if(a1>maxs):
                maxs=a1
                maxi=i
        i=i+0.00001

'''



model=Ridge(alpha=i, fit_intercept=True, normalize=True, max_iter=10000, tol=0.0001)
model.fit(X,Y)

predicted = model.predict(X1)
for j in range(len(predicted)):
 if(predicted[j]>0.5):
    predicted[j]=1
 else:
    predicted[j]=0
 print predicted[j]	
a1=metrics.accuracy_score(Y1, predicted)

#print a1

