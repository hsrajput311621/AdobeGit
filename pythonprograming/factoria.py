
num1 = int(input("Enter the number for the factorial"))
fact = 1

if num1 < 0:
    print("Cannot find the factorial of negative number")
elif num1 == 0:
    print("The factorial of zero is 1")
else:
    for i in range(1, num1+1):
        fact = fact*i
    print("The factorial of the number is ", fact)


#Approach 2: using recurrsive function

def fact(num1):
    if (num1==0 or num1==1):
        return 1
    else:
        return num1 * fact(num1-1)

num1 = int(input("Enter the factorial number"))
print(fact(num1))


# Approach 3 recurrsive with ternary operator

def fact(num1):
    return 1 if (num1==1 or num1==0) else num1*fact(num1-1)

num1 = int(input("Enter the factorial number"))
print(fact(num1))