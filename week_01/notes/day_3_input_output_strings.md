## Week 1, Day 3: Input and Output, String Manipulation - COMPLETE

**Lesson Plan:**

1.  **Input & Output**
    *   Recap of Day 2, Q\&A. Briefly review Variables, Data Types, and Operators. Address any questions learners might have from Day 2's topics and exercises.
    *   `input()` function: Taking user input from the console.
        *   Explain that `input()` pauses the program and waits for user input.
        *   Emphasize that `input()` always returns a string. Type conversion to `int` or `float` is often necessary for numerical input.
        *   Demonstrate using prompt messages within `input()` to guide the user (e.g., `input("Enter your name: ")`).
    *   `print()` function: Displaying output to the console.
        *   Explain `print()`'s role in displaying information to the user.
        *   Demonstrate printing variables, string literals, and expressions.
        *   Formatting output techniques:
            *   **f-strings (formatted string literals)** - Explain this as the modern and preferred method. Demonstrate embedding variables and expressions in strings using curly braces `{}` and format specifiers (e.g., `:.2f` for floats).
            *   **.format() method** - Introduce this as an older but still encountered method. Show examples using placeholders `{}` and the `.format()` method.
            *   **String concatenation using `+`** - Briefly mention and demonstrate string concatenation with `+`, but highlight its inefficiency for complex formatting and prefer f-strings or `.format()`.
            *   Explain the `sep` parameter to control separators between printed items (default space) and `end` parameter to control what's printed at the end (default newline `\n`).
    *   Examples showcasing different input and output techniques in the IDE. Live code demonstrations using VS Code or PyCharm to illustrate all `input()` and `print()` features, including various formatting methods. Encourage learners to experiment alongside.
2.  **String Manipulation**
    *   Strings as sequences:
        *   Explain that strings are ordered sequences of characters.
        *   **Indexing**: Demonstrate accessing individual characters using square brackets `[]` and zero-based indexing. Show positive and negative indexing.
        *   **Slicing**: Explain how to extract substrings using slicing `[:]` with `start`, `end`, and `step`. Demonstrate various slicing examples including omitting `start` or `end`, and using step values (including negative step for reversing).
        *   **Immutability**:  Crucially explain that strings are immutable. Attempting to modify a string in place will result in an error. String operations create *new* strings. Demonstrate this with an example trying to change a character and then show string manipulation creating a new string.
    *   String operations:
        *   **Concatenation (`+`)**: Demonstrate joining strings using the `+` operator.
        *   **Repetition (`*`)**: Show how to repeat a string using the `*` operator.
    *   Common string methods:  Introduce and demonstrate key string methods:
        *   **Case conversion**: `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`. Show examples of each and explain their effects.
        *   **Whitespace manipulation**: `.strip()`, `.lstrip()`, `.rstrip()`. Explain how they remove leading/trailing whitespace and demonstrate their usage.
        *   **Finding and replacing**: `.find()`, `.rfind()`, `.index()`, `.rindex()`, `.replace()`. Explain the difference between `find()` (returns -1 if not found) and `index()` (raises ValueError). Show examples of finding substrings, replacing substrings (with and without count parameter).
        *   **Splitting and joining**: `.split()`, `.join()`. Explain how `split()` breaks a string into a list of substrings based on a separator and how `join()` does the reverse, joining a list of strings into a single string using a separator.
        *   **Checking string content**: `.startswith()`, `.endswith()`, `.isalpha()`, `.isdigit()`, `.isalnum()`, `.isspace()`. Explain that these methods return boolean values and demonstrate their usage for validating string content.
    *   **Hands-on Exercises:** Learners practice string manipulation techniques to solve problems. Exercises should include tasks like:
        *   Extracting parts of strings using indexing and slicing.
        *   Changing string case.
        *   Removing whitespace.
        *   Searching for substrings.
        *   Replacing substrings.
        *   Splitting and joining strings.
        *   Checking string properties.
    *   **Q\&A and wrap-up:** Dedicate time for questions. Briefly recap `input()` and `print()` functions and string manipulation concepts. Preview Day 4's topic: Conditional Statements.

---

**Study Material & Notes:**

### Week 1: Python Fundamentals I - Day 3: Input and Output, String Manipulation

**Notes:**

#### Input and Output:

*   **`input()` function:** Used to get input from the user.

    *   When `input()` is called, the program pauses and waits for the user to type something and press Enter.
    *   Whatever the user types is returned by `input()` as a **string**.
    *   **Syntax:** `input([prompt])`
        *   `prompt` (optional): A string that is displayed to the user before they enter input.
    *   **Example:**

        ```python
        name = input("Enter your name: ") # Prompt message: "Enter your name: "
        print("Hello, " + name + "!")
        ```
    *   Since `input()` always returns a string, if you need to work with numbers, you'll need to convert the input string to the desired numeric type using `int()` or `float()`.

        ```python
        age_str = input("Enter your age: ")
        age = int(age_str) # Convert input string to integer
        print("You will be", age + 1, "next year.")
        ```

