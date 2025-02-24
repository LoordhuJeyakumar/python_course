# functions in python


def add_numbers(a, b):
    result = a + b
    return result
# return a + b

def subtract_numbers(a, b):
    result = a - b
    return result

def multiply_numbers(a, b):
    result = a * b
    return result



num1 = 5
num2 = 3

sum_result = add_numbers(num1, num2)
difference_result = subtract_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)

print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)

def say_goodbye():
    """This function prints a goodbye message."""
    print("Goodbye!")
    # No explicit return statement - implicitly returns None


say_goodbye() # Call say_goodbye function (no arguments needed)
return_value_goodbye = say_goodbye() # Call and capture return value (will be None)
print(f"Return value of say_goodbye(): {return_value_goodbye}") # Print the implicit None return value

def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(animal_type='hamster', pet_name='Harry') # Keyword arguments
describe_pet(pet_name='Lucy', animal_type='dog') # Order doesn't matter with keyword arguments

# Mixing positional and keyword arguments (positional first, then keyword)
describe_pet('cat', pet_name='Bella') # 'cat' is positional (animal_type), 'pet_name' is keyword
# describe_pet(animal_type='rabbit', 'Bunny') # SyntaxError: positional argument follows keyword argument (positional must come first if mixing)

##describe_pet(animal_type="cat","Bella")

#Scope of Variables
def scope_test():
    local_variable = 10  # Local variable
    print("Local x:", local_variable)

scope_test()


# Attempting to access a local variable outside its scope will raise an error
# print("Local x outside function:", local_variable)  # NameError: name 'local_variable' is not defined

# Global Variables
global_variable = 20  # Global variable

def access_global():
    print("Global x:", global_variable)

access_global()


# Modifying Global Variables
def modify_global():
    global global_variable  # Declare the variable as global within the function
    global_variable = 30  # Modify the global variable
    print("Modified Global x:", global_variable)

modify_global()

print("Global x after modification:", global_variable)  # The global variable has been modified


#LEGB Rule
#example

def outer_function():
    x = 10  # Local variable in outer_function

    def inner_function():
        y = 20  # Local variable in inner_function

        def nested_function():
            z = 30  # Local variable in nested_function
            print("Local variables:", x, y, z)

        nested_function()

    inner_function()

outer_function()


#Funtion Return Values
def add_numbers(a, b):
    result = a + b
    return result

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)


# Function with no return value
def say_hello():
    print("Hello!")

say_hello()

# Function with return value
def calculate_area(length, width):
    area = length * width
    return area

result = calculate_area(5, 3)


# Function with default arguments
def greet_user(name, greeting="Hello"): 
    print(f"{greeting}, {name}!")

greet_user("Alice")  # Uses default greeting "Hello"


# Function with variable number of arguments
def add_numbers(a,b,*args):
    total = 0
    for num in args:
        total += num
        
    total -= a + b
    return total

result = add_numbers(1, 2, 3, 4, 5)
print("Sum:", result)


# Function with keyword arguments
def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user(name="Alice", greeting="Hi")


# Function with arbitrary keyword arguments
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Alice", age=30, city="New York")

# Function with arbitrary keyword arguments and default values
def print_kwargs_with_defaults(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs_with_defaults(name="Alice", age=30)


# Function with positional and arbitrary keyword arguments
def print_args_and_kwargs(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args_and_kwargs(1, 2, 3, name="Alice", age=30)


# Function with arbitrary keyword arguments and default values
def print_kwargs_with_defaults(**kwargs ):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs_with_defaults(name="Alice", age=30)


