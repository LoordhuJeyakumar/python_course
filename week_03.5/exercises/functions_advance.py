#functions Advance

#default arguments

# def calculate_area(length, width, height=1):
#     area = length * width * height
#     return area


# area = calculate_area(10,20)
# print(area)

# keyword arguments

# def describe_product(name, price, category="Electronics"):
#     print(f"Name: {name}")
#     print(f"Price: {price}")
#     print(f"Category: {category}")


# describe_product("Laptop", 1000)

# describe_product("Mobile", 500, "Electronics")

# def describe_person(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# describe_person(name="Alice", age=30, city="New York") # Using keyword arguments
# describe_person(age=25, city="London", name="Bob")   # Order doesn't matter with keywords
# describe_person("Charlie", city="Paris", age=35)   # Mixing positional and keyword (positional first)

# variable length arguments
# def calculate_average(*args):
#     print(args)
#     total = sum(args)
#     average = total / len(args)
#     return average


# average = calculate_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(average)

# variable keyword arguments

# def describe_car(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# describe_car(make="Toyota", model="Camry", year=2022, color="Blue", top_speed=200)

# forwarding arguments

# def forward_arguments(func, *args, **kwargs):
#     return func(*args, **kwargs)

# def print_args_and_kwargs(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# result = forward_arguments(print_args_and_kwargs, 1, 2, 3, name="Alice", age=30)
# print(result)


# lambda functions

# square = lambda x: x * x
# add = lambda x, y: x + y

# Function Annotations

# def add(x: int, y: int) -> int:
#      return x + y


# result = add(1, 2)
# print(result)
# result2 = add(1.5, 2.5)
# print(result2)

# Decorators

# import time

# start_time = time.time()

# def decorator_function(func):
#     def wrapper_function(*args, **kwargs):
#         print("Before function execution")
#         #taken time
#         print(
#             f"Function {func.__name__} took {time.time() - start_time} seconds to execute"
#         )
#         result = func(*args, **kwargs)
#         print("After function execution")
#         return result
#     return wrapper_function

# @decorator_function
# def calculate_area(length, width):
#     area = length * width
#     return area

# area = calculate_area(10, 20)
# print(area)


# def simple_logger(func): # 1. Decorator function takes a function 'func' as argument
#     def wrapper(*args, **kwargs): # 2. Define a wrapper function, *args and **kwargs to accept any arguments
#         print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}") # Action before function call
#         result = func(*args, **kwargs) # 3. Call the original function
#         print(f"Function {func.__name__} returned: {result}") # Action after function call
#         return result # 4. Return the result of the original function
#     return wrapper # 5. Decorator returns the wrapper function

# @simple_logger # Apply the decorator to 'add_numbers' function
# def add_numbers(x, y):
#     return x + y

# output = add_numbers(5, 3) # Calling the decorated function
# output_1 = add_numbers(10, 20)
# output_2 = add_numbers(30, 40)
# print(f"Final result: {output}")


# def custom_logger(log_message): # 1. Decorator factory, takes 'log_message' as argument
#     def decorator(func): # 2. Decorator function (returned by factory), takes 'func'
#         def wrapper(*args, **kwargs): # 3. Wrapper function
#             print(f"LOG: {log_message} - Calling function: {func.__name__}") # Custom log message
#             result = func(*args, **kwargs)
#             return result
#         return wrapper # 4. Decorator returns wrapper
#     return decorator # 5. Decorator factory returns decorator

# @custom_logger("Function execution started") # Call decorator factory with argument
# def process_data(data):
#     print(f"Processing data: {data}")
#     return len(data)

# output = process_data("example data")
# print(f"Result length: {output}")


# chaining decorators

# def uppercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# def lowercase_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.lower()
#     return wrapper

# @lowercase_decorator
# @uppercase_decorator
# def greet(name):
#     return f"Hello, {name}!"

# output = greet("Alice")
# print(output)

# import time

# def timer(func): # Timer decorator (simple version)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
#         return result
#     return wrapper

# def simple_logger(func): # (Defined earlier)
#     # ... (same simple_logger decorator as before) ...
#     def wrapper(*args, **kwargs):
#         print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Function {func.__name__} returned: {result}")
#         return result
#     return wrapper


# @timer          # Applied second (outermost)
# @simple_logger  # Applied first (innermost)
# def calculate_sum(numbers):
#     time.sleep(2) # Simulate some work
#     return sum(numbers)

# result = calculate_sum([1, 2, 3, 4, 5])
# print(f"Final sum: {result}")

