# ========================================
#     File name: LinkedListQueue.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/15/2023
#     Date last modified: 12/03/2023
#     Python Version: 3.12.0
# ========================================

from LinkedList.SinglyLinkedList import SinglyLinkedList

class LinkedListQueue:
    def __init__(self):
        self.queue = SinglyLinkedList()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        dequeued = self.queue.popleft()
        return dequeued
    
    def seek(self):
        return self.queue.tail.value
    
    def __str__(self):
        return str(self.queue)

    def clear(self):
        self.queue.head = None

    def isEmpty(self):
        if self.queue.head == None:
            return True
        else:
            return False

customqueue = LinkedListQueue()
customqueue.enqueue(1)
customqueue.enqueue(2)
customqueue.enqueue(3)
customqueue.enqueue(4)

if __name__ == '__main__':
    #access
    print("\n---------------------")
    print("- Access Operations -")
    print("---------------------")
    print("Accessing value by seek: " +str(customqueue.seek()))


    #insert
    print("\n---------------------")
    print("- Insert Operations -")
    print("---------------------")
    customqueue.enqueue(5)
    print("Enqueueing a number: ", customqueue.queue.traverse())

    #delete
    print("\n---------------------")
    print("- Delete Operations -")
    print("---------------------")
    dequeued = customqueue.dequeue() #index can be given optionally else it fetches the last element
    print("Deleting by dequeue method: ", customqueue.queue.traverse())
    print("dequeueed number from list:", dequeued)
    customqueue.clear()
    print("clearing entire queue : ", customqueue.queue.traverse())
    print(customqueue.isEmpty())

#  -- Result --


# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by seek: 4

# ---------------------
# - Insert Operations -
# ---------------------
# enqueueing a number:  [1, 2, 3, 4, 5]

# ---------------------
# - Delete Operations -
# ---------------------
# Deleting by dequeue method:  [1, 2, 3, 4]
# dequeueed number from list: 5
# clearing entire queue :  []
