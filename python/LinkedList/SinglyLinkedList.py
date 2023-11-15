# ========================================
#     File name: SinglyLinkedList.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/05/2023
#     Date last modified: 11/07/2023
#     Python Version: 3.12.0
# ========================================

class Node:
    def __init__(self,value, nxt):
        self.value = value
        self.nxt = nxt

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):
        node = self.head
        lst = []
        while node:
            lst.append(node.value)
            node = node.nxt
        return lst
    
    def __len__(self):
        node = self.head
        count = 0
        while node:
            count+=1
            node = node.nxt
        return count
    
#Access
#TODO: accessing the linked list by normal slicing operations (space complexity optimization)
    def __getitem__(self, subscript):
        lst = []
        node = self.head
        while node:
            lst.append(node.value)
            node = node.nxt
        return lst[subscript]


#Insertion
    def append(self, value):
        tempNode = Node(value, None)
        if self.head is None:
            self.head = tempNode
            self.tail = tempNode
            return
        self.tail.nxt = tempNode
        self.tail = tempNode

    def insert(self, idx, value):
        tempNode = Node(value, None)
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
        if node.value == slicedvalue:
            self.head = node.nxt
            return
        while node:
            if node.nxt:
                if node.nxt.value == slicedvalue:
                    node.nxt = node.nxt.nxt if node.nxt.nxt else None
                    return 
            node = node.nxt
            

    def pop(self):
        node = self.head
        popped = None
        for _ in range(0,len(self)-2):
            node = node.nxt
        self.tail = node
        try:
            popped = node.nxt.value
        except(AttributeError):
            print('pop from empty list')
            return 
        node.nxt = None
        return popped
    
    def popleft(self):
        node = self.head
        popped = self.head.value if self.head.value else None
        self.head = node.nxt
        return popped


            

num_list = SinglyLinkedList()
num_list.extend([1,2,3,4])

# uncomment to review result and comment out. This code is used in another module
# #access
# print(num_list)
# print(num_list.traverse())
# print("\n---------------------")
# print("- Access Operations -")
# print("---------------------")
# print("Accessing value by index: " +str(num_list[1]))
# print("Accessing list by index:  " +str(num_list[0:3]))   #slicing (upper limit index is exclusive)


# #insert
# print("\n---------------------")
# print("- Insert Operations -")
# print("---------------------")
# num_list.append(5)
# print("Appending a number: " , num_list.traverse())

# num_list.append([6,7]) # adds the list as a nested list
# print("Appending a list:   " , num_list.traverse())

# num_list.extend([8,9]) # adds the elements of the list
# print("Extending a list:   " , num_list.traverse())

# num_list.insert(4, 10) # moves the value/list of the given index to next and insert
# print("Inserting a number: " , num_list.traverse())


# #search
# print("\n---------------------")
# print("- Search Operations -")
# print("---------------------")
# print("Reference of the list:    ", num_list.traverse())
# print("Searching by index method: " +str(num_list.index(2))) #find the first occuring index of given value, returns -1 if not exists
# print("In operator (3 in list):  ", 3 in num_list)

# #delete
# print("\n---------------------")
# print("- Delete Operations -")
# print("---------------------")
# print("Reference of the list:    ", num_list.traverse())
# num_list.remove(10) #removes the first occurence of the value given
# print("Deleting by remove method:" , num_list.traverse())
# popped = num_list.pop() #index can be given optionally else it fetches the last element
# print("Deleting by pop method:   " ,num_list.traverse())
# print("Popped number from list:  ", popped)


# # -- Result --

# #<__main__.SinglyLinkedList object at 0x0000020503D6E240>
# #[1, 2, 3, 4]

# # ---------------------
# # - Access Operations -
# # ---------------------
# # Accessing value by index: 2
# # Accessing list by index:  [1, 2, 3]

# # ---------------------
# # - Insert Operations -
# # ---------------------
# # Appending a number:  [1, 2, 3, 4, 5]
# # Appending a list:    [1, 2, 3, 4, 5, [6, 7]]
# # Extending a list:    [1, 2, 3, 4, 5, [6, 7], 8, 9]
# # Inserting a number:  [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]

# # ---------------------
# # - Search Operations -
# # ---------------------
# # Reference of the list:     [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]
# # Searching by index method: 1
# # In operator (3 in list):   True

# # ---------------------
# # - Delete Operations -
# # ---------------------
# # Reference of the list:     [1, 2, 3, 4, 10, 5, [6, 7], 8, 9]
# # Deleting by remove method: [1, 2, 3, 4, 5, [6, 7], 8, 9]
# # Deleting by pop method:    [1, 2, 3, 4, 5, [6, 7], 8]
# # Popped number from list:   9