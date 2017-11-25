import numpy as np
import sys
from sklearn import linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import Lasso
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet
#train=np.genfromtxt(sys.argv[1],delimiter=",")
#test=np.genfromtxt(sys.argv[2],delimiter=",")
#print train[0]
data = np.genfromtxt("train.csv", delimiter=",")
data1 = np.genfromtxt("test.csv", delimiter=",")
#data=train
#data1=test
X=data[:,0:11]
Y=data[:,11]
X1=data1[:,0:11]
Y1=data1[:,11]
alll=0.000000001
model=Lasso(alpha=alll, fit_intercept=False, max_iter=100000,normalize=False, random_state=None,tol=0.000001, warm_start=True)
model.fit(X,Y)

predicted = model.predict(X1)

for i in range(len(predicted)):
	if(predicted[i]>0.5):
		predicted[i]=1
	else:
		predicted[i]=0

a1=metrics.accuracy_score(Y1, predicted)
print a1   
i=0.00001
maxs=0
maxi=-1
while(i<5):
	model=Ridge(alpha=alll, fit_intercept=True, normalize=True, max_iter=10000, tol=0.0001)

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
#print maxi
#i=0.1
#j=0.1   
#maxs=0
#maxj=0.0
#maxi=0.1
#while(i<25):
# j=0.1		
# while(j<0.9):	
model=ElasticNet(alpha=alll,max_iter=1000000, l1_ratio=0.5, fit_intercept=False, normalize=False, tol=0.0000000001)
model.fit(X,Y)

predicted = model.predict(X1)

for i in range(len(predicted)):
	if(predicted[i]>0.5):
		predicted[i]=1
	else:
		predicted[i]=0
a1=metrics.accuracy_score(Y1, predicted)
#print a1
'''	if(a1>maxs):
		maxi=i
		maxs=a1
		maxj=j
	j=j+0.01	
 i=i+0.01
'''
#print maxi
#print maxj
print a1   

model=LogisticRegression()
model.fit(X,Y)
predicted = model.predict(X1)
#print predicted
a1=metrics.accuracy_score(Y1, predicted)
print a1
