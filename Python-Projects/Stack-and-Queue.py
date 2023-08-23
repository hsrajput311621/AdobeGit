#how to implement Stack and Queue using a list Data Type:

#Stack is a linear data structure.
#It stores items in a LIFO or FILO manner.

#Stack Operations:
#Push = >Insertion an Elements
#Pop = > Deletion An Element(Last Element)
#Peek= > Display the Last Element
#Display=> Display List.

l=[]
while True:
    n=(int(input("""
    1) Push The Element in the Stack
    2) Pop the Element from the Stack
    3) Delete/Find the last element in the Stack
    4) Display the whole stack
    5) Exit from the loop
    """)))
    if n==1:
        v=int(input("Please enter the first value of stack:- "))
        l.append(v)
        print(l)
    elif n==2:
        if len(l)==0:
            print("Stack is empty")
        else:
            z=l.pop()
            print(z)
            print(l)
    elif n==3:
        if len(l)==0:
            print("Empty Stack")
        else:
            print("Last stack value",l[-1])
    elif n==4:
        print(l)
    elif n==5:
        break
    else:
        print("Invalid Choice")
        break






