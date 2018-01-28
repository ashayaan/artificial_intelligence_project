import numpy as np
import pandas as pd

def est_accessebility(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		flexibility_seq = map(accessebility, prot_seq)
	except ValueError as e:
		flexibility_seq = []
		print e
	list_of_lists = [ flexibility_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def accessebility(aa):
	if aa == 'A':
		return 6.60
	elif aa == 'R':
		return 4.50
	elif aa == 'N':
		return 6.70
	elif aa == 'D':
		return 7.70
	elif aa == 'C':
		return 0.900
	elif aa == 'Q':
		return 5.200
	elif aa == 'E':
		return 5.700
	elif aa == 'G':
		return 6.700
	elif aa == 'H':
		return 2.500
	elif aa == 'I':
		return 2.800
	elif aa == 'L':
		return 4.800
	elif aa == 'K':
		return 10.300
	elif aa == 'M':
		return 1.000
	elif aa == 'F':
		return 2.400
	elif aa == 'P':
		return 4.800
	elif aa == 'S':
		return 9.400
	elif aa == 'T':
		return 7.000
	elif aa == 'W':
		return 1.400
	elif aa == 'Y':
		return 5.100
	elif aa == 'V':
		return 4.500
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 
