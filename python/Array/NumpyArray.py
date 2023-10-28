# ========================================
#     File name: NumpyArray.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 10/28/2023
#     Date last modified: 10/29/2023
#     Python Version: 3.12.0
# ========================================

import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr))
print("Shape of the array :",arr.shape)
print("Data type of array :",arr.dtype)

'''
Axis 0 = one dimensional
Axis 1 = Two dimensional
Axis 2 = Three dimensional 
'''

#access
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by index:", arr[0])
print("Accessing list by index: ", arr[0:2])

#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
arr = np.append(arr, 6)
print("Appending a number:", arr)
arr = np.append(arr, [7,8,9])
#arr.append([6,7]) -> TypeError: 'list' object cannot be interpreted as an integer
print("Extending a list:  ", arr)
arr = np.insert(arr,4,1)
print("Inserting a number:", arr)
arr[2] = 9
print("Replacing a number:", arr)

#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the list:    ", arr)
print("Searching by where method:", np.where(arr == 1)[0])
print("Counting occurences:      ", len(np.where(arr == 1)[0]))
#find the first occuring index of given value, returns -1 i  f not exists
print("In operator (30 in list): ", 1 in arr)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
print("Reference of the list:    ", arr)
arr = np.delete(arr,2)
#removes the first occurence of the value given
print("Deleting by remove method:" , arr)
arr,popped = arr[:-1], arr[-1]
#index can be given optionally else it fetches the last element
print("Deleting by pop method:   ", arr)
print("Popped number from list:  ", popped)

# -- Result --

# [1 2 3 4 5]
# <class 'numpy.ndarray'>
# Shape of the array : (5,)
# Data type of array : int32

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by index: 1
# Accessing list by index:  [1 2]

# ---------------------
# - Insert Operations -
# ---------------------
# Appending a number: [1 2 3 4 5 6]
# Extending a list:   [1 2 3 4 5 6 7 8 9]
# Inserting a number: [1 2 3 4 1 5 6 7 8 9]
# Replacing a number: [1 2 9 4 1 5 6 7 8 9]

# ---------------------
# - Search Operations -
# ---------------------
# Reference of the list:     [1 2 9 4 1 5 6 7 8 9]
# Searching by where method: [0 4]
# Counting occurences:       2
# In operator (30 in list):  True

# ---------------------
# - Delete Operations -
# ---------------------
# Reference of the list:     [1 2 9 4 1 5 6 7 8 9]
# Deleting by remove method: [1 2 4 1 5 6 7 8 9]
# Deleting by pop method:    [1 2 4 1 5 6 7 8]
# Popped number from list:   9