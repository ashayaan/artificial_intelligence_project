import numpy as np
import pandas as pd

def est_hydrophob(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		hydrophob_seq = map(hydrophob_kyte_dolittle, prot_seq)
	except ValueError as e:
		hydrophob_seq = []
		print e
	list_of_lists = [ hydrophob_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def hydrophob_kyte_dolittle(aa):
	if aa == 'A':
		return 1.800
	elif aa == 'R':
		return -4.500
	elif aa == 'N':
		return -3.500
	elif aa == 'D':
		return -3.500
	elif aa == 'C':
		return 2.500
	elif aa == 'Q':
		return -3.500
	elif aa == 'E':
		return -3.500
	elif aa == 'G':
		return -0.400
	elif aa == 'H':
		return -3.200
	elif aa == 'I':
		return 4.500
	elif aa == 'L':
		return 3.800
	elif aa == 'K':
		return -3.900
	elif aa == 'M':
		return 1.900
	elif aa == 'F':
		return 2.800
	elif aa == 'P':
		return -1.600
	elif aa == 'S':
		return -0.800
	elif aa == 'T':
		return -0.700
	elif aa == 'W':
		return -0.900
	elif aa == 'Y':
		return -1.300
	elif aa == 'V':
		return 4.200
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 

est_hydrophob('AAACDEQKKKLMMMWWWYYCCCEEENVDEFVY')
