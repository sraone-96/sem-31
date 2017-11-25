"""
Course: Statistical Methods in Artificial Intelligence (CSE471)
Semester: Fall '17
Professor: Gandhi, Vineet

Assignment 2: SVM using scikit-learn.
Skeleton code for implementing SVM classifier for a
character recognition dataset having precomputed features for
each character.

Dataset is taken from: https://archive.ics.uci.edu/ml/datasets/letter+recognition

Remember
--------
1) SVM algorithms are not scale invariant.
"""
from sklearn import svm
from sklearn import preprocessing
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.metrics import accuracy_score
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold.t_sne import TSNE
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
import argparse, os, sys
def get_input_data(filename):
    """
    Function to read the input data from the letter recognition data file.

    Parameters
    ----------
    filename: The path to input data file

    Returns
    -------
    X: The input for the SVM classifier of the shape [n_samples, n_features].
       n_samples is the number of data points (or samples) that are to be loaded.
       n_features is the length of feature vector for each data point (or sample).
    Y: The labels for each of the input data point (or sample). Shape is [n_samples,].

    """

    X = []; Y = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            Y.append(line[0])
            X.append([float(x) for x in line[1:]])
    X = np.asarray(X); Y = np.asarray(Y)

    """
    An important part is missing here. Corresponding to point (1) in "Remember".
    ===========================================================================
    """
    X=preprocessing.scale(X)
    #Y=preprocessing.scale(Y)
    # YOUR CODE GOES HERE

    """
    ===========================================================================
    """

    return X, Y

def calculate_metrics(predictions, labels):
    """
    Function to calculate the precision, recall and F-1 score.

    Parameters
    ----------
    predictions: The predictions obtained as output from the SVM classifier
    labels: The true label values corresponding to the entries in predictions

    Returns
    -------
    precision: true_positives / (true_positives + false_positives)
    recall: true_positives / (true_positives + false_negatives)
    f1: 2 * (precision * recall) / (precision + recall)
    ===========================================================================
    """

    # YOUR CODE GOES HERE

    """
    ===========================================================================
    """

    return precision, recall, f1

def calculate_accuracy(predictions, labels):
    """
    Function to calculate the accuracy for a given set of predictions and
    corresponding labels.

    Parameters
    ----------
    predictions: The predictions obtained as output from the SVM classifier
    labels: The true label values corresponding to the entries in predictions

    Returns
    -------
    accuracy: Fraction of total samples that have correct predictions (same as
    true label)

    """
    return accuracy_score(labels, predictions)

def SVM(train_data,
        train_labels,
        test_data,
        test_labels,
        kernel='linear'):
    """
    Function to create, train and test the one-vs-all SVM using scikit-learn.

    Parameters
    ----------
    train_data: Numpy ndarray of shape [n_train_samples, n_features]
    train_labels: Numpy ndarray of shape [n_train_samples,]
    test_data: Numpy ndarray of shape [n_test_samples, n_features]
    test_labels: Numpy ndarray of shape [n_test_samples,]
    kernel: linear (default)
            Which kernel to use for the SVM

    Returns
    -------
    accuracy: Accuracy of the model on the test data
    top_predictions: Top predictions for each test sample
    precision: The precision score for the test data
    recall: The recall score for the test data
    f1: The F1-score for the test data

    """

    """
    Create an SVM instance with the required parameters and train it.
    For details on how to do this in scikit-learn, refer:
        http://scikit-learn.org/stable/modules/svm.html
    ==========================================================================
    """
    model=svm.SVC(C=10.0, gamma=0.1, coef0=1.0, kernel='rbf')
    model.fit(train_data,train_labels)
    # YOUR CODE GOES HERE
    train_predictions=model.predict(train_data)
    test_predictions=model.predict(test_data)
    """
    ==========================================================================
    """

    """
    Calculates training accuracy. Replace predictions and labels with your
    respective variable names.
    """
    train_accuracy = calculate_accuracy(test_predictions, test_labels)
    #print "Training Accuracy: %.4f" % (train_accuracy)

    """
    Use the trained model to perform testing. Using the output of the testing
    prodecure, get the top prediction for each sample and calculate the accuracy
    on test data using the function given (as shown above for train accuracy).

    Also, complete the function given above for metrics using scikit-learn and
    return their values in this function.
    ==========================================================================
    """
    # YOUR CODE GOES HERE
    #accuracy=accuracy_score(test_labels, test_predictions, sample_weight=None)
    recall=recall_score(test_labels, test_predictions, average='micro', sample_weight=None)
    precision=precision_score(test_labels,test_predictions, labels=None, pos_label=1, average='micro', sample_weight=None)
    f1=f1_score(test_labels, test_predictions, labels=None, pos_label=1, average='micro', sample_weight=None)
    """
    ==========================================================================
    """
    #accuracy=0;precision=0;recall=0;f1=0;
    return train_accuracy, precision, recall, f1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default=None,
            help='path to the directory containing the dataset file')

    args = parser.parse_args()
    if args.data_dir is None:
        #print "Usage: python letter_classification_svm.py --data_dir='<dataset dir path>'"
        sys.exit()
    else:
        filename = os.path.join(args.data_dir, 'letter_classification_train.data')
        try:
            if os.path.exists(filename):
                #print "Using %s as the dataset file" % filename
        	pass
	except:
           # print "%s not present in %s. Please enter the correct dataset directory" % (filename, args.data_dir)
            sys.exit()

    # Set the value for svm_kernel as required.
    svm_kernel = 'linear'

    """
    Get the input data using the provided function. Store the X and Y returned
    as X_data and Y_data. Use filename found above as the input to the function.
    ==========================================================================
    """
    
    # YOUR CODE GOES HERE
    X_data,Y_data=get_input_data(filename)
    """
    ==========================================================================
    """

    """
    We use 5-fold cross validation for reporting the final scores and metrics.
    Code to generate the 5-folds (You can change the split function to something
    else that you like as well) and then calling the SVM to classify the present
    split.
    ==========================================================================
    """
    sss = StratifiedShuffleSplit(n_splits=5, test_size=0.125)   # Do not change this split size
    accumulated_metrics = []
    fold = 1
    for train_indices, test_indices in sss.split(X_data, Y_data):
        #print "Fold%d -> Number of training samples: %d | Number of testing "\
         #   "samples: %d" % (fold, len(train_indices), len(test_indices))
        train_data, test_data = X_data[train_indices], X_data[test_indices]
        train_labels, test_labels = Y_data[train_indices], Y_data[test_indices]
        accumulated_metrics.append(SVM(train_data, train_labels, test_data, test_labels,svm_kernel))
        fold += 1
	#print fold
    """
    Print out the accumulated metrics in a good format.
    ==========================================================================
    """
    #print "hi"
    #print accumulated_metrics
    # YOUR CODE GOES HERE
    #print len(accumulated_metrics)
    sums=np.zeros(len(accumulated_metrics))
    for j in range(4):
	 for i in range(len(accumulated_metrics)):
	      sums[j]+=(accumulated_metrics[i][j])
         sums[j]=sums[j]/len(accumulated_metrics)
    
    """
    ==========================================================================
    """
    print str(sums[0])+","+str(sums[1])+","+str(sums[2])+","+str(sums[3])
