from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.constraints import maxnorm
from keras.optimizers import SGD
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.utils import np_utils
from keras import backend as K
K.set_image_dim_ordering('tf')
import sys
import numpy as np

#data=sys.argv[1]
#data1=(sys.argv[2],delimiter=",")
#print data

x1=[]
y1=[]
r=[]
g=[]
b=[]
ys=[]
X1=[]
Y1=[]
X2=[]
Y2=[]
def dataextract(files,i):
	def unpickle(file):
    		import cPickle
    		with open(file, 'rb') as fo:
        		dict = cPickle.load(fo)
    			return dict

	if "__name__" != "__main__":

		'''
	Each of the batch files contains a dictionary with the following elements:

    1. data -- a 10000x3072 numpy array of uint8s. Each row of the array stores a 32x32 colour image. The first 1024 entries contain the red channel values, the next 1024 the green, and the final 1024 the blue. The image is stored in row-major order, so that the first 32 entries of the array are the red channel values of the first row of the image.
    2. labels -- a list of 10000 numbers in the range 0-9. The number at index i indicates the label of the ith image in the array data.

	The  batches.meta file contains a Python dictionary object. It has the label names. 
		'''
		if(i==0):
			a = unpickle(files)
			x1 = a["data"] 
			y1 = a["labels"] 
			r.append(x1[:,0:1024])
			g.append(x1[:,1024:2048])
			b.append(x1[:,2048:3072])
			ys.append(y1)
		elif(i==1):
			a = unpickle(files)
			x1 = a["data"] 
			y1 = a["labels"] 
			X1=x1
			Y1=y1
		elif(i==2):
			a = unpickle(files)
			x1 = a["data"] 
			y1 = a["labels"] 
			X2=x1
			Y2=y1
		#print x1
		#x.append(data)
		#y.append(labels)

	#print x1.shape
	#print len(labels)
	#print label_names

#b=unpickle("batches.meta")
#label_names = b["label_names"]






dataextract("data_batch_1",0)
dataextract("data_batch_2",0)
dataextract("data_batch_3",0)
dataextract("data_batch_4",1)
dataextract("data_batch_5",2)
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
y = np_utils.to_categorical(y)

X2=np.asarray(X2)
X1=np.asarray(X1)
Y2=np.asarray(Y2)
Y1=np.asarray(Y1)

X1=X1.reshape(len(X1),32,32,3)
X2=X2.reshape(len(X2),32,32,3)
Y2=np_utils.to_categorical(Y2)
Y1 =np_utils.to_categorical(Y1)


#input_shape = (img_rows, img_cols, 3)

#print np.shape(y)
# create model
'''
model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape=( 32, 32,3), activation='relu',kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))

model.add(Conv2D(32, (3, 3), activation='relu', padding='same', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.2))



model.add(Conv2D(64, (3, 3), input_shape=(3, 32, 32), padding='same', activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))

model.add(MaxPooling2D(pool_size=(3, 3)))
#,dim_ordering="tf"))
model.add(MaxPooling2D(pool_size=(3, 3)))
#,dim_ordering="tf"))

model.add(Flatten())

model.add(Dense(512, activation='relu', kernel_constraint=maxnorm(3)))
model.add(Dropout(0.5))

model.add(Dense(256, input_dim=8, activation='relu'))

model.add(Dense(64, activation='relu'))

#model.add(Dense(32, activation='relu'))

model.add(Dense(8, activation='relu'))

model.add(Dense(1, activation='softmax'))
'''
# Create the model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=(32, 32, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
model.add(Dropout(0.2))
model.add(Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
model.add(Dropout(0.2))
model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization(axis=-1, momentum=0.99, epsilon=0.001, center=True, scale=True,))
#model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(0.2))
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



# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model
model.fit(xnew, y,epochs=20, batch_size=50)

# evaluate the model
scores = model.evaluate(X1, Y1)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
scores = model.evaluate(X2, Y2)

print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
