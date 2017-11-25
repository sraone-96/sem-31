import numpy as np

def prctrn():
    data=np.genfromtxt('mnist_train.csv',delimiter=",")
    w=np.zeros(len(data[0][1:]))
    while 1:
        count=0
        for i in range(len(data)):
            k=w.T.dot(data[i][1:].astype(float))
            if k<=0 and data[i][0]==1:
                w=w+data[i][1:]
            elif k>=0 and data[i][0]==0:
                w=w-data[i][1:]
        for i in range(len(data)):
            k=w.T.dot(data[i][1:].astype(float))
            if (k< 0 and data[i][0]==1) or (k>0 and data[i][0]==0):
                count=count+1
        print count
        if count==0:
            break
    test_data=np.genfromtxt('mnist_test.csv',delimiter=",")

    count=0
    for i in range(len(test_data)):
        k=w.T.dot(test_data[i][1:].astype(float))
        if (k < 0 and test_data[i][0]==1) or (k>0 and test_data[i][0]==0):
            count=count+1
    print count


def prctrnmargin():
    data=np.genfromtxt('mnist_train.csv',delimiter=",")
    print "prcptrn margin"
    margin=1
    prvtestcount=100
    while 1:
        w=np.zeros(len(data[0][1:]))
        while 1:
            count=0
            for i in range(len(data)):
                k=w.T.dot(data[i][1:])
                if k<=margin*np.sqrt(np.sum(w*w)) and data[i][0]==1:# and np.linalg.norm(w-data[i][1:])>margin:
                    w=w+data[i][1:]
                elif k>=margin*np.sqrt(np.sum(w*w)) and data[i][0]==0:# and np.linalg.norm(w-data[i][1:])>margin:
                    w=w-data[i][1:]
            for i in range(len(data)):
                if (np.dot(w.T,data[i][1:])<0 and data[i][0]==1) or (np.dot(w.T,data[i][1:])>0 and data[i][0]==0):
                    count=count+1
            print count,margin
            if count==0:
                break
        test_data=np.genfromtxt('mnist_test.csv',delimiter=",")
        testcount=0
        for i in range(len(test_data)):
            if (np.dot(w.T,test_data[i][1:])<0 and test_data[i][0]==1) or (np.dot(w.T,test_data[i][1:])>0 and test_data[i][0]==0):
                testcount=testcount+1
        print testcount
        if prvtestcount>=testcount:
            prvtestcount=testcount
            margin=margin+1
        else:
            print prvtestcount,"found at margin",margin-1
            margin=margin+1


def prctrnbatch():
    data=np.genfromtxt('mnist_train.csv',delimiter=",")
    print "Batvh Perceptron"
    w=np.zeros(len(data[0][1:]))
    batch=np.zeros(len(data[0][1:]))
    while 1:
        for i in range(len(data)):
            k=w.T.dot(data[i][1:])
            if k<=0 and data[i][0]==1:
                batch=batch+data[i][1:]
            elif k>=0 and data[i][0]==0:
                batch=batch-data[i][1:]
        w=w+batch
#        print w
        batch=np.zeros(len(data[0][1:]))
        count=0
        for i in range(len(data)):
            if ((w.T.dot(data[i][1:])<0 and data[i][0]==1) or (w.T.dot(data[i][1:])>0 and data[i][0]==0)):
                count=count+1
        if count==0:
            break
        print "hii",count
    count=0
    test_data=np.genfromtxt('mnist_test.csv',delimiter=",")
    for i in range(len(test_data)):
        if (np.dot(w.T,test_data[i][1:]) <= 0 and test_data[i][0]==1) or (np.dot(w.T,test_data[i][1:])>0 and test_data[i][0]==0):
            count=count+1
    print count
#prctrn();
#prctrnmargin();
prctrnbatch()
