## Week 1, Day 2: Variables, Data Types, and Operators - COMPLETE

**Lesson Plan:**

1.  **Variables, Data Types**
    *   Recap of Day 1, Q\&A. Briefly review Python's features, setup process, and basic syntax (indentation, comments). Address any questions learners might have from Day 1's setup.
    *   What are variables? Explain the concept of variables as named storage locations in memory. Use analogies like containers.
    *   Variable naming rules and conventions in Python. Clearly outline the rules (start with letter/underscore, alphanumeric, case-sensitive, no keywords) and best practices (descriptive names, snake\_case).
    *   Assignment operator (`=`). Explain its function for assigning values to variables. Differentiate between assignment and equality comparison (which will come later).
    *   Data Types: Introduce the fundamental data types in Python:
        *   **Numeric Types:**
            *   Integers (`int`): Whole numbers, examples, range (conceptually infinite in Python).
            *   Floating-point numbers (`float`): Numbers with decimals, examples, precision limitations (briefly mention).
        *   **Text Type:**
            *   Strings (`str`): Sequences of characters, different ways to define strings (single, double, triple quotes), immutability of strings.
        *   **Boolean Type:**
            *   Booleans (`bool`): `True` and `False` values, use in logic.
        *   Introduction to `type()` function to check data type. Demonstrate its usage to verify the type of variables.
        *   Type conversion/casting (implicit and explicit). Explain the need for type conversion, differentiate between implicit (automatic by Python) and explicit (using functions like `int()`, `float()`, `str()`, `bool()`). Show examples of both.
    *   Examples and demonstrations in the IDE. Live code examples in VS Code or PyCharm to illustrate variables, data types, and type conversions. Encourage learners to follow along and experiment.
2.  **Operators & Hands-on Practice**
    *   Operators in Python:  Introduce and explain each operator category with examples:
        *   **Arithmetic Operators:** `+`, `-`, `*`, `/`, `//` (floor division - explain integer division vs. float division), `%` (modulo - explain remainder), `**` (exponentiation). Provide clear examples of each.
        *   **Comparison Operators:** `==` (equal to - differentiate from assignment `=`), `!=` (not equal to), `>`, `<`, `>=`, `<=`. Emphasize that comparison operators return boolean values.
        *   **Logical Operators:** `and`, `or`, `not`. Explain truth tables for `and` and `or`. Demonstrate use cases with boolean variables.
        *   **Assignment Operators:** `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `//=` , `**=`. Show the shorthand nature of compound assignment operators.
        *   Operator precedence (briefly). Explain PEMDAS/BODMAS rule and how parentheses can control order of operations. Provide examples to illustrate precedence.
    *   **Hands-on Exercises:** Learners engage in coding exercises that involve:
        *   Declaring variables of different data types.
        *   Performing arithmetic calculations using various operators.
        *   Using comparison and logical operators to create boolean expressions.
        *   Practicing type conversion as needed.
        *   Using assignment operators.
    *   **Example problem solving:** Guide learners through building simple programs that perform calculations based on user input, such as calculating the area of a rectangle, converting temperatures, etc.
    *   **Q\&A and wrap-up:**  Dedicate time for learners to ask questions and clarify any doubts. Briefly review the key concepts covered in Day 2.

---

**Study Material & Notes:**

### Week 1: Python Fundamentals I - Day 2: Variables, Data Types, and Operators

**Notes:**

#### Variables:

*   Variables are like named storage locations in the computer's memory that hold data.
*   Think of them as containers that can store different types of information.
*   In Python, you don't need to declare the type of a variable; it's dynamically typed.
*   **Variable Naming Rules:**
    *   Variable names must start with a letter (a-z, A-Z) or an underscore (`_`).
    *   The rest of the name can consist of letters, numbers (0-9), and underscores.
    *   Variable names are case-sensitive (`age`, `Age`, and `AGE` are different variables).
    *   Keywords (reserved words in Python, like `if`, `for`, `while`, etc.) cannot be used as variable names.
    *   **Best Practices:**
        *   Use descriptive and meaningful names (e.g., `student_name` instead of `x`).
        *   Use lowercase with words separated by underscores (snake\_case convention, e.g., `user_age`, `item_count`).

#### Assignment Operator (=):

*   The `=` symbol is the assignment operator. It's used to assign a value to a variable.
*   **Syntax:** `variable_name = value`
*   **Example:**

    ```python
    name = "Alice"
    age = 30
    price = 99.99
    is_student = False
    ```

#### Data Types:

*   Every value in Python has a data type. Common built-in data types we'll focus on today:

    1.  **Numeric Types:**

        *   **Integers (`int`):** Whole numbers (positive, negative, or zero) without a decimal point. Examples: `-5`, `0`, `10`, `1000`.
        *   **Floating-point numbers (`float`):** Numbers with a decimal point. Examples: `3.14`, `-2.5`, `0.0`, `1.23e5` (scientific notation).

    2.  **Text Type:**

        *   **Strings (`str`):** Sequences of characters. Used to represent text. Enclosed in single quotes (`'...'`), double quotes (`"..."`), or triple quotes (`'''...'''` or `"""..."""`). Examples: `"hello"`, `'Python'`, `"""Multi-line string"""`.

    3.  **Boolean Type:**

        *   **Booleans (`bool`):** Represent truth values: `True` or `False` (note the capitalization). Used in logical operations and conditional statements.

