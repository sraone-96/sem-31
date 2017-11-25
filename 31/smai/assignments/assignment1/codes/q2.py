import numpy as np
import math
import pandas as pd
data=np.genfromtxt('../datasets/q2/train.csv',delimiter=',')
w=[]
data=np.delete(data,0,axis=1)
y=np.zeros(len(data))
for i in range(0,len(data)):
	y[i]=data[i][9]

indices=[]
#print len(data)

for i in range(len(data)):
		for j in range(len(data[0])):
			if(math.isnan(data[i][j])):
				indices.append(i)


#print indices
for i in range(len(indices)):
	data=np.delete(data,indices[i],axis=0)
	indices[:]=[a-1 for a in indices];
				
#print len(data),"changed"
data=np.delete(data,9,axis=1)

#print y[0]
na=0.01
epoch=0
b=20
val=0
#data=data.astype(float)
#print data[0]
#print data
count=0
we=np.zeros((9,1))
for epoch in range(0,200):
	error=0
	for i in range(0,len(data)):
		temp=np.multiply(data[i],we)
		val=np.sum(temp)
		if(val>=b and y[i]==2):
			w.append([we,count])
			we=we-data[i]
			count=1
		
		elif(val<=b and y[i]==4):	
			w.append([we,count])
			we=we+data[i]
			count=1
			
			
		else:
			count=count+1



#for weight,count in w:
#	print weight,count
'''
	for j in range(0,len(data)):
		temp2=np.multiply(data[j],w) 
		val2=np.sum(temp2)
		if(val2>b and y[j]==2):
			error=error+1
		elif(val2<=b and y[j]==4):
			error=error+1
	print "error=",error
		


'''

data1=np.genfromtxt('../datasets/q2/test.csv',delimiter=',')
data1=np.delete(data1,0,axis=1)
y1=np.zeros(len(data1))
for i in range(0,len(data1)):
        y1[i]=data1[i][9]


err=0
data1=np.delete(data1,9,axis=1)

for j in range(len(data1)):
	sums=0
	for weight,cnt in w:
		tempo=(np.sum(np.multiply(weight,data1[j])))
		if(tempo>0):
			sums=sums+cnt
		else:
			sums=sums-cnt
	print sums	
	if(sums>0 and y1[j]==2):
			err=err+1
	elif(sums<=0 and y1[j]==4):
			err=err+1
print err
