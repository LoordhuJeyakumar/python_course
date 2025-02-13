## Week 1, Day 5: Loops - COMPLETE

**Lesson Plan:**

1.  **Introduction to Loops (`for` loop and `while` loop)**
    - Recap of Day 4, Q\&A. Briefly review Conditional Statements. Address any questions learners might have from Day 4's topics and exercises.
    - Introduction to Loops: Why loops are essential in programming - automating repetitive tasks, iterating over data. Real-world examples (repeating actions, processing lists of items).
    - `for` loop: Iterating over sequences.
      - Explain the `for` keyword, the iteration variable, the `in` keyword, and the sequence (iterable).
      - Syntax of `for` loop and the indented code block.
      - Iterating over strings: character by character.
      - Iterating over lists (brief introduction to lists as sequences - mention more detail in Week 2, use simple list examples).
      - Using the `range()` function with `for` loop to generate sequences of numbers. Explain `range(stop)`, `range(start, stop)`, `range(start, stop, step)`. Demonstrate different `range()` usages.
      - `for-else` block (optional but useful): Explain that `else` block in a `for` loop executes if the loop completes normally (i.e., not terminated by `break`).
    - `while` loop: Condition-controlled loops.
      - Explain the `while` keyword, the condition (boolean expression), and the colon `:`.
      - Indentation for the code block under `while`.
      - Loop continues as long as the condition is `True`. Importance of the condition becoming `False` eventually to avoid infinite loops.
      - Need for loop control variables and how they are updated within the loop to control loop termination.
      - `while-else` block (optional but useful): Explain that `else` block in a `while` loop executes if the loop condition becomes `False` and loop terminates normally (not via `break`).
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate both `for` and `while` loops, `range()`, and loop structures. Emphasize correct indentation and loop control. Encourage learners to follow and modify the code.
2.  **Loop Control (`break`, `continue`) and Nested Loops**
    - Loop control statements: `break` and `continue`.
      - `break` statement: Explain its purpose - immediately exit the loop (both `for` and `while`). Demonstrate scenarios where `break` is useful (e.g., searching for an item and stopping when found).
      - `continue` statement: Explain its purpose - skip the current iteration and move to the next iteration of the loop. Demonstrate scenarios where `continue` is useful (e.g., skipping processing certain items in a sequence based on a condition).
      - Examples to clearly differentiate `break` and `continue` behavior within loops.
    - Nested Loops: Loops inside loops.
      - Explain the concept of nested loops: an outer loop and an inner loop.
      - Inner loop executes completely for each iteration of the outer loop.
      - Demonstrate with examples: printing patterns (stars, numbers in a grid), iterating over 2D structures (briefly mention concept in preparation for lists of lists in Week 2).
      - Emphasize indentation and scope in nested loops.
    - **Hands-on Exercises:** Learners practice using `for` and `while` loops, `range()`, `break`, `continue`, and nested loops to solve problems. Exercises should include tasks like:
      - Iterating through sequences (strings, simple lists).
      - Generating number sequences using loops and `range()`.
      - Using `while` loops with conditions.
      - Implementing `break` and `continue` in loops.
      - Creating simple patterns using nested loops.
      - Solving problems that require loop control (searching, filtering).
    - Example problem solving: Guide learners through developing programs like:
      - Calculating the sum of numbers in a range.
      - Finding the factorial of a number.
      - Searching for an element in a string/list.
      - Printing multiplication tables using nested loops.
    - Q\&A and wrap-up: Address learner questions. Recap `for` loops, `while` loops, `range()`, `break`, `continue`, and nested loops. Preview Week 2 topics: Data Structures (Lists, Tuples, Sets, Dictionaries).

---

**Study Material & Notes:**

### Week 1: Python Fundamentals I - Day 5: Loops (`for` and `while` Loops)

**Notes:**

#### Loops: Repeating Actions

- Loops are control flow structures that allow you to execute a block of code repeatedly.
- They are essential for automating repetitive tasks, iterating over collections of data, and making programs more efficient.
- Python provides two main types of loops: `for` loops and `while` loops.

#### 1. `for` loop: Iteration over Sequences

- The `for` loop is used to iterate over a sequence (like a string, list, tuple, or range) or other iterable objects.
- It executes the loop body for each item in the sequence.
- **Syntax:**

  ```python
  for item in sequence:
      # Code to be executed for each item in the sequence
      statement1
      statement2
      ...
  # Code here will execute after the loop finishes iterating through all items
  ```

  - `item`: A variable that takes on the value of each element in the `sequence` during each iteration.
  - `sequence`: An iterable object (e.g., string, list, tuple, range).
  - The code block under the `for` loop **must be indented**.

