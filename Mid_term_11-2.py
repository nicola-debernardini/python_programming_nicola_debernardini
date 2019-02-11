
file_in = open('insulin.gbk')
file_out = open('FASTA_insulin.txt','w')

AccessionID = ''
Organism = ''
Sequence = []

flag = 0

for line in file_in:
    line = line.strip()
    Seq_line = ''
    spl = line.split() 


    if 'ACCESSION' in line:
        spl = line.split()
        #print(spl[1])
        AccessionID = spl[1]

    elif 'ORGANISM' in line:
        spl = line.split()
        Organism = spl[1]+' '+spl[2]

    elif 'ORIGIN' in line:
        flag = 1

    elif len(line) != 0 and spl[0][0].isdigit() and flag == 1:
        spl = line.split()
        for i in range(1,len(spl)):
            Seq_line += spl[i]        
            Seq_line = Seq_line.upper()
            Sequence.append(Seq_line)

Complete_sequence = ''.join(Sequence)
Header = '>'+AccessionID+'|'+Organism
file_out.write(Header+'\n')
file_out.write(Complete_sequence)
file_out.close()