# Encapsulation
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Encapsulated with double underscores to make it private
        self.__model = model
        self.__year = year

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year


# Create a Car object
my_car = Car("Toyota", "Camry", 2022)

# Accessing attributes using methods (encapsulation)
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# Accessing attributes directly (not recommended)
print("Make:", my_car._Car__make)
print("Model:", my_car._Car__model)
print("Year:", my_car._Car__year)

"""
    Accessing attributes directly in object-oriented programming is generally not recommended because it violates the principle of encapsulation. Encapsulation is one of the fundamental concepts in object-oriented programming that promotes data hiding and abstraction.
    When you access attributes directly, you bypass any encapsulation mechanisms that the class may have in place. This means that you can directly modify or retrieve the attribute's value without any restrictions or validation. This can lead to several issues:

1. Lack of Data Validation: By accessing attributes directly, you bypass any validation or checks that the class may have implemented. This can result in inconsistent or invalid data being stored in the attribute.

2. Breaking Encapsulation: Encapsulation is important for maintaining the integrity of an object's internal state. By accessing attributes directly, you expose the internal implementation details of the class, making it harder to change or modify the class in the future without affecting other parts of the code.

3. Inability to Enforce Business Logic: Classes often have business logic associated with their attributes. By accessing attributes directly, you bypass this logic, which can lead to unexpected behavior or inconsistencies in the application.

To overcome these issues, it is recommended to use getter and setter methods (or properties in some languages) to access and modify the attributes of an object. These methods provide a controlled interface to interact with the object's attributes, allowing for data validation, encapsulation, and enforcing business logic.
"""


# Example of using getter and setter methods to encapsulate attributes in Python:
class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


person = Person("John")
print(person.get_name())  # Output: John

person.set_name("Jane")
print(person.get_name())  # Output: Jane

"""In this example, we have a `Person` class with a private attribute `_name`. Instead of directly accessing `_name`, we provide getter and setter methods (`get_name()` and `set_name()`) to interact with the attribute. This way, we can control how the attribute is accessed and modified, ensuring data integrity and encapsulation."""


# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Create instances of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak() method for each animal
print(dog.name + " says:", dog.speak())
print(cat.name + " says:", cat.speak())


"""
    In this example, we have an `Animal` class with an abstract method `speak()`. This method is meant to be overridden by subclasses, so it raises a `NotImplementedError` to indicate that it should be implemented by the subclass.
"""


# Polymorphism
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


# Create instances of Rectangle and Circle
rectangle = Rectangle(5, 4)
circle = Circle(3)

# Calculate the area of each shape
print("Area of Rectangle:", rectangle.area())
print("Area of Circle:", circle.area())

"""
In this example, we have a `Shape` class with an abstract method `area()`. We then have two subclasses, `Rectangle` and `Circle`, each of which implements the `area()` method to calculate the area of the corresponding shape. When we call the `area()` method on each shape, the appropriate implementation is invoked based on the type of the object, demonstrating polymorphism.
"""


# Classes and Objects
class ClassName:
    # Class attributes and methods go here
    pass


class Car:
    # Class attribute
    color = "red"

    # Class method
    def drive(self):
        print("The car is driving.")


object_name = ClassName()

# Create an instance of the Car class
my_car = Car()

# Accessing object attributes
print(my_car.color)

# Calling object methods
my_car.drive()

"""
        In this example, we define a `Car` class with a class attribute `color` and a class method `drive()`. We then create an instance of the `Car` class using the syntax `my_car = Car()`. We can access the class attribute and call the class method using the instance `my_car`.
"""

# Demonstrate how to define a class and create objects from it using the class and __init__ method


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating objects (instances) of the Person class
person1 = Person("John", 30)
person2 = Person("Alice", 25)

# Accessing object attributes
print("Person 1:")
print("Name:", person1.name)
print("Age:", person1.age)

print("\nPerson 2:")
print("Name:", person2.name)
print("Age:", person2.age)
