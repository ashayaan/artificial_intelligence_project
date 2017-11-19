import numpy as np
import pandas as pd

def est_polarity(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		polarity_seq = map(polarity, prot_seq)
	except ValueError as e:
		polarity_seq = []
		print e
	list_of_lists = [ polarity_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def polarity(aa):
	if aa == 'A':
		return 8.100
	elif aa == 'R':
		return 10.500
	elif aa == 'N':
		return 11.600
	elif aa == 'D':
		return 13.00
	elif aa == 'C':
		return 5.500
	elif aa == 'Q':
		return 10.500
	elif aa == 'E':
		return 12.300
	elif aa == 'G':
		return 9.000
	elif aa == 'H':
		return 10.400
	elif aa == 'I':
		return 5.200
	elif aa == 'L':
		return 4.900
	elif aa == 'K':
		return 11.300
	elif aa == 'M':
		return 5.700
	elif aa == 'F':
		return 5.200
	elif aa == 'P':
		return 8.000
	elif aa == 'S':
		return 9.200
	elif aa == 'T':
		return 8.600
	elif aa == 'W':
		return 5.400
	elif aa == 'Y':
		return 6.200
	elif aa == 'V':
		return 5.900
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 
