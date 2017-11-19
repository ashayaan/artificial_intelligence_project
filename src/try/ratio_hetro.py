import numpy as np
import pandas as pd

def est_ratio_hetro(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		flexibility_seq = map(ratio_hetro, prot_seq)
	except ValueError as e:
		flexibility_seq = []
		print e
	list_of_lists = [ flexibility_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def ratio_hetro(aa):
	if aa == 'A':
		return 0.000
	elif aa == 'R':
		return 0.650
	elif aa == 'N':
		return 1.330
	elif aa == 'D':
		return 1.380
	elif aa == 'C':
		return 2.750
	elif aa == 'Q':
		return 0.890
	elif aa == 'E':
		return 0.920
	elif aa == 'G':
		return 0.740
	elif aa == 'H':
		return 0.580
	elif aa == 'I':
		return 0.000
	elif aa == 'L':
		return 0.000
	elif aa == 'K':
		return 0.330
	elif aa == 'M':
		return 0.000
	elif aa == 'F':
		return 0.000
	elif aa == 'P':
		return 0.390
	elif aa == 'S':
		return 1.420
	elif aa == 'T':
		return 0.710
	elif aa == 'W':
		return 0.130
	elif aa == 'Y':
		return 0.200
	elif aa == 'V':
		return 0.000
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 
