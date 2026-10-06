import numpy as np 


#Slicing 


array = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])

# array[start:end:step] 
#the end index is exclusive : array[0:2] = array[0] and array[1] but not array[2]
print(array[1::2])

#Collumn selection 

print(array[0,0::2])
print("\n\n")
print(array[0::3 ,0::3])
print("\n\n")
print(array[-2 :  , 0:2])




