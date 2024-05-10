import numpy as np
MAX = 1000
MILvalores = np.empty(MAX,dtype="i") #MILvalores = tbm existe o np.zeros()
for i in range (MAX):
    MILvalores[i] = i + 1

print (MILvalores)

#inverso
"""
MAX = 1000
MILvalores = np.empty(MAX,dtype="i") 
for i in range (MAX-1,-1,-1):
    print (MILvalores[i])
"""