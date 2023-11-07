tple = (1,2,3,4,5)

#access
print(tple)
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by index: " +str(tple[1]))
print("Accessing list by index:  " +str(tple[0:3]))   #slicing (upper limit index is exclusive)
print("Length of tuple:          " +str(len(tple)))

#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the list:    ", tple)
print("Searching by index method: " +str(tple.index(2))) #find the first occuring index of given value, returns -1 if not exists
print("In operator (3 in list):  ", 3 in tple)

#Insertion, deletion cannot be done on tuples

# -- Result --

# (1, 2, 3, 4, 5)

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by index: 2
# Accessing list by index:  (1, 2, 3)
# Length of tuple:          5

# ---------------------
# - Search Operations -
# ---------------------
# Reference of the list:     (1, 2, 3, 4, 5)
# Searching by index method: 1
# In operator (3 in list):   True