#### Checking Data Type: `type()` function

*   You can use the `type()` function to find out the data type of a variable or a value.
*   **Example:**

    ```python
    x = 10
    print(type(x))  # Output: <class 'int'>

    y = 3.14
    print(type(y))  # Output: <class 'float'>

    name = "Bob"
    print(type(name)) # Output: <class 'str'>

    is_valid = True
    print(type(is_valid)) # Output: <class 'bool'>
    ```

#### Type Conversion (Type Casting):

*   Sometimes you need to convert a value from one data type to another. This is called type conversion or type casting.

*   **Explicit Type Conversion:** You explicitly use functions like `int()`, `float()`, `str()`, `bool()` to convert.

    *   `int(value)`: Converts to integer (if possible).

    *   `float(value)`: Converts to float (if possible).

    *   `str(value)`: Converts to string.

    *   `bool(value)`: Converts to boolean (various values evaluate to `True` or `False` - more on this later).

    *   **Examples:**

        ```python
        num_str = "123"
        num_int = int(num_str) # Convert string "123" to integer 123
        print(num_int, type(num_int)) # Output: 123 <class 'int'>

        num_float = float(num_int) # Convert integer 123 to float 123.0
        print(num_float, type(num_float)) # Output: 123.0 <class 'float'>

        str_num = str(num_float) # Convert float 123.0 to string "123.0"
        print(str_num, type(str_num)) # Output: 123.0 <class 'str'>

        bool_val = bool(0) # Convert integer 0 to boolean False (0 is generally False, non-zero is True)
        print(bool_val, type(bool_val)) # Output: False <class 'bool'>
        ```

*   **Implicit Type Conversion:** Python sometimes performs type conversion automatically (implicitly), especially in arithmetic operations.

    *   **Example:**

        ```python
        result = 5 + 2.5 # Integer + float = float result
        print(result, type(result)) # Output: 7.5 <class 'float'>
        ```

#### Operators:

*   Operators are special symbols in Python that perform operations on values (operands).

    1.  **Arithmetic Operators:**  Used for mathematical calculations.

        | Operator | Operation          | Example     | Result |
        | :------- | :----------------- | :---------- | :----- |
        | `+`      | Addition           | `5 + 3`     | `8`    |
        | `-`      | Subtraction        | `10 - 4`    | `6`    |
        | `*`      | Multiplication     | `6 * 7`     | `42`   |
        | `/`      | Division           | `15 / 4`    | `3.75` |
        | `//`     | Floor Division     | `15 // 4`   | `3`    |
        | `%`      | Modulo (remainder) | `15 % 4`    | `3`    |
        | `**`     | Exponentiation     | `2** 3`    | `8`    |

    2.  **Comparison Operators:** Used to compare values. Result is always a boolean (`True` or `False`).

        | Operator | Operation                  | Example     | Result |
        | :------- | :------------------------- | :---------- | :----- |
        | `==`     | Equal to                   | `5 == 5`    | `True` |
        | `!=`     | Not equal to               | `5 != 6`    | `True` |
        | `>`      | Greater than               | `10 > 5`    | `True` |
        | `<`      | Less than                  | `3 < 7`     | `True` |
        | `>=`     | Greater than or equal to   | `5 >= 5`    | `True` |
        | `<=`     | Less than or equal to      | `4 <= 5`    | `True` |

    3.  **Logical Operators:** Used to combine or modify boolean values.

        | Operator | Description                                     | Example                     | Result |
        | :------- | :---------------------------------------------- | :-------------------------- | :----- |
        | `and`    | Logical AND. Returns `True` if both operands are `True`. | `True and True`           | `True` |
        | `or`     | Logical OR. Returns `True` if at least one operand is `True`.  | `True or False`          | `True` |
        | `not`    | Logical NOT. Returns the opposite boolean value.         | `not True`                | `False`|

    4.  **Assignment Operators:** Shorthand operators to perform an operation and assign the result back to the variable.

        | Operator | Example     | Equivalent to |
        | :------- | :---------- | :------------ |
        | `=`      | `x = 5`     | `x = 5`       |
        | `+=`     | `x += 2`    | `x = x + 2`   |
        | `-=`     | `x -= 3`    | `x = x - 3`   |
        | `*=`     | `x *= 4`    | `x = x * 4`   |
        | `/=`     | `x /= 2`    | `x = x / 2`   |
        | `%=`     | `x %= 5`    | `x = x % 5`   |
        | `//=`    | `x //= 3`   | `x = x // 3`  |
        | `**=`     | `x **= 2`   | `x = x ** 2`  |

#### Operator Precedence (Order of Operations - PEMDAS/BODMAS applies):

1.  Parentheses `()`
2.  Exponentiation `**`
3.  Multiplication `*`, Division `/`, Floor Division `//`, Modulo `%` (from left to right)
4.  Addition `+`, Subtraction `-` (from left to right)
5.  Comparison operators (`==`, `!=`, `>`, `<`, `>=`, `<=`)
6.  Logical NOT `not`
7.  Logical AND `and`
8.  Logical OR `or`
9.  Assignment operators (`=`, `+=`, `-=`, etc.)

---

**Exercises:**

### Week 1: Python Fundamentals I - Day 2: Exercises

---

**Daily Simple Task:**

### Daily Simple Task - Day 2

