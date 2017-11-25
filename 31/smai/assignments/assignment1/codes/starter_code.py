#!/usr/bin/env python
import math
import re
import sys
import os
import numpy as np
dicton={}
colnumber=0
global err
err=0
"""Feel free to add any extra classes/functions etc as and when needed.
This code is provided purely as a starting point to give you a fair idea
of how to go about implementing machine learning algorithms in general as
a part of the first assignment. Understand the code well"""


class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,vocabsize), dtype=np.int)
		self.Y =  np.zeros((numdata,), dtype=np.int)

	def make_featurevector(self, inputs, classid,pos):
		for wor in inputs:
			if( wor!='<s>' or wor!='<\s>'):
				self.X[pos][dicton[wor]]+=1
        			self.Y[pos]=classid
			#else:
			#	print "hie"

class KNN(object):
	def __init__(self,trainVec,testVec):
		self.X_train = trainVec.X
		self.Y_train = trainVec.Y
		self.X_test = testVec.X
		self.Y_test = testVec.Y
		self.metric = Metrics('accuracy')

	def classify(self, nn=1):
		"""
		Takes input X_train, Y_train, X_test and Y_test and displays the accuracies.
		"""
		#err=0
		possibilities=[]
		for i in range(len(self.X_test)):
			for lines in range(len((self.X_train))):
				dist=np.linalg.norm(self.X_test[i]-self.X_train[lines])
				possibilities.append([dist,self.Y_train[lines]])
			possibilities.sort()
			final=[]
			for c in range(0,15):
				final.append(possibilities[c][1])
				print possibilities[c][1]
			count=np.zeros(10)
			for m in final:
				count[m]+=1
			
			ans=np.any(count==count.max())
			
			print "actual=",self.Y_test[i]
			if(ans!=self.Y_test[i]):
				global err
				err=err+1
				
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

if __name__ == '__main__':
	datadir = './datasets/q4/'
	classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']
	inputdir = ['train/','test/']

	#vocab = {}
	trainsz = 0
	testsz = 0
	sentence=""
	for folders in classes:
		direcs = os.listdir(datadir+'train/'+folders)
		for files in direcs:
			trainsz+=1
			with open(datadir+'train/'+folders+files,'r') as f:
				text=f.readlines()
				#print text
				print "dividing lines"
				tempo=""
				for bis in text:
					tempo+=bis
				print "divided lines"
				
        		        #tempos=tempo.split(' ')
	
				#for values in tempo:
					
				
				#print "divided words"
				#print text2
				#print "done"
				
				#sentence+=tempo
				#print "file added\n"	
				datas=re.sub('[^0-9A-Za-z\ ]+','',tempo)
				sentence=datas.split(' ')
				for words in sentence:
	   				if(words!='<s>' and words!='<\s>'):
	      					dicton.update({words:0})	
						alpha=words
					#else:
					#	print "hieee"
	for folders in classes:
		direcs = os.listdir(datadir+'test/'+folders)
		for files in direcs:
			trainsz+=1
			with open(datadir+'test/'+folders+files,'r') as f:
				text=f.readlines()
				#print text
				print "dividing lines"
				tempo=""
				for bis in text:
					tempo+=bis
				print "divided lines"
				
        		        #tempos=tempo.split(' ')
	
				#for values in tempo:
					
				
				#print "divided words"
				#print text2
				#print "done"
				
				#sentence+=tempo
				#print "file added\n"	
				datas=re.sub('[^0-9A-Za-z\ ]+','',tempo)
				sentence=datas.split(' ')
				for words in sentence:
	   				if(words!='<s>' and words!='<\s>'):
	      					dicton.update({words:0})	
						alpha=words
	
	print "done seperating words"
	for words in dicton:
		dicton.update({words:colnumber})
		colnumber=colnumber+1
		
	#print dicton['beatific']
	#print "printed"
	for folders in classes:
		direcs = os.listdir(datadir+'test/'+folders)
		for files in direcs:
			testsz+=1
			'''sentence=""
			with open(datadir+'test/'+folders+files,'r') as f:
				for line in f:
					for word in line.split():
						sentence+=word
			'''

	print('Making the feature vectors.')
	trainVec =FeatureVector(len(dicton),trainsz)
	testVec =FeatureVector(len(dicton),testsz)

	for idir in inputdir:
		pos=0
		classid = 1
		for c in classes:
			listing = os.listdir(datadir+idir+c)
			for filename in listing:
				f = open(datadir+idir+c+filename,'r')
				l={}
				ccc=0
				text=f.readlines()
				tempo=""
				for bis in text:
					tempo+=bis
				datas=re.sub('[^0-9A-Za-z\ ]+','',tempo)
				sentence=datas.split(' ')
				for words in sentence:
	   				if(words!='<s>' and words!='<\s>'):
	      						l.update({words:ccc})
							ccc+=1
					#else:
					#	print "hie"
				
				#print l.keys()
				inputs=l.keys()
				for batches in inputs:
					if(math.isnan(dicton[batches])):
						print btaches
				#print "inputs sent"
				#print inputs

				if idir == 'train/':
					trainVec.make_featurevector(inputs,classid,pos)
				else:
					testVec.make_featurevector(inputs,classid,pos)
				pos+=1
			classid += 1

	print('Finished making features.')
	print('Statistics ->')
	print(trainVec.X.shape,trainVec.Y.shape,testVec.X.shape,testVec.Y.shape)

	knn = KNN(trainVec,testVec)
	knn.classify()
	global err
	print err
