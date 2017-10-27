import numpy as np
import pandas as pd

def est_beat_turn(protein_sequence):
	prot_seq = list(protein_sequence)
	try:
		beta_seq = map(beta_turn, prot_seq)
	except ValueError as e:
		beta_seq = []
		print e
	list_of_lists = [ beta_seq[i-4:i+5] for i in range(4,len(prot_seq)-4) ]
	return np.mean(list_of_lists,axis=1)
	
def beta_turn(aa):
	if aa == 'A':
		return 0.788
	elif aa == 'R':
		return 0.912
	elif aa == 'N':
		return 1.572
	elif aa == 'D':
		return 1.197
	elif aa == 'C':
		return 0.965
	elif aa == 'Q':
		return 0.997
	elif aa == 'E':
		return 1.149
	elif aa == 'G':
		return 1.860
	elif aa == 'H':
		return 0.970
	elif aa == 'I':
		return 0.240
	elif aa == 'L':
		return 0.670
	elif aa == 'K':
		return 1.302
	elif aa == 'M':
		return 0.436
	elif aa == 'F':
		return 0.624
	elif aa == 'P':
		return 1.415
	elif aa == 'S':
		return 1.316
	elif aa == 'T':
		return 0.739
	elif aa == 'W':
		return 0.546
	elif aa == 'Y':
		return 0.795
	elif aa == 'V':
		return 0.387
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 

if __name__ == '__main__':
	print est_beat_turn('AAACDEQKKKLMMMWWWYYCCCEEENVDEFVY')
