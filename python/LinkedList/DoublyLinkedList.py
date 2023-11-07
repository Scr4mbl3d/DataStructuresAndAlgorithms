class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        node = self.head
        count = 0
        while node:
            count+=1
            node = node.nxt
        return count
    
    def traverse(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.value)
            node = node.nxt
        return lst

    def reverseTraverse(self):
        node = self.tail
        lst = []
        while node:
            lst.append(node.value)
            node = node.prev
        return lst
#Access
#TODO: accessing the linked list by normal slicing operations
    def __getitem__(self, subscript):
        lst = []
        node = self.head
        while node:
            lst.append(node.value)
            node = node.nxt
        return lst[subscript]

#Insertion
    def append(self, value):
        tempNode = Node(value, None, None)
        if self.head is None:
            self.head = tempNode
            self.tail = tempNode
            return
        tempNode.prev = self.tail
        self.tail.nxt = tempNode
        self.tail = tempNode

    def insert(self, idx, value):
        tempNode = Node(value, None, None)
        node = self.head
        if idx == 0:
            tempNode.nxt = self.head
            self.head = tempNode
            return
        for i in range(1,idx):
            node = node.nxt
            try:
                node.nxt is None
            except AttributeError:
                print('index out of range')
                return
        tempNode.prev = node
        tempNode.nxt = node.nxt
        node.nxt = tempNode

    def extend(self,lst):
        if isinstance(lst, list):
            for item in lst:
                self.append(item)
        elif isinstance(lst, (str, int, float)):
            self.append(lst)
        
#Search
    def index(self, value):
        node = self.head
        idx = 0
        while node:
            if node.value == value:
                return idx
            node = node.nxt
            idx+=1
        return -1
    
    def __eq__(self,other):
        if isinstance(other, (str, int, float)):
            node = self.head
            while node:
                if node.value == other:
                    return True
                node = node.nxt
            return False

#remove
    def remove(self,slicedvalue):
        node = self.head
        while node:
            if node.value == slicedvalue:
                if node.nxt:
                    node.nxt.prev = node.prev
                else:
                    self.tail = node.prev
                    node.nxt = None
                if node.prev:
                    node.prev.nxt = node.nxt
                else:
                    self.head = node.nxt
                    node.nxt.prev = None
                break
            node = node.nxt
            

    def pop(self):
        node = self.tail
        try:
            node = self.tail
        except(AttributeError):
            print('pop from empty list')
            exit()
        else:
            popped = node.value
            node.prev.nxt = None
        return popped
        
class Node:
    def __init__(self,value, prev, nxt):
        self.value = value
        self.nxt = nxt
        self.prev = prev
    
num_list = DoublyLinkedList()
num_list.extend([1,2,3,4])


#access
print(num_list)
print(num_list.traverse())
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
print("Appending a number: " , num_list.traverse())

num_list.append([6,7]) # adds the list as a nested list
print("Appending a list:   " , num_list.traverse())

num_list.extend([8,9]) # adds the elements of the list
print("Extending a list:   " , num_list.traverse())

num_list.insert(4, 10) # moves the value/list of the given index to next and insert
print("Inserting a number: " , num_list.traverse())


#search
print("\n---------------------")
print("- Search Operations -")
print("---------------------")
print("Reference of the list:    ", num_list.traverse())
print("Searching by index method: " +str(num_list.index(2))) #find the first occuring index of given value, returns -1 if not exists
print("In operator (3 in list):  ", 3 in num_list)

#delete
print("\n---------------------")
print("- Delete Operations -")
print("---------------------")
print("Reference of the list:    ", num_list.traverse())
num_list.remove(10) #removes the first occurence of the value given
print("Deleting by remove method:" , num_list.traverse())
popped = num_list.pop() #index can be given optionally else it fetches the last element
print("Deleting by pop method:   " ,num_list.traverse())
print("Popped number from list:  ", popped)

# -- Result --

# <__main__.DoublyLinkedList object at 0x000002B8D89CE750>
# [1, 2, 3, 4]

# ---------------------
# - Access Operations -
# ---------------------
# Accessing value by index: 2
# Accessing list by index:  [1, 2, 3]

# ---------------------
# - Insert Operations -
# ---------------------
# Appending a number:  [1, 2, 3, 4, 5]
# Appending a list:    [1, 2, 3, 4, 5, [6, 7]]
# Extending a list:    [1, 2, 3, 4, 5, [6, 7], 8, 9]
# Inserting a number:  [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]

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
# Deleting by remove method: [1, 2, 3, 4, 5, [6, 7], 8, 9]
# Deleting by pop method:    [1, 2, 3, 4, 5, [6, 7], 8]
# Popped number from list:   9