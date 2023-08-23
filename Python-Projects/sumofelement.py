
# Sum of element of an array

# s = int(input("please enter the size of an array"))
# sum = 0
#
# for i in range(s):
#     sum = sum+i
# print("The sum of array is ", sum)

# Compare the elements of the arrays and count who won the game eg a[0] 3>1 alica won

# a = [3,2,1]
# b = [1,2,3]
#
# alice = 0
# bob = 0
#
# for i in range(3):
#     if a[i]>b[i]:
#         alice+=1
#
#     elif a[i]<b[i]:
#         bob+=1
#
# print(alice, bob)


# Find the absolute difference of the sum of diagonals of 2d matrix

# a =  123        sum of 1+5+9 - 3+5+7  = 0
#     [456]
#      789

# rows, cols = (5, 5)
# arr=[]
# for i in range(rows):
#     col = []
#     for j in range(cols):
#         col.append(0)
#     arr.append(col)
# print(arr)

# left = 0
# right = 0
# arr=[]
# for i in range(3):
#     left+=arr[i][i]
#     right+=arr[i][3-1-i]
# diff = left-right
# print(diff)

# find the decimal value upto 5 of the element of an array

# arr = [1,1,-1,-1,0,0]
# p = n = z = 0
# for i in range(0, 6):
#     if arr[i]>0:
#         p+=1
#     elif arr[i]<0:
#         n+=1
#     else:
#         z+=1
# print(p/6)
# print(n/6)
# print(z/6)

# find the sum of the element of an array whose sum is maximum and minimum but take any 4 values at one time

# arr = [1,2,3,4,5]
# temp = 0
# sum = 0
# for i in range(0,5):
#     sum = sum + arr[i]
# maximum = max(arr)
# minimum = min(arr)
# print(sum - maximum, sum - minimum)

# find the element of an array which is maximum in count

arr = [1,2,3,4,5,5,5,5]
count = 0
maximum = max(arr)
for i in range(8):
    if arr[i]==maximum:
        count+=1
print("the maximum occurence of element is" , maximum, count)