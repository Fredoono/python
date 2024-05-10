import numpy as np
import random 
arr  = np.empty((3,3),"i")
for i in range (arr.shape[0]):
    for f in range (arr.shape[1]):
        arr[i,f] = random.randint(0,100)
print (arr)