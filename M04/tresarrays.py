import numpy as np
"""juntar o contiudo de dois array num terceiro array"""
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3 = np.empty(8,"i")

#colocar os primeiros 4 elementos no array 3 

for i in range (len(arr1)):
    arr3[i] = arr1[i]
    arr3[i+4] = arr2[i]
print (arr3)

def juntararray():
    pass