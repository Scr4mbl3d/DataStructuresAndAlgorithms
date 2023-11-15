# ========================================
#     File name: ListStack.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/12/2023
#     Date last modified: 11/12/2023
#     Python Version: 3.12.0
# ========================================

class ListStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        popped = self.stack.pop()
        return popped
    
    def seek(self):
        return self.stack[-1]
    
    def __str__(self):
        return str(self.stack)

    def clear(self):
        self.stack = []

customStack = ListStack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

#access
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by seek: " +str(customStack.seek()))


#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
customStack.push(5)
print("Pushing a number: ", customStack)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
popped = customStack.pop() #index can be given optionally else it fetches the last element
print("Deleting by pop method: ", customStack)
print("Popped number from list:", popped)
customStack.clear()
print("clearing entire stack  :", customStack)

# -- Result --

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by seek: 4

# ---------------------
# - Insert Operations -
# ---------------------
# Pushing a number:  [1, 2, 3, 4, 5]

# ---------------------
# - Delete Operations -
# ---------------------
# Deleting by pop method:  [1, 2, 3, 4]
# Popped number from list: 5
# clearing entire stack  : []