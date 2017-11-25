import numpy as np
from collections import defaultdict
import math
array=[]
left=[]

class Tree(object):
	def __init__(self,name="root",value="",children=None):
		self.name=name
		self.value=value
		self.children=[]
		if children is not None:
			for child in children:
				self.add_child(child)
	def add_child(self,node):
		#assert isinstance(node,Tree)
		self.children.append(node)

def entropy(index):
	entr=0
	ret=[]
	total_length=0
	for ind in range(0,len(index)):
		total_length+=len(index[ind])
	for ind in range(0,len(index)):
		n=0.0
		p=0.0
		for i in index[ind]:
			if(left[i]==0):
				n+=1
			else:
				p+=1

		if(n==0 or p==0):
			ret.append(0)
		else:
			ret.append((len(index[ind])/(1.0*total_length))*((-1*(n/(n+p))*np.log2((n/(n+p))))+(-1*(p/(n+p))*np.log2((p/(n+p))))))
	return ret

def calculate_entropy(index,name_list):
	ret_name=""
	ret_val=1000000
	ret_avg1=0
	ret_index=[]
	flag=0
	
	if("sl_v" not in name_list):
		tempo=[sl_v[i] for i in index]
		ret_avg1=sum(tempo)/len(tempo)
		neg=[i for i in index if sl_v[i]<=ret_avg1]
		pos=[i for i in index if sl_v[i]>ret_avg1]
		ret_index=[neg,pos]
		[n,p]=entropy(ret_index)
		ret_val=n+p
		ret_name="sl_v"
		ret_index=[[n,neg],[p,pos]]
		index11=ret_index
		flag=1
		

	if("l_ev" not in name_list):
		tempo=[l_ev[i] for i in index]
		ret_avg=sum(tempo)/len(tempo)
		neg=[i for i in index if l_ev[i]<=ret_avg]
		pos=[i for i in index if l_ev[i]>ret_avg]
		ret_index=[neg,pos]
		[n,p]=entropy(ret_index)
		if(n+p < ret_val):
			ret_val=n+p
			ret_name="l_ev"
			ret_avg1=ret_avg
			ret_index=[[n,neg],[p,pos]]
			index11=ret_index
		flag=1
	
	if("n_p" not in name_list):
		tempo=[n_p[i] for i in index]
		#ret_avg=sum(tempo)/len(tempo)
		ret_avg=-1
		two=[i for i in index if n_p[i]==2]
		three=[i for i in index if n_p[i]==3]
		four=[i for i in index if n_p[i]==4]
		five=[i for i in index if n_p[i]==5]
		six=[i for i in index if n_p[i]==6]
		seven=[i for i in index if n_p[i]==7]
		ret_index=[two,three,four,five,six,seven]
		[to,tr,fr,fe,sx,sn]=entropy(ret_index)

		if(to+tr+fr+fe+sx+sn < ret_val):
			ret_val=to+tr+fr+fe+sx+sn
			ret_name="n_p"
			ret_avg1=ret_avg
			ret_index=[[to,two],[tr,three],[fr,four],[fe,five],[sx,six],[sn,seven]]
			index11=ret_index
		flag=1
	
	if("av_hr" not in name_list):
		tempo=[av_hr[i] for i in index]
		ret_avg=sum(tempo)/len(tempo)
		neg=[i for i in index if av_hr[i]<=ret_avg]
		pos=[i for i in index if av_hr[i]>ret_avg]
		ret_index=[neg,pos]
		[n,p]=entropy(ret_index)

		if(n+p < ret_val):
			ret_val=n+p
			ret_name="av_hr"
			ret_avg1=ret_avg
			ret_index=[[n,neg],[p,pos]]
			index11=ret_index
		flag=1
	
	if("tim" not in name_list):
		tempo=[tim[i] for i in index]
		#ret_avg=sum(tempo)/len(tempo)
		ret_avg=-1
		one=[i for i in index if tim[i]==1]
		two=[i for i in index if tim[i]==2]
		three=[i for i in index if tim[i]==3]
		four=[i for i in index if tim[i]==4]
		five=[i for i in index if tim[i]==5]
		six=[i for i in index if tim[i]==6]
		seven=[i for i in index if tim[i]==7]
		eight=[i for i in index if tim[i]==8]
		nine=[i for i in index if tim[i]==9]
		ten=[i for i in index if tim[i]==10]
		ret_index=[one,two,three,four,five,six,seven,eight,nine,ten]
		[oe,to,te,fr,fe,sx,sn,et,ne,tn]=entropy(ret_index)

		if(oe+to+te+fr+fe+sx+sn+et+ne+tn < ret_val):
			ret_val=oe+to+te+fr+fe+sx+sn+et+ne+tn
			ret_name="tim"
			ret_avg1=ret_avg
			ret_index=[[oe,one],[to,two],[te,three],[fr,four],[fe,five],[sx,six],[sn,seven],[et,eight],[ne,nine],[tn,ten]]
			index11=ret_index
		flag=1

	if("w_ac" not in name_list):
		
		ret_avg=0
		neg=[i for i in index if w_ac[i]<=ret_avg]
		pos=[i for i in index if w_ac[i]>ret_avg]
		ret_index=[neg,pos]
		[n,p]=entropy(ret_index)

		if(n+p < ret_val):
			ret_val=n+p
			ret_name="w_ac"
			ret_avg1=ret_avg
			ret_index=[[n,neg],[p,pos]]
			index11=ret_index
		flag=1

	if("prom" not in name_list):
		
		ret_avg=0
		neg=[i for i in index if prom[i]<=ret_avg]
		pos=[i for i in index if prom[i]>ret_avg]
		ret_index=[neg,pos]
		[n,p]=entropy(ret_index)

		if(n+p < ret_val):
			ret_val=n+p
			ret_name="prom"
			ret_avg1=ret_avg
			ret_index=[[n,neg],[p,pos]]
			index11=ret_index
		flag=1

	if("sales" not in name_list):
		
		sals=[i for i in index if sales[i]=="sales"]
		acctng=[i for i in index if sales[i]=="accounting"]
		tech=[i for i in index if sales[i]=="technical"]
		manag=[i for i in index if sales[i]=="management"]
		it=[i for i in index if sales[i]=="IT"]
		pro_man=[i for i in index if sales[i]=="product_mng"]
		rnd=[i for i in index if sales[i]=="RandD"]
		mark=[i for i in index if sales[i]=="marketing"]
		hr=[i for i in index if sales[i]=="hr"]
		sup=[i for i in index if sales[i]=="support"]

		ret_index=[sals,acctng,tech,manag,it,pro_man,rnd,mark,hr,sup]
		[sa,ac,te,mg,iit,pm,rn,mk,hir,sp]=entropy(ret_index)

		if((sa+ac+te+mg+iit+pm+rn+mk+hir+sp) < ret_val):
			ret_val=sa+ac+te+mg+iit+pm+rn+mk+hir+sp
			ret_name="sales"
			ret_avg1=-1
			ret_index=[[sa,sals],[ac,acctng],[te,tech],[mg,manag],[iit,it],[pm,pro_man],[rn,rnd],[mk,mark],[hir,hr],[sp,sup]]
			index11=ret_index
		flag=1

	if("salary" not in name_list):
		
		high=[i for i in index if salary[i]=="high"]
		med=[i for i in index if salary[i]=="medium"]
		low=[i for i in index if salary[i]=="low"]
		ret_index=[high,med,low]
		[h,m,l]=entropy(ret_index)

		if(h+m+l < ret_val):
			ret_val=h+m+l
			ret_name="salary"
			ret_avg1=-1
			ret_index=[[h,high],[m,med],[l,low]]
			index11=ret_index
		flag=1
	if(flag==0):
		index11=[]

	return ret_val,ret_name,ret_avg1,index11


