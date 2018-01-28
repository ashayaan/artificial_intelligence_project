import pandas as pd
import numpy as np
from hmmlearn import hmm


def fitModel(train,train_len,test,test_len):
	x = np.concatenate(train)
	remodel = hmm.GaussianHMM(n_components=2,covariance_type="full",min_covar=3,n_iter=1000,algorithm = "map")
	remodel.fit(x,train_len)
	result = []
	count = 0
	for i in test:	
		l = remodel.score(i)
		result.append(l)

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

	return train,train_len
	
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

	return test,test_len


if __name__ == '__main__':
	#filename =["../../data_files/genome-properties-alpha.csv","../../data_files/genome-properties-beta.csv","../../data_files/genome-properties-flex.csv","../../data_files/genome-properties-polar.csv","../../data_files/genome-properties-hydro.csv"]
	
	training_filename = ["../../data_files/Ensemble-Data-Files/gennome-non-properties-alpha.csv","../../data_files/Ensemble-Data-Files/gennome-non-properties-beta.csv","../../data_files/Ensemble-Data-Files/gennome-non-properties-flex.csv","../../data_files/Ensemble-Data-Files/gennome-non-properties-polar.csv","../../data_files/Ensemble-Data-Files/gennome-non-properties-hydro.csv","../../data_files/Ensemble-Data-Files/gennome-non-properties-accessebility.csv"]
	testing_filename = ["../../data_files/Ensemble-Data-Files/genome-properties-alpha.csv","../../data_files/Ensemble-Data-Files/genome-properties-beta.csv","../../data_files/Ensemble-Data-Files/genome-properties-flex.csv","../../data_files/Ensemble-Data-Files/genome-properties-polar.csv","../../data_files/Ensemble-Data-Files/genome-properties-hydro.csv","../../data_files/Ensemble-Data-Files/genome-properties-accessebility.csv"]
	

	temp_result = []


	for i in range(len(training_filename)):
		f1 = open(training_filename[i],'r')
		train,train_len = trainData(f1)

		f1 = open(testing_filename[i],'r')
		test,test_len = testData(f1)

		print "running for " + str(testing_filename[i])
		
		temp_result.append(fitModel(train,train_len,test,test_len))

	result = np.array(temp_result)

	result = list(np.sum(result,axis = 0))
	mean = np.mean(result)
	print mean
	count = 0

	f = open('../results/labels2.text','w')
	for i in range(len(result)):
		ans = 0
		if result[i] <= 2700:
			ans = 1
		if ans == test[i][-1]:
			count+=1
		f.write(str(test[i][-1]) + " " + str(ans) + "\n") 
	print "Consolidated labels predicted correctly "+ str(count) + " Consolidated Accuracy " + str(count/108.0) 





		
