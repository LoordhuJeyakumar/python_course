# #abstraction

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     def perimeter(self):
#         pass
   

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# rect = Rectangle(5, 10) 
# print(rect.area())

# circ = Circle(3)
# print(circ.area())


#notification system

# from abc import ABC, abstractmethod

# class Notifier(ABC):
#     @abstractmethod
#     def send_notification(self, message):
#         pass

# class EmailNotifier(Notifier):
#     def send_notification(self, message):
#         print(f"Sending email: {message}")

# class SMSNotifier(Notifier):
#     def send_notification(self, message):
#         print(f"Sending SMS: {message}")

# email_notifier = EmailNotifier()
# sms_notifier = SMSNotifier()

# email_notifier.send_notification("Hello, world! This is an email.")
# sms_notifier.send_notification("Hello, world! This is an SMS.")

#Static method

# class MathOperations:
#     def __init__(self):
#         pass

#     @staticmethod
#     def add( a, b):
#         return a + b

#     @staticmethod
#     def subtract(a, b):
#         return a - b
    


# new_mathoperations = MathOperations()
# print(new_mathoperations.add(1, 2))
# print(MathOperations.add(5, 10))

# static variables

# class Student:
#     # static variable
#     total_students = 5
#     # class variable
#     school_name = "New School"

#     def __init__(self, name, age):
#         # instance variables
#         self.name = name
#         self.age = age

#         Student.total_students +=  1
    
    

# # stuent1 = Student("John", 20)
# # Student.total_students = 10
# # stuent2 = Student("Jane", 21)

# # print(Student.total_students)

# john = Student("John", 20)
# jane = Student("Jane", 21)

# print(john.school_name)
# print(jane.school_name)

#what happens if you try to initiate abstract class that has no implementation of abstract method

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     def perimeter(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# shape = Shape() # Error! Cannot create an instance of an abstract class Shape


# class Circle(Shape):    
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius
    

# rect = Rectangle(5, 10) 
# print(rect.area())

# circ = Circle(3)
# print(circ.area())