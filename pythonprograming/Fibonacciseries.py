# 0 1 1 2 3 5 8 13 .....
num = int(input("Enter the range of the fibonnaci"))
num1 = 0
num2 = 1
add = 0
temp = 0
print(num1)
print(num2)

for i in range(2, num+1):
    add = num1+num2
    print(add)
    num1 = num2
    num2 = add

