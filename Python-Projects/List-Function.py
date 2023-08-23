# insert(), append(), extends()
import imaplib
#insert

a=[10,20,30,40,50,60,70,80,90]
print(a)
a.insert(4,1000)
print(a)
#Output:[10, 20, 30, 40, 1000, 50, 60, 70, 80, 90]

#append()

a=[10,20,30,40,50,60,70,80,90]
print(a)
a.append("hello")
print(a)
#Output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 'hello']

#extends()

a=[10,20,30,40,50,60,70,80,90]
print(a)
n=[1000]
a.extend(n)
print(a)
#output: [10, 20, 30, 40, 50, 60, 70, 80, 90, 1000]

#list comprehension#

for i in range(0,10):
    print(i)

#Funcitons of List

#count(), max(), Min(), sort(), reverse() index()

#count()

a=[10,20,10,10,30,40,50,60,70,80,90,10]
l=a.count(10)
print(l)

#max()

a=[10,20,10,10,30,40,50,60,70,80,90,10]
m=max(a)
print(m)

#min()

a=[10,20,0,10,30,40,50,60,70,80,90,10]
min=min(a)
print(min)

#sort()
a=[10,20,0,10,30,40,50,60,70,80,90,10]
a.sort()
print(a)

#reverse()
a=[10,20,0,10,30,40,50,60,70,80,90,10]
a.reverse()
print(a)

#Index()
a=[10,20,0,10,30,40,50,60,70,80,90,10]
m=a.index(80)
print(m)
