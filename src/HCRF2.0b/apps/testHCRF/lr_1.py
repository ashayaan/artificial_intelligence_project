import pandas as pd
import itertools
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import sys

seq2 = pd.Series(np.arange(2))

def split_train_test(filename, test_ratio):
	genes_df = pd.read_csv(filename, index_col=0)
	#affx_col = [col for col in genes_df if col.startswith('AFFX')]
	#genes_df = genes_df.drop(affx_col, axis=1)
	genes_df = genes_df.dropna()
	print genes_df.shape
	#Slices by label value
	labels = pd.Series(genes_df['label'].unique())
	slices = labels.apply(lambda l: genes_df[genes_df['label']==l])
	slices_ser = pd.Series(np.arange(slices.size))
	slice_sizes = slices_ser.apply(lambda i: slices[i].shape[0])
	random_indices = slices_ser.apply(lambda i : rand.choice(slice_sizes[i], int(slice_sizes[i]*test_ratio), replace=False))
	#Creating test_data
	test = pd.concat(list(seq2.apply(lambda i: slices[i].iloc[list(random_indices[i]),:])))
	test_labels = test['label']
	test_data = test.drop(['label'],axis=1)
	train = pd.concat(list(seq2.apply(lambda i: slices[i].drop(slices[i].index[list(random_indices[i])]))))
	train_labels = train['label']
	train_data = train.drop(['label'], axis=1)
	return (train_data, train_labels, test_data, test_labels)
	
def train(train_data, train_labels):
	lr = LogisticRegression(class_weight='balanced')
	lr.fit(train_data,train_labels)	
	return lr
	
def test(test_data, test_labels, lr):
	test_pred = lr.predict(test_data)
	cnf_matrix = confusion_matrix(test_labels, test_pred)
	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=seq2, normalize=True,title='Normalized confusion matrix')
	plt.show()
	return lr.score(test_data, test_labels)

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')
    print(cm)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt), horizontalalignment="center", color="white" if cm[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

if __name__ == "__main__":
	#(train_data, train_labels, test_data, test_labels) = split_train_test(sys.argv[1], (1.0/3.0))
	#lr = train(train_data, train_labels)
	#print test(test_data, test_labels, lr)
	labels_true = pd.read_csv('genome-label.csv')
	labels_pred = pd.read_csv('Results/train-results.csv')
	cnf_matrix = confusion_matrix(labels_true, labels_pred)	
	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=seq2, normalize=True,title='Normalized confusion matrix')
	plt.show()

