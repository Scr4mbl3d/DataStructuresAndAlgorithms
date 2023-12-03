# ========================================
#     File name: ListQueue.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/15/2023
#     Date last modified: 11/15/2023
#     Python Version: 3.12.0
# ========================================
class ListQueue:
    def __init__(self):
        self.stack = []

    def enqueue(self, value):
        self.stack.append(value)

    def dequeue(self):
        dequeued = self.stack.pop(0)
        return dequeued
    
    def seek(self):
        return self.stack[0]
    
    def __str__(self):
        return str(self.stack)

    def clear(self):
        self.stack = []

customStack = ListQueue()
customStack.enqueue(1)
customStack.enqueue(2)
customStack.enqueue(3)
customStack.enqueue(4)

#access
print("\n---------------------")
print("- Access Operations -")
print("---------------------")
print("Accessing value by seek: " +str(customStack.seek()))


#insert
print("\n---------------------")
print("- Insert Operations -")
print("---------------------")
customStack.enqueue(5)
print("enqueueing a number: ", customStack)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
dequeueped = customStack.dequeue() #index can be given optionally else it fetches the last element
print("Deleting by dequeue method: ", customStack)
print("dequeued number from list:", dequeueped)
customStack.clear()
print("clearing entire stack  :", customStack)

# -- Result --


# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by seek: 1

# ---------------------
# - Insert Operations -
# ---------------------
# enqueueing a number:  [1, 2, 3, 4, 5]

# ---------------------
# - Delete Operations -
# ---------------------
# Deleting by dequeue method:  [2, 3, 4, 5]
# dequeued number from list: 1
# clearing entire stack  : []