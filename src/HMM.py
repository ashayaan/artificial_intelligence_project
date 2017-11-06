import pandas as pd
import numpy as np
from hmmlearn import hmm


def fitModel(train,train_len,test,test_len):
	x = np.concatenate(train)
	# y = np.concatenate(test)
	remodel = hmm.GaussianHMM(n_components=2,covariance_type="full", n_iter=20)
	remodel.fit(x,train_len)
	for i in test:	
		l = np.mean(remodel.predict(i))
		print i[-1]
		if l > 0.5:
			print "1"
		else:
			print "0"

if __name__ == '__main__':
	train = []
	train_len = []
	filename = "../data_files/genome-properties-hydro.csv"
	f1 = open(filename,'r')

	count = 0
	for line in f1:
		if count < 300:
			a = np.array(line.split(','),dtype=np.float32)
			b = np.array([a])
			b = b.T
			train.append(b)
			train_len.append(len(b))
		count += 1

	f1.close()
	f1 = open(filename,'r')
	test = []
	test_len = []
	count = 0
	for line in f1:
		if count > 300:
			a = np.array(line.split(','),dtype=np.float32)
			b = np.array([a])
			b = b.T
			test.append(b)
			test_len.append(len(b))
		count += 1

	# print test[0]
	fitModel(train,train_len,test,test_len)