*   **`print()` function:** Used to display output to the console.

    *   **Syntax:** `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`
        *   `*objects`:  One or more objects to be printed (separated by commas).
        *   `sep=' '`:  Separator between the objects (default is a space).
        *   `end='\n'`:  What to print at the end of the output (default is a newline character `\n` which moves the cursor to the next line).
        *   `file=sys.stdout`:  Where to print the output (default is the standard output, i.e., the console).
    *   **Formatting Output with `print()`:**

        1.  **f-strings (Formatted String Literals) - Recommended:**
            *   Most modern and readable way to format strings.
            *   Start a string with `f` or `F` before the opening quote.
            *   Place variables or expressions inside curly braces `{}` within the string.
            *   Python will evaluate the expressions inside `{}` and insert their values into the string.

            ```python
            name = "Alice"
            age = 30
            print(f"Name: {name}, Age: {age}") # Output: Name: Alice, Age: 30

            price = 99.5
            quantity = 3
            total_cost = price * quantity
            print(f"Price per item: ${price:.2f}, Quantity: {quantity}, Total: ${total_cost:.2f}")
            # Output: Price per item: $99.50, Quantity: 3, Total: $298.50 (:.2f formats float to 2 decimal places)
            ```

        2.  **.format() method:** (Older style, but still seen)
            *   Use curly braces `{}` as placeholders in the string.
            *   Call the `.format()` method on the string and pass the values to be inserted in order.

            ```python
            name = "Bob"
            age = 25
            print("Name: {}, Age: {}".format(name, age)) # Output: Name: Bob, Age: 25

            print("Value of pi is approximately {:.3f}".format(3.14159265359)) # Output: Value of pi is approximately 3.142
            ```

        3.  **String Concatenation with `+`:** (Can be less readable for complex formatting)
            *   Use the `+` operator to join strings together. You need to explicitly convert non-string values to strings using `str()` before concatenating.

            ```python
            greeting = "Hello, " + name + "!" # Name should be a string variable
            print(greeting)
            ```

        4.  **`sep` and `end` parameters:**
            *   `sep`: Change the separator between multiple objects printed with `print()`.
            *   `end`: Change what's printed at the end of the `print()` output (default newline `\n`).

            ```python
            print("apple", "banana", "cherry", sep=", ") # Output: apple, banana, cherry
            print("First line", end="--") # Output: First line--Second line (on the same line)
            print("Second line")
            ```

#### String Manipulation:

*   **Strings as Sequences:** Strings are ordered sequences of characters. You can access individual characters using indexing and get substrings using slicing.

    *   **Indexing:** Access a character at a specific position (index starts from 0).

        ```python
        message = "Python"
        first_char = message[0] # 'P'
        second_char = message[1] # 'y'
        last_char = message[-1] # 'n' (negative indexing starts from the end, -1 is the last character)
        print(first_char, last_char) # Output: P n
        ```

    *   **Slicing:** Extract a substring (a portion of a string). Syntax: `string[start:end:step]`
        *   `start`: Starting index (inclusive, default 0).
        *   `end`: Ending index (exclusive, default end of string).
        *   `step`: Step size (optional, default 1).

        ```python
        text = "Hello World"
        substring1 = text[0:5] # "Hello" (characters from index 0 up to, but not including, index 5)
        substring2 = text[:5] # Same as text[0:5]
        substring3 = text[6:] # "World" (characters from index 6 to the end)
        substring4 = text[::2] # "HloWrd" (every second character)
        substring5 = text[::-1] # "dlroW olleH" (reverse the string)
        print(substring1, substring2, substring3, substring4, substring5)
        ```

    *   **Immutability:** Strings in Python are immutable. Once a string is created, you cannot change its characters directly. String operations create new strings.

        ```python
        text = "Hello"
        # text[0] = 'J'  # This will cause an error! Strings are immutable.
        new_text = 'J' + text[1:] # Create a new string by concatenation and slicing
        print(new_text) # Output: Jello
        ```

*   **String Operations:**

    *   **Concatenation (+):** Join strings together.

        ```python
        str1 = "Hello"
        str2 = "World"
        combined_str = str1 + " " + str2 # "Hello World"
        ```

    *   **Repetition (\*):** Repeat a string multiple times.

        ```python
        repeated_str = "Python" * 3 # "PythonPythonPython"
        ```

