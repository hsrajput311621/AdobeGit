#
# # *
# # **
# # ***
# # ****
# # *****
#
# num = int(input("Enter the number for the pattern"))
#
# for i in range(0, num):
#     for j in range(0, i+1):
#         print("*", end="")
#     print()
#
#
# # 1
# # 12
# # 123
# # 1234
# # 12345
# # 123456
#
# num = int(input("Enter the number for the pattern"))
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(j, end="")
#     print()
#

#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5

# num = int(input("Enter the number for the pattern"))
#
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(i, end=" ")
#     print()

# *                hollow right triangle
# * *
# *  *
# *   *
# * * * *

# num = int(input("Enter the number for the pattern"))
# for i in range(num):
#     for j in range(num):
#         if j==0 or i==(num-1) or i==j:
#           print("*", end="")
#         else:
#             print(end=" ")
#
#     print()

#     *
#    **
#   ***
#  ****
# *****
num = int(input("Enter the number for the pattern"))
for i in range(num):
    for j in range(i,num):
        print(" ",end="")
    for j in range(i+1):    #(j =i ; j<i+1; j++)
        print("*", end="")
    print()





# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# num = int(input("Enter the value of num"))
#
# for i in range(num):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(i, num):
#         print("*",end="")
#     print()


# program for factorial:
#5! = 5*4*3*2*1 = 120
#5! = 1*2*3*4*5 = 120
# num=int(input("Enter the number for factorial"))
# pos=1
# for i in range(1, num+1):
#     pos=pos*i;
# print(pos)
#
# #Using math module
#
# import math
# n = int(input("Enter the factorial number"))
# result = math.factorial(n)
# print(result)

# Using recurssion
# Base Case and Recurssive case

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
#
# n = int(input("Enter the value for factoria"))
# result = fact(n)
# print(result)

# *****
# ****
# ***
# **
# *
# num = int(input("Enter the value of num"))
#
# for i in range(num):
#     for j in range(i, n):
#         print("*",end="")
#
#     print()


# Pattern programming#
# * * * * *
#   *     *
#     *   *
#       * *
#         *

# num = int(input("Enter the value of num"))
#
# for i in range(0, num):
#     for j in range(0, num):
#         if i==0 or j==(num-1) or i==j:
#             print("*",end="")
#         else:
#             print(end=" ")
#
#     print()



#
#         *
#       * * *
#     * * * * *
#   * * * * * * *
#  * * * * * * * * *

# num = int(input("Enter the value of num"))
# for i in range(num):
#     for j in range(i,num):
#         print(" ",end="")
#     for j in range(i+1):
#         print("*",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

#
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# num = int(input("Enter the value of num"))
# for i in range(num):      # i = 0, i<4; i++
#     for j in range(i):
#         print(" ",end="")
#     for j in range(i, num-1):
#         print("*",end="")
#     for j in range(i,num):
#         print("*",end="")
#     print()