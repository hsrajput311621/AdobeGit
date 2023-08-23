# In python there is a difference b/w Function and Methods:
# Function : We can create without class.
# Method: When function create in side class called methods, taking self as argument.
# In class we can define 2 types of methods:
#a) Instanace Method: we can call only through objects.
#b) Static Method: we can directly call using class name, no object required.
# In static method, we need to pass the of self keyword, it is not default argument in static method.




class MyClass:
    def myfun(self):  #function define inside class called methods and every method
                      # take one default argument called self.
                      # Self argument, always represent the function is represt to the class name.
        pass          # pass is showing when the function is blank.
    def display(self,name):
        print(name)


mc = MyClass()
mc.display("Hitesh")
mc.myfun()

#Example 2

class MyClass1:
    def m1(self):
        print("This is the Instance Method")
    @staticmethod
    def m2(self, num):
        print(self,num)

c = MyClass1()
c.m1()
c.m2("hitesh", "Adobe")
MyClass1.m2(100, 200)   # static method do not use object name to call, but can be call by class name.


#Example3:

# Global Variables
# Class Variables
# Local Variables

#If we want to use class variables inside the methods we need to use self keyword.
class NewClass:
    a,b = 10,20        #These are class variables, can not use in method directly, but can use self keyword.
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

nc = NewClass()
nc.add()
nc.mul()

#Example 4

i, j = 15,25   # Global variable

class Global:
    a,b = 10,20   # Class variables
    def add(self,x,y):    # Local variable x and y
        print("The sum of two local variables x and y are "" ", x + y)   # x and y are local varialbes
        print("The sum of two Class variables a and b are " " ", self.a+self.b)  # a and b are class variable use self keyword always
        print("The sum of global variables are "" ", i+j)  # i and j are global variable and can be use anywhere in the class.

g = Global()
g.add(100,200)

#Example 5

p, q = 15,25   # Global variable

class New_Global:
    p,q = 150,250   # Class variables
    def add(self,p,q):    # Local variable x and y
        print("The sum of two local variables x and y are "" ", p + q)   # x and y are local varialbes
        print("The sum of two Class variables a and b are " " ", self.p+self.q)  # a and b are class variable use self keyword always
        print("The sum of global variables are "" ",globals()['p'] + globals()['q'])  # i and j are global variable and can be use anywhere in the class.

ng = New_Global()
ng.add(1000,2000)

## Constructor##

#Differnce b/w methods and constructor,
#Methods: We can use any Name of the methods, it returns the value/s, It can
          # take arguments/parameters, we have use an object to invoke the method.
# Constructor : Constructor Name is fixed, we cannot use any other name apart it: def __init__(self):
         # it does not return any value, it also take arguments and parameters
         # The constructor will be called at the time of object creation itself.

class Cons_Class:
    def __init__(self, name):
        print("This is the constructor", name)

    def func(self):
        print("this is the method")

    def sum(self,x,y):
        sum = x+y
        return sum

cc = Cons_Class("Hitesh")   #Object automatically invoke the construtor,no need to call it.
cc.func()   # Mehtod need to call by the help of object.
sum1 = cc.sum(100,200)
print(sum1)

#Expample 6

class Arg_Class:
    name = "john"                 #Class variable
    def __init__(self, name):    # Constructor accepting some parameter.
        print(name)            # local variable.
        print(self.name)      #Class variable by self.

Arg_Class("Scott")          # Passing paramenter to the constructor.


#Example 7 # Requirements
# Constructor : eid, ename, sal.
# display() : print eid, ename and sal.

class Employee:
    def __init__(self, eid, ename, sal):

        print("The employee constructor has been called")
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print("The employee id is" , self.eid)
        print("The employee name is ", self.ename)
        print("The sal of the employee is", self.sal)

e = Employee(101, "hitesh", 10000)
e1 = Employee(102,"Scott", 20000)
e1.display()
e.display()

## Inheritance ##

# Acquiring all the attributes(varialbles) and behaviour(methods) from one class to
# another class. Parent ---> properties acquired by chile class
#Class A  ----> a,b,c methods ---> m1(), m2() ---Parent class of B.
#Class B(A) ---> x,y,z   methods ---> m3() ----> B is child of A Class.
# when we declare the objec of class B, it is eligible to access the methods of A class
# and Class B also, object of Class B can access to both class methods.
# Objective of the Inheritance is the reusability of the methods and Aviod duplicacy.
#Types of the Inhertance:
# Single line: Only one parents and one child class
# Multi-level: One Parents have one child and the same child has one more child and so on,
#             so the last class have access of the class methods, as it inherits from all the upper class
# Heirarchy: We have one parent and can be multiple child class but the child class are differet from each other.
# Multiple: we have multiple parent classes of single child class.





