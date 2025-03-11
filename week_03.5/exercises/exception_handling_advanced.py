#Exception Handling Advanced

#else block in exception handling


#syntax 
# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code to execute if no exception occurs

""" result = None

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("The result is:", result)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:   
    print("Cannot divide by zero!")
else:
    print("The result is:", result) 
 """

# try:
#     a = 10
#     b = int(input("Enter a number: "))  # May raise ValueError
#     c = a / b  # May raise ZeroDivisionError
# except ValueError:
#     print("Invalid input! Cannot convert to integer.")
#     # `a` is accessible here, but `c` may not exist if exception occurs before its assignment.
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# else:
#     print(f"The result is {c}")  # Accessing 'c' from the try block
#     d = c * 2  # 'd' is defined in else and is accessible only within else


#finally block in exception handling

#syntax
# try:
#     # Code that might raise an exception
# except ExceptionType:
#     # Code to handle the exception
# else:
#     # Code to execute if no exception occurs
# finally:
#     # Code to execute regardless of whether an exception occurred or not

""" 

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("The result is:", result)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:   
    print("Cannot divide by zero!")
else:
    print("The result is:", result)
finally:
    print("Executing finally block.") """


# filename = "numbers.txt"

# try: # Outer try block: for file operations
#     with open(filename, 'r') as file:
#         for line in file:
#             try: # Inner try block: for number processing
#                 number = int(line.strip()) # Convert line to integer (ValueError possible)
#                 reciprocal = 1 / number    # Calculate reciprocal (ZeroDivisionError possible)
#                 print(f"Reciprocal of {number} is: {reciprocal}")
#             except ValueError: # Inner except for ValueError (invalid number format in file)
#                 print(f"Warning: Invalid number format in line: '{line.strip()}'")
#             except ZeroDivisionError: # Inner except for ZeroDivisionError (number is zero)
#                 print(f"Warning: Cannot calculate reciprocal of zero in line: '{line.strip()}'")
#             except Exception as inner_error: # Catch-all for any other error in number processing
#                 print(f"Unexpected error processing line '{line.strip()}': {inner_error}")
# except FileNotFoundError: # Outer except for FileNotFoundError
#     print(f"Error: File '{filename}' not found.")
# except Exception as outer_error: # Catch-all for any other file operation error
#     print(f"General file error: {outer_error}")
# else:
#     print("File processing successfully opened.")



# print("File processing finished (with error handling).")


# The raise Statement

#syntax
# raise ExceptionType("Error message")

import datetime

def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future.") # Raise ValueError for invalid input
    if birth_year < 1900: # Let's say we consider years before 1900 invalid too
        raise ValueError("Birth year seems too early.")

    age = current_year - birth_year
    return age

# Example usage:
try:
    year = int(input("Enter your birth year: "))
    age = calculate_age(year)
    print("Your age is:", age)
except ValueError as e: # Catch the ValueError raised by calculate_age or int()
    print("Error:", e) # Print the error message from the exception