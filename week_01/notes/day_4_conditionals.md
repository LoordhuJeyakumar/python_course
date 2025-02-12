## Week 1, Day 4: Conditionals (Conditional Statements) - COMPLETE

**Lesson Plan:**

1.  **Conditional Statements**
    - Recap of Day 3, Q\&A. Briefly review Input/Output and String Manipulation. Address any questions learners might have from Day 3's topics and exercises.
    - Introduction to Conditional Statements: Why we need decision-making in programs. Real-world analogies (traffic lights, thermostats).
    - `if` statement: Basic syntax and flow.
      - Explain the `if` keyword, the condition (boolean expression), and the colon `:`.
      - Indentation for the code block under `if`.
      - Demonstrate simple `if` statement examples: checking if a number is positive, if a string is empty, etc.
    - `else` statement: Extending `if` with an alternative path.
      - Explain `else` keyword, its placement after the `if` block, and the colon `:`.
      - Indentation for the `else` code block.
      - Examples using `if-else` for binary decisions: even/odd number, adult/minor, etc.
    - `elif` statement: Handling multiple conditions.
      - Explain `elif` (else if) for checking multiple mutually exclusive conditions.
      - Syntax of `elif` blocks placed between `if` and `else`.
      - Order of `elif` conditions is important - first true condition's block executes.
      - Demonstrate using `if-elif-else` for multi-way decisions: grading system based on marks, categorizing temperature ranges (freezing, cold, moderate, hot), etc.
    - Boolean Expressions in Conditionals:
      - Review boolean values (`True`, `False`) and boolean data type.
      - Explain how comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`) and logical operators (`and`, `or`, `not`) are used to form boolean expressions for conditions.
      - Truth tables for `and`, `or`, `not` (revisit briefly).
      - Examples of complex boolean conditions using `and`, `or`, `not`.
    - Nested `if` statements (Introduction):
      - Briefly introduce the concept of nesting `if` statements inside other `if`, `elif`, or `else` blocks.
      - Explain how nesting allows for more complex decision-making logic, but can make code harder to read if overused.
      - Simple example of nested `if` for demonstration, but caution against excessive nesting early on.
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate all conditional statement structures with various boolean expressions. Encourage learners to experiment.
2.  **Hands-on Practice & Exercises**
    - Learners work on coding exercises that involve:
      - Writing simple `if` statements based on different conditions.
      - Using `if-else` for binary decisions.
      - Implementing `if-elif-else` for multiple conditions.
      - Constructing boolean expressions using comparison and logical operators.
      - (Optional, if time permits) Simple nested `if` problems.
    - Example problem solving: Guide learners to solve problems like:
      - Determining the largest of three numbers.
      - Checking if a year is a leap year.
      - Creating a simple calculator that performs different operations based on user input.
      - Building a basic traffic light simulation based on time of day.
    - Q\&A and wrap-up: Address learner questions and clarify any confusion. Recap the different types of conditional statements (`if`, `elif`, `else`) and boolean expressions. Preview Day 5's topic: Loops.

---

**Study Material & Notes:**

### Week 1: Python Fundamentals I - Day 4: Conditional Statements (`if`, `elif`, `else`)

**Notes:**

#### Conditional Statements (Decision Making):

- Conditional statements allow your program to make decisions and execute different blocks of code based on whether certain conditions are true or false.
- They control the flow of execution in your program.
- Python uses keywords `if`, `elif` (else if), and `else` to create conditional statements.

#### 1. `if` statement:

- The most basic conditional statement. Executes a block of code **only if** a condition is `True`.
- **Syntax:**

  ```python
  if condition:
      # Code to be executed if the condition is True
      statement1
      statement2
      ...
  # Code here will always execute after the if block (regardless of condition)
  ```

  - `condition`: An expression that evaluates to either `True` or `False` (a boolean expression).
  - The code block under the `if` statement **must be indented**. Indentation is crucial in Python to define code blocks.
  - If `condition` is `True`, the indented code block is executed. If `condition` is `False`, the code block is skipped, and the program execution continues after the `if` block.

- **Example:**

  ```python
  age = 20
  if age >= 18:
      print("You are an adult.") # This line will be executed because 20 >= 18 is True

  number = -5
  if number > 0:
      print("The number is positive.") # This line will NOT be executed because -5 > 0 is False

  print("This line will always be printed.") # Always executed
  ```

#### 2. `else` statement:

- Used with an `if` statement to execute a block of code when the `if` condition is `False`.
- Provides an alternative path of execution.
- **Syntax:**

  ```python
  if condition:
      # Code to be executed if condition is True
      statement_if_true
  else:
      # Code to be executed if condition is False
      statement_if_false
  # Code here will always execute after the if-else block
  ```

  - The `else` block is executed only when the `if` condition evaluates to `False`.
  - Like `if`, the code block under `else` must be indented.

- **Example:**

  ```python
  number = 7
  if number % 2 == 0: # Check if number is even (remainder when divided by 2 is 0)
      print("The number is even.")
  else:
      print("The number is odd.") # This line will be executed because 7 is not even

  is_raining = False
  if is_raining:
      print("Bring an umbrella.")
  else:
      print("Enjoy the sunshine!") # This line will be executed because is_raining is False
  ```

#### 3. `elif` statement (else if):

- Used to check multiple conditions in sequence. Allows you to have several mutually exclusive conditions.
- Short for "else if". You can have zero or more `elif` clauses after an `if` and before an optional `else`.
- **Syntax:**

  ```python
  if condition1:
      # Code for condition1 being True
      statement1
  elif condition2:
      # Code for condition2 being True (only if condition1 was False)
      statement2
  elif condition3:
      # Code for condition3 being True (only if condition1 and condition2 were False)
      statement3
  ... # You can have more elif blocks
  else: # Optional else block
      # Code to be executed if none of the above conditions were True
      statement_else
  # Code here will always execute after the if-elif-else block
  ```

  - Conditions are checked in order from top to bottom.
  - As soon as one of the `if` or `elif` conditions is `True`, its corresponding code block is executed, and the rest of the `elif` and `else` blocks are skipped.
  - If none of the `if` or `elif` conditions are `True`, and an `else` block is present, the `else` block is executed. If no `else` block is present and none of the conditions are true, then no code block within the conditional structure is executed.

- **Example:**

  ```python
  score = 75

  if score >= 90:
      grade = "A"
  elif score >= 80: # Only checked if score < 90
      grade = "B"
  elif score >= 70: # Only checked if score < 80
      grade = "C"
  elif score >= 60: # Only checked if score < 70
      grade = "D"
  else: # Executed if score < 60
      grade = "F"

  print(f"Score: {score}, Grade: {grade}") # Output: Score: 75, Grade: C

  temperature = 15 # Celsius
  if temperature < 0:
      weather = "Freezing"
  elif temperature < 10:
      weather = "Very Cold"
  elif temperature < 20:
      weather = "Cold" # This block will execute as 15 < 20 is True, and previous conditions were False
  elif temperature < 30:
      weather = "Moderate"
  else:
      weather = "Hot"

  print(f"Temperature: {temperature}°C, Weather: {weather}") # Output: Temperature: 15°C, Weather: Cold
  ```

#### Boolean Expressions in Conditionals:

- Conditions in `if`, `elif` statements must be boolean expressions, meaning they must evaluate to either `True` or `False`.
- Boolean expressions are often formed using:

  - **Comparison Operators:** `==`, `!=`, `>`, `<`, `>=`, `<=`
  - **Logical Operators:** `and`, `or`, `not`
  - Boolean variables or function calls that return boolean values.

- **Examples of Boolean Expressions:**

  ```python
  age = 25
  is_student = False

  if age > 18: # Comparison operator
      print("Adult")

  if is_student == True: # Boolean variable
      print("Student")

  if age > 18 and not is_student: # Logical operators and comparison
      print("Adult, but not a student")

  if "apple" in "I like apples": # 'in' operator (membership - we will learn more later, but can be used in boolean expressions)
      print("Sentence contains 'apple'")
  ```

#### Nested `if` statements (Introduction):

- You can put `if`, `elif`, and `else` statements inside other `if`, `elif`, or `else` blocks. This is called nesting.
- Used for more complex decision-making when one condition depends on another.
- **Example:**

  ```python
  x = 10
  y = 5

  if x > 0:
      print("x is positive")
      if y > 0: # Nested if statement
          print("y is also positive")
      else: # Nested else statement (associated with the inner if)
          print("y is not positive")
  else: # else statement associated with the outer if
      print("x is not positive")
  ```

- **Caution:** While nesting is possible, deeply nested `if` statements can make code harder to read and understand. For complex scenarios, consider alternative approaches like using functions or breaking down logic into smaller, more manageable parts.

---

**Exercises:**

### Week 1: Python Fundamentals I - Day 4: Exercises

1.  **Positive, Negative, or Zero:** Write a program that takes a number as input and checks if it is positive, negative, or zero. Print an appropriate message.

2.  **Even or Odd:** Write a program that takes an integer as input and determines if it is even or odd. Print "Even" or "Odd".

3.  **Largest of Two Numbers:** Write a program that takes two numbers as input and prints the larger number. If both are equal, print "Numbers are equal".

4.  **Grading System:** Write a program to assign grades based on marks obtained by a student. Use the following grading scale:

    - 90 and above: A+
    - 80-89: A
    - 70-79: B
    - 60-69: C
    - Below 60: Fail
      Take the marks as input and print the corresponding grade.

5.  **Leap Year Check:** Write a program to determine if a given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. Take the year as input and print "Leap Year" or "Not a Leap Year".

---

**Daily Simple Task:**

### Daily Simple Task - Day 4

Write a program that takes user's age as input and checks if they are eligible to vote (age 18 or above). Print "Eligible to vote" or "Not eligible to vote".
