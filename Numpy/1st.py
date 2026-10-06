import numpy as np 

print(np.__version__)

my_list =  [1,2,3,4,5]
print(my_list)
print(my_list * 2)

#Multiplying a list by 2 doubles the number of it's  elements 

my_array = np.array(my_list)
my_array = my_array * 2 

print(my_array)

#multiplying a np.array by 2 doubles the value of it's numbers , equivale,t to [element * 2 for element in my_list]