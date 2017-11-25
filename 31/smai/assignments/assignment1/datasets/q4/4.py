#!/usr/bin/env python

import sys
import os ,re
import numpy as np
from collections import defaultdict

"""Feel free to add any extra classes/functions etc as and when needed.
This code is provided purely as a starting point to give you a fair idea
of how to go about implementing machine learning algorithms in general as
a part of the first assignment. Understand the code well"""


class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,self.vocabsize), dtype=np.int)
		self.Y =  np.zeros((numdata,), dtype=np.int)
		
	def make_featurevector(self, inputs, classid ,f_no):
		self.Y[f_no]=classid
		for i in inputs.keys():
			if(pos[i]!=0):
				self.X[f_no][pos[i]]=inputs[i]
		# key=ret.keys()
		# for i in range(0,len(key)):
		# 	self.X[f_no][i]=inputs[key[i]]
		"""
		Takes input the documents and outputs the feature vectors as X and classids as Y.
		"""

class KNN(object):
	def __init__(self,trainVec,testVec):
		self.X_train = trainVec.X
		self.Y_train = trainVec.Y
		self.X_test = testVec.X
		self.Y_test = testVec.Y
		self.metric = Metrics('accuracy')

	def classify(self, nn=1):
		train_num=len(self.Y_train)
		test_num=len(self.Y_test)
		predicted=[]
		for i in range(0,test_num):
			test_vector=self.X_test[i]
			dist=[]
			for j in range(0,train_num):
				dist.append((np.linalg.norm(np.subtract(test_vector,self.X_train[j])),self.Y_train[j]))
			dist=sorted(dist)
			final=dist[0:nn]
			print(final)
			final=self.find(final)
			predicted.append(final[1])
		print(self.Y_test)
		print(predicted)
		"""
		Takes input X_train, Y_train, X_test and Y_test and displays the accuracies.
		"""

	def find(self,final):
		votes=defaultdict(int)
		for i in final:
			votes[i[1]]+=1
		sortedorder=sorted(votes,key=votes.get,reverse=True)
		highest=votes[sortedorder[0]]
		lst=[]
		for i in votes.keys():
			if(votes[i]==highest):
				lst.append(i)
		for i in final:
			if(i[1] in lst):
				return i

class Metrics(object):
	def __init__(self,metric):
		self.metric = metric

	def score(self):
		if self.metric == 'accuracy':
			return self.accuracy()
		elif self.metric == 'f1':
			return self.f1_score()

	def get_confmatrix(self,y_pred,y_test):
		"""
		Implements a confusion matrix
		"""

	def accuracy(self):
		"""
		Implements the accuracy function
		"""

	def f1_score(self):
		"""
		Implements the f1-score function
		"""
ret=defaultdict(int)
pos=defaultdict(int)
def get_dict(string):
	dic=defaultdict(int)
	string=string.lower()
	# string=re.sub('e g ','eg ',string)
	string=re.sub("<s>","",string)
	string=re.sub("<\s>","",string)
	string=re.sub("<\\s>","",string)
	string=re.sub('[^a-zA-Z\ ]+', '', string)
	string=re.sub("\n","",string)
	temp=string.split(" ")
	for i in temp:
		dic[i]+=1
	return dic
def getuniquewords(string):

	string=string.lower()
	# string=re.sub('e g ','eg ',string)
	string=re.sub("<s>","",string)
	string=re.sub("<\s>","",string)
	string=re.sub("<\\s>","",string)
	string=re.sub('[^a-zA-Z\ ]+', '', string)
	# string=re.sub("<.*?>","",string)
	string=re.sub("\n","",string)
	# for i in liset:
	# 	string=re.sub(i,'',string)
	# 	print(string)
	temp=string.split(" ")
	for i in temp:
		ret[i]+=1
	


def getvocab(datadir,classes,inputdir):
	vocabulory=[]
	string=""
	tsz=0
	for idir in inputdir:
		for c in classes:
			listing=os.listdir(datadir+idir+c)
			for filename in listing:
				f=open(datadir+idir+c+filename,'r')
				tsz+=1
				string=""
				for i in f:
					string+=i
				f.close()
				if(inputdir==['train/']):
					getuniquewords(string)
	return tsz
	# if(inputdir==['train/']):
	# 	return ret.keys(),tsz
	# else:
	# 	return tsz


if __name__ == '__main__':
	datadir = './'
	classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']
	inputdir = ['train/','test/']


	# length = getvocab(datadir,classes,['train/'])#Write code
	# print(length[0])
	#stoplist=['','a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'arent', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'cant', 'cannot', 'could', 'couldnt', 'did', 'didnt', 'do', 'does', 'doesnt', 'doing', 'dont', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadnt', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 'hes', 'her', 'here', 'heres', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'hows', 'i', 'id', 'ill', 'im', 'ive', 'if', 'in', 'into', 'is', 'isnt', 'it', 'its', 'its', 'itself', 'lets', 'me', 'more', 'most', 'mustnt', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shant', 'she', 'shed', 'shell', 'shes', 'should', 'shouldnt', 'so', 'some', 'such', 'than', 'that', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'theres', 'these', 'they', 'theyd', 'theyll', 'theyre', 'theyve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasnt', 'we', 'wed', 'well', 'were', 'weve', 'were', 'werent', 'what', 'whats', 'when', 'whens', 'where', 'wheres', 'which', 'while', 'who', 'whos', 'whom', 'why', 'whys', 'with', 'wont', 'would', 'wouldnt', 'you', 'youd', 'youll', 'youre', 'youve', 'your', 'yours', 'yourself', 'yourselves']	
	trainsz = getvocab(datadir,classes,['train/']) #Write code
	#map(lambda x: ret.pop(x,None), stoplist)
	vocab=len(ret.keys())
	testsz = getvocab(datadir,classes,['test/'])#Write code
	k=ret.keys()
	for i in range(0,len(k)):
		pos[k[i]]=i
	print('Making the feature vectors.')
	trainVec = FeatureVector(vocab,trainsz)
	testVec = FeatureVector(vocab,testsz)
	
	for idir in inputdir:
		f_no=0
		classid = 1
		for c in classes:
			listing = os.listdir(datadir+idir+c)
			for filename in listing:
				f = open(datadir+idir+c+filename,'r')
				strng=""
				for line in f:
					strng+=line
				inputs=get_dict(strng)
				#Insert code here
				if idir == 'train/':
					trainVec.make_featurevector(inputs,classid,f_no)
					f_no+=1
				else:
					testVec.make_featurevector(inputs,classid,f_no)
					f_no+=1
			classid += 1

	print('Finished making features.')
	print('Statistics ->')
	print(trainVec.X.shape,trainVec.Y.shape,testVec.X.shape,testVec.Y.shape)

	knn = KNN(trainVec,testVec)
	knn.classify(1)
