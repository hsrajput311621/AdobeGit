
# num1 = int(input("Enter the number to check the prime"))
#
# if num1 < 0:
#     print("The number is a negative number")
#
# elif num1 == 1:
#     print("One is a prime number")
# else:
#     for i in range(2, num1):
#         if (num1 % i) == 0:
#             print("the number is not prime")
#             break
#         else:
#             print("number is prime")
#             break
#
#
#
#
# num1 = int(input("Enter the number to check the prime"))
# count = 0
# if num1 <= 0:
#     print("The number is very less of find the prime")
# elif num1 ==1:
#     print("it is a prime number")
# elif num1 > 1:
#     for i in range(1,num1+1):
#         if (num1 % i) == 0:
#             print(i)
#             count = count+1
#     if count ==2:
#         print("The number is a prime")
#     else:
#         print("the number is not prime")


# print all prime number btween the given interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
















