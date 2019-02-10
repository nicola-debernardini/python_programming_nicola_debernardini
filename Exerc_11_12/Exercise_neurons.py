
f = open('neuron_data.txt')
l1 = []; l2 = []

for line in f:
	# spl = line.split()   --> in this case it split on every type of space like: ' ' or '\t' or '\n'
	if line.split()[0] == '1':
		l1.append(float(line.split()[1]))
	else:
		l2.append(float(line.split()[1]))
print(l1,l2)

def average(L1):
	average_l = round(sum(L1)/len(L1),3)
	return average_l

def stdev(list1):
	import math 
	nominator = 0
	for i in list1:
		nominator += (i-average(list1))**2
	print(nominator)
	stdeviation = math.sqrt(nominator/len(list1))
	print(stdeviation)
	return stdeviation
	

print('The average of l1 is %f and of l2 is %f' %(average(l1), average(l2)))
print('The standard deviation of l1 is %f and of l2 %f' %(stdev(l1),stdev(l2)))




