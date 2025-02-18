# input and output

# name = input("Enter your name: ")
# print("Hello", name)

# age = int(input("Enter your age: "))
# print("You are", age + 1, "years old")

# print() function

# """ print('''
# Hello World
#     #   welcome py
# ''')
#  """
# #escape 
# string = "Welcome to python \n hello world"

# print(string)

#f-string formatted string

name = "Rahul"
age = 20
print(f"Hello {name} your age is {age}")
#string formatting

name = "Rahul"
age = 20

print("Hello {} your age is {}".format(name, age))
print("Hello {1} your age is {0}".format(name, age))
print("Hello {name} your age is {age}".format(name = "Rahul", age = 20))

#string methods

string = "Hello world"

# print("Upper" , string.upper())
# print("Lower",string.lower())
# print("Capitalize", string.capitalize())

# print("Title", string.title())

# print("Count", string.count("l"))
# print("Find", string.find("d"))

# print("Replace", string.replace("l", "A"))
# print("Split", string.split(" "))

# print("Join", " ".join(string))

# print("Strip", string.strip())
# print("RStrip", string.rstrip())
# print("LStrip", string.lstrip())
# print("Center", string.center(20, "*"))
# print("LJust", string.ljust(20, "*"))
# print("RJust", string.rjust(20, "*"))

# string indexing
""" print(string[0])

print(string[-1])

# string slicing
print(string[0:5])
print(string[:5])
print(string[6:])
print(string[::2])  # string "Hello world"
print(string[::-1])
# string concatenation
string1 = "Hello"

text = "Hello"
# text[0] = 'J'  # This will cause an error! Strings are immutable.
new_text = 'J' + text[1:] # Create a new string by concatenation and slicing
print(new_text) # Output: Jello

repeated_str = "Python " * 3 # "PythonPythonPython"

print(repeated_str)
 """

message = "Hello World, Hello Python"
print(message.find("Hello"))    # 0 (first occurrence of "Hello" starts at index 0)
print(message.rfind("Hello"))   # 13 (last occurrence of "Hello" starts at index 13)
print(message.find("World"))    # 6
print(message.find("Java"))     # -1 (not found)
# print(message.index("Java"))  # ValueError: substring not found

new_message = message.replace("Hello", "Hi")
print(new_message) # Output: Hi World, Hi Python

replaced_once = message.replace("Hello", "Hi", 1) # Replace only the first occurrence
print(replaced_once) # Output: Hi World, Hello Python


greet = ' '

print(greet.isspace())

# numbers methods

num1 = 12.898

print("Round",round(num1,1))
print("Ceil", round(num1, 1))
print("Floor", round(num1, 2))

print("Abs", abs(-12.89))

print("Pow", pow(2, 3))

print("Max", max(2, 3))
print("Min", min(2, 3))

print("Sum", sum([2, 3]))

print("Divmod", divmod(10, 3)) # (3, 1) 10 // 3 = 3, 10 % 3 = 1
10 / 3

print("Bin", bin(10)) # 0b1010
print("Oct", oct(10)) # 0o12

print("Hex", hex(10)) # 0xa

print("Id", id(10)) # 140717245094400
print("Type", type(10)) # <class 'int'>
print("Isinstance", isinstance("10", int)) # True


#




