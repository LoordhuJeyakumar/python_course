## Week 2, Day 4: Functions - COMPLETE

**Lesson Plan:**

1.  **Introduction to Functions**

    - Recap of Day 3 (Dictionaries), Q\&A. Briefly review Dictionaries and address any questions from Day 3 exercises or data structure selection scenarios.
    - Introduction to Functions:
      - Definition: Reusable blocks of code that perform a specific task. Emphasize "reusable" and "specific task".
      - Why Functions?
        - Modularity: Breaking down complex programs into smaller, manageable, self-contained functions.
        - Reusability: Write code once, use it multiple times from different parts of the program. Avoid code duplication.
        - Readability: Makes code easier to read, understand, and maintain. Logic is organized into logical units.
        - Abstraction: Hiding implementation details behind a function name. Focus on _what_ the function does, not _how_ it does it.
    - Defining Functions:
      - `def` keyword: Keyword to start a function definition.
      - Function name: Naming conventions for functions (descriptive, lowercase, using underscores).
      - Parameters (optional): Input values the function can accept, enclosed in parentheses `()`. Explain formal parameters.
      - Docstring (optional but highly recommended): Documenting what the function does, its parameters, and what it returns. Triple quotes `"""Docstring goes here"""`.
      - Function body: Indented block of code that executes when the function is called.
      - `return` statement (optional): Specifies the value the function sends back to the caller. Functions can return values or perform actions without explicitly returning anything (implicitly return `None`).
    - Calling Functions:
      - Using the function name followed by parentheses `()`: `function_name()`.
      - Providing arguments (actual parameters) that match the function's parameters (if any).
    - Function Arguments:
      - Positional Arguments: Arguments passed in order, matched to parameters by position in the function definition.
      - Keyword Arguments: Arguments passed with `keyword=value` syntax. Order doesn't matter, but must match parameter names. Can improve readability especially with many arguments.
      - Default Arguments: Providing default values for parameters in the function definition. If an argument is not provided during the function call, the default value is used. Default parameters must come after positional parameters.
    - Scope of Variables:
      - Local Variables: Variables defined inside a function. Scope is limited to the function. Cannot be accessed outside the function.
      - Global Variables: Variables defined outside of any function (at the top level of a script). Can be accessed inside functions (but need `global` keyword to modify within a function, generally discouraged for best practices). Emphasize best practices: minimize global variable usage, pass data as arguments and return values.
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate function definition, different argument types, function calls, return values, and scope. Emphasize best practices of function design and code organization. Encourage learners to experiment and observe.

