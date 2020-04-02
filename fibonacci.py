class Queue:
    def __init__(self):
        self.last = -1
        self.data = []
    
    def isEmpty(self):
        return self.last == -1
    
    def enqueue(self,  numb): #enqueue: add an element to the queue.
        self.last += 1
        self.data.append(numb)
    
    def dequeue(self): #dequeue: remove an element from the queue.
        for i in range(self.last):
            self.data[i] = self.data[ i+1 ]
        self.last -= 1
            
    def print_queue(self):
        print('')
        if(self.last == -1):
            print('No data!')
            print('')
            return
        for i in range(0, self.last+1):
            print(self.data[i], end = ' ')
      
odd = Queue() #making object
even = Queue()

choose = int()
while(choose != 3):
    print()
    print(6*'-', 'MENU', 6*'-')
    print('[1] Add numbers\n[2] Delete Numbers\n[3] Exit')
    choose = int(input('Your choice : '))
    if(choose == 1):
        print(13*'=')
        print(' INPUT ANGKA ')
        print(13*'=')

        for i in range(10):
            number = int(input('Masukkan data : '))
            if(number%2 == 1):
                odd.enqueue(number)
            elif(number%2 == 0):
                even.enqueue(number)

        print(20*'=')
        print('\nIsi Queue Pertama : ')
        odd.print_queue()
        print()
        print('\nIsi Queue Kedua : ')
        even.print_queue()
        print()
    elif(choose == 2):
        print('---Delete Data---')
        odd.dequeue()
        even.dequeue()
        odd.print_queue()
        even.print_queue()