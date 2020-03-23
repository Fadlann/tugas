import queue

def getPivots(a): 
    result = [] 
    arrQueue = queue.Queue() 
    arrQueue.put(a)
    while arrQueue.qsize() > 0:
        a = arrQueue.get() 
        n = len(a) 
        if (n >= 1):
            pivot = n//2 
            result.append(a[pivot]) 

            l = a[0:pivot] 
            r = a[pivot + 1:] 

            arrQueue.put(l)   
            arrQueue.put(r)
    return result   


def getArrayInput():
    banyakBilangan = int(input("Masukkan jumlah bilangan : "))

    a = []

    for i in range(banyakBilangan):
        a.append(i)

    print("")
    print("array yang telah diinput")
    print(a)

    return a

arr = getArrayInput()
print("setelah diproses")
print(getPivots(arr))