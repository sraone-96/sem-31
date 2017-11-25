import numpy as np
import sys
fp=open(sys.argv[1],"r")
array=[]
y=[]
b=0.5
flag=0
for i in fp:
	if "?" in i or i=="":
		continue
	if(i[len(i)-1]=='\n'):
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
count=0
cnt=0
eta=0.05
while True:
	flag=0
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		if(val>=b and y[i]=='2'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.subtract(w,np.multiply(array[i],mul))
			flag=1
		elif(val<=b and y[i]=='4'):
			mul=(eta * abs(val-b))/np.dot(array[i],array[i])
			w=np.add(w,np.multiply(array[i],mul))
			flag=1

		
		# if((val<=b and y[i]=='2') or (val>=b and y[i]=='4')):
		# 	nom=np.linalg.norm(array[i])
		# 	mul=(eta*(b-val))/np.dot(array[i],array[i])
		# 	kk=np.multiply(array[i],mul)
		# 	w=np.add(w,kk)
		# 	flag=1
		# elif((val>=b and y[i]=='4')):
		# 	nom=np.linalg.norm(array[i])
		# 	mul=(eta*(val-b))/(nom**2)
		# 	w=np.subtract(w,np.multiply(array[i],mul))
		# 	flag=1
	count+=1
	if(flag==0 or count >200):
		#print "hie"
		break
fp1=open("train.csv","r")
print(w)
for i in fp1:
	if "?" in i or i=="":
		continue
	if(i[len(i)-1]=='\n'):
		i=i[0:len(i)-1]
	i=i[0:len(i)-1]
	a=np.array([])
	j=i.split(',')
	length=len(j)
	label=j[length-1]
	a=np.append(a,j[1:length-1])
	a = map(float,a)
	#print(a)
	val=np.dot(w,a)
	#print val
	if(val<b):
		print('2'+label)
	elif(val>b):
		print('4'+label)
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
	#print(a)
	val=np.dot(w,a)
	#print val
	if(val<b):
		print('2'+label)
	elif(val>b):
		print('4'+label)