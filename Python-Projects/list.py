#List : it is a mutable data type, declare inside [] brackets and
# comma seperated i=[1,2,3,4,5,6] index will be from 0 left to right.
i=[1,2,3,4,5,6,7,8,9,0]
print(type(i))
print(i[6])
#output:<class 'list'>
#output=7

#nested list
i=[1,2,3,4,5,6,7,8,9,[11,12,13]]
print(type(i))
print(i[9][1])
#output:<class 'list'>
#output:12

i=[1,2,4,"Hello",[6,7,8]]
print(type(i))
print(i[3])
#output: <class 'list'>
#output: Hello

#Slicing of List and strings are same

i=[1,2,3,'Hello',[7,8,9,0]]
print(i[0:])
print(i[0::2])
print(i[-1::-1])
#output:[1, 2, 3, 'Hello', [7, 8, 9, 0]]
#output:[1, 3, [7, 8, 9, 0]]
#output:[[7, 8, 9, 0], 'Hello', 3, 2, 1]

#List Iteration
a=[10,20,30,40,50,60,70,80,90]
b=len(a)
print(b)
for i in range(b):
    print(a[i])
#output:10 20 30 40 50 60 70 80 90

a=[10,20,30,40,50,60,70,80,90]
b=len(a)
print(b)
for i in a:
    print(i)
#output:10 20 30 40 50 60 70 80 90

#List Iteration in reverse
a=[10,20,30,40,50,60,70,80,90]
b=len(a)
print(b)
for i in range(b-1,-1,-1):
    print(a[i])
#output:90 80 70 60 50 40 30 20 10

#list -Function##

# del, pop, remove(), clear(), reverse()

#reverse()#

a=[10,20,30,40,50,60,70,80,90]
a.reverse()
print(a)
#output: [90, 80, 70, 60, 50, 40, 30, 20, 10]

a=[10,20,30,40,50,60,70,80,90]
print(a)
del a[4]
print(a)
del a[6:]
print(a)
#output:[10, 20, 30, 40, 60, 70, 80, 90]
#output[10, 20, 30, 40, 60, 70]

#pop() function

a=[10,20,30,40,50,60,70,80,90]
print(a)
print(a.pop(2))
print(a)
#output: 30
#output: [10, 20, 40, 50, 60, 70, 80, 90]

#remove() function

a=[10,20,30,40,50,60,70,80,90]
print(a)
a.remove(60)
print(a)
#output:[10, 20, 30, 40, 50, 70, 80, 90]

#clear() Function

a=[10,20,30,40,50,60,70,80,90]
print(a)
a.clear()
print(a)
#output: []

#update the list value:
a=[10,20,30,40,50,60,70,80,90]
print(a)
a[5]=100
print(a)
#output: [10, 20, 30, 40, 50, 100, 70, 80, 90]

a=[10,20,30,40,50,60,70,80,90]
l=len(a)
print(l)
#output: 9

#while loop in list####
l=[]
while True:
    c=int(input('''
    1) inter the value for the list
    2) Break the logic
    '''))
    if c==1:
        a=int(input("Enter the values"))
        v=l.append(a)
        print(l)
    if c==2:
        break

#output



