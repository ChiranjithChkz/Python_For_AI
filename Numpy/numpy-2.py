#multidimensional array
import numpy as np

# array = np.array([['A', 'B', 'C'],
#                   ['D', 'E', 'F'] ,
#                   ['G', 'H', 'I']])


# print(array.ndim)  #to print dimension


array = np.array([[['A', 'B', 'C'],['D', 'E', 'F'] ,['G', 'H', 'I']],
                  [['J', 'K', 'L'],['M', 'N', 'O'] ,['P', 'Q', 'R']],
                  [['S', 'T', 'U'],['V', 'W', 'X'] ,['Y', 'Z',' ']]])


print(array.ndim)  #to print dimension
print(array.shape)  #to print SHAPE
print(array[0][0][0])

word = array[0,0,0] + array[1,2,0]+ array[1,2,0]+array[1,0,2]+ array[0,1,1]
print(word)