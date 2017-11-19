import csv
import os
import numpy as np
from alphahelix import est_aplha_helix
from betaturn import est_beat_turn
from flexibility import est_flexibility
from hydrophobicity import est_hydrophob
from polarity import est_polarity
from recognition_factor import est_rec_factor
from accessebility import est_accessebility
from tfa_retention import est_tfa_retention

global_count = 0

def writeValues(antisequence,name,data_file_antigenic,data_file_nonantigenic,genomename,list_antiname):
	genome_name_writer=csv.writer(open(genomename,'a'))
	
	genome_name_writer.writerow([str(name)])
	
	lable = 0
	if name.upper() in list_antiname:
		label = 1
	else:
		label = 0

	aplha = np.asarray(est_aplha_helix(antisequence))
	aplha = np.insert(aplha,aplha.size,label)
	
	beat = np.asarray(est_beat_turn(antisequence))
	beat = np.insert(beat,beat.size,label)
	
	flex = np.asarray(est_flexibility(antisequence))
	flex = np.insert(flex,flex.size,label)

	pol = np.asarray(est_polarity(antisequence))
	pol = np.insert(pol,pol.size,label)

	hydro = np.asarray(est_hydrophob(antisequence))
	hydro = np.insert(hydro,hydro.size,label)

	rec_f = np.asarray(est_rec_factor(antisequence))
	rec_f = np.insert(rec_f,rec_f.size,label)

	accessebility = np.asarray(est_accessebility(antisequence))
	accessebility = np.insert(accessebility,accessebility.size,label)

	retention = np.asarray(est_tfa_retention(antisequence))
	retention = np.insert(retention,retention.size,label)

	features = [aplha,beat,flex,pol,hydro,rec_f,accessebility,retention]
	
	if label == 0 and global_count <=300:
		for i in range(len(data_file_nonantigenic)):
			with open(data_file_nonantigenic[i],'a') as csvfile:
				data_file_write = csv.writer(csvfile)
				data_file_write.writerow(features[i])
		
	else:
		for i in range(len(data_file_antigenic)):
			with open(data_file_antigenic[i],'a') as csvfile:
				data_file_write = csv.writer(csvfile)
				data_file_write.writerow(features[i])




def delteFile(filename):
	try:
		os.remove(filename)
	except OSError:
		pass

def processing(f,list_antiname):
	dict_name = ''
	antisequence = ''
	count = 0

	data_file_antigenic = ["../../data_files/try/genome-properties-alpha.csv","../../data_files/try/genome-properties-beta.csv","../../data_files/try/genome-properties-flex.csv","../../data_files/try/genome-properties-polar.csv","../../data_files/try/genome-properties-hydro.csv","../../data_files/try/genome-properties-rec.csv","../../data_files/try/genome-properties-accessebility.csv","../../data_files/try/genome-properties-retention.csv"]
	data_file_nonantigenic = ["../../data_files/try/gennome-non-properties-alpha.csv","../../data_files/try/gennome-non-properties-beta.csv","../../data_files/try/gennome-non-properties-flex.csv","../../data_files/try/gennome-non-properties-polar.csv","../../data_files/try/gennome-non-properties-hydro.csv","../../data_files/try/gennome-non-properties-rec.csv","../../data_files/try/gennome-non-properties-accessebility.csv","../../data_files/try/gennome-non-properties-retention.csv"]
	genomename = "../../data_files/try/genome-name.csv"

	delteFile(genomename)
	for i in data_file_antigenic:
		delteFile(i)
	for i in data_file_nonantigenic:
		delteFile(i)
	
	for line in f:
		if line[0] == '>':
			if(antisequence and dict_name):
				writeValues(antisequence,name,data_file_antigenic,data_file_nonantigenic,genomename,list_antiname)
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
	f = open('../../data_files/uniprot-plasmodium+falciparum.fasta' , 'r')
	anti = open('../../data_files/antiname.txt','r')
	list_antiname=[]
	
	for name in anti:
		x = name.split('\n')
		list_antiname.append(x[0].upper())
	anti.close()

	processing(f,list_antiname)
