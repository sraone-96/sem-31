import numpy as np
fp=open("mnist_train.csv","r")
array=[]
y=[]
#b=2800000
b=100
flag=0
for i in fp:
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	y.append(j[0])
	a=np.append(a,j[1:])
	a = map(float,a)
	array.append(a)
#print(array)
length=len(array[0])
w=np.zeros(shape=(1,length))
count=0
"""
while True:
	flag=0
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		val=val[0]
		if((val<=0 and y[i]=='1')):#or(val==0 and y[i]=='0')):
			w=np.add(w,array[i])
			flag=1
		elif((val>=0 and y[i]=='0')):#or(val==0 and y[i]=='1')):
			w=np.subtract(w,array[i])
			flag=1
	count+=1
	if(flag==0):
		#print "hie"
		break
#print(count)
fp1=open("mnist_test.csv","r")
for i in fp1:
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	label=j[0]
	a=np.append(a,j[1:])
	a = map(float,a)
	val=np.dot(w,a)
	if(val>0):
		print('1'+label)
	elif(val<0):
		print('0'+label)


#________________________2_________________________
w=np.zeros(shape=(1,length))
count=0
while True:
	flag=0
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		val=val[0]
		if((val<=b and y[i]=='1')):#or(val==0 and y[i]=='0')):
			w=np.add(w,array[i])
			flag=1
		elif((val>=b and y[i]=='0')):#or(val==0 and y[i]=='1')):
			w=np.subtract(w,array[i])
			flag=1
	count+=1
	if(flag==0):
		#print "hie"
		break
#print(count)
fp1=open("mnist_test.csv","r")
for i in fp1:
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	label=j[0]
	a=np.append(a,j[1:])
	a = map(float,a)
	val=np.dot(w,a)
	if(val>0):
		print('1'+label)
	elif(val<0):
		print('0'+label)
"""
#________________________3_________________________
eta=0.005
w=np.zeros(shape=(1,length))
tep=np.zeros(shape=(1,length))
while True:
	flag=0
	tep=np.subtract(tep,tep)
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		val=val[0]
		if((val<=0 and y[i]=='1')):#or(val==0 and y[i]=='0')):
			tep=np.add(tep,array[i])
			flag=1
		elif((val>=0 and y[i]=='0')):#or(val==0 and y[i]=='1')):
			tep=np.subtract(tep,array[i])
			flag=1
	w=np.add(w,tep)
	count+=1
	#print(np.linalg.norm(tep))
	#print(count)
	if(flag==0 or count>3000):
		#print "hie"
		break
#print(count)
fp1=open("mnist_train.csv","r")
for i in fp1:
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	label=j[0]
	a=np.append(a,j[1:])
	a = map(float,a)
	val=np.dot(w,a)
	if(val>0):
		print('1'+label)
	elif(val<0):
		print('0'+label)

"""
#________________________4_________________________
w=np.zeros(shape=(1,length))
count=0
while True:
	flag=0
	tep=np.zeros(shape=(1,length))
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		val=val[0]
		if((val<=b and y[i]=='1')):#or(val==0 and y[i]=='0')):
			tep=np.add(tep,array[i])
			flag=1
		elif((val>=b and y[i]=='0')):#or(val==0 and y[i]=='1')):
			tep=np.subtract(tep,array[i])
			flag=1
	w=np.add(w,tep)
	count+=1
	if(flag==0 or count >100):
		#print "hie"
		break
#print(count)

fp1=open("mnist_test.csv","r")
for i in fp1:
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	label=j[0]
	a=np.append(a,j[1:])
	a = map(float,a)
	val=np.dot(w,a)
	#print(a , val)
	if(val>0):
		print('1'+label)
	elif(val<0):
		print('0'+label)
"""