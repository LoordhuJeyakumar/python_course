# Day 5: Functions - Part 2 (Advanced), Decorators, and Unit Testing - Study Material & Notes

## 1. Quick Recap: Functions - Part 1 (Basics)

Let's quickly refresh our memory about the fundamental concepts of functions we covered in Week 2.

*   **Defining Functions:** We use the `def` keyword to define a function, followed by the function name, parentheses `()`, and a colon `:`.

    ```python
    def greet(name):
        print(f"Hello, {name}!")
    ```

*   **Function Arguments (Positional):**  Functions can take input values called arguments. In the example above, `name` is a positional argument. When you call the function, you provide values in the order they are defined:

    ```python
    greet("Alice")  # "Alice" is passed as the argument for 'name'
    ```

*   **Return Values:** Functions can return a value using the `return` statement. If a function doesn't have a `return` statement, it implicitly returns `None`.

    ```python
    def add(a, b):
        return a + b

    result = add(5, 3) # result will be 8
    ```

*   **Scope (Local vs. Global):** Variables defined inside a function have local scope (accessible only within the function). Variables defined outside functions have global scope (accessible throughout the script).

    ```python
    global_var = 10

    def my_function():
        local_var = 5
        print(global_var) # Accessing global variable is okay
        print(local_var)  # Accessing local variable

    my_function()
    # print(local_var) # This would cause an error (NameError) - local_var is not accessible here
    ```

Today, we're expanding on these basics to explore more powerful and flexible features of functions in Python.

## 2. Functions - Part 2: Advanced Features

### 2.1. Default Argument Values

*   **Concept:** You can provide **default values** for function parameters in the function definition. If you call the function without providing a value for a parameter that has a default value, the default value will be used automatically.

*   **Syntax:**

    ```python
    def function_name(param1, param2=default_value, param3=another_default_value):
        # Function body
        ...
    ```

    *   Parameters with default values must come **after** parameters without default values in the function definition.

*   **Example:**

    ```python
    def power(base, exponent=2): # 'exponent' has a default value of 2
        return base ** exponent

    result1 = power(5)     # exponent is not provided, so default value 2 is used: 5**2 = 25
    result2 = power(3, 3)  # exponent is provided as 3: 3**3 = 27
    print(result1) # Output: 25
    print(result2) # Output: 27
    ```

*   **Use Cases:**
    *   **Making Arguments Optional:** Default values make arguments optional. Users can call the function with fewer arguments, using the defaults for the rest.
    *   **Providing Common Defaults:** Set sensible default values for parameters that are frequently used with the same value, reducing the need to specify them every time.
    *   **Simplifying Function Calls:** For functions with many parameters, default values can simplify common use cases by reducing the number of arguments users need to provide.

### 2.2. Keyword Arguments

*   **Concept:** When calling a function, you can provide arguments using **keywords** (parameter names) instead of just their position.

*   **Syntax:**

    ```python
    function_name(param1=value1, param2=value2, param3=value3)
    ```

*   **Example:**

    ```python
    def describe_person(name, age, city):
        print(f"Name: {name}, Age: {age}, City: {city}")

    describe_person(name="Alice", age=30, city="New York") # Using keyword arguments
    describe_person(age=25, city="London", name="Bob")   # Order doesn't matter with keywords
    describe_person("Charlie", city="Paris", age=35)   # Mixing positional and keyword (positional first)
    ```

*   **Benefits of Keyword Arguments:**
    *   **Readability:** Function calls become more self-documenting and easier to understand because you explicitly name the parameters being assigned values.
    *   **Order Independence:** You can pass arguments in any order when using keywords, as long as you specify the correct parameter names.
    *   **Selective Argument Passing:** You can choose to provide values only for specific parameters by name, especially useful for functions with many optional parameters (those with default values).

*   **Mixing Positional and Keyword Arguments:**
    *   You can mix positional and keyword arguments in a function call, but positional arguments must come **first**, followed by keyword arguments.
    *   Once you use a keyword argument, all subsequent arguments must also be keyword arguments.

    ```python
    def example_function(a, b, c, d=4, e=5):
        print(f"a={a}, b={b}, c={c}, d={d}, e={e}")

    example_function(1, 2, 3, e=10) # Valid: positional a, b, c, keyword e, default d
    # example_function(1, 2, d=40, 3) # Invalid: positional argument after keyword argument
    ```

### 2.3. Variable-Length Arguments (`*args` and `**kwargs`)

*   **Concept:** Python provides special syntax to handle situations where you want to pass a **variable number of arguments** to a function, without knowing in advance how many arguments will be passed.

