
# 1.

#     - Define Class
        # A class serves as a blue print or template for creating an object which can contain variables that store data about the object and methods that describe it

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Hi im', self.name,)

#     - Define Instance
        # When we make an object from a class we are creating an instantiation from that class template, called an instance.

first_animal = Animal('Tom')
first_animal = Animal('Joe')

# #     - Define Inheritence
# Inheritence allows us to define classes that can pass down its properties like variables and methods so that another class and inherit and use them

class Dog(Animal):
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name

dog_one = Animal('Rex')
dog_one.get_name()

#     - Define Composition
# this is a process that lets us combine classes of different objects to create complex types
# a composite class uses the class of another object while a component class is the class being used to create an instance in another class

# Class A 
# |
# V
# instance = class_B()

#     - Define Polymorphism

# In programming this refers to something having many forms such as a method, operator, or object to respresent different things in different situations as needed

x = "abc"
y = "xyz"

print(x+y)

x = "1234"
y = "5678"

print(x+y)


# 2.

#     - Define Encapsulation
# Encapsulation - describes the idea of wrapping up a bunch of things into a single unit, a class is an example of this containing all of its variables and methods into one entity

class Animal:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Hi im', self.name,)

#     - Define Subclass
# Subclass - subclass or a child class extends a parent class to create a new object, like in the example the Dog class extends the Animal class and inherits all of its variables and methods. The dog class being the subclass of Animal (or child class), Animal being the parent class

class Dog(Animal):
    def __init__(self, name):
        super().__init__(self, name)
        self.name = name

dog_one = Animal('Rex')
dog_one.get_name()

#     - Define Superclass
# Superclass - is what allows us to class down the variables to the child class and even override the pervious values 
# def __init__(self, name):
#         super().__init__(self, name)

#     - Define Method Overloading
# Method Overloading - allows us to change the previous entity and change it to meet our new need. For example if Dog inherited a get_name method from Animal. But in the new Dog class we update the way our get_name works

# def get_name(self):
#     print('Hi im', self.name,)

# def get_name(self):
#     print('Hi im a Dog', self.name,)

#     - Define Method Overriding

# Method Overriding