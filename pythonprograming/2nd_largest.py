
mylist = [1,2,3,4,5,6,7,8,9,2,2,2,2,2,3]
mylist.sort()
print(mylist)
print("The maximum element in the list is ", max(mylist))
print("The 2nd highest number in the list is ", mylist[-2])


#Approach 2:
mylist = [1,2,3,4,5,6,7,8,9,2,2,2,2,2,3]
mylist1 = set (mylist)
print("list before remove", mylist1)
mylist1.remove(max(mylist1))
print(mylist1)
print(max(mylist1))




