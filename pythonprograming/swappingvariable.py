
# Approach 1 with temporary variable
num1 = int(input("Enter first number"))
num2 = int(input("Enter Second number"))

print("value of first number", num1)
print("value of second number", num2)

temp = 0

temp = num1
num1 = num2
num2 = temp

print("value after swap", num1)
print("value after swap", num2)

# Approach 2 without temp

num1 = int(input("Enter first number"))
num2 = int(input("Enter Second number"))

print("value of first number", num1)
print("value of second number", num2)

num1,num2 = num2, num1

print("value after  num 1 swap", num1)
print("value after num 2 swap", num2)
