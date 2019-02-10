# miscellaneous.py
# For the following exercises, pseudo-code is not required

# Exercise 1
# Create a list L of numbers from 21 to 39
# print the numbers of the list that are even
# print the numbers of the list that are multiples of 3

l = []
for i in range(21,40):
	l.append(i)

for a in l:   # print the numbers of the list that are even
	if a%2 == 0:
		print(a)

for b in l:   # print the numbers of the list that are multiples of 3
	if b%3 == 0:
		print(b)


# Exercise 2
# Print the last two elements of L 

lengh_l = len(l)
print(l[lengh_l-2],l[lengh_l-1])

# Exercise 3
# What's wrong with the following piece of code? Fix it and 
# modify the code in order to have it work AND to have "<i> is in the list" 
# printed at least once

L = [1, 2, 3]
for i in range(10):
	if i in L:
		print(str(i)+' is in the list')
	else:
		print(str(i)+' not found')    


# Exercise 4
# Read the first line from the sprot_prot.fasta file
# Split the line using 'OS=' as delimiter and print the second element
# of the resulting list 

f = open('sprot_prot.fasta').readlines()
spl = f[0].split('OS=')
spl[1]

# Exercise 5
# Split the second element of the list of Exercise 4 using blanks
# as separators, concatenate the first and the second elements and print
# the resulting string

spl2 = spl[1].split(' ')
specie = spl2[0]+' '+spl2[1]
print(specie)

# Exercise 6
# reverse the string 'asor rosa'

string = 'asor rosa'
string[::-1]

# Exercise 7
# Sort the following list: L = [1, 7, 3, 9]

L = [1, 7, 3, 9]
L.sort()

# Exercise 8
# Create a new sorted list from L = [1, 7, 3, 9] without modifying L

sort_L = sorted(L)


# Exercise 9
# Write to a file the following 2 x 2 table:
# 2 4
# 3 6

f = open('Table_exercise9.txt','w')
f.write('2 4\n3 6')
f.close()
