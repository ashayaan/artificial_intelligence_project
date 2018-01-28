import pandas as pd
import numpy as np
from hmmlearn import hmm


def fitModel(train,train_len,test,test_len):
	print train.shape
	remodel = hmm.GaussianHMM(n_components=2,min_covar=1,n_iter=10)
	remodel.fit(train,train_len)
	result = []

	count = 0
	
	for i in range(len(test_len)-1):	
		# print test[test_len[i]+1:test_len[i]+test_len[i+1],:]
		# print '\n'
		scr = remodel.decode(test[test_len[i]+1:test_len[i]+test_len[i+1],:])
		# print scr[0]
		result.append(scr[0])

	return result

def trainData(f1):
	train = []
	train_len = []

	count = 0
	for line in f1:
		if count < 300:
			a = np.array(line.split(','),dtype=np.float32)
			#print a
			b = np.array([a])
			b = b.T
			train.append(b)
			train_len.append(len(b))
		count += 1

	f1.close()

	return np.concatenate(train),train_len
	
def testData(f1):
	test = []
	test_len = []
	count = 0
	for line in f1:
		if count >= 300:
			a = np.array(line.split(','),dtype=np.float32)
			b = np.array([a])
			b = b.T
			test.append(b)
			test_len.append(len(b))
		count += 1

	f1.close()

	return np.concatenate(test),test_len


if __name__ == '__main__':	
	filename =["../../data_files/genome-properties-alpha.csv","../../data_files/genome-properties-beta.csv","../../data_files/genome-properties-flex.csv","../../data_files/genome-properties-hydro.csv","../../data_files/genome-properties-accessebility.csv"]
	temp_result = []
	
	f = open(filename[0],'r')
	trainset,trainlen = trainData(f)
	f = open(filename[0],'r')
	testset,testlen = testData(f)
	for name in filename[1:]:
		f1 = open(name,'r')
		train,train_len = trainData(f1)
		trainset = np.column_stack([trainset,train])

		f1 = open(name,'r')
		test,test_len = testData(f1)
		testset = np.column_stack([testset,test])
		print "running for " + str(name)
	
	x = fitModel(trainset,train_len,testset,test_len)
	y = np.mean(x)

	print y