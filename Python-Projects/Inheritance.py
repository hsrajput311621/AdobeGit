# ### Inheritance with the Class#####
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

#
class Vehicle:
    def __init__(self, mileage, cost, year_manuf):
        self.mileage = mileage
        self.cost = cost
        self.year_manuf = year_manuf

    def show_details(self):
        print("I have a car with me which is giving best performance")
        print("The Mileage of the car is", self.mileage)
        print("The Cost of the car us =", self.cost)
        print("The year of manufacture of the car is", self.year_manuf)


veh = Vehicle(20, 500000, 2022)

veh.show_details()


class Car(Vehicle):
    def show_car(self):
        print("The color is great and i do not want to change it")


c = Car(24, 600000, 2023)

c.show_details()
c.show_car()

#
# ## Constructure call in the child class####
#
#
class Adobe:
    def __init__(self, developers, testers, managers):
        self.developers = developers
        self.testers = testers
        self.managers = managers

    def show_details_employees(self):
        print("The number of developers in Adobe are", self.developers)
        print("The numbers of testers in Adobe are ", self.testers)
        print("The numbers of managers in Adobe are ", self.managers)


adobe = Adobe(500, 300, 100)
adobe.show_details_employees()


class Techdepat(Adobe):
    def __init__(self, developers, testers, managers, devleads, testleads):
        super().__init__(developers, testers, managers)
        self.devleads = devleads
        self.testleads = testleads

    def show_print_details(self):
        print("the number of Devleads in Print dept", self.devleads)
        print("the number of Testleads in Print dept", self.testleads)


p = Techdepat(1000, 700, 200, 50, 25)
p.show_print_details()
p.show_details_employees()


##Multiple Inheritence in python##

class Parent1:
    def assign_string1(self, str1):
        self.str1 = str1

    def show_string_one(self):
        return self.str1


class Parent2:
    def assign_string2(self, str2):
        self.str2 = str2

    def show_string_two(self):
        return self.str2


class Child(Parent1, Parent2):
    def assign_string3(self, str3):
        self.str3 = str3

    def show_string_three(self):
        return self.str3


d = Child()
d.assign_string1("My name is khan")
d.assign_string2("But")
d.assign_string3("I am not Sharu-k-khan")

print(d.show_string_one())
print(d.show_string_two())
print(d.show_string_three())
