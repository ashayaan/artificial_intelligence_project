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
		scr = remodel.score(test[test_len[i]+1:test_len[i]+test_len[i+1],:])
		result.append(scr)
	
	return result

def trainData(f1):
	train = []
	train_len = []
	for line in f1:
		a = np.array(line.split(','),dtype=np.float32)
		b = np.array([a])
		b = b.T
		train.append(b)
		train_len.append(len(b))

	f1.close()
	return np.concatenate(train),train_len
	
def testData(f1):
	test = []
	test_len = []
	for line in f1:
		a = np.array(line.split(','),dtype=np.float32)
		b = np.array([a])
		b = b.T
		test.append(b)
		test_len.append(len(b))

	f1.close()

	return np.concatenate(test),test_len


if __name__ == '__main__':	
	training_filename = ["../../data_files/try/gennome-non-properties-alpha.csv","../../data_files/try/gennome-non-properties-beta.csv","../../data_files/try/gennome-non-properties-flex.csv","../../data_files/try/gennome-non-properties-polar.csv","../../data_files/try/gennome-non-properties-hydro.csv","../../data_files/try/gennome-non-properties-accessebility.csv","../../data_files/try/gennome-non-properties-retention.csv"]
	testing_filename = ["../../data_files/try/genome-properties-alpha.csv","../../data_files/try/genome-properties-beta.csv","../../data_files/try/genome-properties-flex.csv","../../data_files/try/genome-properties-polar.csv","../../data_files/try/genome-properties-hydro.csv","../../data_files/try/genome-properties-accessebility.csv","../../data_files/try/genome-properties-retention.csv"]
	
	temp_result = []
	
	f = open(training_filename[0],'r')
	print "Creating Training data from " + str(training_filename[0])
	trainset,train_len = trainData(f)
	f = open(testing_filename[0],'r')
	print "Creating testing data from " + str(testing_filename[0])
	testset,test_len = testData(f)
	for name in training_filename[1:]:
		print "Creating Training data from " + str(name)
		f1 = open(name,'r')
		train,train_len = trainData(f1)
		trainset = np.column_stack([trainset,train])

	for name in testing_filename[1:]:
		print "Creating testing data from " + str(name)
		f1 = open(name,'r')
		test,test_len = testData(f1)
		testset = np.column_stack([testset,test])

	result = fitModel(trainset,train_len,testset,test_len)

	file = open("label.txt","r")

	lable_list = []
	count = 0
	for line in file:
		line = line.strip('\n')
		a = line
		a = int(a)
		if a == 1:
			count+=1
		lable_list.append(a)
	
	count = 0
	for i in range(len(result)):
		temp_label = 0
		if result[i] <= 3000:
			temp_label = 1
		x = str(lable_list[i]) + ' ' + str(temp_label)
		print x
		with open("result.txt",'a') as res:
			res.write(x + '\n')

		if temp_label == lable_list[i]:
			count+=1;
	print count