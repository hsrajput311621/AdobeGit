

# # num =input("Enter the word to know the meening")
# #
# # dic = { "Abate": "Moderate",
# #         "Adhere": "Comply",
# #         "Abolish": "Abrogate",
# #         "Acumen": "brilliance"}
#
# print(dic[num])
#---------------------------------------------------------------------------------------------------------
# age =int(input("Enter your age"))
# if age>7 and age<85:
#     if age > 18:
#         print("you can drive the car or eligible of liscense")
#     elif age ==18:
#         print("Please come physically to the liscense office")
#     else:
#         print("you are too young to drive, not eligible for liscense")
#
# else:
#     print("you have used wrong age out of limit")

#--------------------------------------------------------------------------------------------------------
# list = [1,2,3,4,5,6,7,8,9]
# # to check the element exist in list
# num =int(input("Enter"))
# if num in list:
#     print("num is present in list")
#
# else:
#     print("Num is not present")

#---------------------------------------------------------------------------------------------------------------

# while (True):
#     num1 = int(input("Enter the first number"))
#     num2 = int(input("Enter the second number"))
#     print(""" Which operator want to use for the calcultions
#     1) sum " + "
#     2) sub " - "
#     3) mul " * "
#     4) divide " / "
#     """)
#     ch = int(input("Enter you choice"))
#
#     if ch == 1:
#         if num1==56 or num2==9:
#             output = 77
#             print("The sum of two numbers are :" , output)
#
#         elif num1==9 or num2==56:
#             output = 77
#             print("The sum of two numbers are :" , output)
#
#         else:
#             output = num1 + num2
#             print("The sum of two numbers are :" ,output)
#
#     if ch == 3:
#
#         if num1==45 or num2==3:
#             mul = 555
#             print("The multipliation is:", mul)
#
#         elif num1==3 or num2==45:
#             mul = 555
#             print("The multipliation is:", mul)
#
#         else:
#             mul = num1 * num2
#             print("The multiplication of two numbers are :",mul )
#
#     if ch == 4:
#         if num1==56 or num2==6:
#             output = 4
#             print("The division of two numbers are:" , output)
#         else:
#             output = (num1/num2)
#             print("The division of two numbers are :", output)
#
#     else:
#         print("wrong selection")
#
#     again = input("Enter you want to calclate again 'y' and if not press 'n'")
#     if again =='y':
#         continue
#     elif again=='n':
#         print('Thanks for using our calculator, have a nice day.')
#         break

#---------------------------------------------------------------------------------------------------------------
# flag = 0
# count =0
# list1 = [1,2,7,88,700,45,23,6,569,9,9, 'Hitesh','Rajput', 'Ashi']
# print(list1)
# for item in list1:
#     if str(item).isnumeric() and item > 6:
#         count = count+1
#         print(item, end=" ")


# while(True):
#     num = int(input("Enter the number you want to print"))
#     if num < 100:
#         print("Try again\n")
#         continue
#     else:
#         print("Congratulation you have seleted more than 100\n")
#         break
#-------------------------------------------------------------------------------------------------------------------
# num = 25
# guess =3
# while(guess>0):
#     n = int(input("enter your number"))
#
#
#     if n == num:
#         print("Congratulations! you have guessed correct number")
#         print("you won")
#         break
#     else:
#         if n > num:
#             print("OOPS! you have guessed greater number")
#             guess = guess -1
#             print(guess)
#         elif n<num:
#             print("OOPS! you have gussed smaller number")
#             guess = guess - 1
#             print(guess)
#
# print("Gameover")
# print("you have left ", guess, "guess")
#------------------------------------------------------------------------------------------------------------------
# n =25
# guess = 1
# while(guess<=5):
#     number = int(input("Enter your guess to guess"))
#     if number > n:
#         print("The number is too high")
#     elif number < n:
#         print("The number is too low")
#     else:
#         print("You won the game \n")
#         print(guess , " Number of guess took to finish the game")
#         break
#     print(5-guess, "number of guesses left")
#     guess = guess +1
#
# if guess >5:
#     print("Gameover")
#---------------------------------------------------------------------------------------------------------------------------
# pattern printing with condition

