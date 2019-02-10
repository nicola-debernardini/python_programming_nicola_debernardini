# average_function.py
# For this exercise the pseudo-code is required (in this same file) 
# Write a function that calculates the average of the values of
# any vector of 10 numbers 
# Each single value of the vector should be read from the keyboard
# and added to a list.
# Print the input vector and its average 
# Define separate functions for the input and for calculating the average

'''
Pseudo-code:

First function:
1) Define a function average that take in input a vector of ten number
2) Sum all the numbers of the vector 
3) Divide the result by 10

Input from keyboard:
1) Define a function input_vector
2) Create an empty vector
3) Ask to the enduser the ten elements of his vector and save them in the vector 

Finally:
1) call the fuction input_vector to input the vector
2) call the function average using as input the outcome of the previous fuction 
3) print the result 
'''

def average(vec):
	aver = 0
	som = 0
	for i in vec:
		som += i
	aver = som/10
	
	return aver

def input_vector():
	vec = []
	print('Inser the element of your vector:\n')
	for i in range(0,10):
		n = int(input('Element number %d: ' %(i+1)))
		vec.append(n)
	
	return vec

vector = input_vector()
print('\nThe average of the element of the vector just inputed is:', average(vector))
