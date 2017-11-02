import pandas as pd
import numpy as np
from alphahelix import est_alpha_helix
from betaturn import est_beta_turn
from flexibility import est_flexibility
from polarity import est_polarity
from hydrophobicity import est_hydrophob
from recognition_factor import est_rec_factor

def get_feature_vector(sequence):
	alpha = np.asarray(est_alpha_helix(sequence))
	beta = np.asarray(est_beta_turn(sequence))
	flex = np.asarray(est_flexibility(sequence))
	pol = np.asarray(est_polarity(sequence))
	hydro = np.asarray(est_hydrophob(sequence))
	rec_f = np.asarray(est_rec_factor(sequence))
	features = np.vstack((alpha,beta,flex,pol,hydro,rec_f))
	return features 

def write_feature_file(filename):
	sequence_file = open(filename,'r')
	for sequence in sequence_file:
		features = get_feature_vector(sequence.strip())	
		shp = features.shape
		dims = np.asarray([ [shp[0],shp[1]] ])
		with open('train_small.csv','a') as train:
			np.savetxt(train,dims,fmt="%d",delimiter=',')
			np.savetxt(train, features,fmt="%.2f",delimiter=',')
		

if __name__ == "__main__":
	write_feature_file('proteins-small.txt')
#print get_feature_vector('EEMVEENVILE')
#print get_feature_vector('EEMVEENVILE').shape


