""" 1.  **Simple Calculation:** Write a program that calculates the sum, difference, product, and quotient of two numbers entered by the user. Print all the results with clear labels. """


""" 2.  **Area of a Triangle:** Write a program to calculate the area of a triangle. Take the base and height as input from the user (you can assume they are integers or floats).  Area of triangle = (1/2) * base * height. """

""" 3.  **Temperature Conversion:** Write a program to convert temperature from Celsius to Fahrenheit. Take the temperature in Celsius as input. Formula: Fahrenheit = (Celsius * 9/5) + 32. """



""" 4.  **Swap Variables:** Write a program to swap the values of two variables without using a temporary variable. (Hint: You can use simultaneous assignment in Python). """



""" 5.  **Circle Properties:** Write a program to calculate the circumference and area of a circle given its radius. Use `pi = 3.14159`.  Circumference = 2 * pi * radius, Area = pi * radius * radius. """

   


# variables

#variable declaration

_name = "john"
_age = 10
name_0014 = "john"


#direct variable declaration
age = 10
name = "John"


#indirect variable declaration
age = 10
name = "John"

#type conversion




#type casting examples

""" num_str = "123"
num_int = int(num_str)  
print(num_int)  # Output: 123

num_float = float(num_int)
print(num_float)  # Output: 123.0

str_num = str(num_float)
print(str_num)  # Output: "123.0"

bool_val = bool(1)
print(bool_val)  # Output: False """



# operators

""" #arithmetic operators

num1 = 13
num2 = 5
result = num1 + num2
print("Addition:",result)  # Output: 15

result = num1 - num2
print("Subtraction:",result)  # Output: 8

result = num1 * num2
print("Multiplication:",result)  # Output: 65

result = num1 / num2
print("Division:",result)  # Output: 2.6

result = num1 // num2
print("Floor Division:",result)  # Output: 2

result = num1 % num2
print("Modulus:",result)  # Output: 3

result = num1 ** num2
print("Exponentiation:",result)  # Output: 78125 """


""" #assignment operators

x = 10
x += 5
print(x)  # Output: 15

x -= 3
print(x)  # Output: 12

x *= 2
print(x)  # Output: 24

x /= 4
print(x)  # Output: 3.0

x **= 2
print(x)  # Output: 96

x %= 7
print(x)  # Output: 3 """



""" #comparison operators

num1 = 10
num2 = 5

result = num1 == num2
print("num1 == num2:",result)  # Output: False

result = num1 != num2
print("num1 != num2:",result)  # Output: True

result = num1 > num2
print("num1 > num2:",result)  # Output: True

result = num1 < num2
print("num1 < num2:",result)  # Output: False

result = num1 >= num2
print("num1 >= num2:",result)  # Output: True

result = num1 <= num2
print("num1 <= num2:",result)  # Output: False """



""" #logical operators

num1 = 10
num2 = 5

result = num1 > 5 and num2 < 10
print("num1 > 5 and num2 < 10:",result)  # Output: True

result = num1 > 15 or num2 < 1
print("num1 > 15 or num2 < 10:",result)  # Output: True

result = not num1 > 5
print("not num1 > 5:",result)  # Output: False

data = True

if not data:
    print("Data is not found")
else:
    print("Data is True")
 """


""" # Operator precedence

result = 2 + 3 * 4
print(result)  # Output: 14

result = (2 + 3) * 4
print(result)  # Output: 20

 """

#geting input from user

#input function

#input function always returns a string

num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")

num1 = float(num1_str) # Use float to handle decimal input
num2 = float(num2_str)  
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2
print(f"Sum: {num1} + {num2} = {sum_result}")
print(f"Difference: {num1} - {num2} = {difference_result}")
print(f"Product: {num1} * {num2} = {product_result}")
print(f"Quotient: {num1} / {num2} = {quotient_result}")
# without f string
print("Sum:", num1, "+", num2, "=", sum_result)
