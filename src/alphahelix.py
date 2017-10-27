import numpy as np
import pandas as pd

def est_aplha_helix(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		alpha_seq = map(alpha_helix, prot_seq)
	except ValueError as e:
		alpha_seq = []
		print e
	list_of_lists = [ alpha_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def alpha_helix(aa):
	if aa == 'A':
		return 1.489
	elif aa == 'R':
		return 1.224
	elif aa == 'N':
		return 0.772
	elif aa == 'D':
		return 0.924
	elif aa == 'C':
		return 0.966
	elif aa == 'Q':
		return 1.164
	elif aa == 'E':
		return 1.504
	elif aa == 'G':
		return 0.510
	elif aa == 'H':
		return 1.003
	elif aa == 'I':
		return 1.003
	elif aa == 'L':
		return 1.236
	elif aa == 'K':
		return 1.172
	elif aa == 'M':
		return 1.363
	elif aa == 'F':
		return 1.195
	elif aa == 'P':
		return 0.492
	elif aa == 'S':
		return 0.739
	elif aa == 'T':
		return 0.785
	elif aa == 'W':
		return 1.090
	elif aa == 'Y':
		return 0.787
	elif aa == 'V':
		return 0.990
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 

if __name__ == '__main__':
	print est_aplha_helix('AAACDEQKKKLMMMWWWYYCCCEEENVDEFVY')
