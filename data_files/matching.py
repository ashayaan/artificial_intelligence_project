
l = []

def match(f):
	n = open('antiname.txt','r')
	
	for name in n:
		x = name.split('\n')
		l.append(x[0].upper())
	n.close()

	n = open('filtered.txt','w')
	flag = 0
	for line in f:
		if line[0] == '>':
			flag = 0
			n.write('ENDING\n')
			x = line.split()
			s=''
			for  i in range(1,len(x)):
				if x[i] == 'OS=Plasmodium':
					break
				s = s + x[i] + ' '
			s = s.strip()
			if s.upper() in l:
				n.write(s+'\n')
				flag = 1
		if flag == 1 and line[0] != '>':
		 	n.write(line)

def seperate(f):
	flag = 0
	count = 0
	file = open('names.txt','r')
	for line in f:
		if line == 'ENDING\n':
			flag = 0
			try:
				file.close()
			except:
				continue
		elif flag == 0 and line != 'ENDING\n':
			count = count + 1
			line = line + str(count)
			filename = 'data/'+line+'.txt'
			file = open(filename,'w')
			flag = 1
		elif flag == 1:
			file.write(line)

if __name__ == '__main__':
	f = open('uniprot-plasmodium+falciparum.fasta' , 'r')
	match(f)
	f.close()

	t = open('filtered.txt','r')
	seperate(t)
	