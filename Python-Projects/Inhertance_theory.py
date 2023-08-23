
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

class A:
    def m1(self):
        print("This is m1 method from A class")

class B(A):
    def m2(self):
        print("This is m2 method of B class")

b = B()
b.m2()
b.m1()

class C:
    x,y =10,20
    def m3(self):
        print("Method m3 is calling")
        print(self.x + self.y)


class D(C):
    a,b = 200,100
    def m4(self):
        print("Method m4 is calling")
        print(self.a - self.b)

d = D()
d.m4()
d.m3()


##--------------Multi-Level Inheritance----------------------#

class E:
    p, q = 1000, 2000

    def m3(self):
        print("Method m3 is calling")
        print(self.p + self.q)


class F(E):
    m, n = 200, 100

    def m4(self):
        print("Method m4 is calling")
        print(self.m - self.n)

class G(F):
    i,j = 5,4

    def m5(self):
        print("Method m5 is calling")
        print(self.i * self.j)


g = G()
g.m4()
g.m3()
g.m4()
g.m5()

#------------Hirarchy Inheritance#------------------#

class H:
    s, t = 1, 2

    def m6(self):
        print("Method m6 is calling")
        print(self.s + self.t)


class I(H):
    o, p = 2000, 1000

    def m7(self):
        print("Method m7 is calling")
        print(self.o - self.p)

class J(H):
    q,r = 5,4

    def m8(self):
        print("Method m8 is calling")
        print(self.q * self.r)

i = I()
j = J()
i.m6()
i.m7()
j.m6()
j.m8()

##--------------Multiple Inheritance------------------##

class K:
    u, v = 1, 2

    def m9(self):
        print("Method m9 is calling")
        print(self.u + self.v)


class L:
    w, x = 2000, 1000

    def m10(self):
        print("Method m10 is calling")
        print(self.w - self.x)

class M(K,L):

    y,z = 5,4

    def m11(self):
        print("Method m11 is calling")
        print(self.y * self.z)

m = M()
m.m9()
m.m10()
m.m11()


##---------------------Overriding-Concept----------------------------##
# Calling parent class method using child class using (super())

class N:
    a,b = 10,20
    def m12(self):
        print("This is the m12 method of class N")

class O(N):
    a,b = 30,40
    def m12(self):
        print("This is the m12 result of class O")
        super().m12()
    def test(self):
        print(super().a,super().b)

o = O()
o.m12()
print(o.a,o.b)
o.test()


#-------------------##Example 11##-----------------------

class P:
    a,b = 10,20

class Q(P):
    i,j = 100,200

    def m13(self,x,y):
        print(x+y)      # Local vaiables
        print(self.i+self.j)     # accessing Class variables by self keyword
        print(self.a+self.b)     # accessing parent Class variable by self keyword

q = Q()
q.m13(5000,6000)


###------------Polymorphiam-----------------------------##
# one object can have many forms, we can define polymorphism as the ability of a message to be displayed in more than one form.
# A real-life example of polymorphism is a person who at the same time can have different characteristics. Like a man at the same time is a father, a husband and an employee
# shape : circle---rectangle---square--pyramid...
#Polymorphism can be implement using overloading concept.
# eg add()
#add(1,3)
#add(1,3,4)
#add(1,2,3,4)

#Example 10 : Overloading Concept #---------------

class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("Hello" " " +name)
        else:
            print("Hello")

h = Human()
h.sayhello()
h.sayhello("Hitesh")

#Example 11 : Overloading Concept #---------------

class Calculation:
    def add(self, a=0,b=0,c=0):
        print(a+b+c)

cal = Calculation()
cal.add(10,20,30)
cal.add()
cal.add(300,200)


