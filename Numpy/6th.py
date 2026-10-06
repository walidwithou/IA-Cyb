import numpy as np 

# Aggregate functions = summarize data and typically 
# return a single value

array = np.array([[1,2,3,4] , [1,2,3,6]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))# Standard deviation  = measure of spread in the data
print(np.var(array))# Varience
print(np.min(array))#minimum , for the index : np.argmin
print(np.max(array))#maximum , for the index : np.argmax

# we can also apply the functions on the rows / columns with the axis arg

print(np.sum(array,axis=0)) #axis = 0 , sum each collumn 
print(np.sum(array, axis = 1)) # axis = 1 , sum each line