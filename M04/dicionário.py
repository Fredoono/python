import numpy as np
#9 FALTAS 5 MODULO 4 / 4 MODULO 3

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Target found
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Target not found

# exemplo
arr = np.array([1, 3, 5, 7, 9])
target = 5
result = binary_search(arr, target)

print(f"Index of {target}: {result}")