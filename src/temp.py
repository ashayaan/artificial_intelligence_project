import pandas as pd
import numpy as np
from hmmlearn import hmm

def fitModel(train,train_len,test_len,test):
	x = np.concatenate(train)
	y = np.concatenate(test)
	remodel = hmm.GaussianHMM(n_components=2,covariance_type="tied", n_iter=100)
	remodel.fit(x,train_len)
	print remodel.predict(test[20])
	# print test[0]
	# for i in test:
	# 	l = remodel.predict(i)
	# 	x = np.mean(l)
	# 	print i[-1],
	# 	if x >= 0.5:
	# 		print "1"
	# 	else:
	# 		print "0"
	

if __name__ == '__main__':
	train=[]
	train_len = []

	for i in range(0,21):
		f1 = open('../data_files/genome-properties-rec.csv','r')
		f2 = open ('../data_files/genome-properties-rec.csv','r')
		count = 0;
		if i%2 == 0:
			for line in f2:
				if count == i:
					a = np.array(line.split(','),dtype=np.float32)
					b = np.array([a])
					b = b.T
					# print b
					train.append(b)
					train_len.append(len(b))
				count += 1
		else:
			for line in f1:
				if count == i:
					a = np.array(line.split(','),dtype=np.float32)
					b = np.array([a])
					b = b.T
					train.append(b)
					train_len.append(len(b))
				count += 1

	test = []
	test_len = []
	for i in range(21,51):
		f1 = open('../data_files/genome-properties-rec.csv','r')
		f2 = open ('../data_files/genome-properties-rec.csv','r')
		count = 0;
		if i%2 == 0:
			for line in f2:
				if count == i:
					a = np.array(line.split(','),dtype=np.float32)
					b = np.array([a])
					b = b.T
					# print b
					test.append(b)
					test_len.append(len(b))
				count += 1
		else:
			for line in f1:
				if count == i:
					a = np.array(line.split(','),dtype=np.float32)
					b = np.array([a])
					b = b.T
					test.append(b)
					test_len.append(len(b))
				count += 1
	
	
	fitModel(train,train_len,test_len,test)
