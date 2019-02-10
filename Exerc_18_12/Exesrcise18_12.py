f = open('Data.txt','r')
table = []
for line in f:
	table.append(line.split())

table.pop(2)
print(table)
exp = [5,45,3,23,222]
table.insert(1,exp)
print(table)

f2 = open('Table.txt', 'w')
for l in table:
	lin = '\t'.join(l)
	f2.write(lin+'\n')

f2.close()

