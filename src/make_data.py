from alphahelix import est_aplha_helix
from betaturn import est_beat_turn
from flexibility import est_flexibility
from hydrophobicity import est_hydrophob
from polarity import est_polarity
from recognition_factor import est_rec_factor


def writeProperty(l,data_file):
	for i in l:
		data_file.write(str(i))
		data_file.write(',')
	data_file.write('\n')


def writeValues(antisequence,dict_name,name,data_file,labels,list_antiname):
	if name.upper() in list_antiname:
		labels.write(name)
		labels.write(',')
		labels.write('1'+'\n')
	else:
		labels.write(name)
		labels.write(',')
		labels.write('0'+'\n')

	data_file.write('6')
	data_file.write(',')
	data_file.write(str(len(antisequence))+'\n')
	writeProperty(est_aplha_helix(antisequence),data_file)
	writeProperty(est_beat_turn(antisequence),data_file)
	writeProperty(est_flexibility(antisequence),data_file)
	writeProperty(est_hydrophob(antisequence),data_file)
	writeProperty(est_polarity(antisequence),data_file)
	writeProperty(est_rec_factor(antisequence),data_file)

def processing(f,list_antiname):
	dict_name = ''
	antisequence = ''
	count = 0
	
	data_file = open('../data_files/genome-properties.csv','w')
	labels = open('../data_files/genome-label.csv','w')
	
	for line in f:
		if line[0] == '>':
			if(antisequence and dict_name):
				writeValues(antisequence,dict_name,name,data_file,labels,list_antiname)
			x = line.split()
			dict_name = ''
			name=''
			antisequence = ''
			for i in range(len(x)):
				if x[i] == 'OS=Plasmodium':
					break
				dict_name = dict_name + x[i] +' '

			for  i in range(1,len(x)):
				if x[i] == 'OS=Plasmodium':
					break
				name = name + x[i] + ' '

			dict_name = dict_name.strip()
			dict_name = dict_name.strip('>')
			name = name.strip()
			name = name.replace(',','')
		else:
			antisequence += line.split('\n')[0]
	

if __name__ == '__main__':
	f = open('../data_files/uniprot-plasmodium+falciparum.fasta' , 'r')
	anti = open('../data_files/antiname.txt','r')
	
	list_antiname=[]
	
	for name in anti:
		x = name.split('\n')
		list_antiname.append(x[0].upper())
	anti.close()

	processing(f,list_antiname)
	