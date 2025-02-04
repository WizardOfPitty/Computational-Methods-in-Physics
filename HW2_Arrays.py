import numpy as np


# Make the array
M = np.array([[1, 2, 3, 4, 5],[6, 8, 10, 12, 14]], int)
print(M[0, 0:3])
print(M[0, 2:4])
print(M[0:2, 0])
print(M[0:4, 1:4])
# Print the separate rows of M to display 
# a varying number of columns
print(M[0, 1:4], M[1, 0:2])
print(M[0,4], M[1, :])
print(M[0,4], M[1, 0:2])
# Print all rows of the second column 
print(M[1,:])
#Select odd elements and set to 0
M[0,[0,2,4]] = 0

print(M)