- **Iterating over a String:**

  ```python
  message = "Python"
  for char in message: # 'char' will take values 'P', 'y', 't', 'h', 'o', 'n' in each iteration
      print(char)
  # Output:
  # P
  # y
  # t
  # h
  # o
  # n
  ```

- **Iterating over a List (Introduction - Lists will be covered in detail in Week 2):**

  ```python
  fruits = ["apple", "banana", "cherry"] # List of strings
  for fruit in fruits: # 'fruit' will take values "apple", "banana", "cherry"
      print(fruit)
  # Output:
  # apple
  # banana
  # cherry
  ```

- **`range()` function with `for` loop:** Generates a sequence of numbers.

  - `range(stop)`: Generates numbers from 0 up to (but not including) `stop`. Step is 1 by default.
  - `range(start, stop)`: Generates numbers from `start` up to (but not including) `stop`. Step is 1 by default.
  - `range(start, stop, step)`: Generates numbers from `start` up to (but not including) `stop`, incrementing by `step`.

  ```python
  # range(stop) - from 0 to stop-1, step 1
  for i in range(5): # Generates numbers 0, 1, 2, 3, 4
      print(i)
  # Output: 0 1 2 3 4

  # range(start, stop) - from start to stop-1, step 1
  for i in range(2, 7): # Generates numbers 2, 3, 4, 5, 6
      print(i)
  # Output: 2 3 4 5 6

  # range(start, stop, step) - from start to stop-1, step 'step'
  for i in range(0, 20, 2): # Generates even numbers from 0 to 18
      print(i)
  # Output: 0 2 4 6 8 10 12 14 16 18

  for i in range(5, 0, -1): # Countdown from 5 to 1
      print(i)
  # Output: 5 4 3 2 1
  ```

