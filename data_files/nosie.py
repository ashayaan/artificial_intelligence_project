import pandas as pd
import numpy as np
import random

def noise(filename):
	df = pd.read_csv(filename, index_col = 0 )
	t = 60 - df.shape[0]
	
	for i in range(0,t):
		x = random.randint(0,(df.shape[0]-1))
		temp = df.iloc[x].copy()
		for j in range(0,temp.shape[0]-1):
			temp[j] = temp[j] + random.uniform(0,0.01)
		print "printing labels for " + str(temp['label']) + " " + str(df.iloc[x]['label'])
		df.loc[str(i)]=temp
	df.to_csv('day5/day5_nosieadded.csv', index = True , encoding= 'utf-8')

		


if __name__ == '__main__':
	filename = 'day5/day5.csv'
	noise(filename)