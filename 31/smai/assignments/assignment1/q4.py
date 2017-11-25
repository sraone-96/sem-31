#!/usr/bin/env python

import sys
import os
import numpy as np

"""Feel free to add any extra classes/functions etc as and when needed.
This code is provided purely as a starting point to give you a fair idea
of how to go about implementing machine learning algorithms in general as
a part of the first assignment. Understand the code well"""


class FeatureVector(object):
	def __init__(self,vocabsize,numdata):
		self.vocabsize = vocabsize
		self.X =  np.zeros((numdata,self.vocabsize), dtype=np.int)
		self.Y =  np.zeros((numdata,), dtype=np.int)

	def make_featurevector(self, input, classid):
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
		"""
		Takes input X_train, Y_train, X_test and Y_test and displays the accuracies.
		"""


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
	datadir = '../data/'
	classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']
	inputdir = ['train/','test/']

	vocab = {}
	trainsz = #Write code
	testsz = #Write code

	print('Making the feature vectors.')
	trainVec = FeatureVector(vocab,trainsz)
	testVec = FeatureVector(vocab,testsz)

	for idir in inputdir:
		classid = 1
		for c in classes:
			listing = os.listdir(datadir+idir+c)
			for filename in listing:
				f = open(datadir+idir+c+filename,'r')

				#Insert code here

				if idir == 'train/':
					trainVec.make_featurevector(inputs,classid)
				else:
					testVec.make_featurevector(inputs,classid)
			classid += 1

	print('Finished making features.')
	print('Statistics ->')
	print(trainVec.X.shape,trainVec.Y.shape,testVec.X.shape,testVec.Y.shape)

	knn = KNN(trainVec,testVec)
	knn.classify()
