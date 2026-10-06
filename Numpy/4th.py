import numpy as np 


#Scalar arithmetic 
array = np.array([1 , 2 , 3 , 4])

#basic operations 

print("ADDITION" , array +1)
print("SUBTRACTION" , array  - 2)
print("MULTIPLICATION" , array * 2)
print("DIVISION" , array / 3 )
print("MODULO" , array % 2)
print("EXPONENT" , array ** 4)

#Vectorized math functions

array = np.array([1,2,3])

# a vector is a 1 dimension array 
# numpy comes with some math functions : np.sqrt , np.square , np.abs (absolute value) , np.sign() : returns -1 fr negative numbers and 1 for positive , 0 FOR ZERO!!!!!
print(np.sqrt(array))
#rounding : using np.round ; to always round down we use np.floor
array2 = np.array([1.53 , 3.22 ,4.1])
print(np.round(array2))
print(np.floor(array2))
print(np.pi * array2 ** 2)


#Element wise operations 
# Two arrays , Each operation is applied element by element between two arrays


arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

mat1 = np.array([[2 , 6  , 7],[4 , 3 , 9 ]])
mat2 = np.array([[1,4],[4,2],[7,6]])


print(arr1 + arr2)
print(arr1 * arr2)
print(np.matmul(mat2 , mat1))

#Comparision operator 

scores = np.array([91 , 55  , 100 , 23 , 64  , 30])
perfect = scores == 100 
perfect[perfect == False] = True
print(perfect)
print(scores >= 60 )




