import keras
import os
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.optimizers import Adadelta

from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('tf')
import sys
import numpy as np
import keras
	
#data=sys.argv[1]
#data1=(sys.argv[2],delimiter=",")
#print data

x1=[]
y1=[]
r=[]
g=[]
b=[]
ys=[]
def unpickles(file):
         import cPickle
         with open(file, 'rb') as fo:
             dict = cPickle.load(fo)
             return dict

def dataextract(files):
	def unpickle(file):
    		import cPickle
    		with open(file, 'rb') as fo:
        		dict = cPickle.load(fo)
    			return dict

	if "name" != "main":

		'''
	Each of the batch files contains a dictionary with the following elements:

    1. data -- a 10000x3072 numpy array of uint8s. Each row of the array stores a 32x32 colour image. The first 1024 entries contain the red channel values, the next 1024 the green, and the final 1024 the blue. The image is stored in row-major order, so that the first 32 entries of the array are the red channel values of the first row of the image.
    2. labels -- a list of 10000 numbers in the range 0-9. The number at index i indicates the label of the ith image in the array data.

	The  batches.meta file contains a Python dictionary object. It has the label names. 
		'''
		a = unpickle(files)
		x1 = a["data"] 
		y1 = a["labels"] 
		r.append(x1[:,0:1024])
		g.append(x1[:,1024:2048])
		b.append(x1[:,2048:3072])
		ys.append(y1)
		#print x1
		#x.append(data)
		#y.append(labels)

	#print x1.shape
	#print len(labels)
	#print label_names

#b=unpickle("batches.meta")
#label_names = b["label_names"]
def dataextract2(files):
	def unpickle(file):
    		import cPickle
    		with open(file, 'rb') as fo:
        		dict = cPickle.load(fo)
    			return dict

	if "name" != "main":

		'''
	Each of the batch files contains a dictionary with the following elements:

    1. data -- a 10000x3072 numpy array of uint8s. Each row of the array stores a 32x32 colour image. The first 1024 entries contain the red channel values, the next 1024 the green, and the final 1024 the blue. The image is stored in row-major order, so that the first 32 entries of the array are the red channel values of the first row of the image.
    2. labels -- a list of 10000 numbers in the range 0-9. The number at index i indicates the label of the ith image in the array data.

	The  batches.meta file contains a Python dictionary object. It has the label names. 
		'''
		a = unpickle(files)
		x1 = a["data"] 
		#y1 = a["labels"] 
		r.append(x1[:,0:1024])
		g.append(x1[:,1024:2048])
		b.append(x1[:,2048:3072])
		#ys.append(y1)



direcs = os.listdir(sys.argv[1])
for files in direcs:
    dataextract(sys.argv[1]+files)
    #print files
	#dataextract("data_batch_2")
	#dataextract("data_batch_3")
	#dataextract("data_batch_4")
	#dataextract("data_batch_5")
#print len(b[0][0])
#print len(ys[0])
#print r[0][0]+g[0][0]
x=[]
count=0
'''for i in range(0,5):
	for j in range(len(r[i])):
		#print i,j
		alpha=r[i][j]+g[i][j]+b[i][j]
		beta=ys[i][j]
		x.append(alpha)
		y.append(beta)
		count+=1			
'''		
#xnew=np.zeros((len(ys[0])*5,32,32))
#xnew=[]
#print np.shape(x[0])
#for m in range(0,5):
# for i in range(len(r[m])):

rf=[]
gf=[]
bf=[]
y=[]
for i in range(len(r)):
	for j in range(len(r[0])):
		rf.append(r[i][j])
		gf.append(g[i][j])
		bf.append(b[i][j])
		y.append(ys[i][j])


rf=np.asarray(rf)
gf=np.asarray(gf)
bf=np.asarray(bf)
y=np.asarray(y)
rf=rf.reshape(len(rf),32,32)
gf=gf.reshape(len(gf),32,32)
bf=bf.reshape(len(bf),32,32)

xnew=np.zeros((len(rf),32,32,3))
xnew[:,:,:,0]=rf[:,:,:]
xnew[:,:,:,1]=gf[:,:,:]
xnew[:,:,:,2]=bf[:,:,:]
y=np.asarray(y)
y = keras.utils.to_categorical(y,10)

#print np.shape(y)
# create model
'''
model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=( 32, 32,3), activation='relu',kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))

model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))



'''
b = unpickles("batches.meta")
oplabels = b["label_names"]
#print oplabels
#oplabels=['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
# Create the model

model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
#model.add(Dropout(0.2))

model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
#model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
#model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(1024, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))
# Compile model

epochs = 25
lrate = 0.01
decay = lrate/epochs
sgd = SGD(lr=lrate, momentum=0.9, decay=decay, nesterov=False)
#model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])


opt=keras.optimizers.Adadelta()
# Compile model
model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])

# Fit the model
model.fit(xnew, y,epochs=25, batch_size=128)

# evaluate the model
#print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

#print np.shape(xnew)
#print np.shape(y)


x1=[]
y1=[]
r=[]
g=[]
b=[]
x=[]
ys=[]
rf=[]
gf=[]
bf=[]
y=[]
dataextract2(sys.argv[2])
for i in range(len(r)):
	for j in range(len(r[0])):
		rf.append(r[i][j])
		gf.append(g[i][j])
		bf.append(b[i][j])
		#y.append(ys[i][j])


rf=np.asarray(rf)
gf=np.asarray(gf)
bf=np.asarray(bf)
#y=np.asarray(y)
rf=rf.reshape(len(rf),32,32)
gf=gf.reshape(len(gf),32,32)
bf=bf.reshape(len(bf),32,32)

xnew=np.zeros((len(rf),32,32,3))
xnew[:,:,:,0]=rf[:,:,:]
xnew[:,:,:,1]=gf[:,:,:]
xnew[:,:,:,2]=bf[:,:,:]
file = open("q2_b_output.txt","w") 

scores = model.predict(xnew)
final=np.zeros(len(scores))
for i in range(len(scores)):
    index=np.where(scores[i]==scores[i].max())
    final[i]=index[0]
    file.write( oplabels[int(final[i])]+"\n")
    #print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


file.close()