*   **Common String Methods:** (Strings in Python have many built-in methods. Here are some important ones)

    *   **Case Conversion:**
        *   `.upper()`: Returns a new string with all characters in uppercase.
        *   `.lower()`: Returns a new string with all characters in lowercase.
        *   `.title()`: Returns a new string with the first letter of each word capitalized.
        *   `.capitalize()`: Returns a new string with the first letter capitalized and the rest lowercase.
        *   `.swapcase()`: Returns a new string with the case of all characters swapped.

        ```python
        text = "hello WORLD"
        print(text.upper())      # HELLO WORLD
        print(text.lower())      # hello world
        print(text.title())      # Hello World
        print(text.capitalize()) # Hello world
        print(text.swapcase())   # HELLO world
        ```

    *   **Whitespace Manipulation:**
        *   `.strip()`: Returns a new string with leading and trailing whitespace removed.
        *   `.lstrip()`: Returns a new string with leading whitespace removed (left strip).
        *   `.rstrip()`: Returns a new string with trailing whitespace removed (right strip).

        ```python
        text = "  \t  Example with spaces and tabs  \n  "
        print(text.strip())   # 'Example with spaces and tabs'
        print(text.lstrip())  # 'Example with spaces and tabs  \n  '
        print(text.rstrip())  # '  \t  Example with spaces and tabs'
        ```

    *   **Finding and Replacing:**
        *   `.find(substring, [start, end])`: Returns the index of the first occurrence of `substring`. Returns -1 if not found. Optional `start` and `end` arguments specify the search range.
        *   `.rfind(substring, [start, end])`:  Same as `find()` but searches from the right (returns index of the *last* occurrence).
        *   `.index(substring, [start, end])`: Same as `find()` but raises a `ValueError` if `substring` is not found.
        *   `.rindex(substring, [start, end])`: Same as `index()` but searches from the right.
        *   `.replace(old, new, [count])`: Returns a new string where all occurrences of `old` are replaced with `new`. Optional `count` argument limits the number of replacements.

        ```python
        message = "Hello World, Hello Python"
        print(message.find("Hello"))    # 0 (first occurrence of "Hello" starts at index 0)
        print(message.rfind("Hello"))   # 13 (last occurrence of "Hello" starts at index 13)
        print(message.find("World"))    # 6
        print(message.find("Java"))     # -1 (not found)
        # print(message.index("Java"))  # ValueError: substring not found

        new_message = message.replace("Hello", "Hi")
        print(new_message) # Output: Hi World, Hi Python

        replaced_once = message.replace("Hello", "Hi", 1) # Replace only the first occurrence
        print(replaced_once) # Output: Hi World, Hello Python
        ```

    *   **Splitting and Joining:**
        *   `.split(separator=None, maxsplit=-1)`: Splits a string into a list of substrings based on the `separator`. If `separator` is not specified or `None`, splits by whitespace. `maxsplit` limits the number of splits.
        *   `.join(iterable)`: Joins elements of an iterable (like a list or tuple of strings) into a single string, using the string on which `.join()` is called as a separator.

        ```python
        sentence = "This is a sample sentence."
        words = sentence.split() # Split by whitespace (default) -> ['This', 'is', 'a', 'sample', 'sentence.']
        words_comma_separated = "apple,banana,cherry".split(",") # Split by comma -> ['apple', 'banana', 'cherry']

        words_list = ['This', 'is', 'a', 'joined', 'string']
        joined_sentence = " ".join(words_list) # Join with space as separator -> "This is a joined string"
        comma_joined = ",".join(words_list) # Join with comma and space -> "This,is,a,joined,string"
        ```

    *   **Checking String Content:**  Return boolean values (`True` or `False`).
        *   `.startswith(prefix, [start, end])`: Checks if the string starts with the given `prefix`.
        *   `.endswith(suffix, [start, end])`: Checks if the string ends with the given `suffix`.
        *   `.isalpha()`: Checks if all characters in the string are alphabetic (letters).
        *   `.isdigit()`: Checks if all characters in the string are digits (0-9).
        *   `.isalnum()`: Checks if all characters are alphanumeric (letters or digits).
        *   `.isspace()`: Checks if all characters are whitespace characters (space, tab, newline, etc.).

        ```python
        text = "HelloWorld123"
        print(text.startswith("Hello")) # True
        print(text.endswith("456"))   # False
        print("Alphabet".isalpha())     # True
        print("12345".isdigit())       # True
        print("Alphanumeric123".isalnum()) # True
        print("  \t\n".isspace())         # True
        ```

---

**Exercises:**

### Week 1: Python Fundamentals I - Day 3: Exercises

1.  **Greeting Message:** Write a program that takes the user's first name and last name as input separately and then prints a full greeting message like "Hello, [FirstName] [LastName]! Welcome!". Use f-strings for formatting.



2.  **String Length and First Character:** Ask the user to enter a string. Print the length of the string and its first character.

   

3.  **Word Count:** Write a program that takes a sentence as input and counts the number of words in it. (Assume words are separated by spaces). Use the `split()` method.

   

4.  **Email Validation (Basic):** Ask the user to enter an email address. Check if the email address contains the "@" symbol and a "." symbol. Print "Valid Email" or "Invalid Email" based on this simple check. (Note: This is a very basic validation and not a complete email validation).

    

5.  **Reverse String:** Ask the user to enter a string. Print the reverse of the string using slicing.

   

---

**Daily Simple Task:**

### Daily Simple Task - Day 3

Write a program that takes user's name and age as input and prints a formatted greeting message using f-strings.

