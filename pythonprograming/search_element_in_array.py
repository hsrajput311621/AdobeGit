mylist = [1,2,3,4,5,6,7,8,9]
l = len(mylist)
num = int(input("Enter the element to search in array"))
flag = 0
for i in mylist:
    if(i == num):
        print("Element is exist in the array")
        flag=1
        break

if (flag ==0):
    print("Element does not exist")

#Approach 2: Using in operator

mylist = [1,2,3,4,5,6,7,8,9,10,11,12]
num = int(input("Enter the element to search in array"))
if (num in mylist):
    print("Element found")
else:
    print("Element not found")