def valueFinder(tepp,tree):
	name=tree.name
	if(len(tree.children)<1):
		return -1
	if(name!="salary" and name!="sales" and name!="n_p" and name!="tim"):
		#print(name,tepp[name],tree.value)
		if(float(tepp[name])<=tree.value):
			try:
				k=tree.children[0]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		else:
			try:
				k=tree.children[1]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

	elif(name=="tim"):
		#print(name,tepp[name])
		if(float(tepp[name])==1):
			try:
				k=tree.children[0]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==2):
			try:
				k=tree.children[1]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==3):
			try:
				k=tree.children[2]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==4):
			try:
				k=tree.children[3]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==5):
			try:
				k=tree.children[4]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==6):
			try:
				k=tree.children[5]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==7):
			try:
				k=tree.children[6]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==8):
			try:
				k=tree.children[7]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==9):
			try:
				k=tree.children[8]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==10):
			try:
				k=tree.children[9]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

	elif(name=="salary"):
		#print(name,tepp[name])
		if(tepp[name]=="high"):
			try:
				k=tree.children[0]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="medium"):
			try:
				k=tree.children[1]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="low"):
			try:
				k=tree.children[2]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
	elif(name=="n_p"):
		#print(name,tepp[name])
		if(float(tepp[name])==2):
			try:
				k=tree.children[0]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==3):
			try:
				k=tree.children[1]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==4):
			try:
				k=tree.children[2]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(float(tepp[name])==5):
			try:
				k=tree.children[3]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==6):
			try:
				k=tree.children[4]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(float(tepp[name])==7):
			try:
				k=tree.children[5]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		

	elif(name=="sales"):
		#print(name,tepp[name])
		if(tepp[name]=="sales"):
			try:
				k=tree.children[0]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="accounting"):
			try:
				k=tree.children[1]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="technical"):
			try:
				k=tree.children[2]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(tepp[name]=="management"):
			try:
				k=tree.children[3]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="IT"):
			try:
				k=tree.children[4]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="product_mng"):
			try:
				k=tree.children[5]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(tepp[name]=="RandD"):
			try:
				k=tree.children[6]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="marketing"):
			try:
				k=tree.children[7]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

		elif(tepp[name]=="hr"):
			try:
				k=tree.children[8]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)
		elif(tepp[name]=="support"):
			try:
				k=tree.children[9]
			except:
				return -1
			if(type(k)!=Tree):
				return k
			else:
				return valueFinder(tepp,k)

	return -1


