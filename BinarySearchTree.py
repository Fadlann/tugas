class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def find(self, id):
        current = self.root
        while current != None:
            if current.data == id:
                return True
            elif current.data > id:
                current = current.left
            else:
                current = current.right
        return False  

    def delete(self, id):
        parent = self.root
        current = self.root
        isLeftChild = False

        while current.data != id:
            parent = current
            if current.data > id:
                isLeftChild = True
                current = current.left
            else:
                isLeftChild = False
                current = current.right
            if current == None:
                return False

        if current.left == None and current.right == None:
            if current == self.root:
                self.root = None
            if isLeftChild:
                parent.left = None
            else:
                parent.right = None
        elif current.right == None:
            if current == self.root:
                self.root = current.left
            elif isLeftChild:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left == None:
            if current == self.root:
                self.root = current.right
            elif isLeftChild:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.left and current.right:
            successor = self.getSuccessor(current)
            if current == self.root:
                self.root = successor
            elif isLeftChild:
                parent.left = successor
            else:
                parent.right = successor
            successor.left = current.left
        return True
    
    def getSuccessor(self, deleteNode):
        successor = None
        successorParent = None
        current = deleteNode.right
        while current != None:
            successorParent = successor
            successor = current
            current = current.left
        
        if successor != deleteNode.right:
            successorParent.left = successor.right
            successor.right = deleteNode.right
        
        return successor
    
    def insert(self, id):
        newNode = Node(id)
        if self.root == None:
            self.root = newNode
            return
        current =   self.root
        parent = None
        while True:
            parent = current
            if id < current.data:
                current = current.left
                if current == None:
                    parent.left = newNode
                    return
            else:
                current = current.right
                if current == None:
                    parent.right = newNode
                    return
    
    def display(self, root):
        if root != None:
            self.display(root.left)
            print(root.data, end = " ")
            self.display(root.right)

b = BinarySearchTree()
b.insert(3)
b.insert(8)
b.insert(1)
b.insert(4)
b.insert(6)
b.insert(2)
b.insert(10)
b.insert(9)
b.insert(20)
b.insert(25)
b.insert(15)
b.insert(16)

print(b.root.right.data)
print("Original tree: ")
b.display(b.root)
print(" ")
print("\nCheck whether node with value 4 exists: ", b.find(4))
print("\nDelete node with no children(2): ", b.delete(2))
b.display(b.root)
print("\n\nDelete node with one child(4): ",b.delete(4))
b.display(b.root)
print("\n\nDelete node with two children(10): ",b.delete(10))
b.display(b.root)