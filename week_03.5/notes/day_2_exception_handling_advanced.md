# Day 2: Exception Handling - Part 2: Advanced Features - Study Material & Notes

## Introduction

Welcome back to Week 3.5, Day 2! Today, we are diving into **Advanced Exception Handling** in Python. Yesterday, we built a strong foundation by understanding errors and exceptions and using basic `try...except` blocks. Today, we'll expand our toolkit with more powerful features to make our error handling even more robust and flexible.

We will cover:

- The `else` and `finally` blocks to enhance `try...except` structures.
- Nested `try...except` blocks for handling errors in complex code.
- How to manually `raise` exceptions to signal errors in your own code.
- Creating your own **custom exception types** for highly specific error scenarios.

Let's level up our exception handling skills!

## Review of Day 1: Exception Handling Foundations

Before we move to advanced topics, let's quickly recap the key concepts from Day 1:

- **Errors vs. Exceptions:**
  - **Syntax Errors:** Problems in code grammar, caught before running.
  - **Logical Errors:** Errors in program logic, program runs but gives wrong results.
  - **Exceptions (Runtime Errors):** Errors during program execution that can crash the program if unhandled.
- **Importance of Exception Handling:** Writing robust, user-friendly, and maintainable code by preventing crashes and handling errors gracefully.
- **Basic `try...except` Block:** The fundamental structure to catch and handle exceptions:

  ```python
  try:
      # Risky code that might raise an exception
      ...
  except ExceptionType:
      # Code to handle the exception
      ...
  ```

- **Handling Specific Exception Types:** Using multiple `except` blocks to handle different exception types with tailored responses.

  ```python
  try:
      ...
  except ValueError:
      # Handle ValueError
      ...
  except ZeroDivisionError:
      # Handle ZeroDivisionError
      ...
  except Exception: # Catch-all
      # Handle any other exception
      ...
  ```

## Main Topic 1: Expanding `try...except`: The `else` and `finally` Blocks

Python provides two optional blocks that can be used with `try...except` to add more control and flexibility to your exception handling: `else` and `finally`.

### 1.1. The `else` Block

- **Syntax:** The `else` block is placed _after_ all `except` blocks (if any) in a `try...except...else` structure.

  ```python
  try:
      # Risky code
      ...
  except ExceptionType:
      # Handle exception
      ...
  else:
      # Code to execute if NO exception occurred in the try block
      ...
  ```

- **When it Executes:** The code inside the `else` block is executed **only if the code in the `try` block completes without raising any exceptions.** If an exception _does_ occur in the `try` block and is caught by an `except` block, the `else` block is **skipped**.

