class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, size):
        self.size = size
        self.head = None
        self.count = 0
    
    # public function to insert element
    def insert(self,number):
        if(self.count == self.size):
            print("List is full")
        else:
            self.count += 1
            newNode = Node(number)
            if self.head == None:
                self.head = Node(number)
            elif number < self.head.value:
                newNode.next = self.head
                self.head = newNode
            else:
                self._insert(newNode, self.head)
    
    # private recursive function to insert element
    def _insert(self, newNode, node):
        if node.next == None:
            node.next = newNode
        elif newNode.value < node.next.value:
            newNode.next = node.next
            node.next = newNode
        else:
            self._insert(newNode, node.next)

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

newList = LinkedList(6)
newList.insert(16)
newList.insert(49)
newList.insert(32)
newList.insert(10)
newList.insert(99)
newList.insert(54)
newList.printList()
