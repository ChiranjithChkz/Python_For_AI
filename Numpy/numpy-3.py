#slicing


import numpy as np

array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

#array[start:end:step]
#your also use negative index number 

# print(array[::-1]) #reverse row
#print(array[:, 0:3]) # first three column
# print(array[:, 0:3])
# print(array[:, 1:])

print(array[0:2, 0:2]) #access specific matrix
print(array[2:, 2:]) #last 2*2
