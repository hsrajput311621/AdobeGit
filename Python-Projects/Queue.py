#Queue is linear data structure,It stores items in First in First out fifp
# 1)Enqueue: Adds an item to the Queue
# 2)Dequeue: Removes an item from the Queue
# 3)Front: Get the front item from queue.
# 4)Rear: get the last item from queue.

l=[]
while True:
    c=int(input('''
    1) Push the Element in the list
    2) Pop the first element from the list
    3)Find the Front item from the queue
    4)find the Rear item in the list
    5) Display the queue
    6) Exit the queue
    '''))
    if c==1:
        n=input("Enter the value of Queue")
        l.append(n)
        print(l)
    elif c==2:
        if len(l)==0:
            print("Queue is empyt,please add item before removing it:- ")
        else:
            del l[0]
            print(l)
    elif c==3:
        if len(l)==0:
            print("Queue is empyt,please add item before removing it:- ")
        else:
            print("The Front item of the queue is", l[0])
    elif c==4:
        if len(l)==0:
            print("Queue is empyt,please add item before removing it:- ")
        else:
            print("The rear item of the queue is:-", l[-1])
    elif c==5:
        print(l)
    elif c==6:
        break
    else:
        print("Invalid Entry")
        break

