class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.lowest = 999
        self.highest = -999
        self.head = None
    
    # public function to insert element
    def insert(self,number):
        newNode = Node(number)
        if self.head == None:
            self.head = Node(number)
        elif number > self.head.value:
            newNode.next = self.head
            self.head = newNode
        else:
            self._insert(newNode, self.head)
    
    # private recursive function to insert element
    def _insert(self, newNode, node):
        if node.next == None:
            node.next = newNode
        elif newNode.value > node.next.value:
            newNode.next = node.next
            node.next = newNode
        else:
            self._insert(newNode, node.next)
    
    def deleteLast(self):
        if self.head == None:
            return
        if self.head.next == None:
            head = None
            return
        cur = self.head
        while cur.next.next != None:
            cur = cur.next
        cur.next = None

    # public function to printList
    def printList(self):
        if self.head == None:
            print("List is empty")
            return
        else:
            print("List : ")
            self._printList(self.head)

    # private recursive function to printList
    def _printList(self,node):
        print(node.value)
        if node.next != None:
            self._printList(node.next)

l = LinkedList()

for i in range(10):
    l.insert(int(input("Masukkan data: ")))

l.printList()

l.insert(int(input("input data baru: ")))
l.deleteLast()

l.printList()
