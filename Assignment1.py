import numpy as np

arr = np.array([[[1,2,3,4],
               [5,6,7,8] ],
               [[1,2,3,4],
                [9,10,11,12]]]
               )

arr3 = np.array([
    [[1,2,3,4,5],[6,7,8,9,20]],
    [[11,12,13,14,15],[16,17,18,19,20]]
])
# print("1D array")
# print(arr)

# print()
# print("3D Array")
print(arr.data) #memory address

print(arr.shape)  #Dimension

print(arr.dtype) #DataType

print(arr.strides) 

ones = np.ones((3,4))
print(ones)

