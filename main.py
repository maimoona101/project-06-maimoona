# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):  # Constructor
        self.name = name        # yeh line student ka naam set karti hai
        self.marks = marks      # yeh line student ke marks set karti hai

    def display(self):          # Method to show student details
        print("Student Name:", self.name)
        print("Marks:", self.marks)

student1 = Student("Maimoona", 90)  # Naya student banaya
student1.display()                 # Student ki details print ki

# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count = 0  # class variable to track object count

    def __init__(self):
        Counter.count += 1  # jab bhi naya object banay, count barhayein

    @classmethod
    def display_count(cls):  # cls ka matlab hai class khud
        print("Total objects created:", cls.count)

obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.display_count() 

# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand  # public variable

    def start(self):        # public method
        print(self.brand, "car is starting...")

my_car = Car("Toyota")

print("Brand:", my_car.brand)

my_car.start()

# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Old Bank"  # class variable

    def __init__(self, account_holder):
        self.account_holder = account_holder

    @classmethod
    def change_bank_name(cls, name):  # class method
        cls.bank_name = name

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {Bank.bank_name}")

acc1 = Bank("Zubair")
acc2 = Bank("Moona")

acc1.display() 
acc2.display()   

Bank.change_bank_name("New Bank")

acc1.display()   
acc2.display()  

# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):  # Static method
        return a + b

result = MathUtils.add(8, 5)
print("Sum:", result)

# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger object created.")  # Constructor message

    def __del__(self):
        print("Logger object destroyed.")  # Destructor message

log = Logger()

del log  

# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         # public variable
        self._salary = salary    # protected variable
        self.__ssn = ssn         # private variable

    def show_info(self):
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


# Object banate hain
emp = Employee("Amjad", 80000, "123-45-6789")

# Public variable access
print("Public - Name:", emp.name)

# Protected variable access
print("Protected - Salary:", emp._salary)

# Private variable access (will cause error if accessed directly)
try:
    print("Private - SSN:", emp.__ssn)
except AttributeError as e:
    print("Private - SSN: Cannot access directly!", e)

# Accessing private variable using name mangling
print("Private - SSN (via name mangling):", emp._Employee__ssn)

# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Person:
    def __init__(self, name):
        self.name = name  # Base class constructor

    def display(self):
        print("Name:", self.name)

class Teacher(Person):  # Inheriting from Person class
    def __init__(self, name, subject):
        super().__init__(name)  # Calling base class constructor
        self.subject = subject  # Additional attribute for Teacher

    def display_teacher_info(self):
        self.display()  # Calling base class method
        print("Subject:", self.subject)

teacher1 = Teacher("Mr. Azfar", "Mathematics")

teacher1.display_teacher_info()

# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract class inheriting from ABC
    @abstractmethod
    def area(self):  # Abstract method
        pass


class Rectangle(Shape):  # Inheriting from Shape class
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):  # Implementing the abstract method
        return self.length * self.width

rect = Rectangle(10, 5)

print("Area of Rectangle:", rect.area())

# 10. Instance Methods
# Assignment:
# Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable for name
        self.breed = breed  # Instance variable for breed

    def bark(self): 
        print(f"{self.name} says: Woof! Woof!")

dog1 = Dog("Tommy", "Labrador")

dog1.bark()

# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0  # Class variable to track total books

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()  # Increment book count when a new book is added

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increase the total_books count

    @classmethod
    def display_total_books(cls):
        print("Total Books:", cls.total_books)

book1 = Book("Python Basics", "Amjad")
book2 = Book("Advanced Python", "Moona")
book3 = Book("Data Science with Python", "Azfar")

Book.display_total_books()

# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        # Celsius to Fahrenheit conversion formula
        return (c * 7/3) + 32

# Static method ko call karte hain
celsius = 30
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")

# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine is starting... Vroom Vroom!")

class Car:
    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine  # Composition: Car has an Engine

    def drive(self):
        print(f"Driving a {self.make} {self.model}")
        self.engine.start()  # Accessing Engine's method via Car

# Engine object banate hain
engine = Engine()

# Car object banate hain aur Engine object ko pass karte hain
car = Car("Toyota", "Corolla", engine)

# Car ka drive method call karte hain
car.drive()

# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}")


class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to Employee

    def display_department_info(self):
        print(f"Department: {self.dept_name}")
        self.employee.display_info()  # Accessing Employee's method

emp1 = Employee("Azfar", "Manager")

dept1 = Department("HR", emp1)

dept1.display_department_info()

# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        print("Showing from class A")

class B(A):
    def show(self):
        print("Showing from class B")

class C(A):
    def show(self):
        print("Showing from class C")

class D(B, C): 
    pass

obj = D()

obj.show()  

# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().

# Decorator function
def log_function_call(func):
    def wrapper():
        print("Function is being called")
        func()  # Calling the original function
    return wrapper

@log_function_call
def say_hello():
    print("Hello, World!")

say_hello()

# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

# Class decorator
def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    
    cls.greet = greet  # greet method ko class mein add kar diya
    return cls

# Person class par decorator apply kar rahe hain
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Moona")

print(p.greet())

# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Invalid price! Must be non-negative.")
        else:
            print("Setting price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

# Object banate hain
p = Product(100)

# Price ko get karte hain
print(p.price)

# Price ko set karte hain
p.price = 150

# Dobara get karte hain
print(p.price)

# Price ko delete karte hain
del p.price

# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor

# Object banate hain
double = Multiplier(2)

print(callable(double))  

result = double(5)
print(result)  

# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

# Custom Exception
class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18"):
        self.message = message
        super().__init__(self.message)

# Function to check age
def check_age(age):
    if age < 22:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print("Age is valid.")

# Try-Except block
try:
    check_age(20)
except InvalidAgeError as e:
    print("Caught an exception:", e)

# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

# Once you are done submit this form ASAP:    

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            value = self.current
            self.current -= 1
            return value

cd = Countdown(5)

for num in cd:
    print(num)






















