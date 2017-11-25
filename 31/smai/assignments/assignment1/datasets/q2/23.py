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
c=[0.0 for i in range(0,len(y)+1)]
eta=0.05
count=0
weighted_percp=[]
c=0
while True:
	flag=0
	for i in range(0,len(y)):
		val=np.dot(w,array[i])
		if(val>=b and y[i]=='2'):
			weighted_percp.append([w,c])
			w=np.subtract(w,array[i])
			flag=1
			c=1
		elif(y[i]=='2'):
			c+=1
		elif(val<=b and y[i]=='4'):
			weighted_percp.append([w,c])
			w=np.add(w,array[i])
			flag=1
			c=1
		elif(y[i]=='4'):
			c+=1
	count+=1
	if(flag==0 or count >200):
		break
# w=np.zeros(shape=(1,length))
# summ=0
# for i in range(0,len(y)+1):
# 	summ+=c[i]
# while True:
# 	flag=0
# 	for i in range(0,len(y)):
# 		# if(c[i]==0):
# 		# 	continue
# 		val=np.dot(w,array[i])
# 		if(val>=b and y[i]=='2'):
# 			print c[i]/summ
# 			w=np.subtract(w,np.multiply(array[i],c[i]/summ))
# 			flag=1
			
# 		elif(val<=b and y[i]=='4'):
# 			w=np.add(w,np.multiply(array[i],c[i]/summ))
# 			flag=1

# 	count+=1
# 	if(flag==0 or count >500):
# 		break
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
	summ=0
	for wght in weighted_percp:
		val=np.dot(wght[0],a)
		if(val<0):
			summ-=wght[1]
		elif(val>0):
			summ+=wght[1]
	print(summ)
	if(summ<0):
		print('2'+label)
	elif(summ>0):
		print('4'+label)
	# val=np.dot(w,a)
	# print val
	# if(val<0):
	# 	print('2'+label)
	# elif(val>0):
	# 	print('4'+label)