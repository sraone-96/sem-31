import numpy as np
def perceptronbatch():
	array=np.genfromtxt('mnist_train.csv',delimiter=",")
	print array
	length=len(array[0])-1
	w=np.zeros(shape=(1,length))
	count=0
	while True:
		flag=0
		tep=np.zeros(shape=(1,length))
		for i in range(0,len(array)):
			vec=array[i][1:]
			val=np.dot(w,vec)
			if val<=0 and array[i][0]==1:
				tep=np.add(tep,vec)
				flag=1
			elif val>=0 and array[i][0]==0:
				tep=np.subtract(tep,vec)
				flag=1
		w=np.add(w,tep)
		count+=1
		if(flag==0):
			break
	array=np.genfromtxt('mnist_test.csv',delimiter=",")
	for i in range(0,len(array)):
		vec=array[i][1:]
		val=np.dot(w,vec)
		if(val>0):
			print('1'+str(array[i][0]))
		elif(val<0):
			print('0'+str(array[i][0]))


def perceptronbatchmargin():
	b=1000
	array=np.genfromtxt('mnist_train.csv',delimiter=",")
	print array
	length=len(array[0])-1
	w=np.zeros(shape=(1,length))
	count=0
	while True:
		flag=0
		tep=np.zeros(shape=(1,length))
		for i in range(0,len(array)):
			vec=array[i][1:]
			val=np.dot(w,vec)
			if val<=b and array[i][0]==1:
				tep=np.add(tep,vec)
				flag=1
			elif val>=b and array[i][0]==0:
				tep=np.subtract(tep,vec)
				flag=1
		w=np.add(w,tep)
		count+=1
		if(flag==0):
			break
	array=np.genfromtxt('mnist_test.csv',delimiter=",")
	for i in range(0,len(array)):
		vec=array[i][1:]
		val=np.dot(w,vec)
		if(val>0):
			print('1'+str(array[i][0]))
		elif(val<0):
			print('0'+str(array[i][0]))


#perceptronbatch()
perceptronbatchmargin()