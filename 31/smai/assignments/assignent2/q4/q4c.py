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

model=ElasticNet(alpha=0.00000001,max_iter=1000000, l1_ratio=0.5, fit_intercept=False, normalize=False, tol=0.0000000001)
model.fit(X,Y)

predicted = model.predict(X1)

for i in range(len(predicted)):
        if(predicted[i]>0.5):
                predicted[i]=1
        else:
                predicted[i]=0
	print predicted[i]
a1=metrics.accuracy_score(Y1, predicted)
#print a1
'''     if(a1>maxs):
                maxi=i
                maxs=a1
                maxj=j
        j=j+0.01        
 i=i+0.01
'''
#print maxi
#print maxj
#print a1


