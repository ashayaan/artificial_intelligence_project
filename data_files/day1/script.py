import pandas as pd;
import numpy as np;
import os;

def read(files):
	# for file in files: 
	data =[]
	label = []
	for name in files:
		file = open(name,"r")
		label.append(name.split('_')[0])
		x={}
		l = []
		for line in file:
			l.append(line)

		for i in range(3,len(l)-4):
			t = l[i].split()
			x[t[0]] = t[1]
		data.append(x)
	df = pd.DataFrame(data,index=label)
	filename = 'day1.csv'
	df.to_csv(filename, index=True, encoding='utf-8')


if __name__ == '__main__':
	files=[]
	indir = '/home/shayaan/sem_7/AI/data_files/day1'
	for filename in os.listdir(indir):
		if filename.endswith(".txt"):
			files.append(filename)
	read(files)
