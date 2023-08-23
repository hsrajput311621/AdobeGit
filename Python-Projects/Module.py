## I am creating my first module in python language to use this moudle in my different programs##

# def sum_file(a, b):
#     c = a + b
#     return c
#
#
# def mul_file(d, e):
#     f = d * e
#     return f


def calc(a, b, m):
    print('''
    + ADD
    - SUBTRACT
    * MULTIPLY
    / DIVIDE
    ''')
      c= int(input('''
    1) it is for sum
    2) it is for sub
    3) it is for mul
    4) it is for div
    5) it is for remind
    6) it is an invalid entry
        '''))
    if c==1:
        print("The sum of two number is", a+b)
        return d
    elif c==2:
        print("The sub of the two number is", a-b)
        return d
    elif c==3:
        print("the multiplication of the two number", a*b)
        return d
    elif c==4:
        print("The division of the two numbers are", a/b)
        return d
    elif c==5:
        if m%2==0:
            print("The number is even")
        else:
            print("The number is odd")
        return d

    elif c==6:
        print("Invalid path")
        return d

x= calc()
a= int(input("Enter the vaule of a"))
b= int(input("Enter the vaulue of b"))
m= int(input("enter the value for reminder"))

print(x)



