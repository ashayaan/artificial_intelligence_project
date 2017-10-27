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
		return 78.00
	elif aa == 'R':
		return 95.00
	elif aa == 'N':
		return 94.00
	elif aa == 'D':
		return 81.00
	elif aa == 'C':
		return 89.00
	elif aa == 'Q':
		return 87.00
	elif aa == 'E':
		return 78.00
	elif aa == 'G':
		return 84.00
	elif aa == 'H':
		return 84.00
	elif aa == 'I':
		return 88.00
	elif aa == 'L':
		return 85.00
	elif aa == 'K':
		return 87.00
	elif aa == 'M':
		return 80.00
	elif aa == 'F':
		return 81.00
	elif aa == 'P':
		return 91.00
	elif aa == 'S':
		return 107.00
	elif aa == 'T':
		return 93.00
	elif aa == 'W':
		return 104.00
	elif aa == 'Y':
		return 84.00
	elif aa == 'V':
		return 89.00
	else:	
		raise ValueError('The input must be one of the twenty amino acids: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V') 

if __name__ == '__main__':
	print est_flexibility('AAACDEQKKKLMMMWWWYYCCCEEENVDEFVY')
