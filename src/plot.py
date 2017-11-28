import itertools
import pandas as pd
import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


seq2 = pd.Series(np.arange(2))


def test(test_data, test_labels):
	cnf_matrix = confusion_matrix(test_data, test_labels)
	plt.figure()
	plot_confusion_matrix(cnf_matrix, classes=seq2, normalize=True,title='Normalized confusion matrix')
	plt.show()

def plot_confusion_matrix(cm, classes, normalize=False, title='Confusion matrix', cmap=plt.cm.Blues):
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


if __name__ == '__main__':
	file = open("labels.text",'r')
	original = []
	predicted = []
	for line in file:
		l = line.split()
		print l
		original.append(l[0])
		predicted.append(l[1])

	# print original
	test(original,predicted)
