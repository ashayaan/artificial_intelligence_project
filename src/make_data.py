import csv
import os
import numpy as np
from alphahelix import est_aplha_helix
from betaturn import est_beat_turn
from flexibility import est_flexibility
from hydrophobicity import est_hydrophob
from polarity import est_polarity
from recognition_factor import est_rec_factor


def writeValues(antisequence,dict_name,name,data_file,labels,genomename,list_antiname):
	genome_name_writer=csv.writer(open(genomename,'a'))
	label_writer=csv.writer(open(labels,'a'))
	
	genome_name_writer.writerow([str(name)])
	
	if name.upper() in list_antiname:
		label_writer.writerow([1])
	else:
		label_writer.writerow([0])
	# data_file.write('6')
	# data_file.write(',')
	# data_file.write(str(len(antisequence))+'\n')
	
	aplha = np.asarray(est_aplha_helix(antisequence))
	beat = np.asarray(est_beat_turn(antisequence))
	flex = np.asarray(est_flexibility(antisequence))
	pol = np.asarray(est_polarity(antisequence))
	hydro = np.asarray(est_hydrophob(antisequence))
	rec_f = np.asarray(est_rec_factor(antisequence))

	with open(data_file,'a') as csvfile:
		data_file_write = csv.writer(csvfile)
		data_file_write.writerow([6]+[len(aplha)])
		data_file_write.writerow(aplha)
		data_file_write.writerow(beat)
		data_file_write.writerow(flex)
		data_file_write.writerow(pol)
		data_file_write.writerow(hydro)
		data_file_write.writerow(rec_f)
		# data_file_write.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



def delteFile(filename):
	try:
		os.remove(filename)
	except OSError:
		pass

def processing(f,list_antiname):
	dict_name = ''
	antisequence = ''
	count = 0

	data_file = "../data_files/genome-properties.csv"
	labels = "../data_files/genome-label.csv"
	genomename = "../data_files/genome-name.csv"

	delteFile(genomename)
	delteFile(data_file)
	delteFile(labels)
	
	for line in f:
		if line[0] == '>':
			if(antisequence and dict_name):
				writeValues(antisequence,dict_name,name,data_file,labels,genomename,list_antiname)
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