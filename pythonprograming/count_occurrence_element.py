
mylist = [1,2,3,4,5,6,7,8,9,2,2,2,2,2,3]
count1 = 0
num1 = 2

for i in mylist:
    if (i == num1):
        count1 = count1+1
print(count1)


#Approach 2: using count function

mylist = [1,2,3,4,5,6,7,8,9,2,2,2,2,2,2,2]
print(mylist.count(2))

# Approach 3 : uning counter() function:

from collections import Counter
mylist = [1,2,3,3,4,5,6,7,8,9,9,9,2,2,2,2,2,2,2,2,2]
dic = Counter(mylist)
print(dic)

