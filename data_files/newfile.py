def fiter(f):
	for line in f:
		if line[0] == '>':
			x = line.split()
			for  i in range(1,len(x)):
				if x[i] == 'OS=Plasmodium':
					break
				print x[i],
			print " "

if __name__ == '__main__':
	f = open('uniprot-plasmodium+falciparum.fasta','r')
	fiter(f)