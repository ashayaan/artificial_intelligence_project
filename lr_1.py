import pandas as pd
import numpy as np
import numpy.random as rand
from sklearn.linear_model import LogisticRegression
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
	lr = LogisticRegression()
	lr.fit(train_data,train_labels)	
	return lr
	
def test(test_data, test_labels, lr):
	return lr.score(test_data, test_labels)


if __name__ == "__main__":
	(train_data, train_labels, test_data, test_labels) = split_train_test(sys.argv[1], (1.0/3.0))
	lr = train(train_data, train_labels)
	print test(test_data, test_labels, lr)
		

