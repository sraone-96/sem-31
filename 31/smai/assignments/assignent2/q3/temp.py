# Logistic Regression
from sklearn import datasets
from sklearn import metrics
import numpy as np
from sklearn.linear_model import LogisticRegression
#from sklearn.linear_model import predict_log_proba
# load the iris datasets
dataset = datasets.load_iris()
# fit a logistic regression model to the data
model = LogisticRegression()
model.fit(dataset.data, dataset.target)

expected = dataset.target
predicted = model.predict_log_proba(dataset.data)
p=[]
for i in range(len(predicted)):
	index=np.where(predicted[i] == predicted[i].max())
	p.append(index)
#print np.shape(p)
#print (expected-p)
p=np.asarray(p)
# summarize the fit of the model

print(metrics.classification_report(expected, p))
print(metrics.confusion_matrix(expected, p))
