import numpy as np
import os , re
import sys
vocab=[]
vocabpos={}
classpos={}
datadir = '../data/'
classes = ['galsworthy/','galsworthy_2/','mill/','shelley/','thackerey/','thackerey_2/','wordsmith_prose/','cia/','johnfranklinjameson/','diplomaticcorr/']
inputdir = ['train/','test/']

class FeatureVector(object):
    def __init__(self,vocab,numdata):
        self.X =  np.zeros((numdata,len(vocab)), dtype=np.int)
        self.Y =  np.zeros((numdata,), dtype=np.int)

    def make_featurevector(self, inputs, classid, pos):
        #print pos,classid
        for j in inputs:
            if j!='s' and j!='ss':
                self.X[pos][vocabpos[j]]+=1
        self.Y[pos]=classid

class KNN(object):
    def __init__(self,trainVec,testVec):
        self.X_train = trainVec.X
        self.Y_train = trainVec.Y
        self.X_test = testVec.X
        self.Y_test = testVec.Y

    def classify(self):
        wrong=0
        correct=0
        k=7
        for i in range(len(self.X_test)):
            knnlist=[]
            for j in range(len(self.X_train)):
                dist = np.linalg.norm(self.X_train[j]-self.X_test[i])
                knnlist.append([dist,self.Y_train[j]])
            knnlist.sort()
            classes_cnt=np.zeros(len(classes))
            maxx=0
            final_classId=100
            for j in range(k):
                classes_cnt[knnlist[j][1]]+=1
                if(classes_cnt[knnlist[j][1]]>maxx):
                    maxx=classes_cnt[knnlist[j][1]]
                    final_classId=knnlist[j][1]
            print "final_classId is ",final_classId,"original is ",self.Y_test[i]
            if final_classId==self.Y_test[i]:
                correct+=1
            else:
                wrong+=1
        print "wrong:",wrong,"correct:",correct
if __name__=='__main__':
    trainsz=0
    testsz=0
    for idir in inputdir:
        for c in classes:
            listing = os.listdir(datadir+idir+c)
            for filename in listing:
                if idir=="train/":
                    trainsz=trainsz+1
                elif idir=="test/":
                    testsz=testsz+1
                f = open(datadir+idir+c+filename,'r')
                lines=f.readlines()
                string=""
                for line in lines:
                    string+=line

                data=re.sub('[^0-9A-Za-z\ ]+','',string)
                data=data.split(' ')
                for j in range(len(data)):
                    if data[j]!='s' and data[j]!='ss':
                        vocabpos.update({data[j]:0})
    for x in vocabpos:
        vocabpos.update({x:len(vocab)})
        vocab.append(x)
    #print vocabpos,len(vocabpos),len(vocab)
    #print trainsz,testsz
    trainVec=FeatureVector(vocab,trainsz)
    testVec=FeatureVector(vocab,testsz)
    traincount=0
    testcount=0
    classid = 0
    for c in classes:
        classpos.update({c:classid})
        listing = os.listdir(datadir+'train/'+c)
        for filename in listing:
            f = open(datadir+'train/'+c+filename,'r')
#               print datadir+idir+c+filename
            lines=f.readlines()
            string=""
            for line in lines:
                string+=line
            data=re.sub('[^0-9A-Za-z\ ]+','',string)
            inputs=data.split(' ')
            trainVec.make_featurevector(inputs,classid,traincount)
            traincount=traincount+1
        classid += 1
    #print classpos
    for c in classes:
        listing=os.listdir(datadir+'test/'+c)
        for filename in listing:
            f=open(datadir+'test/'+c+filename,'r')
            #print datadir+idir+c+filename
            lines=f.readlines()
            string=""
            for line in lines:
                string+=line
            data=re.sub('[^0-9A-Za-z\ ]+','',string)
            inputs=data.split(' ')
            #print c,classpos[c]
            testVec.make_featurevector(inputs,classpos[c],testcount)
            testcount=testcount+1
    knn = KNN(trainVec,testVec)
    knn.classify()
