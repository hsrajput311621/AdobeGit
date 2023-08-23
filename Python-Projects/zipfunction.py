#zip function:

a=[10,20,0,10,30,40,50]
b=[60,70,80,90,10]
for i,j in zip(a,b):
    print(i,j)

#2nd method
a=[10,20,0,10,30,40,50]
b=[60,70,80,90,10,20,50]
l1=len(a)
for i in range(l1):
    print(a[i],b[i])

#program to convert the String to a List

# n=input("Enter the value")
# s=n.split();
# print(s)

a=[]
for i in range(1,4):
    n=input("Enter the first value of list")
    a.append(n)
print(a)

