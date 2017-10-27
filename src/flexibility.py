import numpy as np
import pandas as pd

def est_flexibility(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		felxibility_seq = map(average_flexibility, prot_seq)
	except ValueError as e:
		felxibility_seq = []
		print e
	list_of_lists = [ felxibility_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def average_flexibility(aa):
	if aa == 'A':
		return 0.360
	elif aa == 'R':
		return 0.530
	elif aa == 'N':
		return 0.460
	elif aa == 'D':
		return 0.510
	elif aa == 'C':
		return 0.350
	elif aa == 'Q':
		return 0.490
	elif aa == 'E':
		return 0.500
	elif aa == 'G':
		return 0.540
	elif aa == 'H':
		return 0.320
	elif aa == 'I':
		return 0.460
	elif aa == 'L':
		return 0.370
	elif aa == 'K':
		return 0.470
	elif aa == 'M':
		return 0.300
	elif aa == 'F':
		return 0.310
	elif aa == 'P':
		return 0.510
	elif aa == 'S':
		return 0.510
	elif aa == 'T':
		return 0.440
	elif aa == 'W':
		return 0.310
	elif aa == 'Y':
		return 0.420
	elif aa == 'V':
		return 0.390
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 

if __name__ == '__main__':
	print est_flexibility('AAACDEQKKKLMMMWWWYYCCCEEENVDEFVY')
