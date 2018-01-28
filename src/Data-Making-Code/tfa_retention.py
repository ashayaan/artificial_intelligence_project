import numpy as np
import pandas as pd

def est_tfa_retention(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		flexibility_seq = map(tfa_retention, prot_seq)
	except ValueError as e:
		flexibility_seq = []
		print e
	list_of_lists = [ flexibility_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def tfa_retention(aa):
	if aa == 'A':
		return 7.300
	elif aa == 'R':
		return -3.600
	elif aa == 'N':
		return -5.700
	elif aa == 'D':
		return -2.900
	elif aa == 'C':
		return -9.200
	elif aa == 'Q':
		return -0.300
	elif aa == 'E':
		return -7.100
	elif aa == 'G':
		return -1.200
	elif aa == 'H':
		return -2.100
	elif aa == 'I':
		return 6.600
	elif aa == 'L':
		return 20.000
	elif aa == 'K':
		return -3.70
	elif aa == 'M':
		return 5.60
	elif aa == 'F':
		return 19.200
	elif aa == 'P':
		return 5.100
	elif aa == 'S':
		return -4.100
	elif aa == 'T':
		return 0.800
	elif aa == 'W':
		return 16.300
	elif aa == 'Y':
		return 5.900
	elif aa == 'V':
		return 3.500
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 
