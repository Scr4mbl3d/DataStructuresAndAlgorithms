# ========================================
#     File name: LinkedListStack.py
#     Author: Aadhawan Maadheshwaran
#     Date created: 11/12/2023
#     Date last modified: 11/12/2023
#     Python Version: 3.12.0
# ========================================

from Queue.LInkedListQueue import LinkedListQueue

class Node:
    def __init__(self, val):
        self.val = val
        self.leftChild = None
        self.rightChild = None



def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    print(rootNode.val)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.val)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.val)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    customQueue = LinkedListQueue()
    customQueue.enqueue(rootNode)
    while not customQueue.isEmpty():
        root = customQueue.dequeue()
        print(root.val)
        if root.leftChild is not None:
            customQueue.enqueue(root.leftChild)
        if root.rightChild is not None:
            customQueue.enqueue(root.rightChild)

def insert(rootNode, value):
    node = Node(value)
    if not rootNode:
        return
    customQueue = []
    customQueue.append(rootNode)
    while customQueue:
        root = customQueue.pop(0)
        if root.leftChild:
            customQueue.append(root.leftChild)
        else:
            root.leftChild = node
            return
        if root.rightChild:
            customQueue.append(root.rightChild)
        else:
            root.rightChild = node
            return

def getDeepestNode(rootNode):
    if not rootNode:
        return 'BT does not exist'
    else:
        customqueue = LinkedListQueue()
        customqueue.enqueue(rootNode)
        while not(customqueue.isEmpty()):
            root = customqueue.dequeue()
            if root.leftChild is not None:
                customqueue.enqueue(root.leftChild)
            if root.rightChild is not None:
                customqueue.enqueue(root.rightChild)
        deepestNode = root.val
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        customQueue = LinkedListQueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.val is dNode:
                root.val = None
                return
            if root.rightChild:
                if root.rightChild.val == dNode:
                    root.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.rightChild)
            if root.leftChild:
                if root.leftChild.val == dNode:
                    root.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.leftChild)

def deleteNode(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        customQueue = LinkedListQueue()
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.val == node:
                dNode = getDeepestNode(rootNode)
                deleteDeepestNode(rootNode, dNode)
                root.val = dNode
                return "The node has been successfully deleted"
            if (root.leftChild is not None):
                customQueue.enqueue(root.leftChild)
            
            if (root.rightChild is not None):
                customQueue.enqueue(root.rightChild)
        return "Failed to delete"

def deleteTree(rootNode):
    if not rootNode:
        return
    else:
        rootNode.val = None
        rootNode.leftChild = None
        rootNode.rightChild = None
    
new = Node('Drinks')

levelOrderTraversal(new)
deleteTree(new)
levelOrderTraversal(new)