def makedecision(stng,tree):
	tep=defaultdict(str)
	j=stng.split(',')
	tep["sl_v"]=j[0]
	tep["l_ev"]=j[1]
	tep["n_p"]=j[2]
	tep["av_hr"]=j[3]
	tep["tim"]=j[4]
	tep["w_ac"]=j[5]
	tep["prom"]=j[7]
	tep["sales"]=j[8]
	tep["salary"]=j[9]
	k=valueFinder(tep,tree)
	return int(k)

def printTree(tree):
	strng=tree.name+"--"
	for i in tree.children:
		if(type(i)==Tree):
			strng+=i.name+" "
		else:
			strng+=str(i)+" "
	print(strng)
	for i in tree.children:
		if(type(i)==Tree):
			printTree(i)

def appender(tree1,name1,tree2):
	if(tree1.name==name1):
		#print("hie")
		tree1.add_child(tree2)
		#return tree1
	else:
		for child in tree1.children:
			if (type(child)==Tree):
				return appender(child,name1,tree2)
		#return tree1



def buildtree(tree,prev_name,name_list,index1):
	collective_entropy=0
	#print(prev_name)

	for i in range(0,len(index1)):

		if(index1[i][0]==0):
			if(len(index1[i][1])!=0):
				#appender(tree,prev_name,left[index1[i][1][0]])
				tree.add_child(left[index1[i][1][0]])
			else:
				#appender(tree,prev_name,-1)
				tree.add_child(-1)
		else:
			#print(calculate_entropy(index1[i][1],name_list))
			entr,name,val,index=calculate_entropy(index1[i][1],name_list)
			# print(name)
			# print(index)
			if(entr>1):
				return tree
			tokka=[j for j in name_list]
			#tokka.append(name)
			temp=Tree()
			temp.name=name
			temp.value=val
			#appender(tree,prev_name,temp)
			
			tree.add_child(temp)

			buildtree(temp,name,tokka,index)
			# tree=appender(tree,prev_name,temp)
			# print(tree.name)
			# tree=buildtree(tree,name,tokka,index)
			#print(tree.name)
			collective_entropy+=entr	
	#return tree
	#if(collective_entropy==0 or collective_entropy==1000000):
	#	return tree

