#Polymorphism is the ability of objects of different classes to respond to the same message in different ways.
#Polymorphism is a fundamental concept in object-oriented programming that allows objects of different types to be treated as if they have the same interface.
#In Python, polymorphism is implemented through method overloading and method overriding.


#Polymorphism types:
  # 1. Compile time polymorphism
  #  2. Run time polymorphism


# 1. Compile time polymorphism
 # c++, java, c# - compile time polymorphism

'''
c++ example:

Class SumCalculator {
public:
    int sum(int x, int y) {
        return x + y;
    }

    double sum(double x, double y) {
        return x + y;
    }

    int sum(int x, int y, int z) {
        return x + y + z;
    }
};

int main() {
    SumCalculator calculator;
    int result1 = calculator.sum(1, 2);
    double result2 = calculator.sum(1.5, 2.5);
    int result3 = calculator.sum(1, 2, 3);

    return 0;
}
'''

# Python does not support compile time polymorphism
# Python uses duck typing, which allows objects of different classes to be treated as if they have the same interface.
# This is achieved through method overloading and method overriding.

# class SumCalculator:
#     def sum(self, x, y):
#         print('Sum with 2 arguments')
#         return x + y

#     def sum(self, x, y, z):
#         print('Sum with 3 arguments')
#         return x + y + z
#     def sum(self, x ,y):
#         print('Sum with 3 arguments')
#         return x + y

# calculator = SumCalculator()

# result1 = calculator.sum(1, 2)
# result2 = calculator.sum(1.5, 2.5)
# result3 = calculator.sum(1, 2, 3)

# print(result1)  # Output: 3
# print(result2)  # Output: 4.0
# print(result3)  # Output: 6

# class SumCalculator:
#     def sum(self, x, y, z=None, *args, **kwargs):
#         if args:
#             print('Sum with variable number of arguments')
#             return sum(args)
#         elif z is not None:
#             print('Sum with 3 arguments')
#             return x + y + z
#         else:
#             print('Sum with 2 arguments')
#             return x + y

# calculator = SumCalculator()

# result1 = calculator.sum(1, 2)
# result2 = calculator.sum(1.5, 2.5)
# result3 = calculator.sum(1, 2, 3)
# result4 = calculator.sum(1, 2, 3, 4, 5,67,89)

# print(result1)  # Output: 3
# print(result2)  # Output: 4.0
# print(result3)  # Output: 6
# print(result4)  # Output: 6

# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
    

# # 1. Compile time polymorphism
# def animal_sound(animal):
#     return animal.make_sound()

# dog = Dog()
# cat = Cat()

# print(animal_sound(dog))  # Output: "Woof!"
# print(animal_sound(cat))  # Output: "Meow!"\


# # Duck typing

# class Duck:
#     def quack(self):
#         return "Quack!"

# class Chicken:
#     def quack(self):
#         return "Cluck!"
    

# 2.Run time polymorphism - method overriding

# class Animal:
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         return "Woof!"

# class Cat(Animal):
#     def make_sound(self):
#         return "Meow!"
    
# def animal_sound(animal):
#     return animal.make_sound()

# dog = Dog()
# cat = Cat()

# print(animal_sound(dog))  # Output: "Woof!"
# print(animal_sound(cat))  # Output: "Meow!"

