class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):
        node = self.head
        while node:
            print(node.value, end = ' -> ')
            node = node.nxt
        print('\b \b')
    def reverseTraverse(self):
        node = self.tail
        while node:
            print(node.value, end = ' -> ')
            node = node.prev
        print()
#Access
#TODO: accessing the linked list by normal slicing operations
    def __getitem__(self, subscript):
        lst = []
        if isinstance(subscript, slice):
            # do your handling for a slice object:
            for i in range(subscript.start, subscript.stop):
                pass
        else:
            # Do your handling for a plain index
            print(subscript)

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

    def listToLinkedList(self,list):
        for item in list:
            self.append(item)
        

        
class Node:
    def __init__(self,value, prev, nxt):
        self.value = value
        self.nxt = nxt
        self.prev = prev
    
linkedList = DoublyLinkedList()
linkedList.listToLinkedList([1,2,3,4])
linkedList.traverse()
linkedList.reverseTraverse()