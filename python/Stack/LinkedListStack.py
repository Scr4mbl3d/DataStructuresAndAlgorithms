# ========================================
#     File name: NativeList.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/12/2023
#     Date last modified: 11/12/2023
#     Python Version: 3.12.0
# ========================================

from LinkedList.SinglyLinkedList import SinglyLinkedList

class LinkedListStack:
    def __init__(self):
        self.stack = SinglyLinkedList()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        popped = self.stack.popleft()
        return popped
    
    def seek(self):
        return self.stack.head.value
    
    def __str__(self):
        return str(self.stack)

    def clear(self):
        self.stack = SinglyLinkedList()

customStack = LinkedListStack()
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
print("Pushing a number: ", customStack.stack.traverse())

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
popped = customStack.pop() #index can be given optionally else it fetches the last element
print("Deleting by pop method: ", customStack.stack.traverse())
print("Popped number from list:", popped)
customStack.clear()
print("clearing entire stack : ", customStack.stack.traverse())

#  -- Result --


# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by seek: 1

# ---------------------
# - Insert Operations -
# ---------------------
# Pushing a number:  [1, 2, 3, 4, 5]

# ---------------------
# - Delete Operations -
# ---------------------
# Deleting by pop method:  [2, 3, 4, 5]
# Popped number from list: 1