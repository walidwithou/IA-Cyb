import numpy as np 

#Broadcasting 

# Broadcasting allowds Numpy to perform operations on arrays 
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape 

# The dimensions have the same size 
#OR
# One of the dimensions has a size of 1

array1 = np.array([[1,2,3,4],[5,6,7,9],[2 , 3 , 4 , 3],[1 ,1 ,1 ,1]])
array2 = np.array([[1],[2],[3],[4]])

print(array1.shape)
print(array2.shape)

print(array1 + array2)
# Example : array1(First dimension = 1 , second dimension = 4) , array1(First dimension = 4, second dimension = 1) 
# dimensions dont match but for each array , one of the dimensions is 1


#Multiplication table 

array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(array1 * array2)

array3 = array1 * array2

print("MULTIPLICATION TABLE ")
