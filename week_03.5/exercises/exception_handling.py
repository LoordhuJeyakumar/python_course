#Exceptions and Error Handling

#Errors
    #compiler errors
        #Syntax Errors
        #Logical Errors
    #Exceptions
    #Runtime Errors

#syntex errors
    #Syntax Errors happen when you write Python code that violates the grammar rules of the Python language. It's like writing a sentence with incorrect grammar in English.
    #Syntax Errors are caught before your program even starts running, during the parsing (reading and understanding) phase.
    #Example: Forgetting a colon at the end of an `if` statement, misspelling a keyword, or incorrect indentation.

""" print("Hello World")
print("Hello World") """

#logical errors
    #Logical Errors happen when you write Python code that doesn't make sense. It's like writing a sentence that doesn't make sense in English.
    #Logical Errors are caught during the execution phase, when the program is running.
    #Example: Trying to divide by zero, accessing an index that doesn't exist, or calling a function with the wrong number of arguments.

""" numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print("Average:", average) # Output: Average: 3.0 """

#Exceptions

#Runtime Errors

#try...except
""" 
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
result = num1 / num2
print("Result:", result) """

""" try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ValueError as e:
    print("Invalid input. Please enter valid numbers.", e)
except Exception as e:
    print(f"An error occurred: {e}") """


#example

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

result_sum = number1 + number2

print("The sum of", number1, "and", number2, "is:", result_sum)

