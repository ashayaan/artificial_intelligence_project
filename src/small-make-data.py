import numpy as np
import csv
from alphahelix import est_aplha_helix
from betaturn import est_beat_turn
from flexibility import est_flexibility
from hydrophobicity import est_hydrophob
from polarity import est_polarity
from recognition_factor import est_rec_factor

def get_feature_vector(sequence,name,list_antiname):
	label = 0
	if name.upper() in list_antiname:
		label = 1
	else:
		label = 0
	rec_f = np.asarray(est_rec_factor(sequence))
	rec_f = np.insert(rec_f,rec_f.size,label)
	return rec_f

def writeValues(antisequence,dict_name,name,data_file,labels,genomename,list_antiname):
	genomename.write(str(name)+'\n')
	features = get_feature_vector(antisequence,name,list_antiname)	
	print features.shape
	print len(features)
	print antisequence
	flag = features[features.shape[0]-1]
	if(flag == 1):
		with open('antigenic.csv','a') as train1:
			features.tofile(train1,sep=',',format='%10.5f')
			train1.write("\n")
	else:
		with open('nonantigenic.csv','a') as train2:
			features.tofile(train2,sep=',',format='%10.5f')
			train2.write("\n")

def processing(f,list_antiname):
	dict_name = ''
	antisequence = ''
	count = 0
	
	data_file = open('../data_files/genome-properties.csv','w')
	labels = open('../data_files/genome-label.csv','w')
	genomename = open('../data_files/genome-name.csv','w')
	
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