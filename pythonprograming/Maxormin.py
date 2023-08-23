
arr = []
num = int(input("Enter the size of an array"))
for i in range(num):
    arr.append(int(input("Enter the elements")))
print(arr)

max = arr[0]
for i in range(1, num):
     if arr[i]>max:
         max=arr[i]

print("maximum element in array is ", max)


# Finding minimum element

arr1=[20,30,40,10,6]
n = len(arr1)
min = arr1[0]

for i in range(n):
    if arr1[i]<min:
        min=arr1[i]
print(min)


