# parsing_fasta.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a script that:
# a) Reads sprot_prot.fasta line by line
# b) Copies to a new file ONLY the record(s) that are not from Homo sapiens
# b) And prints their source organism and sequence lenght 
# Use separate functions for the input and the output 


'''
Pseudo-code:

1) Open the file sprot_prot.fasta

2) Define two variable that are uese to save the header and the sequence 
3) Use a for cicle that go trough the lines of the file
4) If the first character of the line is equal to '>' and the sequence is empty 
	1) Verify if the line don't belongue to Homo sapiens'
		- in that case save the line as the header 

5) Check if the first character is not '>' and the header is full:
	-save the following sequence in a variable seq 

6) Check if the first character of the string is '>' and the sequence is full:
	- wirte the header and the sequence in a new file 
	- clear the variable of the sequence and the header 
	- check again if the line where the cicle is now don't belongue to Homo sapiens'
		- in that case save the line as the header
		
7) finally out of the cicle print the records of the last sequence that don't belongue to an Homo sapiens that where not printed before because the cicle where finished 
'''

f = open('sprot_prot.fasta')
file_out = open('output_parsing.fasta','w')
seq = ''
header = ''

for l in f:
	if l[0] == '>' and seq == '':		
		spl = l.split('OS=')
		spl2 = spl[1].split(' ')
		specie = spl2[0]+' '+spl2[1]
		if specie != 'Homo sapiens':
			header = l
			true_specie = specie

	elif l[0] == '>' and seq != '':
		file_out.write(header+seq+'\n'+'The lengh of the sequence is %d and the source organism is %s' %(sequence_lengh,true_specie)+'\n\n\n')
		seq = ''
		header = ''	
		spl = l.split('OS=')
		spl2 = spl[1].split(' ')
		specie = spl2[0]+' '+spl2[1]
		if specie != 'Homo sapiens':
			header = l
			true_specie = specie
	
	elif l[0] != '>' and header:
		seq += (l.strip()+'\n')
		sequence_lengh = len(seq)

if header:
	file_out.write(header+seq+'\n'+'The lengh of the sequence is %d and the source organism is %s' %(sequence_lengh,true_specie))

file_out.close()
		 



