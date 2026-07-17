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

arr = np.array([1,2,3,4,5])
print(f"Arrays={arr}\n")
print(f"SUM={np.sum(arr)}\n")
print(f"MIN={np.min(arr)}\n")
print(f"MAX={np.max(arr)}\n")
print(f"PRODUCT={np.prod(arr)}\n")
print(f"STANDERD DEVIATION={np.std(arr)}\n")
print(f"VARIANCE={np.var(arr)}\n")
print(f"MEAN={np.mean(arr)}\n")
print(f"ZEROS={np.zeros((2,3))}\n")
print(f"FULL={np.full(2,5),10}\n")
print(f"ONCE={np.ones((2,3))}\n")
print(f"ARANGE={np.arange(1,10,2)}\n")
print(f"3D Array={arr3}\n")
print(f"LINESPACE={np.linspace(1,10,5)}\n")



