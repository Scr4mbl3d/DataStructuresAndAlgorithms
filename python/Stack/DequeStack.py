# ========================================
#     File name: DequeStck.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/12/2023
#     Date last modified: 12/03/2023
#     Python Version: 3.12.0
# ========================================

from collections import deque 

# Declaring deque 
customStack = deque([1,2,3,4])


#access
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by seek: " +str(customStack[-1]))


#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
customStack.append(5)
print("Pushing a number: ", customStack)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
popped = customStack.pop() #index can be given optionally else it fetches the last element
print("Deleting by pop method: ", customStack)
print("Popped number from list:", popped)
customStack.clear()
print("clearing entire stack : ", customStack)


# -- Result --

# [1, 2, 3, 4]

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by seek: 4

# ---------------------
# - Insert Operations -
# ---------------------
# Pushing a number:  deque([1, 2, 3, 4, 5])

# ---------------------
# - Delete Operations -
# ---------------------
# Deleting by pop method:  deque([1, 2, 3, 4])
# Popped number from list: 5
# clearing entire stack :  deque([])