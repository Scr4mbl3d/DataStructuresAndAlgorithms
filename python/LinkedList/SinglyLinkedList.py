class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def traverse(self):
        node = self.head
        while node:
            print(node.value, end = ' -> ')
            node = node.nxt
        print('\b \b')
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

    def listToLinkedList(self,list):
        for item in list:
            self.append(item)
        

        
class Node:
    def __init__(self,value, nxt):
        self.value = value
        self.nxt = nxt

linkedList = SinglyLinkedList()
linkedList.listToLinkedList([1,2,3,4,5,6,7,8])
linkedList.traverse()
print(linkedList[::-1])

