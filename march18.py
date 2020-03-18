class customer:
    name = None
    drink = None

    def __init__(self, name, drink):
        self.name = name
        self.drink = drink

class queue:
    last = -1
    customer = []

    def isEmpty(self):
        return self.last == -1
    
    def enqueue(self, name, drink):
        self.last += 1
        self.customer.append(customer(name, drink))
    
    def dequeue(self):
        for i in range(self.last):
            self.customer[i] = self.customer[i+1]
        self.last -= 1

    def printQueue(self):
        print('')
        if self.last == -1:
            print("Queue is empty")
            print('')
            return
        print("==== Orders left ====")
        for i in range(0, self.last + 1):
            print("--")
            print("Order Number",i+1)
            print("Name :",self.customer[i].name)
            print("Drink :",self.customer[i].drink)
        print('')

queue = queue()

choice = ""
while(choice != 'q'):
    choice = input("Add customer? <a> Order's served? <k> Quit? <q> ")
    if choice == 'k':
        queue.dequeue()
        queue.printQueue()
    elif choice == 'a':
        name = input("Name: ")
        drink = input("Drink: ")
        queue.enqueue(name, drink)
        queue.printQueue()



        