*   **`*args` (Variable Positional Arguments):**
    *   Used to pass a **non-keyword, variable-length argument list** to a function.
    *   In the function definition, `*args` is written as a parameter name prefixed with a single asterisk `*`.
    *   Inside the function, `args` becomes a **tuple** containing all the positional arguments passed to the function beyond the explicitly defined parameters.

    ```python
    def sum_all(*args): # *args collects variable positional arguments into a tuple called 'args'
        total = 0
        for num in args:
            total += num
        return total

    result1 = sum_all(1, 2, 3)       # args will be (1, 2, 3)
    result2 = sum_all(10, 20, 30, 40) # args will be (10, 20, 30, 40)
    result3 = sum_all()            # args will be an empty tuple ()
    print(result1) # Output: 6
    print(result2) # Output: 100
    print(result3) # Output: 0
    ```

*   **`**kwargs` (Variable Keyword Arguments):**
    *   Used to pass a **keyword, variable-length argument dictionary** to a function.
    *   In the function definition, `**kwargs` is written as a parameter name prefixed with a double asterisk `**`.
    *   Inside the function, `kwargs` becomes a **dictionary** where the keys are the keyword argument names (strings) and the values are the corresponding argument values.

    ```python
    def process_data(**kwargs): # **kwargs collects variable keyword arguments into a dictionary 'kwargs'
        for key, value in kwargs.items():
            print(f"Parameter: {key}, Value: {value}")

    process_data(name="Alice", age=30, city="New York") # kwargs will be {'name': 'Alice', 'age': 30, 'city': 'New York'}
    process_data(item="book", price=25.0, quantity=2)    # kwargs will be {'item': 'book', 'price': 25.0, 'quantity': 2}
    process_data() # kwargs will be an empty dictionary {}
    ```

