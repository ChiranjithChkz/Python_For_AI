import numpy as np

#Filtering = refers to the process of selecting elements
#             from an array that match a given condition

ages = np.array([[21, 17, 18, 19, 55, 98, 65],
                 [39, 22, 15, 99, 18, 19, 20]])

# teenagers = ages[ages < 19]
# adults = ages[(ages >= 18) & (ages < 65)]
# seniors = ages[ages >= 65]
# evens = ages[ages % 2 == 0]
# odds = ages[ages % 2 != 0]

# print(odds)

#to show full matrix

adults = np.where(ages >= 18, ages, -1)
 

print(adults)

