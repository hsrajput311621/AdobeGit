# How to define function

# def hello():     # function defination
# #     print("Hello world")
#
# hello()     # function calling/invoking

# def add():
#     a=int(input("Enter the value in the function"))
#     n=a+10
#     print(n)
#
# add()

def add_10(x):
    c=x+10
    return c

print(add_10(100))





def odd_even(x):
    if x%2==0:
        print("x is an even number")
    else:
        print("X is an odd number")

odd_even(498)

#Lamda with Filter function#

# filter function with lambda
# l1 = [1,2,3,4,5,6,7,8,9,10]
# final_list=list(filter(lambda x: (x%2!=0),l1))
#
# print(final_list)

##Lambda funcion##

g =lambda x: x*x*x

a=10
g(a)
print(g)
#
# #lambda with map function##
#
# l1 = [1,2,3,4,5,6,7,8,9,10]
# final_list=list(map(lambda x: x*2, l1))
#
# print(final_list)
#
# #Lambda with reduce
# l1 = [1,2,3,4,5,6,7,8,9,10]
# from functools import reduce
# final_list=reduce(lambda x,y: x+y,l1)
# print(final_list)

