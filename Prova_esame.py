
# Sample-exercises-mid-term-exam

# 1. The function times_table takes a number n as input and returns its times table 

def times_table(n):
#	table = {}
	times_table = []
	for i in range(1,11):
#		print(i, n*i)
#		table[i] = n*i
		times_table.append([i, i*n])		
	return times_table


# 2. The function print_table takes a 2x2 times-table as input and print it nicely

def print_table(t):
	for i in t:
		print("{0:4.1f} * {1:3.1f} = {2:3.1f}".format(i[0],t[0][1],i[1]))


#3 Use  the functioon print_table(t) to print the times_table(n) of a number inputted from the keyboard

N = float(input('For which number would you like to create a time table? '))
t = times_table(N)
print_table(t)



#4 This function read a multiple sequence FASTA file an write to a new file only the records from Homo sapiens

f = open('sequence.fasta').readlines()
lis =  []
num_seq = 0
dic = {}

for i in f:
	if i[0] == '>':
		lis = []		
		num_seq += 1		
		l = i.split(' ')
		specie = l[1]+' '+l[2]	
		sequence = i

	elif i[0] != '>' and specie == 'Homo sapiens':
			lis.append(i[:len(i)-1])
	
	if specie == 'Homo sapiens':
		seq = sequence
		dic[seq] = '\n'.join(lis)
				
for k in dic:
	records = open('records_Homo_sapiens','a+')
	records.write('\n\n'+str(k)+dic[k])
	records.close()
		

#5 Read a multiple sequence file in Fasta format and only write to a ne new file the records of the sequence which statt with a methionine and contain at least two tryptophane residues 

f = open('sequenceProt.fasta').readlines()
lis =  []
num_seq = 0
dic = {}

for i in f:
	if i[0] == '>':
		seq_validator = 0
		count_W = 0
		sequence = ''		
		lis = []			
		if f[f.index(i)+1].startswith('M') == True:
			sequence = i
			seq_validator = True

	elif seq_validator == True:
		lis.append(i[:len(i)-1])
		count_W += i.count('W')
			 
	
	if seq_validator == True and count_W >= 2:
		dic[sequence] = '\n'.join(lis)
				
for k in dic:
	records = open('Seq_2W_startw_M.txt','a+')
	records.write('\n\n'+str(k)+dic[k])
	records.close()