sl=[]
names=defaultdict(int)
names["sl_v"]=0
names["l_ev"]=0
names["n_p"]=0
names["av_hr"]=0
names["tim"]=0
names["w_ac"]=0
names["prom"]=0
names["sales"]=0
names["salary"]=0

#sl_v,l_ev,n_p,av_hr,tim,w_ac,left,prom,sales,salary
sl_v=[]
l_ev=[]
n_p=[]
av_hr=[]
tim=[]
w_ac=[]
prom=[]
sales=[]
salary=[]


fp=open("train.csv","r")
t_len=0
for i in fp:
	if(i[0]=='s'):
		continue
	t_len+=1
	i=i[0:len(i)-1]
	j=i.split(',')
	sl_v.append(float(j[0]))
	l_ev.append(float(j[1]))
	n_p.append(float(j[2]))
	av_hr.append(float(j[3]))
	tim.append(float(j[4]))
	w_ac.append(float(j[5]))
	left.append(float(j[6]))
	prom.append(float(j[7]))
	sales.append(j[8])
	salary.append(j[9])
fp.close()

order=[]
sl_v1=["",""]
l_ev1=["",""]
n_p1=["",""]
av_hr1=["",""]
tim1=["",""]
w_ac1=["",""]
prom1=["",""]
sales1=["","","","","","","","","",""]
salary1=["","",""]

entr,name,val,index=calculate_entropy([i for i in range(0,t_len)],[])


flag=0
root=Tree()
root.name=name
root.value=val
prev_name=name
buildtree(root,prev_name,[],index)
#printTree(root)
#print(root.name)

# k=makedecision("0.1,0.9,7,286,4,0,1,0,sales,low",root)
# print(k)

fp=open("test.csv","r")
for i in fp:
	if(i[0]=='s'):
		continue
	i=i[0:len(i)-1]
	j=i.split(",")
	print(j[6]+"___"+str(makedecision(i[0:len(i)-1],root)))

"""
# print(name)
# print(index)

while True:	
	if(name==""):
		break
	names[name]=1
	#if(name=="sl_v"):
	# satis=Tree()
	# satis.name=name
	# satis.value=val
	# order.append(name)
	collective_entropy=0
	for i in range(0,len(index)):
		if(index[i][0]==0):
			if(len(index[i][1])!=0):
				satis.add_child(left[index[i][1][0]])
			else:
				satis.add_child(-1)
		else:
			entr,name,val,index=calculate_entropy(index[i][1])
			temp=Tree()
			temp.name=name
			temp.value=val
			print(i,name)
			root=appender(root,prev_name,temp)
			collective_entropy+=entr
		# if(index[1][0]==0):
		# 	if(len(index[1][1])!=0):
		# 		satis.add_child(left[index[1][1][0]])
		# 	else:
		# 		satis.add_child(-1)
	if(collective_entropy==0):
		break
print(root)
	# root.name=name
	# root.value=val
	# print(entr)
	# print(name)
	# print(val)
	# print(index)
	#a=np.array([])
	#a=np.append(a,j[0:6]+j[7:])
	#a=np.append(a,j[7:])
	#a=j[0:6]+j[7:]
	#array.append(a)

"""