*   **Use Cases for `*args` and `**kwargs`:**
    *   **Flexible Function Design:** When you want to create functions that can accept a varying number of inputs without having to define a fixed number of parameters in advance.
    *   **Wrapper Functions:**  `*args` and `**kwargs` are very useful when creating wrapper functions or decorators (which we'll learn about next) because they allow you to pass any number of arguments to the wrapped function without knowing their specific names or count.
    *   **Forwarding Arguments:** In some cases, you might want to create a function that takes some arguments and then forwards the remaining arguments to another function. `*args` and `**kwargs` make this easy.

### 2.4. Lambda Functions (Anonymous Functions)

*   **Concept:** **Lambda functions** (also called anonymous functions) are small, single-expression functions that can be defined without a name using the `lambda` keyword.

*   **Syntax:**

    ```python
    lambda arguments: expression
    ```

    *   `lambda`: Keyword to define a lambda function.
    *   `arguments`: Comma-separated list of input arguments (like parameters in a regular function).
    *   `: `: Separator between arguments and the expression.
    *   `expression`: A single expression that is evaluated and returned as the result of the lambda function. **Lambda functions can only contain a single expression, not statements.**

*   **Example:**

    ```python
    square = lambda x: x * x # Lambda function to square a number
    add = lambda x, y: x + y # Lambda function to add two numbers

    print(square(5))   # Output: 25
    print(add(3, 7))    # Output: 10
    ```

*   **Use Cases for Lambda Functions:**
    *   **Short, Simple Operations:** Lambda functions are best suited for defining very short, simple functions that perform a single operation.
    *   **As Arguments to Higher-Order Functions:** Lambda functions are frequently used as arguments to higher-order functions like `map()`, `filter()`, `sorted()`, and in GUI event handlers (though we're not diving deep into these today, just illustrating use cases). These functions expect a function as an argument, and lambda functions provide a concise way to define these functions inline.

    ```python
    numbers = [1, 2, 3, 4, 5]
    squared_numbers = list(map(lambda x: x**2, numbers)) # Using lambda with map() to square each number
    print(squared_numbers) # Output: [1, 4, 9, 16, 25]

    even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Using lambda with filter() to get even numbers
    print(even_numbers) # Output: [2, 4]

    points = [(1, 5), (3, 2), (2, 8)]
    sorted_points_by_y = sorted(points, key=lambda point: point[1]) # Sort points based on y-coordinate using lambda as key
    print(sorted_points_by_y) # Output: [(3, 2), (1, 5), (2, 8)]
    ```

*   **Limitations of Lambda Functions:**
    *   **Single Expression:** Lambda functions can only contain a single expression. They cannot contain statements (like `if`, `for`, `while`, `print`, assignments, etc.).
    *   **Anonymity:** Lambda functions are anonymous, meaning they don't have a name unless you explicitly assign them to a variable (like `square = lambda x: x*x`). For more complex or reusable functions, it's better to use regular `def` functions with names.

### 2.5. Function Annotations (Type Hints - Brief Introduction)

*   **Concept:** **Function annotations** (or type hints) are a way to add **metadata** to function parameters and return values to indicate their expected data types. They are written in the function definition syntax.

*   **Syntax:**

    ```python
    def function_name(param1: type, param2: type) -> return_type:
        # Function body
        ...
    ```

    *   `: type` after a parameter name indicates the expected type of that parameter.
    *   `-> return_type` after the parameter list indicates the expected type of the return value.

*   **Example:**

    ```python
    def greet_person(name: str, age: int) -> str: # Type hints for parameters and return type
        return f"Hello, {name}! You are {age} years old."

    message = greet_person("Alice", 30) # Arguments match the type hints
    print(message)

    # greet_person(123, "Bob") # This will run, but type checkers would flag it (argument types don't match hints)
    ```

*   **Purpose of Type Hints:**
    *   **Documentation:** Type hints make function signatures more informative and easier to understand by explicitly stating the expected types of inputs and outputs.
    *   **Readability:** Improve code readability by making type expectations clear.
    *   **Static Analysis (Type Checkers):** Type hints enable static type checkers (like `mypy`) to analyze your code *before* runtime and catch potential type errors. This can help prevent bugs early in development.
    *   **Not Enforced at Runtime (by default in standard Python):**  **Important:** Python's standard interpreter does **not** enforce type hints at runtime. If you pass arguments of the wrong type, the code will still run (unless there's a type-related error within the function logic itself). Type hints are primarily for static analysis and documentation, not runtime type checking in standard Python. (There are libraries like `pydantic` or runtime type checking tools that can enforce types at runtime if needed).

*   **Tools like `mypy` for Static Type Checking:**
    *   `mypy` is a popular static type checker for Python. You can install it using `pip install mypy`.
    *   After adding type hints to your code, you can run `mypy your_script.py` from the command line to check for type errors. `mypy` will analyze your code and report any type inconsistencies based on your annotations.

    ```bash
    # Example using mypy (after installing it)
    # mypy your_script_with_type_hints.py
    ```

    Type hints and static type checking are becoming increasingly important in larger Python projects to improve code quality and maintainability.

## 3. Decorators: Enhancing Functions

### 3.1. What are Decorators?

*   **Decorators in Python** are a powerful and elegant way to **modify or enhance the behavior of functions or methods** in a reusable manner. They are a form of metaprogramming, allowing you to write code that manipulates or extends other code.

*   **Decorators as Wrappers:**  Think of a decorator as a "wrapper" around a function. It allows you to add extra functionality (like logging, timing, access control, etc.) to a function **without directly modifying the original function's code**.

*   **Motivation for Decorators:**
    *   **Code Reusability:**  Decorators promote code reuse. You can define a decorator once and apply it to multiple functions to add the same functionality to all of them.
    *   **Separation of Concerns:** Decorators help separate concerns. You can keep the core logic of your functions clean and focused on their primary task, while decorator functions handle auxiliary tasks like logging or security.
    *   **Adding Functionality Non-Intrusively:** Decorators allow you to add functionality to existing functions without altering their internal code. This is especially useful when you are working with code you don't want to or cannot directly modify (e.g., code from a library).

*   **Common Use Cases for Decorators:**
    *   **Logging:**  Decorators can automatically log function calls, arguments, and return values.
    *   **Timing Execution:** Measure the execution time of functions.
    *   **Access Control/Authentication:** Implement security checks to control who can access certain functions.
    *   **Input Validation:** Validate function arguments before the function's main logic is executed.
    *   **Memoization:** Cache results of expensive function calls to improve performance.
    *   **Function Registration:** Register functions with a framework or system.

### 3.2. Basic Decorator Syntax

*   **`@decorator_name` Syntax:** To apply a decorator to a function, you use the `@` symbol followed by the decorator function's name, placed immediately above the function definition you want to decorate.

    ```python
    @decorator_function_name
    def my_function():
        # Function code
        ...
    ```

*   **How Decorators are Applied and Executed:**
    When you use the `@decorator_name` syntax, Python essentially does the following behind the scenes:

    ```python
    def my_function():
        # ... function code ...

    my_function = decorator_function_name(my_function) # Decorator applied
    ```

    It calls the `decorator_function_name` with `my_function` as an argument, and then reassigns the result back to the name `my_function`.  The decorator function is expected to return a modified version of the original function (usually a wrapper function).

### 3.3. Creating Simple Decorators

*   **Decorator Function Structure:** A decorator is typically implemented as a function that:
    1.  **Takes a function as an argument** (let's call it `func`). This is the function you want to decorate.
    2.  **Defines a wrapper function** (inside the decorator function). This wrapper function is what will replace the original function.
    3.  **The wrapper function** usually:
        *   Does something *before* calling the original function (`func`). (e.g., logging, timing start).
        *   Calls the original function (`func(*args, **kwargs)`) – important to use `*args` and `**kwargs` to handle any arguments the original function might take.
        *   Does something *after* the original function call (e.g., logging return value, timing end).
        *   **Returns the result** of the original function call.
    4.  **The decorator function returns the wrapper function.**

*   **Example: Simple Logging Decorator:**

    ```python
    def simple_logger(func): # 1. Decorator function takes a function 'func' as argument
        def wrapper(*args, **kwargs): # 2. Define a wrapper function, *args and **kwargs to accept any arguments
            print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}") # Action before function call
            result = func(*args, **kwargs) # 3. Call the original function
            print(f"Function {func.__name__} returned: {result}") # Action after function call
            return result # 4. Return the result of the original function
        return wrapper # 5. Decorator returns the wrapper function

    @simple_logger # Apply the decorator to 'add_numbers' function
    def add_numbers(x, y):
        return x + y

    output = add_numbers(5, 3) # Calling the decorated function
    print(f"Final result: {output}")
    ```

    **Output:**

    ```
    Calling function: add_numbers with arguments: (5, 3), {}
    Function add_numbers returned: 8
    Final result: 8
    ```

    **Explanation:**
    *   `simple_logger` is our decorator function. It takes the function `add_numbers` as input (`func`).
    *   Inside `simple_logger`, `wrapper` is defined. This is the function that will replace `add_numbers` after decoration.
    *   `wrapper` logs the function call, calls the original `func` (using `*args, **kwargs` to pass any arguments), logs the return value, and then returns the result.
    *   `@simple_logger` above `add_numbers` applies the decorator. Now, when you call `add_numbers(5, 3)`, you are actually calling the `wrapper` function returned by `simple_logger(add_numbers)`.

### 3.4. Decorators with Arguments (Parameterized Decorators)

*   **Concept:** Sometimes, you might want to create decorators that can be configured or customized by passing arguments to the decorator itself. These are called **parameterized decorators**.

*   **Decorator Factory:** To create a decorator that takes arguments, you need to create a **decorator factory**. A decorator factory is a function that:
    1.  **Takes arguments** that configure the decorator's behavior.
    2.  **Returns the actual decorator function.**  The decorator function it returns will then follow the structure of a simple decorator (take a function as input, define a wrapper, return the wrapper).

*   **Example: Parameterized Logging Decorator (Custom Log Message):**

    ```python
    def custom_logger(log_message): # 1. Decorator factory, takes 'log_message' as argument
        def decorator(func): # 2. Decorator function (returned by factory), takes 'func'
            def wrapper(*args, **kwargs): # 3. Wrapper function
                print(f"LOG: {log_message} - Calling function: {func.__name__}") # Custom log message
                result = func(*args, **kwargs)
                return result
            return wrapper # 4. Decorator returns wrapper
        return decorator # 5. Decorator factory returns decorator

    @custom_logger("Function execution started") # Call decorator factory with argument
    def process_data(data):
        print(f"Processing data: {data}")
        return len(data)

    output = process_data("example data")
    print(f"Result length: {output}")
    ```

    **Output:**

    ```
    LOG: Function execution started - Calling function: process_data
    Processing data: example data
    Result length: 12
    ```

    **Explanation:**
    *   `custom_logger(log_message)` is the decorator factory. It takes `log_message` as an argument.
    *   Inside `custom_logger`, `decorator(func)` is the actual decorator function. It's defined and returned by `custom_logger`.
    *   When you use `@custom_logger("Function execution started")`, you are first calling `custom_logger("Function execution started")`, which returns the `decorator` function. Then, this returned `decorator` function is applied to `process_data`.

### 3.5. Chaining Decorators

*   **Concept:** You can apply **multiple decorators** to a single function. This is called decorator chaining. Decorators are applied in the order they are listed, from **bottom to top**.

*   **Example: Chaining `@simple_logger` and a `@timer` decorator (assume `simple_logger` is defined as before, and we define a `timer` decorator):**

    ```python
    import time

    def timer(func): # Timer decorator (simple version)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
            return result
        return wrapper

    def simple_logger(func): # (Defined earlier)
        # ... (same simple_logger decorator as before) ...
        def wrapper(*args, **kwargs):
            print(f"Calling function: {func.__name__} with arguments: {args}, {kwargs}")
            result = func(*args, **kwargs)
            print(f"Function {func.__name__} returned: {result}")
            return result
        return wrapper


    @timer          # Applied second (outermost)
    @simple_logger  # Applied first (innermost)
    def calculate_sum(numbers):
        time.sleep(1) # Simulate some work
        return sum(numbers)

    result = calculate_sum([1, 2, 3, 4, 5])
    print(f"Final sum: {result}")
    ```

    **Output:**

    ```
    Calling function: calculate_sum with arguments: ([1, 2, 3, 4, 5],), {}
    Function calculate_sum returned: 15
    Function 'calculate_sum' executed in 1.0012 seconds
    Final sum: 15
    ```

    **Order of Execution:**
    1.  `@simple_logger` is applied first (innermost). So, `calculate_sum` is first decorated with `simple_logger`.
    2.  Then, `@timer` is applied (outermost) to the *already decorated* function from step 1.
    3.  When you call `calculate_sum`, you are actually calling the `wrapper` of `timer`, which in turn calls the `wrapper` of `simple_logger`, which finally calls the original `calculate_sum` function.

## 4. Unit Testing: Ensuring Code Quality

### 4.1. Introduction to Unit Testing

*   **What is Unit Testing?**
    *   **Unit testing** is a software testing technique where you test individual **units** or components of your code in isolation. A "unit" is typically the smallest testable part of your code, such as a function, a method within a class, or a small module.
    *   The goal of unit testing is to verify that each unit of code is working correctly and as intended, independently of other parts of the system.

*   **Why is Unit Testing Important?**

    *   **Code Quality:** Unit tests encourage you to write better, more modular, and testable code. When you know you need to write tests, you tend to design your code in a way that is easier to test (e.g., smaller functions with well-defined inputs and outputs).
    *   **Bug Prevention:** Unit tests help catch bugs and errors early in the development process, often before they become more complex and harder to track down. Finding bugs early is much cheaper and faster than finding them later in integration or production.
    *   **Regression Prevention:** When you make changes to your code (bug fixes, new features, refactoring), unit tests act as a safety net. You can run your tests after making changes to quickly verify that you haven't broken any existing functionality (regression).
    *   **Maintainability and Refactoring:** Unit tests make your code easier to maintain and refactor. If you have a good suite of unit tests, you can confidently refactor your code knowing that if you accidentally introduce a bug, your tests will likely catch it.
    *   **Documentation and Understanding:** Unit tests can serve as living documentation for your code. They show how individual units are supposed to behave and what inputs and outputs are expected. They can help others (and your future self) understand how to use your code.
    *   **Confidence in Changes:** Unit tests give you confidence when making changes or adding new features. Knowing that your tests are passing gives you assurance that your code is working correctly.

*   **Unit Testing in Professional Software Development:** Unit testing is a fundamental practice in professional software development. It's a cornerstone of good software engineering and is often integrated into development workflows, continuous integration (CI) systems, and quality assurance processes.

### 4.2. `unittest` Module in Python

*   **Python's `unittest` Framework:** Python has a built-in module called `unittest` (sometimes also referred to as `PyUnit`, as it's inspired by JUnit for Java and other unit testing frameworks). `unittest` provides a structured way to write, organize, and run unit tests in Python.

*   **Importing `unittest`:** To use the `unittest` framework, you need to import the `unittest` module in your test files:

    ```python
    import unittest
    ```

*   **Key Components of `unittest`:**
    *   **`TestCase` Class:**  The foundation of unit testing in `unittest` is the `TestCase` class. You create test cases by subclassing `unittest.TestCase`. Each test case class groups together tests for a specific unit of code (e.g., tests for a particular function or class).
    *   **Test Methods:** Within a `TestCase` class, you define individual test methods. Each test method is a function that tests a specific aspect of the unit you are testing. Test method names **must start with `test_`** (e.g., `test_add_positive_numbers`, `test_calculate_average_empty_list`). The `unittest` framework automatically discovers and runs methods that start with `test_`.
    *   **Assertions:** Inside test methods, you use **assertion methods** provided by the `unittest.TestCase` class to check if the actual outcome of your code matches the expected outcome. Assertions are used to verify conditions and report test success or failure.

### 4.3. Writing Basic Unit Tests

Let's write some basic unit tests for a simple function. Suppose we have a function called `add(a, b)` in a module named `my_math_module.py`:

```python
# my_math_module.py
def add(a, b):
    """Adds two numbers."""
    return a + b
```

Now, let's create a separate test file, say `test_my_math_module.py`, in the same directory to write unit tests for the `add` function:

```python
# test_my_math_module.py
import unittest # Import unittest module
from my_math_module import add # Import the function to be tested

class TestAddFunction(unittest.TestCase): # 1. Define a test class inheriting from unittest.TestCase

    def test_add_positive_numbers(self): # 2. Test method name starts with 'test_'
        self.assertEqual(add(2, 3), 5) # 3. Assertion: Check if add(2, 3) is equal to 5

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -4), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(5, -2), 3)

    def test_add_zero(self):
        self.assertEqual(add(10, 0), 10)

if __name__ == '__main__': # Standard way to run tests when the script is executed directly
    unittest.main()
```

**Explanation:**

1.  **`import unittest`:** Imports the `unittest` module.
2.  **`from my_math_module import add`:** Imports the `add` function from `my_math_module.py` that we want to test.
3.  **`class TestAddFunction(unittest.TestCase):`:** Defines a test class named `TestAddFunction` that inherits from `unittest.TestCase`. This class will contain our test methods for the `add` function.
4.  **`def test_add_positive_numbers(self):`**, **`def test_add_negative_numbers(self):`**, etc.: These are test methods. Their names start with `test_`. Each method tests a specific scenario or aspect of the `add` function.
5.  **`self.assertEqual(add(2, 3), 5)`:** This is an **assertion**. `assertEqual(a, b)` is an assertion method from `unittest.TestCase`. It checks if the first argument (`add(2, 3)`) is equal to the second argument (`5`). If they are equal, the test passes. If they are not equal, the test fails, and `unittest` will report a failure.
    *   We use different test methods to test `add` with positive numbers, negative numbers, mixed numbers, and zero to cover various input scenarios.
6.  **`if __name__ == '__main__': unittest.main()`:** This is a standard way to run unit tests when you execute the test file directly. `unittest.main()` discovers and runs all test methods in the current file.

**Common Assertion Methods in `unittest.TestCase`:**

| Assertion Method               | Checks if...                                 |
| :----------------------------- | :------------------------------------------- |
| `assertEqual(a, b)`            | `a == b`                                     |
| `assertNotEqual(a, b)`         | `a != b`                                     |
| `assertTrue(condition)`        | `condition is True`                          |
| `assertFalse(condition)`       | `condition is False`                         |
| `assertIs(a, b)`               | `a is b` (object identity)                   |
| `assertIsNot(a, b)`            | `a is not b`                                 |
| `assertIsNone(x)`              | `x is None`                                  |
| `assertIsNotNone(x)`           | `x is not None`                              |
| `assertIn(member, container)`   | `member in container`                        |
| `assertNotIn(member, container)`| `member not in container`                    |
| `assertIsInstance(obj, cls)`   | `isinstance(obj, cls)`                       |
| `assertNotIsInstance(obj, cls)`| `not isinstance(obj, cls)`                   |
| `assertGreater(a, b)`          | `a > b`                                      |
| `assertGreaterEqual(a, b)`     | `a >= b`                                     |
| `assertLess(a, b)`             | `a < b`                                      |
| `assertLessEqual(a, b)`        | `a <= b`                                     |
| `assertRaises(exception, func, ...)` | `func(...)` raises `exception`          |
| ... (and many more)            | ...                                          |

### 4.4. Running Unit Tests

*   **Running Tests from the Command Line:** To run your unit tests, you typically open a terminal or command prompt, navigate to the directory where your test file (`test_my_math_module.py` in our example) is located, and run the following command:

    ```bash
    python -m unittest test_my_math_module.py
    ```

    *   `python -m unittest`:  Invokes the `unittest` module as a script.
    *   `test_my_math_module.py`:  Specifies the test file to run.

*   **Test Output:** When you run the tests, `unittest` will execute all methods in your `TestCase` classes that start with `test_`. The output will indicate:
    *   How many tests were run.
    *   Whether each test passed (`.`) or failed (`F`) or encountered an error (`E`).
    *   If there are failures or errors, `unittest` will provide details about the failures (assertion errors) or errors (exceptions).

    **Example of Successful Test Run Output:**

    ```
    ...
    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    OK
    ```

    This output indicates that 4 tests were run, and all of them passed ("OK").

    **Example of Test Failure Output:**

    If, for example, we intentionally made a test fail by changing `self.assertEqual(add(2, 3), 5)` to `self.assertEqual(add(2, 3), 6)` in `test_add_positive_numbers`, the output would look something like:

    ```
    F
    ======================================================================
    FAIL: test_add_positive_numbers (test_my_math_module.TestAddFunction)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File ".../test_my_math_module.py", line 6, in test_add_positive_numbers
        self.assertEqual(add(2, 3), 6)
    AssertionError: 5 != 6

    ----------------------------------------------------------------------
    Ran 4 tests in 0.001s

    FAILED (failures=1)
    ```

    This output shows that one test (`test_add_positive_numbers`) failed (`F`), and it provides a traceback and an `AssertionError` to explain why the test failed (because 5 is not equal to 6, as expected).

### 4.5. Test-Driven Development (TDD) - Concept (Brief Introduction)

*   **Test-Driven Development (TDD)** is a software development approach where you write **tests before you write the actual code** that you want to test. It's a development cycle that revolves around tests.

*   **TDD Cycle: Red-Green-Refactor:** The TDD process typically follows these steps in a loop:

    1.  **Red:** Write a test that describes a small piece of functionality you want to implement. Initially, this test will **fail** because you haven't written the code yet. This is the "Red" phase (test fails).
    2.  **Green:** Write the **minimum amount of code** necessary to make the test pass. Focus only on making the current test pass, not on adding extra features or perfect code. This is the "Green" phase (test passes).
    3.  **Refactor:** Once the test is passing, look at your code and see if you can **refactor** it to improve its design, readability, and maintainability, without changing its behavior. Run the tests again after refactoring to ensure you haven't broken anything. This is the "Refactor" phase (tests still pass after refactoring).
    4.  Repeat the cycle: Go back to the "Red" phase and write the next test for a new piece of functionality, and continue the Red-Green-Refactor cycle.

*   **Benefits of TDD:**
    *   **Design Thinking:** TDD forces you to think about the design and behavior of your code *before* you implement it. You start by defining what you want your code to do (in the form of tests), which can lead to better-designed and more focused code.
    *   **Better Code Coverage:** TDD naturally leads to higher test coverage because you are writing tests for every piece of functionality you implement.
    *   **Early Feedback:** You get very early feedback on your code. As soon as you write a test and run it, you know whether your code is meeting the requirements you defined in the test.
    *   **Reduced Debugging:** Because you are testing in small increments and catching bugs early, debugging becomes easier and less time-consuming.
    *   **Living Documentation (Tests as Examples):** Your tests serve as executable examples of how your code is intended to be used.

TDD is a powerful development practice, especially for complex projects. While it might seem like it adds extra work upfront (writing tests first), in the long run, it can save time and improve the quality and maintainability of your code.

## Summary of Day 5: Functions - Part 2, Decorators, and Unit Testing

Today, we've covered advanced function features, decorators, and the basics of unit testing in Python:

*   **Advanced Function Features:** Default arguments, keyword arguments, variable-length arguments (`*args`, `**kwargs`), lambda functions, and a brief introduction to function annotations (type hints).
*   **Decorators:** What decorators are, basic decorator syntax (`@decorator`), creating simple decorators, decorators with arguments (decorator factories), and chaining decorators.
*   **Unit Testing:** Introduction to unit testing, why it's important, the `unittest` module, writing basic unit tests (test cases, test methods, assertions), running tests, and a brief overview of Test-Driven Development (TDD).

These are all valuable tools and concepts for writing more robust, flexible, and maintainable Python code, especially as you move into more complex projects and web development.

## Exercises

**Exercise 1: Function with Variable Keyword Arguments**

1.  **Write a function called `display_info`** that accepts a fixed argument `title` and a variable number of keyword arguments (`**kwargs`).
2.  The function should print the `title` followed by each key-value pair from `kwargs` in a formatted way (e.g., "Key: value").
3.  Call the `display_info` function with different sets of keyword arguments to test it.

**Exercise 2: Lambda Function for String Reversal**

1.  **Write a lambda function** that takes a string as input and returns the reversed string.
2.  Test the lambda function with a few example strings.

**Exercise 3: Simple Timing Decorator**

1.  **Create a decorator function called `timer_decorator`** (similar to the `timer` example in the study material, but you can simplify it if you like). This decorator should measure and print the execution time of the decorated function.
2.  Apply the `timer_decorator` to a function of your choice (e.g., a function that performs some calculation or sleeps for a while using `time.sleep()`).
3.  Call the decorated function and observe the output, including the execution time.

**Exercise 4: Unit Tests for a Simple Calculator Function**

1.  **Create a Python file named `calculator.py`**. In this file, define a function `multiply(a, b)` that returns the product of two numbers `a` and `b`.
2.  **Create another file named `test_calculator.py`** in the same directory. This will be your test file.
3.  In `test_calculator.py`, write a test class `TestCalculator` that inherits from `unittest.TestCase`.
4.  Write at least three test methods within `TestCalculator` to test different aspects of the `multiply` function (e.g., test with positive numbers, test with negative numbers, test with zero). Use `self.assertEqual` to make assertions.
5.  Run the unit tests from the command line using `python -m unittest test_calculator.py`. Make sure all tests pass.

**Self-Check Questions (Optional):**

*   Explain the difference between default arguments and keyword arguments in Python functions. When would you use each?
*   What are `*args` and `**kwargs`? How are they used in function definitions and function calls?
*   What is a lambda function? When are lambda functions useful, and what are their limitations?
*   Describe the structure of a decorator function. What is a wrapper function, and what role does it play in decorators?
*   What are the key benefits of unit testing? Briefly explain the Red-Green-Refactor cycle in Test-Driven Development (TDD).

## Daily Task

**Task: Create a Decorator for Input Validation**

Write a decorator function called `validate_input` that:

1.  Takes a function as input (the function to be decorated).
2.  Inside the decorator, define a wrapper function.
3.  The wrapper function should:
    *   Check if all arguments passed to the decorated function are of type `int`.
    *   If all arguments are integers, call the original function with the arguments and return its result.
    *   If any argument is not an integer, print an error message "Input arguments must be integers" and return `None`.
4.  Apply the `validate_input` decorator to a function that performs some arithmetic operation (e.g., a function that adds two numbers).
5.  Test the decorated function by calling it with valid integer inputs and invalid (non-integer) inputs to see if the validation works correctly.

---

## Solutions to Exercises and Daily Task

<details>
<summary><b>Solution for Exercise 1: Function with Variable Keyword Arguments</b></summary>

```python
def display_info(title, **kwargs):
    print(title)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

display_info("Person Details", name="Alice", age=30, city="New York")
display_info("Product Info", item="Laptop", price=1200.0, brand="TechCorp", in_stock=True)
display_info("Empty Info", description="No details provided")
```

</details>

<details>
<summary><b>Solution for Exercise 2: Lambda Function for String Reversal</b></summary>

```python
reverse_string = lambda s: s[::-1] # Lambda for string reversal

print(reverse_string("hello"))       # Output: olleh
print(reverse_string("python"))      # Output: nohtyp
print(reverse_string("madam"))       # Output: madam (palindrome)
```

</details>

<details>
<summary><b>Solution for Exercise 3: Simple Timing Decorator</b></summary>

```python
import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result
    return wrapper

@timer_decorator
def slow_function():
    print("Starting slow function...")
    time.sleep(2) # Simulate slow operation
    print("Slow function finished.")
    return "Result from slow function"

output = slow_function()
print(f"Function output: {output}")
```

</details>

<details>
<summary><b>Solution for Exercise 4: Unit Tests for a Simple Calculator Function (calculator.py and test_calculator.py)</b></summary>

**`calculator.py`:**

```python
def multiply(a, b):
    """Multiplies two numbers."""
    return a * b
```

**`test_calculator.py`:**

```python
import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, 5), -10)

    def test_multiply_zero(self):
        self.assertEqual(multiply(7, 0), 0)

    def test_multiply_floats(self): # Added test for float numbers
        self.assertEqual(multiply(2.5, 2), 5.0)

if __name__ == '__main__':
    unittest.main()
```

To run the tests, navigate to the directory containing `test_calculator.py` in your terminal and run:

```bash
python -m unittest test_calculator.py
```

You should see output indicating that all tests passed (e.g., `Ran 4 tests in ... OK`).

</details>

<details>
<summary><b>Solution for Daily Task: Create a Decorator for Input Validation</b></summary>

```python
def validate_input(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                print("Error: Input arguments must be integers.")
                return None # Or raise an exception if you prefer
        for value in kwargs.values():
            if not isinstance(value, int):
                print("Error: Input arguments must be integers.")
                return None
        return func(*args, **kwargs) # Call original function if inputs are valid
    return wrapper

@validate_input
def add_integers(x, y):
    return x + y

print(add_integers(10, 20))    # Output: 30 (valid input)
print(add_integers(5, "hello")) # Output: Error message, then None (invalid input)
print(add_integers(a=7, b=8)) # Output: 15 (keyword arguments, valid)
print(add_integers(a=3.5, b=2)) # Output: Error message, then None (invalid keyword argument)
```

</details>

---

**End of Day 5 Study Material & Notes**
```
