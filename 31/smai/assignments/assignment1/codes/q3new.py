import numpy as np
def qual(f[],length):
	

data=np.genfromtxt('decision_tree_train.csv',delimiter=",",dtype=None)
f0=data[1:len(data),0]
f1=data[1:len(data),1]
f2=data[1:len(data),2]
f3=data[1:len(data),3]
f4=data[1:len(data),4]
f5=data[1:len(data),5]
f6=data[1:len(data),7]
f7=data[1:len(data),8]
f8=data[1:len(data),9]


sales=0
accounting=0
technical=0
management=0
it=0
product_mng=0
marketing=0 
RandD=0
support=0
hr=0

for i in f7:
	
for j in f8:
	
