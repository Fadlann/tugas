class Simpul:

    def __init__(self):
        self.container = None
        self.left = None
        self.right = None

    def setContainer(self, container):
        self.container = container
    
    def getContainer(self):
        return self.container

    def setRight(self, right):
        self.right = right
        return right
    
    def getRight(self):
        return self.right

    def setLeft(self, left):
        self.left = left
        return left
    
    def getLeft(self):
        return self.left

class Tree:
    
    def __init__(self):
        self.root = Simpul()

    def setRoot(self, root):
        self.root = root

    def getRoot(self):
        return self.root

    def makeTree(self, c):
        baru = Simpul()

        baru.setContainer(c)
        baru.setRight(None)
        baru.setLeft(None)
        self.root = baru
    
    def addRight(self, c, root):
        if root.getRight() == None:
            baru = Simpul()

            baru.setContainer(c)
            root.setRight(baru)
        else:
            print("Sub pohon kanan telah terisi")

    def addLeft(self, c, root):
        if root.getLeft() == None:
            baru = Simpul()

            baru.setContainer(c)
            root.setLeft(baru)
        else:
            print("Sub pohon kanan telah terisi")

    def delAll(self, root):
        if root:
            self.delAll(root.getLeft())
            self.delAll(root.getRight())
            root = None

    def delRight(self, root):
        if root:
            if root.getRight():
                self.delAll(root.getRight())
                root.setRight(None)

    def delLeft(self, root):
        if root:
            if root.getLeft():
                self.delAll(root.getLeft())
                root.setLeft(None)

    def printTreePreOrder(self, root):
        if root:
            print(root.getContainer(),end="")
            self.printTreePreOrder(root.getLeft())
            self.printTreePreOrder(root.getRight())

    def printTreeInOrder(self, root):
        if root:
            self.printTreeInOrder(root.getLeft())
            print(root.getContainer(),end="")
            self.printTreeInOrder(root.getRight())

    def printTreePostOrder(self, root):
        if root:
            self.printTreePostOrder(root.getLeft())
            self.printTreePostOrder(root.getRight())
            print(root.getContainer(),end="")

T = Tree()
T.makeTree('A')
T.addLeft('B',T.getRoot())
T.addRight('C',T.getRoot())
T.addLeft('D',T.getRoot().getLeft())
T.addRight('E',T.getRoot().getLeft())
T.addLeft('F',T.getRoot().getRight())
T.addRight('G',T.getRoot().getRight())

print("Preorder: ")
T.printTreePreOrder(T.getRoot())
print("\n")

print("Inorder: ")
T.printTreeInOrder(T.getRoot())
print("\n")

print("Postorder: ")
T.printTreePostOrder(T.getRoot())
print("\n")

print("Preorder setelah node kiri dari root dihapus: ")
T.delLeft(T.getRoot())
T.printTreePreOrder(T.getRoot())
print("\n")

print("Preorder setelah node kanan dari root dihapus: ")
T.delRight(T.getRoot())
T.printTreePreOrder(T.getRoot())