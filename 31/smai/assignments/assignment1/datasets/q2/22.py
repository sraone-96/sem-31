import numpy as np
fp=open("train.csv","r")
array=[]
y=[]
b=0.5
flag=0
for i in fp:
	if "?" in i or i=="":
		continue
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	length=len(j)
	y.append(j[length-1])
	a=np.append(a,j[1:length-1])
	a = map(float,a)
	array.append(a)
length=len(array[0])
#print(array)
w=np.zeros(shape=(1,length))
c=[0 for i in range(0,len(y))]
eta=0.05
count=0
while True:
	flag=0
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		if(val>=b and y[i]=='2'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.subtract(w,np.multiply(array[i],mul))
			flag=1
			c[i]=0
		elif(y[i]=='2'):
			c[i]+=1
		elif(val<=b and y[i]=='4'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.add(w,np.multiply(array[i],mul))
			flag=1
			c[i]=0
		elif(y[i]=='4'):
			c[i]+=1
	count+=1
	if(flag==0 or count >500):
		break
w=np.zeros(shape=(1,length))
while True:
	flag=0
	for i in range(0,len(y)):
		if(c[i]==0):
			continue
		val=np.dot(w,array[i])
		if(val>=b and y[i]=='2'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.subtract(w,np.multiply(array[i],mul))
			flag=1
			
		elif(val<=b and y[i]=='4'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.add(w,np.multiply(array[i],mul))
			flag=1

	count+=1
	if(flag==0 or count >500):
		break
fp1=open("test.csv","r")
print(w)
for i in fp1:
	if "?" in i:
		continue
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	length=len(j)
	label=j[length-1]
	a=np.append(a,j[1:length-1])
	a = map(float,a)
	print(a)
	val=np.dot(w,a)
	print val
	if(val<b):
		print('2'+label)
	elif(val>b):
		print('4'+label)