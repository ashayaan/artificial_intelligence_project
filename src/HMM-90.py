import pandas as pd
import numpy as np
from hmmlearn import hmm


def fitModel(train,train_len,test,test_len):
	x = np.concatenate(train)
	# y = np.concatenate(test)
	remodel = hmm.GaussianHMM(n_components=2,covariance_type="full",min_covar=2 ,n_iter=10,algorithm='map')
	remodel.fit(x,train_len)
	result = []
	count = 0
	for i in test:	
		l = np.mean(remodel.predict(i))
		# print i[-1],
		ans = 0
		if l > 0.5:
			ans = 1
			result.append(1)
		else:
			ans = 0
			result.append(0)
		if ans == i[-1]:
			count+=1
	print "labels predicted correctly "+ str(count) + " Accuracy " + str(count/56.0) + "\n"
	return result

def trainData(f1):
	train = []
	train_len = []

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

	return train,train_len
	
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

	return test,test_len


if __name__ == '__main__':
	#filename =["../data_files/genome-properties-alpha.csv","../data_files/genome-properties-beta.csv","../data_files/genome-properties-flex.csv","../data_files/genome-properties-polar.csv","../data_files/genome-properties-hydro.csv"]
	
	filename =["../data_files/genome-properties-alpha.csv","../data_files/genome-properties-beta.csv","../data_files/genome-properties-flex.csv","../data_files/genome-properties-hydro.csv","../data_files/genome-properties-accessebility.csv"]

	temp_result = []


	for name in filename:
		f1 = open(name,'r')
		train,train_len = trainData(f1)

		f1 = open(name,'r')
		test,test_len = testData(f1)
		print "running for " + str(name)
		temp_result.append(fitModel(train,train_len,test,test_len))

	result = np.array(temp_result)
	result = np.sum(result,axis=0)
	result = result / 5.0

	count = 0
	for i in range(len(result)):
		ans = 0
		if result[i] > 0.5:
			ans = 1
		if ans == test[i][-1]:
			count+=1
	print "Consolidated labels predicted correctly "+ str(count) + " Consolidated Accuracy " + str(count/56.0) 

		
