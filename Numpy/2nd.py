import numpy as np

#Multi dimensional arrays 

array = np.array('A')
print("dimension of array :" , array.ndim , array.shape)
# a list is a one dimensional array

array2 = np.array(['A' , 'B' , 'C'])
print("dimension of array : " , array2.ndim , array2.shape)
# a matrix (2 dimensional array)
array3 = np.array([[1 , 2 , 4] ,
                   [1 , 2 , 4] , 
                   [1 , 2 , 4]
                    ])
print("dimension of array : " , array3.ndim , array3.shape)
array4 = np.array([[['A' , 'B' , 'C'],
                  ['A' , 'B' , 'D'],
                  ['A' , 'B' , 'M']],[['A' , 'B' , 'C'],
                  ['A' , 'B' , 'D'],
                  ['A' , 'B' , 'M']],[['A' , 'B' , 'C'],
                  ['A' , 'B' , 'D'],
                  ['A' , 'B' , 'M']]]
                  )
print("dimension of array : " , array4.ndim , array4.shape )
# bigger dimensions are possible to create
# 
# array.ndim = number of dimensions
# 
# array.shape =  size of the array (number of rows , cols , depth ) => array.ndim = len(array.shape)


print(array4[0][1][2])
#chain indexing : first layer , 2nd row , 3rd element

print(array4[0,0,0])
#Multidimensional indexing

for i in range(array4.shape[0]) : 
    for j in range(array4.shape[1]):
        for k in range(array4.shape[2]):
            print("element position : " , i ,",", j ,",", k , "   | ELEMENT / " , array4[i,j,k])