- **`for-else` block (Optional):**

  - The `else` block after a `for` loop is executed **if the loop completes all iterations normally** (i.e., it's not terminated by a `break` statement).
  - **Syntax:**

    ```python
    for item in sequence:
        # loop body
    else:
        # else block - executes if loop completes without break
    ```

  ```python
  numbers = [1, 2, 3, 4, 5]
  for num in numbers:
      if num == 3:
          print("Found 3!")
          break # Loop terminates here
  else: # This else block will NOT execute because the loop was terminated by 'break'
      print("Loop completed normally")

  for num in numbers:
      print(num)
  else: # This else block WILL execute because the loop completed all iterations
      print("Loop completed normally") # This will be printed
  ```

#### 2. `while` loop: Condition-Controlled Loops

- The `while` loop repeatedly executes a block of code as long as a given condition remains `True`.
- It's used when you don't know in advance how many times you need to iterate; the loop continues until a certain condition is met.
- **Syntax:**

  ```python
  while condition:
      # Code to be executed as long as the condition is True
      statement1
      statement2
      # ... (Important: something inside the loop should eventually make the condition False to avoid infinite loop)
  # Code here will execute after the loop condition becomes False
  ```

  - `condition`: A boolean expression. The loop continues as long as this condition is `True`.
  - The code block under the `while` loop **must be indented**.
  - **Important:** You must ensure that something inside the `while` loop body will eventually make the `condition` `False`. Otherwise, the loop will run forever (an **infinite loop**).

- **Example:**

  ```python
  count = 0
  while count < 5: # Condition: count is less than 5
      print("Count is:", count)
      count += 1 # Increment count - this is crucial to eventually make the condition False
  # Output:
  # Count is: 0
  # Count is: 1
  # Count is: 2
  # Count is: 3
  # Count is: 4

  # Example of infinite loop (if you remove count += 1):
  # count = 0
  # while count < 5:
  #     print("Count is:", count) # Condition count < 5 will always be True! Loop runs forever!

  # Using while loop to get valid user input (example):
  user_input = ""
  while user_input.lower() != "quit": # Loop until user types "quit" (case-insensitive)
      user_input = input("Enter command (or 'quit' to exit): ")
      print("You entered:", user_input)
  print("Exiting program.")
  ```

- **`while-else` block (Optional):**

  - Similar to `for-else`, the `else` block after a `while` loop executes **if the loop condition becomes `False` and the loop terminates normally** (not by `break`).

  - **Syntax:**

    ```python
    while condition:
        # loop body
    else:
        # else block - executes if loop condition becomes False without break
    ```

  ```python
  count = 0
  while count < 3:
      print("Count:", count)
      count += 1
  else: # This else block WILL execute because loop condition became False naturally
      print("While loop condition became false, loop ended.") # This will be printed

  count = 0
  while count < 5:
      print("Count:", count)
      if count == 2:
          break # Loop terminated by break
      count += 1
  else: # This else block will NOT execute because the loop was terminated by 'break'
      print("While loop condition became false, loop ended.") # This will NOT be printed
  ```

#### Loop Control Statements: `break` and `continue`

- **`break` statement:**

  - Immediately terminates the loop (both `for` and `while`) and jumps to the statement immediately following the loop.
  - Used to exit a loop prematurely based on a condition.

  ```python
  for i in range(10):
      if i == 5:
          break # Exit the loop when i is 5
      print(i)
  # Output: 0 1 2 3 4 (loop stops at 5)

  number = 0
  while True: # Intentionally create an infinite loop (condition always True)
      print(number)
      number += 1
      if number > 3:
          break # Exit the while loop when number becomes greater than 3
  # Output: 0 1 2 3
  ```

- **`continue` statement:**

  - Skips the rest of the current iteration of the loop and proceeds to the next iteration.
  - Does not terminate the loop itself, only the current iteration.

  ```python
  for i in range(10):
      if i % 2 == 0: # If i is even
          continue # Skip to the next iteration, don't print even numbers
      print(i) # Only odd numbers will be printed
  # Output: 1 3 5 7 9

  number = 0
  while number < 5:
      number += 1
      if number == 3:
          continue # Skip printing when number is 3
      print(number)
  # Output: 1 2 4 5 (3 is skipped)
  ```

#### Nested Loops: Loops within Loops

- Nested loops occur when you place a loop inside another loop (either a `for` loop inside a `for` loop, a `while` loop inside a `while` loop, or a mix).
- The inner loop will execute completely for each iteration of the outer loop.
- Used for tasks that involve iteration over multiple dimensions or levels, like processing 2D arrays (matrices), generating combinations, etc.

- **Example: Nested `for` loops for a pattern:**

  ```python
  for i in range(3): # Outer loop (runs 3 times)
      for j in range(4): # Inner loop (runs 4 times for each iteration of outer loop)
          print(f"i={i}, j={j}")
  # Output:
  # i=0, j=0
  # i=0, j=1
  # i=0, j=2
  # i=0, j=3
  # i=1, j=0
  # i=1, j=1
  # i=1, j=2
  # i=1, j=3
  # i=2, j=0
  # i=2, j=1
  # i=2, j=2
  # i=2, j=3

  # Example: Printing a star pattern
  rows = 5
  for i in range(rows): # Outer loop for rows
      for j in range(i + 1): # Inner loop for columns (number of stars in each row increases)
          print("*", end=" ") # Print a star and a space, end=' ' keeps output on the same line
      print() # Move to the next line after each row is printed
  # Output:
  # *
  # * *
  # * * *
  # * * * *
  # * * * * *
  ```

---

**Exercises:**

### Week 1: Python Fundamentals I - Day 5: Exercises

1.  **Sum of Numbers:** Write a program to calculate the sum of numbers from 1 to 10 using a `for` loop.

2.  **Factorial of a Number:** Write a program to calculate the factorial of a given number. Take the number as input from the user. (Factorial of n = 1 _ 2 _ 3 _ ... _ n). Use a `for` loop.

3.  **Multiplication Table:** Write a program to print the multiplication table of a given number up to 10. Take the number as input. Use a `for` loop.

4.  **Count Digits in a Number:** Write a program to count the number of digits in a given integer. Take the integer as input. Use a `while` loop. (Hint: You can repeatedly divide the number by 10 until it becomes 0 and count the divisions).

5.  **Simple Number Guessing Game:** Create a simple number guessing game. Generate a random number between 1 and 10 (you can just hardcode a secret number for now, we'll use random number generation later). Ask the user to guess the number. Use a `while` loop to keep asking until the user guesses correctly. Give hints like "Too high" or "Too low" after each incorrect guess. Once guessed correctly, print "Congratulations! You guessed it!". Use `break` to exit the loop when the guess is correct.

---

**Daily Simple Task:**

### Daily Simple Task - Day 5

Write a program to print numbers from 1 to 5 using a `while` loop.
