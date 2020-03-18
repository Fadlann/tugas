class customer:
    name = None
    drink = None

    def __init__(self, name, drink):
        self.name = name
        self.drink = drink

class queue:
    customer = []

    def isEmpty(self):
        return len(self.customer) == 0
    
    def enqueue(self, name, drink):
        self.customer.append(customer(name, drink))
    
    def dequeue(self):
        if len(self.customer) > 0:
            self.customer.remove(self.customer[0])

    def printQueue(self):
        print('')
        if self.isEmpty():
            print("Queue is empty")
        else:
            print("==== Orders left ====")
            for i in range(0, len(self.customer)):
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
    elif choice == 'a':
        name = input("Name: ")
        drink = input("Drink: ")
        queue.enqueue(name, drink)
    queue.printQueue()