- **Purpose and Use Cases:**
  - **Code for Success:** The `else` block is used for code that you want to execute _only when the `try` block is successful_ (i.e., no exceptions).
  - **Clarity and Organization:** It helps to clearly separate the "risky" code in the `try` block from the code that should run only if everything goes well. This makes your `try...except` blocks more readable and focused.
  - **Example Scenario:** In a division program, you might perform the division in the `try` block and print the result in the `else` block, because you only want to print the result if the division was successful (and didn't raise a `ZeroDivisionError` or other exception).

**Example: Division with `else` Block**

Let's modify our division example to use an `else` block:

```python
numerator_str = input("Enter numerator: ")
denominator_str = input("Enter denominator: ")

try:
    numerator = int(numerator_str)
    denominator = int(denominator_str)
    result = numerator / denominator

except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else: # Executes only if try block completes without exceptions
    print("The result is:", result)

print("Program continues...")
```

In this example, `print("The result is:", result)` is inside the `else` block. It will only be executed if _both_ `int()` conversions are successful and the division `numerator / denominator` does not raise a `ZeroDivisionError`. If any exception occurs in the `try` block, the `else` block is skipped.

### 1.2. The `finally` Block

- **Syntax:** The `finally` block is placed _after_ all `except` and `else` blocks (if any) in a `try...except...finally` or `try...except...else...finally` structure.

  ```python
  try:
      # Risky code
      ...
  except ExceptionType:
      # Handle exception
      ...
  else:
      # Code if no exception
      ...
  finally:
      # Code that ALWAYS executes, regardless of exceptions
      # Cleanup code goes here
      ...
  ```

- **When it Executes:** The code inside the `finally` block is **always executed**, no matter what happens in the `try`, `except`, or `else` blocks. It executes:

  - If the `try` block completes successfully without exceptions.
  - If an exception occurs in the `try` block and is handled by an `except` block.
  - Even if an exception occurs in the `try` block and is _not_ handled by any `except` block (in which case the exception will still propagate outwards after the `finally` block runs).

- **Purpose and Use Cases:**
  - **Cleanup Operations:** The primary purpose of `finally` is to ensure that essential **cleanup code** is always executed, regardless of whether errors occurred.
  - **Resource Release:** Common cleanup tasks include:
    - **Closing files:** If you opened a file in the `try` block, you should almost always close it in the `finally` block to release system resources, even if an error occurred while processing the file.
    - **Closing database connections:** Similar to files, database connections should be closed to free up resources.
    - **Releasing network connections:** Sockets and network connections should be properly closed.
    - **Releasing locks or other system resources:** Any resource that needs to be explicitly released should be handled in `finally`.
  - **Ensuring Actions Happen:** `finally` guarantees that certain actions will always happen, whether the code succeeds or fails.

**Example: File Handling with `finally` Block**

Let's look at file handling. It's crucial to close files after you are done with them to free up system resources. The `finally` block is perfect for this:

```python
filename = "my_data.txt"
file = None # Initialize file variable outside try block

try:
    file = open(filename, 'r') # Open file for reading
    contents = file.read()
    # Process file contents (imagine some code here that might raise errors)
    print("File contents:\n", contents)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
except Exception as e: # Generic exception for other file errors
    print(f"An error occurred: {e}")
finally:
    if file: # Check if file was successfully opened
        file.close() # Ensure file is closed, even if errors occurred
        print("File closed in finally block.")

print("Program execution continues...")
```

**Walkthrough:**

1.  We initialize `file = None` before the `try` block because the `file` variable needs to be accessible in the `finally` block's scope, even if the `open()` operation in the `try` block fails.
2.  In the `try` block, we attempt to open the file, read its contents, and process it. `FileNotFoundError` might occur if the file doesn't exist, and other exceptions might occur during file operations.
3.  `except FileNotFoundError:` and `except Exception as e:` handle specific file-related errors.
4.  The `finally` block is _always_ executed.
5.  Inside `finally`, we check `if file:` to make sure the file was actually opened successfully (if `open()` failed, `file` would still be `None`). If `file` is not `None`, we call `file.close()` to close the file.
6.  "File closed in finally block." will always be printed after the `try...except` (or after the `try` block if no exception).
7.  Even if a `FileNotFoundError` or other exception occurs, the `finally` block ensures that we attempt to close the file if it was opened, preventing resource leaks.

## Main Topic 2: Nested `try...except` Blocks

Just like `if` statements or loops, `try...except` blocks can be **nested** inside each other. This means you can place a `try...except` block within the `try` block, or within an `except` block of another `try...except` structure.

**Concept of Nesting:**

```python
try: # Outer try block
    # Code that might raise an exception (outer level)
    statement1
    try: # Inner try block (nested inside outer try)
        # Code that might raise another exception (inner level)
        statement2
        ...
    except InnerExceptionType: # Handler for exceptions in inner try block
        # Handle inner exception
        ...
    statement3 # Still inside outer try block
except OuterExceptionType: # Handler for exceptions in outer try block
    # Handle outer exception
    ...
# Code after outer try...except block
```

**How Nesting Works:**

- **Inner and Outer Contexts:** Nested `try...except` blocks create layers of exception handling. The inner `try` block is protected by its `except` blocks, and the outer `try` block protects a larger section of code, including the inner `try` block.
- **Exception Propagation (Bubbling Up):**

  1.  If an exception occurs in the **inner `try` block**, Python first looks for a matching `except` block _within_ the inner `try...except` structure.
  2.  If a matching `except` block is found in the inner structure, it's handled there, and execution continues after the inner `try...except` block.
  3.  If **no matching `except` block is found in the inner `try...except`**, the exception "bubbles up" to the **outer `try` block**. Python then looks for a matching `except` block in the _outer_ structure.
  4.  If the outer `try` block has a suitable `except` block, it's handled there.
  5.  If **no `except` block in _either_ inner or outer `try...except` can handle the exception**, then the exception remains unhandled and will potentially crash the program (unless caught by an even further outer handler, if nesting is deeper).

- **Use Cases for Nested `try...except`:**
  - **Fine-grained Error Handling:** Nesting allows you to handle different types of errors at different levels of code granularity. You can have specific error handling for a small section of code (inner `try`) and more general handling for a larger block (outer `try`).
  - **Complex Operations with Multiple Potential Errors:** When performing a complex task that involves multiple steps, each of which might raise different exceptions, nesting can help organize the error handling logic. For example, reading data from a file (outer `try`) and then processing that data (inner `try`, as data processing might have its own set of potential errors).
  - **Retry Mechanisms:** In more advanced scenarios, you might use nested `try` blocks to implement retry logic. If an operation fails (inner `try`), you might catch the exception, attempt some recovery or alternative action in the inner `except`, and if that fails, let the outer `try` block handle the overall failure.

**Example: Nested `try...except` for File Processing**

Let's say we want to read numbers from a file, and then calculate the reciprocal of each number. Both file reading and number conversion/division can raise exceptions. Nested `try...except` can help:

```python
filename = "numbers.txt"

try: # Outer try block: for file operations
    with open(filename, 'r') as file:
        for line in file:
            try: # Inner try block: for number processing
                number = int(line.strip()) # Convert line to integer (ValueError possible)
                reciprocal = 1 / number    # Calculate reciprocal (ZeroDivisionError possible)
                print(f"Reciprocal of {number} is: {reciprocal}")
            except ValueError: # Inner except for ValueError (invalid number format in file)
                print(f"Warning: Invalid number format in line: '{line.strip()}'")
            except ZeroDivisionError: # Inner except for ZeroDivisionError (number is zero)
                print(f"Warning: Cannot calculate reciprocal of zero in line: '{line.strip()}'")
            except Exception as inner_error: # Catch-all for any other error in number processing
                print(f"Unexpected error processing line '{line.strip()}': {inner_error}")
except FileNotFoundError: # Outer except for FileNotFoundError
    print(f"Error: File '{filename}' not found.")
except Exception as outer_error: # Catch-all for any other file operation error
    print(f"General file error: {outer_error}")

print("File processing finished (with error handling).")
```

**Explanation:**

- **Outer `try` block:** Encloses the file opening and reading loop. It handles `FileNotFoundError` if the file doesn't exist and a generic `Exception` for other file-related issues.
- **Inner `try` block (inside the `for` loop):** Encloses the code that processes each line: converting it to an integer and calculating the reciprocal. This inner block handles `ValueError` (if a line is not a valid integer), `ZeroDivisionError` (if the number is zero), and a generic `Exception` for any other errors during number processing.
- **Error Handling Scope:** If a `ValueError` or `ZeroDivisionError` occurs while processing a number in a line, the _inner_ `except` blocks will catch it, print a warning message, and the loop will continue to the next line. The _outer_ `except` blocks are for errors related to file operations themselves (like not finding the file).
- **Exception Propagation:** If an exception occurs in the inner `try` block that is _not_ a `ValueError` or `ZeroDivisionError` and _not_ caught by the inner generic `except`, it would propagate outwards. In this example, there's an inner generic `except Exception as inner_error:`, so all exceptions in the inner `try` are handled at the inner level. If we removed that inner generic `except`, any unhandled exception from the inner `try` would bubble up and potentially be caught by the _outer_ generic `except Exception as outer_error:`. If even the outer block didn't handle it, the program would terminate.

## Main Topic 3: Raising Exceptions Manually

So far, we've been _handling_ exceptions that Python automatically raises when errors occur. But you can also **manually raise** exceptions in your own code using the `raise` statement. This is useful for signaling errors or exceptional conditions that are specific to your program's logic.

### 3.1. The `raise` Statement

- **Syntax:** To raise an exception, you use the `raise` keyword followed by an exception object:

  ```python
  raise ExceptionType("Error message")
  ```

  - **`ExceptionType`:** This is the type of exception you want to raise (e.g., `ValueError`, `TypeError`, `RuntimeError`, or a custom exception class).
  - **`"Error message"` (optional):** You can provide an optional string that acts as an error message or description of the problem. This message will be part of the exception object and can be accessed when the exception is caught.

- **Raising Built-in Exceptions:** You can raise any of Python's built-in exception types using `raise`. Choose the exception type that best describes the error situation in your code.

  - **Common built-in exceptions to raise manually:**
    - `ValueError`: For invalid input values (e.g., argument out of range, wrong format).
    - `TypeError`: For incorrect data types.
    - `IndexError`: For invalid sequence indices.
    - `FileNotFoundError`: For file not found situations.
    - `RuntimeError`: For general errors that don't fit into more specific categories.
    - `NotImplementedError`: To indicate that a method or function is not yet implemented.
    - `AssertionError`: To signal that an assertion (a condition that should be true) has failed (often used in debugging and testing).

- **Use Cases for `raise`:**
  - **Input Validation:** When you receive input (from users, files, other parts of your program), you should validate it to ensure it's in the expected format and range. If input is invalid, `raise ValueError` or `TypeError` to signal the problem.
  - **Signaling Business Logic Errors:** In your program's logic, you might encounter situations that are not technically Python errors, but represent errors in your application's context. For example, in an e-commerce system, if a user tries to purchase an item that is out of stock, you might `raise` a custom `OutOfStockError` exception.
  - **"Not Implemented Yet":** If you are writing a function or method that is intended to be implemented later, you can put `raise NotImplementedError("This feature is not yet implemented")` as a placeholder. This will clearly signal to anyone using your code that this part is not ready.
  - **Re-raising Exceptions (with or without modification):** Sometimes, you might catch an exception, do some partial handling (e.g., logging), and then want to re-raise the same exception or raise a different exception to propagate the error up the call stack. You can use `raise` (without any exception object) inside an `except` block to re-raise the originally caught exception. Or, you can `raise` a new exception.

**Example: Input Validation with `raise ValueError`**

Let's create a function to calculate age from birth year. We want to validate that the birth year is a reasonable value:

```python
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
```

**Walkthrough:**

1.  The `calculate_age` function takes `birth_year` as input.
2.  It checks if `birth_year` is in a valid range (not in the future, not before 1900).
3.  If `birth_year` is invalid, it uses `raise ValueError("Birth year cannot be in the future.")` or `raise ValueError("Birth year seems too early.")` to manually raise a `ValueError` exception with a descriptive message.
4.  If `birth_year` is valid, it calculates the age and returns it.
5.  In the main part of the program, we use a `try...except ValueError:` block to call `calculate_age`.
6.  If `calculate_age` (or `int(input(...))` which can also raise `ValueError`) raises a `ValueError`, the `except` block catches it, and we print the error message associated with the exception (which we set in the `raise` statement).

### 3.2. Customizing Error Messages

When you `raise` an exception, providing a clear and informative error message is very important. This message helps:

- **Users:** If the error is presented to a user, a good message helps them understand what went wrong and how to fix it (e.g., "Invalid input. Please enter a number between 1 and 100.").
- **Developers (including yourself later):** When debugging, error messages in tracebacks are invaluable for quickly identifying the source of the problem.

**Best Practices for Error Messages:**

- **Be Clear and Concise:** The message should quickly explain what the error is.
- **Be Specific:** If possible, indicate _what_ specific input or condition caused the error. Instead of "Invalid input", say "Invalid input: Age must be a positive number."
- **User-Friendly (if shown to users):** Avoid technical jargon if the message is for end-users. Focus on guiding them to correct the problem.
- **Developer-Friendly (for debugging):** For errors that are mainly for developers (e.g., internal logic errors), include enough technical detail to help with debugging (e.g., variable values, function names).

In our `calculate_age` example, `"Birth year cannot be in the future."` and `"Birth year seems too early."` are reasonably clear and specific messages that explain the validation failures.

## Main Topic 4: Custom Exception Types

While Python's built-in exceptions are useful for many common error situations, sometimes you need to signal errors that are very specific to your application's domain or logic. For these cases, you can create your own **custom exception types**.

### 4.1. Need for Custom Exceptions

- **Limitations of Built-in Exceptions:** Built-in exceptions like `ValueError`, `TypeError`, `FileNotFoundError` are general-purpose. They might not always perfectly describe the specific errors that can occur in your application's business logic.
- **Benefits of Custom Exceptions:**
  - **More Specific Error Signaling:** Custom exceptions allow you to create error types that are precisely tailored to the problems in your application. For example, in a banking app, you might have `InsufficientFundsError`, `TransactionFailedError`, `InvalidAccountNumberError`. These are much more descriptive than just using generic `ValueError` or `RuntimeError`.
  - **Improved Code Organization and Readability:** Using custom exceptions makes your code more organized and easier to understand. When you see `except InsufficientFundsError:`, it's immediately clear what type of error is being handled.
  - **Better Exception Hierarchy:** You can create a hierarchy of custom exceptions, inheriting from a common base class. This allows you to catch groups of related exceptions easily. For example, you might have a base class `BankingError` and then specific exceptions like `InsufficientFundsError`, `InvalidAccountNumberError`, `TransactionLimitExceededError` inheriting from it. You could then `except BankingError:` to catch any banking-related error.

### 4.2. Defining Custom Exception Classes

To create a custom exception type in Python, you define a new class that **inherits from the built-in `Exception` class** (or from a more specific built-in exception if it makes sense).

**Basic Structure of a Custom Exception Class:**

```python
class CustomExceptionName(Exception): # Inherit from Exception
    """Optional docstring describing the exception."""
    def __init__(self, message="A custom exception occurred"): # Optional: Customize constructor
        self.message = message # Store error message
        super().__init__(self.message) # Call superclass constructor

    # You can add custom methods or attributes if needed (more advanced)
    # For simple custom exceptions, often just the class definition is enough
```

**Key parts:**

- **`class CustomExceptionName(Exception):`**: This line defines your new exception class, making it inherit from the base `Exception` class. By convention, custom exception class names often end in "Error".
- **`"""Optional docstring..."""`**: It's good practice to include a docstring to explain what this custom exception represents.
- **`__init__(self, message="A custom exception occurred"):` (Optional but common):** You can customize the constructor (`__init__` method) to accept an error message (or other relevant data) when the exception is raised. The `super().__init__(self.message)` line calls the constructor of the parent `Exception` class, passing the message so that it's stored as the exception's error message.
- **Custom Attributes or Methods (Optional, Advanced):** For more complex custom exceptions, you could add custom attributes to store additional error details, or custom methods to provide specific behavior. For simple cases, just the class definition inheriting from `Exception` is often sufficient.

**Example: `InsufficientFundsError` Custom Exception**

Let's create a custom exception for a banking scenario:

```python
class InsufficientFundsError(Exception):
    """Exception raised when a bank account has insufficient funds for a transaction."""
    def __init__(self, account_number, attempted_withdrawal, balance):
        self.account_number = account_number
        self.attempted_withdrawal = attempted_withdrawal
        self.balance = balance
        message = f"Account {account_number} has insufficient funds. Balance: {balance}, attempted withdrawal: {attempted_withdrawal}"
        super().__init__(message) # Call Exception class constructor

# Example function that might raise this exception:
def withdraw_funds(account_number, amount_to_withdraw, current_balance):
    if amount_to_withdraw > current_balance:
        raise InsufficientFundsError(account_number, amount_to_withdraw, current_balance) # Raise custom exception
    else:
        new_balance = current_balance - amount_to_withdraw
        return new_balance

# Example usage:
account = "12345"
balance = 100
withdrawal_amount = 150

try:
    new_balance = withdraw_funds(account, withdrawal_amount, balance)
    print(f"Withdrawal successful. New balance for account {account}: {new_balance}")
except InsufficientFundsError as e: # Catch the custom exception
    print(f"Transaction failed for account {e.account_number}: {e}") # Access custom attributes and message
```

**Walkthrough:**

1.  We define a custom exception class `InsufficientFundsError` that inherits from `Exception`.
2.  The `__init__` method of `InsufficientFundsError` is customized to take `account_number`, `attempted_withdrawal`, and `balance` as arguments, store them as attributes of the exception object, and create a more informative error message.
3.  The `withdraw_funds` function checks if the `amount_to_withdraw` exceeds the `current_balance`. If it does, it raises an `InsufficientFundsError` exception, passing in the account number, withdrawal amount, and balance as arguments to the exception's constructor.
4.  In the `try...except` block, we call `withdraw_funds`. If an `InsufficientFundsError` is raised, the `except InsufficientFundsError as e:` block catches it.
5.  Inside the `except` block, we can access the custom attributes of the `InsufficientFundsError` object (e.g., `e.account_number`, `e.balance`, `e.attempted_withdrawal`) and print a detailed error message.

### 4.3. Raising and Handling Custom Exceptions

Raising and handling custom exceptions is done using the same `raise` and `except` mechanisms we've already learned:

- **Raising:** Use `raise CustomExceptionType("Error message")` to raise your custom exception.
- **Handling:** Use `except CustomExceptionType:` to create an `except` block that specifically catches your custom exception type. You can have multiple `except` blocks to handle different custom exception types (and built-in types) as needed.

Custom exceptions make your code more expressive and error handling more targeted in domain-specific scenarios.

## Summary of Day 2: Advanced Exception Handling Features

Today, we've expanded our exception handling skills with advanced features:

- **`else` and `finally` Blocks:** You learned how to use `else` for code that runs only on successful `try` execution, and `finally` for cleanup code that always runs.
- **Nested `try...except` Blocks:** You explored how to nest `try...except` blocks for more fine-grained error management in complex code structures and how exceptions propagate in nested blocks.
- **Raising Exceptions Manually:** You learned to use `raise` to signal errors in your code, especially for input validation and business logic errors, and how to customize error messages.
- **Custom Exception Types:** You discovered how to create your own exception classes to represent domain-specific errors, improving code clarity and error handling precision.

With these advanced techniques, you can write even more robust, reliable, and maintainable Python programs!

## Exercises

**Exercise 1: Division with `else` and `finally`**

Modify your "Improved Division" program from Day 1, Exercise 1 to include:

1.  An `else` block that prints the division result _only if_ the division is successful (no exceptions in the `try` block).
2.  A `finally` block that always prints "Division operation attempt finished." regardless of whether an exception occurred or not.

**Exercise 2: File Processing with Nested `try...except`**

Write a program that does the following:

1.  **Outer `try` block:** Attempts to open a file specified by the user for reading. Handle `FileNotFoundError` in an outer `except` block and print "Error: File not found."
2.  **Inner `try` block (inside the outer `try` block, within a loop that reads lines from the file):** For each line read from the file:
    - Try to convert the line to an integer. Handle `ValueError` in an inner `except` block and print a warning message like "Warning: Invalid number in line: [line content]".
    - If conversion to integer is successful, calculate the square root of the number. Handle `ValueError` (if number is negative, square root of negative numbers is not real) in another inner `except` block and print "Warning: Cannot calculate square root of negative number: [number]". You might need to import the `math` module for `math.sqrt()`.
    - If both conversion and square root calculation are successful, print "Square root of [number] is: [square root]".

**Exercise 3: Raising Custom Exceptions for Password Validation**

Create a function `validate_password(password)` that validates a password based on the following rules:

- Password must be at least 8 characters long.
- Password must contain at least one uppercase letter.
- Password must contain at least one digit.

Define three custom exception classes:

- `PasswordTooShortError(Exception)`: Raised if the password is less than 8 characters.
- `PasswordMissingUppercaseError(Exception)`: Raised if the password does not contain an uppercase letter.
- `PasswordMissingDigitError(Exception)`: Raised if the password does not contain a digit.

In the `validate_password` function, check each rule. If a rule is violated, `raise` the corresponding custom exception with an informative message. If all rules pass, the function should return `True`.

Write a main program that prompts the user to enter a password and then calls `validate_password`. Use a `try...except` block to catch any of the custom password exception types that might be raised and print user-friendly error messages. If the password is valid (function returns `True`), print "Password valid!".

**Self-Check Questions (Optional):**

- Explain when the `else` block in a `try...except...else` structure is executed and what its purpose is.
- Explain when the `finally` block in a `try...except...finally` structure is executed and what it's typically used for.
- Describe a scenario where nested `try...except` blocks are useful. How does exception propagation work in nested blocks?
- What is the `raise` statement used for? Give examples of situations where you would manually raise exceptions.
- Why and when would you create custom exception types in Python? What are the benefits?

## Daily Task

**Task: Enhance Your "Favorite Fruits" Loop with `finally`**

Take your "Favorite Fruits" loop program from Day 1's Daily Task (the one with `try...except IndexError` inside the loop). Add a `finally` block _inside_ the `for` loop, after the `try...except` block. Make the `finally` block print the message "Processed fruit at index: [index]" in _every_ iteration of the loop, regardless of whether an `IndexError` occurred or not.

This task is to practice using the `finally` block within a loop to ensure some code (like logging or cleanup) always runs at the end of each loop iteration.

---

## Solutions to Exercises and Daily Task

<details>
<summary><b>Solution for Exercise 1: Division with `else` and `finally`</b></summary>

```python
numerator_str = input("Enter numerator: ")
denominator_str = input("Enter denominator: ")

try:
    numerator = int(numerator_str)
    denominator = int(denominator_str)
    result = numerator / denominator
except ValueError:
    print("Invalid input. Please enter numbers only.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("The result is:", result) # Executed only if no exception in try
finally:
    print("Division operation attempt finished.") # Always executed
```

</details>

<details>
<summary><b>Solution for Exercise 2: File Processing with Nested `try...except`</b></summary>

```python
import math

filename = input("Enter filename: ")

try: # Outer try for file operations
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1): # Enumerate for line numbers
            try: # Inner try for line processing
                number = int(line.strip())
                sqrt_val = math.sqrt(number)
                print(f"Square root of {number} is: {sqrt_val}")
            except ValueError as ve: # Inner except for ValueError (non-integer or negative number)
                if "invalid literal" in str(ve): # Check if ValueError is due to non-integer
                    print(f"Warning: Invalid number format in line {line_number}: '{line.strip()}'")
                else: # Assume ValueError is due to negative number for sqrt
                    print(f"Warning: Cannot calculate square root of negative number in line {line_number}: '{line.strip()}'")
            except ZeroDivisionError: # Example - though square root won't cause this, demonstrating multiple inner excepts
                print(f"Warning: Division by zero error (unlikely in sqrt, but shown for example) in line {line_number}: '{line.strip()}'")
            except Exception as inner_error: # Catch-all for other inner errors
                print(f"Unexpected error processing line {line_number}: '{line.strip()}': {inner_error}")
except FileNotFoundError: # Outer except for file not found
    print(f"Error: File '{filename}' not found.")
except Exception as outer_error: # Catch-all for other file errors
    print(f"General file error: {outer_error}")

print("File processing finished.")
```

</details>

<details>
<summary><b>Solution for Exercise 3: Raising Custom Exceptions for Password Validation</b></summary>

```python
class PasswordTooShortError(Exception):
    """Exception raised when password is too short."""
    pass

class PasswordMissingUppercaseError(Exception):
    """Exception raised when password lacks an uppercase letter."""
    pass

class PasswordMissingDigitError(Exception):
    """Exception raised when password lacks a digit."""
    pass

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password must be at least 8 characters long.")
    if not any(char.isupper() for char in password):
        raise PasswordMissingUppercaseError("Password must contain at least one uppercase letter.")
    if not any(char.isdigit() for char in password):
        raise PasswordMissingDigitError("Password must contain at least one digit.")
    return True # Password is valid if no exceptions raised

# Main program
password_attempt = input("Enter a password to validate: ")
try:
    if validate_password(password_attempt):
        print("Password valid!")
except PasswordTooShortError as e:
    print("Password invalid:", e)
except PasswordMissingUppercaseError as e:
    print("Password invalid:", e)
except PasswordMissingDigitError as e:
    print("Password invalid:", e)
```

</details>

<details>
<summary><b>Solution for Daily Task: Enhance Your "Favorite Fruits" Loop with `finally`</b></summary>

```python
favorite_fruits = ["mango", "strawberry", "blueberry"]
for index in range(len(favorite_fruits)):
    try:
        fruit = favorite_fruits[index]
        print(fruit)
    except IndexError:
        print(f"Warning: Could not access fruit at index {index}")
    finally:
        print(f"Processed fruit at index: {index}") # Always executed

print("Finished processing fruits.")
```

</details>

---

**End of Day 2 Study Material & Notes**
