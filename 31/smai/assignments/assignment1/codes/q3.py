import numpy as np
import pandas as pd
#data=np.genfromtxt('decision_tree_train.csv',delimiter=',')

data=pd.read_csv('decision_tree_train.csv',sep=",")
print data
x=data[1:len(data),0:10]
x=np.delete(x,6,1)
y=data[1:len(data),6]
x[:,8:10]=x[:,8:10].astype(str)
print x[1]
print y[1]