2.  **Function Return Values, Scope Deep Dive, and Function Design**
    - Function Return Values (in detail):
      - Functions returning single values, multiple values (as tuples), or no explicit return (implicitly returning `None`).
      - Using `return` to exit a function early.
      - Demonstrate returning different data types from functions.
    - Scope Deep Dive:
      - Detailed explanation of local scope, global scope, and enclosing scope (briefly touch on closures if appropriate for the level).
      - LEGB Rule (Local, Enclosing, Global, Built-in) for variable lookup.
      - `global` keyword: Use sparingly and understand its implications for modifying global variables from within functions. Emphasize it should be used thoughtfully and generally avoided for cleaner function design.
      - Best practices for scope management: Pass data into functions as arguments and return results. Minimize reliance on global variables.
    - Function Design Principles:
      - Single Responsibility Principle: Functions should do one thing well and clearly.
      - Function Length: Keep functions reasonably short and focused. If a function becomes too long, consider breaking it down into smaller, more specialized functions.
      - Descriptive Naming: Choose function names that clearly indicate what the function does.
      - Docstrings: Always write clear and concise docstrings to explain function purpose, arguments, and return values.
      - Testing Functions: Importance of testing functions in isolation to ensure they work correctly (unit testing concept introduction).
    - **Hands-on Exercises:** Learners practice defining and using functions with different argument types, return values, and explore scope rules. Exercises should include tasks like:
      - Defining functions with positional, keyword, and default arguments.
      - Calling functions with different argument combinations.
      - Writing functions that return single values, multiple values, and `None`.
      - Exploring variable scope (local vs. global).
      - Refactoring code into functions to improve modularity and reusability.
      - Designing and implementing functions to solve specific sub-problems within larger tasks.
    - Example problem solving: Guide learners to solve problems like:
      - Writing functions for basic arithmetic operations (add, subtract, multiply, divide).
      - Creating functions to validate user input (e.g., check if input is an integer, check password strength using criteria from Day 1 exercise, but now in a function).
      - Writing functions to perform string manipulations (reverse a string, count words in a string).
      - Designing a function that takes a list of numbers and returns the average and the maximum value (returning multiple values as a tuple).
      - Refactoring a larger piece of code (from previous days' exercises or assignment problems) by breaking it down into well-defined functions.
    - Q\&A and wrap-up: Address learner questions. Recap functions, their benefits, definition, calling, arguments, return values, scope, and design principles. Preview Day 5's topic: Modules and Packages.

---

**Study Material & Notes:**

### Week 2: Day 4: Functions

**Notes:**

#### 1. Introduction to Functions

- **Definition:** A function is a **named block of reusable code** that performs a **specific task**.

- **Why Use Functions?**

  - **Modularity (Code Organization):** Functions break down large, complex programs into smaller, self-contained, and logically organized units. This makes the code easier to manage, understand, and debug.
  - **Reusability (Avoid Code Duplication):** Once you define a function, you can call (execute) it multiple times from different parts of your program without rewriting the same code. This significantly reduces code duplication, making your code shorter, cleaner, and easier to maintain.
  - **Readability (Improved Code Clarity):** Functions give meaningful names to blocks of code, making the program logic easier to follow. Instead of seeing a long sequence of operations, you see function calls that represent higher-level actions.
  - **Abstraction (Simplify Complexity):** Functions allow you to hide the implementation details of a task behind a function name. You can use a function without needing to know exactly how it works internally. This is abstraction – focusing on _what_ a function does, not _how_ it does it.

#### 2. Defining Functions

- **Function Definition Syntax:**

  ```python
  def function_name(parameter1, parameter2, ...):
      """Docstring: Briefly describe what the function does.

      Optionally, explain parameters and return value here.
      """
      # Function body - code to be executed
      # ...
      return result # Optional return statement
  ```

  - **`def` keyword:** Indicates the start of a function definition.
  - **`function_name`:** A descriptive name for your function. Follow naming conventions (lowercase, underscores for readability, e.g., `calculate_average`, `greet_user`).
  - **`(parameter1, parameter2, ...)` (Parameters - Optional):** Input values that the function can receive when called. Parameters are variable names listed inside the parentheses in the function definition. A function can have zero or more parameters.
  - **`:` (Colon):** Marks the end of the function signature (name and parameters) and the start of the function body.
  - **Docstring (`"""Docstring goes here"""` - Optional but highly recommended):** A string literal enclosed in triple quotes, placed immediately after the function signature. It's used to document what the function does, its parameters, and what it returns. Good practice to always include docstrings.
  - **Function Body (Indented Code Block):** The code that gets executed when the function is called. It must be indented to indicate it's part of the function.
  - **`return result` (Return Statement - Optional):** Used to send a value back from the function to the caller. When a `return` statement is executed, the function ends, and the specified value (if any) is returned. If there is no `return` statement, or just `return` without a value, the function implicitly returns `None`.

- **Example Function Definition:**

  ```python
  def greet(name):
      """This function greets the person passed in as a parameter."""
      print(f"Hello, {name}!")

  def add_numbers(num1, num2):
      """This function adds two numbers and returns their sum."""
      sum_result = num1 + num2
      return sum_result

  def say_goodbye():
      """This function prints a goodbye message."""
      print("Goodbye!")
      # No explicit return statement - implicitly returns None
  ```

#### 3. Calling Functions

- **Function Call Syntax:** To execute a function that you have defined, you need to "call" it by using its name followed by parentheses `()`. If the function expects arguments (parameters), you must provide them inside the parentheses.

  ```python
  greet("Alice") # Call the greet function with argument "Alice"

  sum_of_5_and_3 = add_numbers(5, 3) # Call add_numbers with arguments 5 and 3
  print(f"The sum is: {sum_of_5_and_3}") # Print the returned value

  say_goodbye() # Call say_goodbye function (no arguments needed)
  return_value_goodbye = say_goodbye() # Call and capture return value (will be None)
  print(f"Return value of say_goodbye(): {return_value_goodbye}") # Print the implicit None return value
  ```

#### 4. Function Arguments

- **Positional Arguments:** Arguments are passed to a function based on their **position** in the function call, matching the order of parameters in the function definition.

  ```python
  def describe_pet(animal_type, pet_name):
      """Displays information about a pet."""
      print(f"I have a {animal_type} named {pet_name}.")

  describe_pet('hamster', 'Harry') # Positional arguments: 'hamster' is animal_type, 'Harry' is pet_name
  describe_pet('dog', 'Lucy') # 'dog' -> animal_type, 'Lucy' -> pet_name
  # describe_pet('Harry', 'hamster') # Wrong order - 'Harry' would be animal_type, 'hamster' pet_name (order matters)
  ```

- **Keyword Arguments:** Arguments are passed using the syntax `keyword=value`. You explicitly specify which parameter each value corresponds to. Order does not matter when using keyword arguments, as long as the keyword matches a parameter name in the function definition. Keyword arguments often improve code readability, especially for functions with many parameters.

  ```python
  def describe_pet(animal_type, pet_name):
      """Displays information about a pet."""
      print(f"I have a {animal_type} named {pet_name}.")

  describe_pet(animal_type='hamster', pet_name='Harry') # Keyword arguments
  describe_pet(pet_name='Lucy', animal_type='dog') # Order doesn't matter with keyword arguments

  # Mixing positional and keyword arguments (positional first, then keyword)
  describe_pet('cat', pet_name='Bella') # 'cat' is positional (animal_type), 'pet_name' is keyword
  # describe_pet(animal_type='rabbit', 'Bunny') # SyntaxError: positional argument follows keyword argument (positional must come first if mixing)
  ```

- **Default Arguments:** You can specify default values for parameters in the function definition. If an argument for a parameter with a default value is not provided in the function call, the default value is used. Parameters with default values must come **after** parameters without default values (positional parameters) in the function definition.

  ```python
  def greet_user(name, greeting="Hello"): # 'greeting' has a default value "Hello"
      """Greets a user with an optional custom greeting."""
      print(f"{greeting}, {name}!")

  greet_user('Alice') # Uses default greeting "Hello"
  greet_user('Bob', greeting="Hi") # Overrides default greeting with "Hi"
  greet_user(name="Charlie") # Uses default greeting, keyword argument for name
  ```

#### 5. Scope of Variables

- **Scope** refers to the region of a program where a variable can be accessed (where it is "visible" and can be used). Python has different scopes, primarily:

  - **Local Scope:** Variables defined **inside a function** have local scope. They are only accessible within that function. Local variables are created when the function is called and destroyed when the function finishes executing.

    ```python
    def my_function():
        local_variable = 10 # local_variable has local scope within my_function
        print(f"Inside function: {local_variable}")

    my_function() # Output: Inside function: 10
    # print(local_variable) # NameError: name 'local_variable' is not defined (cannot access outside function)
    ```

  - **Global Scope:** Variables defined **outside of any function** (at the top level of your script) have global scope. Global variables can be accessed from anywhere in the script, including inside functions.

    ```python
    global_variable = 20 # global_variable has global scope

    def another_function():
        print(f"Inside function, accessing global variable: {global_variable}") # Accessing global variable is OK

    another_function() # Output: Inside function, accessing global variable: 20
    print(f"Outside function, accessing global variable: {global_variable}") # Output: Outside function, accessing global variable: 20
    ```

- **Modifying Global Variables within Functions (using `global` keyword - Use with Caution):** If you need to modify a global variable from within a function, you must use the `global` keyword before the variable name inside the function. However, **modifying global variables inside functions is generally discouraged** as it can make code harder to understand, debug, and maintain. It's better to pass data into functions as arguments and return modified data as return values.

  ```python
  global_counter = 0

  def increment_counter():
      global global_counter # Declare intention to modify the global variable
      global_counter += 1
      print(f"Counter incremented inside function: {global_counter}")

  increment_counter() # Output: Counter incremented inside function: 1
  increment_counter() # Output: Counter incremented inside function: 2
  print(f"Global counter after function calls: {global_counter}") # Output: Global counter after function calls: 2
  ```

- **LEGB Rule for Variable Scope Resolution:** When you use a variable name in Python, Python searches for its definition in the following order of scopes (Local, Enclosing, Global, Built-in - LEGB):

  1.  **Local (L):** Current function's scope.
  2.  **Enclosing (E):** Scopes of any enclosing functions (relevant for nested functions, not covered in detail yet in Week 2).
  3.  **Global (G):** Module-level scope (the scope of the current `.py` file).
  4.  **Built-in (B):** Built-in names in Python (e.g., `print`, `len`, `int`).

  Python stops searching as soon as it finds a matching name in one of these scopes.

#### 6. Function Return Values

- **Functions Can Return Values:** Functions can return a value back to the part of the code that called them using the `return` statement. The returned value can be of any data type.

  ```python
  def square(number):
      """Returns the square of a number."""
      return number * number

  result1 = square(5) # Call square(5), returned value (25) is assigned to result1
  print(f"Square of 5 is: {result1}") # Output: Square of 5 is: 25

  def get_initials(first_name, last_name):
      """Returns the initials of a name as a string."""
      initials = first_name[0].upper() + last_name[0].upper()
      return initials

  name_initials = get_initials("john", "doe")
  print(f"Initials: {name_initials}") # Output: Initials: JD
  ```

- **Returning Multiple Values (using Tuples):** Python functions can effectively return multiple values by packing them into a tuple and returning the tuple. The caller can then unpack the tuple to get individual values.

  ```python
  def divide_and_remainder(dividend, divisor):
      """Returns both the quotient and remainder of division."""
      quotient = dividend // divisor
      remainder = dividend % divisor
      return quotient, remainder # Returns a tuple (quotient, remainder)

  division_result = divide_and_remainder(17, 5) # Returns tuple (3, 2)
  print(f"Division result (tuple): {division_result}") # Output: Division result (tuple): (3, 2)

  q, r = divide_and_remainder(17, 5) # Unpack the returned tuple into q and r
  print(f"Quotient: {q}, Remainder: {r}") # Output: Quotient: 3, Remainder: 2
  ```

- **Functions without Explicit `return` (Implicitly Return `None`):** If a function does not have a `return` statement, or if it has `return` without specifying a value, it implicitly returns the special value `None`. `None` represents the absence of a value.

  ```python
  def print_message(message):
      """Prints a message to the console. Does not explicitly return anything."""
      print(message)
      # No explicit return statement

  result_from_print = print_message("Hello, function!")
  # Output: Hello, function! (printed by the function)
  print(f"Return value of print_message: {result_from_print}") # Output: Return value of print_message: None
  ```

#### 7. Function Design Principles (Good Practices)

- **Single Responsibility Principle:** Each function should have a clear, well-defined, and single purpose. It should do one thing and do it well. This makes functions easier to understand, test, and reuse. If a function tries to do too many things, break it down into smaller, more focused functions.
- **Keep Functions Short and Focused:** Aim for functions that are reasonably short and to the point. Long functions are harder to read and understand. If a function becomes lengthy, consider breaking it into smaller, more specialized helper functions.
- **Use Descriptive Function Names:** Choose function names that clearly and accurately describe what the function does. Good function names make your code self-documenting and easier to read. Use verbs or verb phrases in function names (e.g., `calculate_area`, `validate_input`, `get_user_data`).
- **Write Docstrings:** Always include a docstring for each function to explain its purpose, parameters, and return value. Docstrings serve as documentation for your functions and are essential for code readability and maintainability.
- **Test Your Functions (Unit Testing Concept - Introduction):** It's crucial to test your functions in isolation (unit testing). Write small test cases to verify that each function behaves as expected for various inputs and edge cases. This helps ensure that your functions are correct and reliable. (Unit testing will be covered more formally later, but introduce the concept of simple testing now).
- **Minimize Global Variables:** Avoid overuse of global variables. Pass data into functions as arguments and return results. This promotes modularity, reduces side effects, and makes functions more self-contained and easier to test.

---

**Exercises:**

### Week 2: Day 4: Exercises

1.  **Simple Function Definition and Calling:**

    - Define a function called `greet_person` that takes one parameter, `name`, and prints a greeting message like "Hello, \[name]!".
    - Call the `greet_person` function three times with different names as arguments.

2.  **Function with Return Value:**

    - Define a function called `calculate_circle_area` that takes one parameter, `radius`, and calculates and **returns** the area of a circle. (Area of a circle = π _ radius _ radius, use `math.pi` for π).
    - Call the `calculate_circle_area` function with a radius of `5`.
    - Print the returned area with a user-friendly message.

3.  **Function with Positional and Keyword Arguments:**

    - Define a function called `describe_product` that takes three parameters: `name`, `price`, and `category`.
    - Call `describe_product` three times:
      - Once using positional arguments for all parameters.
      - Once using keyword arguments for all parameters (in a different order than defined).
      - Once using a mix of positional and keyword arguments.

4.  **Function with Default Arguments:**

    - Define a function called `send_email` that takes two parameters: `recipient_email` and `subject`, with an optional third parameter `body` that has a default value of "No message body provided.".
    - Call `send_email` in the following ways:
      - Provide only `recipient_email` and `subject` (body should use default).
      - Provide `recipient_email`, `subject`, and a custom `body`.

5.  **Variable Scope Exploration:**
    - Define a global variable `global_message = "Hello from global scope"`.
    - Define a function `scope_test` that:
      - Prints the `global_message`.
      - Defines a local variable `local_message = "Hello from local scope"` inside the function.
      - Prints the `local_message`.
    - Call `scope_test()`.
    - Try to print `local_message` outside the function. What happens? (Expect a `NameError`).
    - Modify `scope_test` to use the `global` keyword to modify `global_message` to `"Global message changed inside function"`. Call `scope_test()` again, and then print `global_message` outside the function. Observe the change in the global variable (and note: this is generally discouraged for most cases in good function design).

---

**Daily Simple Task:**

### Daily Simple Task - Day 4, Week 2

Write a function called `is_even` that takes an integer as input and returns `True` if the number is even, and `False` otherwise. Call this function with a few different numbers and print the returned results.
