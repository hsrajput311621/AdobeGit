print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')
a=int(input("Enter first number"))
b=int(input("Enter second number"))
c=int(input("What operator you want to use 1='+', 2='-', 3='*', 4='/'"))

if c==1:   #if c=="+"
    print("Sum of two number is ", a+b)

elif c==2: #if c=="-"
    print("Subraction of the two number is", a-b)

elif c==3: #if c=="*"
    print("Multipication of two number", a*b)

elif c==4: #if c=="/"
    print("Division of the two value", a/b)

else:
    print("Invalid entry")


