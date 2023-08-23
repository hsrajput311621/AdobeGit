

### Exception Handling##------------

# Exception is an event which will cause program termination

# Three keywaord to handle the Exception handling
# Try, Except, else
# finally block is used at the last, if we need to execute anything always.
#Except: executes only when exception occured
#Else: executes only exception not occured


#Expample 1:
print("This is the first line of the code/programming")
print("This is the second line of the code/programming")
print("This is the middle line of the code")

try:
    print(x)
except:
    print("Exception occured")

print("This is the last line of the code/programming")


# Example 2

print("This is the starting point of the code")
print("This is the middle of the code")
try:
    print(10/0)
except ZeroDivisionError:  # add the name of the exception
    print("Exception occured... and handled")
print("Program completed")

##Example 3  : Multiple except block -- try, except, else and finally keyword
try:
    num1, num2 = 10,0
    result = num1/num2
    print("result is: ", result)
except ZeroDivisionError:
    print("Thrown ZeroDivisionError.....")
except SyntaxError:
    print("Thrown SyntaxError Exception")
except:
    print("Exception handled")
else:
    print("No exception occured")
finally:
    print("Always execute")

##Example 4 Rising our own exception

    def agenum(age):
        if age<0:
            raise ValueError("only Interger are allowed")

        if age%2==0:
            print ("even")
        else:
            print("odd")
print("Checking number is even or odd by calling function")
num = -1
try:
    agenum(num)
except ValueError:
    print("value error exception occured and handled..")
print("program completed")