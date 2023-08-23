## Class and Objects in OOPS programming


class Phone:
    def make_call(self):
        print("I am making call")

    def play_game(self):
        print("I am playing game")


p1 = Phone()

p1.make_call()
p1.play_game()


class Iphone:
    def set_color(self, color):
        self.color = color

    def set_cost(self, cost):
        self.cost = cost

    def show_color(self):
        return self.color

    def show_cost(self):
        return self.cost

    def make_call(self):
        print("I am calling")

    def play_game(self):
        print("I have game")


p2 = Iphone()

p2.set_color("purple")
p2.set_cost(81000)
p2.show_color()
p2.show_cost()
p2.make_call()
p2.play_game()


# class with constructor####

class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name of the employee is :", self.name)
        print("Age of the employee is :", self.age)
        print("Salary of the employee is :", self.salary)
        print("Gender of the employee is :", self.gender)


emp = Employee('Sam', 32, 85000, 'Male')

emp.employee_details()


### Inheritance with the Class#####

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


## Constructure call in the child class####


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
