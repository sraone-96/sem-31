import numpy as np
import math
import pandas as pd
data=np.genfromtxt('../datasets/q2/train.csv',delimiter=',')
w=np.zeros((9,1))
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
b=0.5
val=0
#data=data.astype(float)
#print data[0]
#print data



for epoch in range(0,200):
	#print "epoch=",epoch
	error=0
	#print w
	for i in range(0,len(data)):
		temp=np.multiply(data[i],w)
		#print temp
		val=np.sum(temp)
		#print val
		if(val>b and y[i]==2):
			w=w+na*((data[i]*((b-val))/(np.linalg.norm(data[i])) ))
		elif(val<=b and y[i]==4):	
			w=w+na*(( data[i]*((b-val))/(np.linalg.norm(data[i])) ))

	for j in range(0,len(data)):
		temp2=np.multiply(data[j],w) 
		val2=np.sum(temp2)
		if(val2>b and y[j]==2):
			error=error+1
		elif(val2<=b and y[j]==4):
			error=error+1
	print epoch
	print "error=",error
		

print w

data1=np.genfromtxt('../datasets/q2/test.csv',delimiter=',')

data1=np.delete(data1,0,axis=1)
y=np.zeros(len(data1))
for i in range(0,len(data1)):
	y[i]=data1[i][9]


err=0
data1=np.delete(data1,9,axis=1)
for i in range(0,len(data1)):
	temps=np.multiply(data1[i],w)
	vals=np.sum(temps)
	if(vals>b and y[i]==2):
			err=err+1
	elif(vals<=b and y[i]==4):	
#			w=w+na*((b-val)*y[i])/(y[i]*y[i])
			err=err+1

print err
