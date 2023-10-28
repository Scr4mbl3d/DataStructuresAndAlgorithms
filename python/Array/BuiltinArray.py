# ========================================
#     File name: BuiltinArray.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 10/28/2023
#     Date last modified: 10/28/2023
#     Python Version: 3.12.0
# ========================================

# typecodes:
# +-----------+--------------------+-------------------+-----------------------+-------+
# | Type code | C Type             | Python Type       | Minimum size in bytes | Notes |
# +===========+====================+===================+=======================+=======+
# | ``'b'``   | signed char        | int               | 1                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'B'``   | unsigned char      | int               | 1                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'u'``   | wchar_t            | Unicode character | 2                     | \(1)  |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'w'``   | Py_UCS4            | Unicode character | 4                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'h'``   | signed short       | int               | 2                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'H'``   | unsigned short     | int               | 2                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'i'``   | signed int         | int               | 2                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'I'``   | unsigned int       | int               | 2                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'l'``   | signed long        | int               | 4                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'L'``   | unsigned long      | int               | 4                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'q'``   | signed long long   | int               | 8                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'Q'``   | unsigned long long | int               | 8                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'f'``   | float              | float             | 4                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+
# | ``'d'``   | double             | float             | 8                     |       |
# +-----------+--------------------+-------------------+-----------------------+-------+

import array

arr = array.array('i', [1,2,3])

#traversal of the array

def traversal(arr):
    for i in range(0,len(arr)):
        print(arr[i], end = ' ')
    print()

traversal(arr)
print(arr)



#methods

#access
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by index:", arr[0], "(returns typecode type)")
print("Accessing list by index: ", arr[0:2], "(returns array object)")

#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
arr.append(4)
print("Appending a number:", arr)
arr.extend([5,6,7])
#arr.append([6,7]) -> TypeError: 'list' object cannot be interpreted as an integer
print("Extending a list:  ", arr)
arr.insert(4,10)
print("Inserting a number:", arr)
arr[2] = 30
print("Replacing a number:", arr)

#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the list:    ", arr)
print("Searching by index method:", arr.index(4)) 
#find the first occuring index of given value, returns -1 if not exists
print("In operator (30 in list): ", 30 in arr)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
print("Reference of the list:    ", arr)
del(arr[6]) #removes the value in the index
print("Deleting by index:        ", arr)
arr.remove(10)
#removes the first occurence of the value given
print("Deleting by remove method:" , arr)
popped = arr.pop()
#index can be given optionally else it fetches the last element
print("Deleting by pop method:   ", arr)
print("Popped number from list:  ", popped)

#other methods
print("\n---------------------")
print("-   Other Methods   -")
print("---------------------")
print("Reference of the list:", arr)
print("Buffer info:          ", arr.buffer_info(),"-> (object address, length)")
print("Counting given value: ", arr.count(30))
arr.reverse()
print("Reversing the array:  ",arr)
print("converting to list:   ", arr.tolist())

#attributes
print("\n---------------------")
print("-    Attributes     -")
print("---------------------")
print("Supported Datatypes:", array.typecodes)
print("Object typecode:    ",arr.typecode)
print("Object size:        ",arr.itemsize,"(not array size)")

# -- Result --

# 1 2 3 
# array('i', [1, 2, 3])

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by index: 1 (returns typecode type)
# Accessing list by index:  array('i', [1, 2]) (returns array object)

# ---------------------
# - Insert Operations -
# ---------------------
# Appending a number: array('i', [1, 2, 3, 4])
# Extending a list:   array('i', [1, 2, 3, 4, 5, 6, 7])
# Inserting a number: array('i', [1, 2, 3, 4, 10, 5, 6, 7])
# Replacing a number: array('i', [1, 2, 30, 4, 10, 5, 6, 7])

# ---------------------
# - Search Operations -
# ---------------------
# Reference of the list:     array('i', [1, 2, 30, 4, 10, 5, 6, 7])
# Searching by index method: 3
# In operator (30 in list):  True

# ---------------------
# - Delete Operations -
# ---------------------
# Reference of the list:     array('i', [1, 2, 30, 4, 10, 5, 6, 7])
# Deleting by index:         array('i', [1, 2, 30, 4, 10, 5, 7])
# Deleting by remove method: array('i', [1, 2, 30, 4, 5, 7])
# Deleting by pop method:    array('i', [1, 2, 30, 4, 5])
# Popped number from list:   7

# ---------------------
# -   Other Methods   -
# ---------------------
# Reference of the list: array('i', [1, 2, 30, 4, 5])
# Buffer info:           (1841788432672, 5) -> (object address, length)
# Counting given value:  1
# Reversing the array:   array('i', [5, 4, 30, 2, 1])
# converting to list:    [5, 4, 30, 2, 1]

# ---------------------
# -    Attributes     -
# ---------------------
# Supported Datatypes: bBuhHiIlLqQfd
# Object typecode:     i
# Object size:         4 (not array size)