# size = int(input("Enter the size of the pattern"))
# value = int(input("Enter '1' or '0' "))
# condition = bool(value)
#
# if condition == True:
#     for i in range(size):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()
#
# elif condition == False :
#     for i in range(size):
#         for j in range(i,size):
#             print("*", end="")
#         print()
#
# else:
#     print("Worng choice")
#------------------------------------------------------------------------------------------------------------------
# this is the method to open the file named hitesh.txt

# f = open("hitesh.txt", "rt")
#content = f.read()
#print("1", content)
# print(f.readline())   # it will read line by line
# print(f.readlines())   #it will print the list of the lines
#
# # for line in content:
# #     print(line)
# f.close()

#f = open("hitesh.txt", "rt")  # this is used to open the file with read by default
#f = open("hitesh.txt", "a")   # append mode add the new data in the existing data
#content = f.read() # this is used to read the data from the file
# content = f.write("""Hi This is the python programming
# I am going to lear programming by the end of the year
# This is my deadline of the year 2022
# This new data added by f.write() function which remove the old data with
# new data
# """)
#content = f.write("Hitesh bhai bhot acche h")   # this is used to write in the file
# content = f.read()   # this is use to read the existing data in the file
# print(content)
# f.close()   # it is use to close the file

# how to use r+ as handle read and write both #

# f = open("hitesh.txt", "r+")
# print(f.tell())
# content = f.read()
# # print(f.tell())   # it will tell the place of file pointer
# #content1 = f.write("Thank you for the content")
# print(content)
# f.seek(10)       # it will take the file pointer to desired position
# print(f.tell())
# f.close()

# file open with block #
# with open("hitesh.txt") as f:   # this is use to open the file and close the file with one syntax
#     a = f.readlines()
#     print(a)

# here no need to write the f.close()

#-----------------------------------------------------------------------------------------------------------------

# Health Management System
# 3 clients - Harry, Rohan and Hammad
# write a function that when executed takes as input client name

#-------------------------------------------------------------------------------------------------------------

# Global keyword and local keyword:

# l = 10  # global variable
# def func(n):
#     # l = 500  # local variable inside function
#     global l
#     l = l + 445
#     print(n, "This is the testing function for global and local variable")
#     print(l)
#
# func("Hi this is an object")
# print(l, "This will print global value of l")
# x = 90
# def hitesh():
#     x =100
#     def harry():
#         global x
#         x =200
#     print("Before calling harry()", x)
#     harry()
#     print("After calling harry()", x)
#
# hitesh()
# print(x)

#-----------------------------------------------------------------------------
# Recurssion : function inside function

# def fact_iterative(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact * i
#     return fact
#
# def fact_recurssive(n):
#     if n ==1 or n==0:
#         return 1
#     else:
#         return n * fact_recurssive(n-1)
#
# num = int(input("Enter the number to find factorial"))
# f1 = fact_recurssive(num)
# f = fact_iterative(num)
# print("Factorial by recurssive", f1)
# print("Factorial by iterative", f)

#----------------------------------------------------------------------------
#Fibonacci series#

# def fibo(num):
#     first = 0
#     second = 1
#     sum = 0
#     for i in range(2, num+1):
#         sum = first + second
#         print(sum)
#         first = second
#         second = sum
#
#
# num = int(input("Enter the number for fibonacci"))
# first = 0
# second = 1
# print(first)
# print(second)
# f = fibo(num)
# print(f)

#Fibonacci series# By recurssion#

def fibonacci(n):
    if n == 0:
        return 0
    elif n ==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n = int(input("Enter the number"))
print(fibonacci(n))
