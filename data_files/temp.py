if __name__ == '__main__':
	file = open('genome-label.csv','r')
	count = 0

	for line in file:
		if count >= 300:
			print line,
		count+=1