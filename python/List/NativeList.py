# ========================================
#     File name: NativeList.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 10/27/2023
#     Date last modified: 10/28/2023
#     Python Version: 3.12.0
# ========================================

num_list = [1,2,3,4]

#access
print(num_list)
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by index: " +str(num_list[1]))
print("Accessing list by index:  " +str(num_list[0:3]))   #slicing (upper limit index is exclusive)


#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
num_list.append(5)
print("Appending a number: " + str(num_list))

num_list.append([6,7]) # adds the list as a nested list
print("Appending a list:   " + str(num_list))

num_list.extend([8,9]) # adds the elements of the list
print("Extending a list:   " + str(num_list))

num_list.insert(4, 10) # moves the value/list of the given index to next and insert
print("Inserting a number: " + str(num_list))

num_list[4] = 10
print("Replacing a number: " + str(num_list))

#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the list:    ", num_list)
print("Searching by index method: " +str(num_list.index(2))) #find the first occuring index of given value, returns -1 if not exists
print("In operator (3 in list):  ", 3 in num_list)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
print("Reference of the list:    ", num_list)
del(num_list[6]) #removes the value in the index
print("Deleting by index:        ", str(num_list))
num_list.remove(10) #removes the first occurence of the value given
print("Deleting by remove method: " +str(num_list))
popped = num_list.pop() #index can be given optionally else it fetches the last element
print("Deleting by pop method:    " +str(num_list))
print("Popped number from list:  ", str(popped))

# -- Result --

# [1, 2, 3, 4]

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by index: 2
# Accessing list by index:  [1, 2, 3]

# ---------------------
# - Insert Operations -
# ---------------------
# Appending a number: [1, 2, 3, 4, 5]
# Appending a list:   [1, 2, 3, 4, 5, [6, 7]]
# Extending a list:   [1, 2, 3, 4, 5, [6, 7], 8, 9]
# Inserting a number: [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]
# Replacing a number: [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]

# ---------------------
# - Search Operations -
# ---------------------
# Reference of the list:     [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]
# Searching by index method: 1 
# In operator (3 in list):   True

# ---------------------
# - Delete Operations -
# ---------------------
# Reference of the list:     [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]
# Deleting by index:         [1, 2, 3, 4, 10, 5, 8, 9]
# Deleting by remove method: [1, 2, 3, 4, 5, 8, 9]
# Deleting by pop method:    [1, 2, 3, 4, 5, 8]
# Popped number from list:   9