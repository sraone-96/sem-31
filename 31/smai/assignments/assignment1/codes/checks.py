import csv
import numpy as np
#file1=open('mnist_train.csv',"rb")
#reader=csv.reader(file1,delimiter=",")
#data=list(reader)


test=np.genfromtxt('../datasets/q1/train.csv',delimiter=',')
data2=np.genfromtxt('../datasets/q1/test.csv',delimiter=',')


x=test[:,1:]
y=test[:,0]
x=x.astype(np.int)
y=y.astype(np.int)
#print type(x)
#print type(y)
'''count=0
for i in y:
	if(i==1):
		count+=1
		print count-1
		break 

input(count)
'''
'''for i in test:
	temp=i[1:len(i)]
	temp=map(int,temp)	
	x.append(temp)
	temp2=i[0]
	temp2=np.astype(np.int64)
	y.append(temp2)
'''
	
#x=x.astype(float)
#y=y.astype(float)
#print y
w=np.random.random(len(x[0]))
w=w.astype(int)
#print w
b=28000
#print w
counter=0
temp3=[]
z=10
error=123
#for i in x[0:5]:
#	print len(i)
while(error>0):
	error=0
	for i in x:
#                print i.shape,w.shape
		#print i
		#temp3=np.multiply(i,w)
		temp3=np.multiply(i,w)
		#print np.sum(w-i)
		#print np.sum(temp3)
#                print np.sum(temp3)
		if (np.sum(temp3)>b and y[counter]==0):
#					print "changed"
					w=w-i
		elif(np.sum(temp3)<=b and y[counter]==1):
#					print counter
					w=w+i
#					print "changed w"
		counter=counter+1
		#print w
	counter=0
	for i in x:
		temp3=i*w
		if np.sum(temp3)>b:
			#g.append(1)
			if(y[counter]!=1):
				error=error+1
                elif np.sum(temp3)<b:
			#g.append(0)
			if(y[counter]!=0):
				error=error+1
		counter=counter+1
	counter=0
        print error
#print error

'''

x=data2[:,:]
x=x.astype(np.int)
#=np.random.random(len(x[0]))
#w=w.astype(int)
for i in x:
	tempos=np.multiply(i,w)
	if(np.sum(tempos)>0):
		print "1"
	elif(np.sum(tempos)<=0):
		print 0


'''
