## Week 2, Day 1: Data Structures - Lists - COMPLETE

**Lesson Plan:**

1.  **Introduction to Lists**
    - Recap of Week 1 Assignment, Q\&A. Briefly discuss common challenges and key learnings from the Week 1 assignment. Address any questions related to the assignment or Week 1 topics.
    - Introduction to Data Structures: What are data structures and why are they important for organizing data? Briefly contrast simple variables with structures that can hold collections of data.
    - Introduction to Lists in Python:
      - Definition: Ordered, mutable collections of items. Emphasize "ordered" (maintains insertion order) and "mutable" (can be changed after creation).
      - Why Lists? Use cases: storing collections of similar items, representing sequences, dynamic data storage.
      - Creating Lists:
        - Using square brackets `[]`: Empty list `[]`, list with initial elements `[1, 2, 3]`, list of different data types `[1, "hello", 3.14, True]`.
        - Using the `list()` constructor: `list()`, `list("hello")` (creates list of characters), `list((1, 2, 3))` (from tuple - briefly mention tuples).
    - Accessing List Elements:
      - Indexing: Zero-based indexing. Accessing elements using positive and negative indices (forward and backward access).
      - IndexError: What happens when you try to access an index that is out of range.
    - List Slicing:
      - Extracting sublists using slicing `[:]`: `list[start:end:step]`.
      - Slicing with positive and negative indices.
      - Omitting `start`, `end`, or `step` in slicing.
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate list creation, indexing, and slicing. Encourage learners to experiment and observe the behavior.
2.  **List Mutability, Operations, and Methods**
    - List Mutability in Detail:
      - Demonstrate that lists are mutable: you can change their contents after creation.
      - Modifying list elements using indexing: `list[index] = new_value`.
      - Adding elements:
        - `.append(item)`: Adds an item to the end of the list.
        - `.insert(index, item)`: Inserts an item at a specific index.
      - Removing elements:
        - `.remove(item)`: Removes the first occurrence of a specific item (ValueError if not found).
        - `.pop([index])`: Removes and returns the item at a given index (default: last item). `del list[index]` also to delete by index.
        - `.clear()`: Removes all items from the list.
      - List Operations:
        - Concatenation (`+`): Joining two lists to create a new list.
        - Repetition (`*`): Repeating a list multiple times to create a new list.
      - Other useful list methods:
        - `.index(item, [start, end])`: Finds the index of the first occurrence of an item (ValueError if not found).
        - `.count(item)`: Counts the number of occurrences of an item in the list.
        - `len(list)`: Returns the number of items in the list.
        - `sorted(list)`: Returns a _new_ sorted list (non-mutating).
        - `list.sort()`: Sorts the list _in place_ (mutating).
        - `list.reverse()`: Reverses the list _in place_ (mutating).
        - `copy()`: Creates a shallow copy of the list. (Briefly introduce the concept of shallow vs. deep copy, but focus on basic usage for now).
    - **Hands-on Exercises:** Learners practice list operations and methods. Exercises should include tasks like:
      - Creating lists and accessing elements.
      - Modifying lists by adding, inserting, and removing elements.
      - Using list slicing to extract sublists.
      - Applying various list methods (`append`, `insert`, `remove`, `pop`, `index`, `count`, `sort`, `reverse`).
      - Solving problems that require list manipulation.
    - Example problem solving: Guide learners to solve problems like:
      - Reversing a list.
      - Finding the maximum/minimum element in a list (without using built-in `max`/`min` initially, then show using them later).
      - Filtering a list based on a condition (e.g., extracting even numbers from a list).
      - Creating a list of squares of numbers in a range.
    - Q\&A and wrap-up: Address learner questions. Recap list creation, indexing, slicing, mutability, operations, and key methods. Preview Day 2's topics: Tuples and Sets.

---

**Study Material & Notes:**

### Week 2: Data Structures - Day 1: Lists

**Notes:**

#### Introduction to Data Structures

- Data structures are ways to organize and store data in a computer so that it can be used efficiently.
- They provide different ways to structure data based on the relationships between the data and the operations you need to perform on them.
- In Python, we have several built-in data structures: Lists, Tuples, Sets, Dictionaries (we will cover these in Week 2).

#### Lists in Python

- **Definition:** Lists are **ordered** and **mutable** collections of items.

  - **Ordered:** Items in a list have a defined order, and that order is maintained. When you add items to a list, they stay in that order unless you explicitly change it.
  - **Mutable:** You can change the contents of a list after it's created. You can add, remove, or modify items in a list.
  - Lists can contain items of **different data types**.

- **Why Lists?**

  - Store collections of related items (e.g., a list of student names, a list of product prices).
  - Represent ordered sequences of data.
  - Dynamically grow or shrink in size as needed.
  - Used extensively in Python programming.

- **Creating Lists:**

  1.  **Using Square Brackets `[]`:**

      - **Empty list:**

        ```python
        my_list = []
        print(my_list) # Output: []
        print(type(my_list)) # Output: <class 'list'>
        ```

      - **List with initial elements:**

        ```python
        numbers = [10, 20, 30, 40, 50]
        print(numbers) # Output: [10, 20, 30, 40, 50]

        mixed_list = [1, "apple", 3.14, True] # Different data types
        print(mixed_list) # Output: [1, 'apple', 3.14, True]
        ```

  2.  **Using the `list()` constructor:**

      - **Creating an empty list:**

        ```python
        another_list = list()
        print(another_list) # Output: []
        ```

      - **Creating a list from an iterable (like a string or tuple):**

        ```python
        char_list = list("hello") # Create list of characters from string
        print(char_list) # Output: ['h', 'e', 'l', 'l', 'o']

        tuple_data = (1, 2, 3) # Tuple (covered later)
        list_from_tuple = list(tuple_data)
        print(list_from_tuple) # Output: [1, 2, 3]
        ```

#### Accessing List Elements: Indexing

- Lists are ordered, so each item has a position or index, starting from 0 for the first item.
- Use square brackets `[]` to access elements by their index.

  - **Positive Indexing:** Starts from 0 for the first element, 1 for the second, and so on.

    ```python
    fruits = ["apple", "banana", "cherry", "date"]
    first_fruit = fruits[0] # "apple"
    second_fruit = fruits[1] # "banana"
    third_fruit = fruits[2] # "cherry"
    last_fruit_positive_index = fruits[3] # "date"
    # fruits[4] # IndexError: list index out of range (if you try to access index beyond the last element)

    print(f"First fruit: {first_fruit}, Second fruit: {second_fruit}, Last fruit (positive index): {last_fruit_positive_index}")
    ```

  - **Negative Indexing:** Starts from -1 for the last element, -2 for the second to last, and so on.

    ```python
    fruits = ["apple", "banana", "cherry", "date"]
    last_fruit = fruits[-1] # "date"
    second_last_fruit = fruits[-2] # "cherry"
    first_fruit_negative_index = fruits[-4] # "apple"
    # fruits[-5] # IndexError: list index out of range (if you try to access index before the first element)

    print(f"Last fruit (negative index): {last_fruit}, Second last fruit: {second_last_fruit}, First fruit (negative index): {first_fruit_negative_index}")
    ```

  - **`IndexError`:** If you try to access an index that is outside the valid range of indices for the list (i.e., index less than negative list length or index greater than or equal to list length), you will get an `IndexError`.

#### List Slicing: Extracting Sublists

- Slicing allows you to extract a portion (sublist) of a list.
- Syntax: `list[start:end:step]` (Similar to string slicing)

  - `start`: Starting index (inclusive, default 0).
  - `end`: Ending index (exclusive, default end of list).
  - `step`: Step size (optional, default 1).

  ```python
  numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

  sublist1 = numbers[2:5] # [30, 40, 50] (elements from index 2 up to, but not including, index 5)
  sublist2 = numbers[:5] # [10, 20, 30, 40, 50] (from start to index 5-1)
  sublist3 = numbers[5:] # [60, 70, 80, 90, 100] (from index 5 to end)
  sublist4 = numbers[:] # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] (copy of the entire list)
  sublist5 = numbers[1:8:2] # [20, 40, 60, 80] (from index 1 to 7, with step of 2)
  sublist6 = numbers[::-1] # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10] (reverse the list)

  print(f"Original list: {numbers}")
  print(f"numbers[2:5]: {sublist1}")
  print(f"numbers[:5]: {sublist2}")
  print(f"numbers[5:]: {sublist3}")
  print(f"numbers[:]: {sublist4}")
  print(f"numbers[1:8:2]: {sublist5}")
  print(f"numbers[::-1]: {sublist6}")
  ```

#### List Mutability: Modifying Lists

- Lists are mutable, which means you can change their contents after they are created. This is a key difference from strings and tuples (which are immutable).

  - **Modifying elements by index:**

    ```python
    fruits = ["apple", "banana", "cherry"]
    fruits[1] = "grape" # Change the item at index 1 (banana -> grape)
    print(fruits) # Output: ['apple', 'grape', 'cherry']
    ```

  - **Adding elements:**

    - `.append(item)`: Adds `item` to the end of the list.

      ```python
      colors = ["red", "green", "blue"]
      colors.append("yellow") # Add "yellow" at the end
      print(colors) # Output: ['red', 'green', 'blue', 'yellow']
      ```

    - `.insert(index, item)`: Inserts `item` at the specified `index`.

      ```python
      numbers = [1, 2, 3, 4]
      numbers.insert(2, 100) # Insert 100 at index 2 (shifting elements to the right)
      print(numbers) # Output: [1, 2, 100, 3, 4]
      ```

  - **Removing elements:**

    - `.remove(item)`: Removes the first occurrence of `item` from the list. Raises `ValueError` if `item` is not in the list.

      ```python
      animals = ["cat", "dog", "rabbit", "dog"]
      animals.remove("dog") # Removes the first "dog"
      print(animals) # Output: ['cat', 'rabbit', 'dog']
      # animals.remove("elephant") # ValueError: list.remove(x): x not in list
      ```

    - `.pop([index])`: Removes and returns the item at the specified `index`. If `index` is not given, it removes and returns the last item.

      ```python
      items = ["pen", "paper", "book", "ruler"]
      removed_item = items.pop(1) # Remove and return item at index 1 ("paper")
      print(items) # Output: ['pen', 'book', 'ruler']
      print(removed_item) # Output: paper

      last_item = items.pop() # Remove and return the last item ("ruler")
      print(items) # Output: ['pen', 'book']
      print(last_item) # Output: ruler
      ```

    - `del list[index]`: `del` is a statement to delete items by index.

      ```python
      my_list = [10, 20, 30, 40, 50]
      del my_list[2] # Delete the item at index 2 (30)
      print(my_list) # Output: [10, 20, 40, 50]
      ```

    - `.clear()`: Removes all items from the list, making it an empty list.

      ```python
      data = [1, 2, 3, 4, 5]
      data.clear()
      print(data) # Output: []
      ```

#### List Operations:

- **Concatenation (+):** Joins two lists to create a new list.

  ```python
  list1 = [1, 2, 3]
  list2 = [4, 5, 6]
  combined_list = list1 + list2 # [1, 2, 3, 4, 5, 6]
  print(combined_list)
  ```

- **Repetition (\*):** Repeats a list a certain number of times to create a new list.

  ```python
  original_list = [1, 2]
  repeated_list = original_list * 3 # [1, 2, 1, 2, 1, 2]
  print(repeated_list)
  ```

#### Other Useful List Methods:

- `.index(item, [start, end])`: Returns the index of the first occurrence of `item`. Raises `ValueError` if not found. Optional `start` and `end` specify search range.

  ```python
  letters = ['a', 'b', 'c', 'b', 'd']
  index_b = letters.index('b') # 1 (first occurrence of 'b')
  index_b_from_2 = letters.index('b', 2) # 3 (first occurrence of 'b' starting from index 2)
  # letters.index('e') # ValueError: 'e' is not in list

  print(f"Index of 'b': {index_b}, Index of 'b' from index 2: {index_b_from_2}")
  ```

- `.count(item)`: Returns the number of times `item` appears in the list.

  ```python
  numbers = [1, 2, 2, 3, 2, 4, 2]
  count_2 = numbers.count(2) # 4 (number of times 2 appears)
  count_5 = numbers.count(5) # 0 (number of times 5 appears)

  print(f"Count of 2: {count_2}, Count of 5: {count_5}")
  ```

- `len(list)`: Returns the number of items in the list (length of the list).

  ```python
  my_list = [10, 20, 30, 40]
  list_length = len(my_list) # 4
  print(f"Length of list: {list_length}")
  ```

- `sorted(list)`: Returns a _new_ sorted list. The original list is not modified (non-mutating).

  ```python
  unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  sorted_list = sorted(unsorted_numbers) # Returns a new sorted list
  print(f"Original list: {unsorted_numbers}, Sorted list: {sorted_list}") # Original unchanged
  # Output: Original list: [3, 1, 4, 1, 5, 9, 2, 6], Sorted list: [1, 1, 2, 3, 4, 5, 6, 9]
  ```

- `list.sort()`: Sorts the list _in place_. The original list is modified (mutating). Returns `None`.

  ```python
  unsorted_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  unsorted_numbers.sort() # Sorts the list in place
  print(f"Sorted list in place: {unsorted_numbers}") # Original list is now sorted
  # Output: Sorted list in place: [1, 1, 2, 3, 4, 5, 6, 9]
  ```

- `list.reverse()`: Reverses the list _in place_. The original list is modified (mutating). Returns `None`.

  ```python
  my_list = [1, 2, 3, 4, 5]
  my_list.reverse() # Reverse the list in place
  print(f"Reversed list: {my_list}") # Output: Reversed list: [5, 4, 3, 2, 1]
  ```

- `.copy()`: Creates a shallow copy of the list.

  ```python
  list1 = [1, 2, 3]
  list2 = list1.copy() # Create a copy
  list2.append(4) # Modify the copy - original list remains unchanged
  print(f"Original list: {list1}, Copied list: {list2}")
  # Output: Original list: [1, 2, 3], Copied list: [1, 2, 3, 4]
  ```

---

**Exercises:**

### Week 2: Data Structures - Day 1: Exercises

1.  **List Creation and Access:**

    - Create a list named `programming_languages` containing the strings "Python", "Java", "JavaScript", "C++", "C#".
    - Print the list.
    - Print the first element of the list.
    - Print the third element of the list.
    - Print the last element of the list using negative indexing.

2.  **List Modification:**

    - Start with a list `numbers = [1, 2, 3, 4, 5]`.
    - Change the second element (index 1) to `10`.
    - Append the number `6` to the end of the list.
    - Insert the number `0` at the beginning of the list (index 0).
    - Remove the element `4` from the list.
    - Print the modified list after each operation.

3.  **List Slicing:**

    - Create a list `letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']`.
    - Extract and print the following sublists using slicing:
      - The first 5 elements.
      - Elements from index 3 to 7 (inclusive of 3, exclusive of 7).
      - Every second element from the beginning to the end.
      - The list in reverse order.
      - The last 3 elements.

4.  **List Methods Practice:**

    - Create a list `colors = ['red', 'green', 'blue', 'red', 'yellow', 'red']`.
    - Count how many times 'red' appears in the list. Print the count.
    - Find the index of the first occurrence of 'blue'. Print the index.
    - Sort the `colors` list in place (alphabetical order). Print the sorted list.
    - Reverse the sorted `colors` list in place. Print the reversed list.
    - Create a copy of the `colors` list named `colors_copy`. Append 'purple' to `colors_copy`. Print both `colors` and `colors_copy` to show that `colors` is unchanged.

5.  **List Filtering and Transformation:**

    - Create a list `numbers = [1, 5, 12, 3, 18, 22, 7, 30]`.
    - Using a loop, create a new list called `even_numbers` that contains only the even numbers from the `numbers` list.
    - Using another loop, create a new list called `squared_numbers` that contains the square of each number from the original `numbers` list.
    - Print both `even_numbers` and `squared_numbers` lists.

---

**Daily Simple Task:**

### Daily Simple Task - Day 1, Week 2

Create a list of your 3 favorite fruits and print each fruit from the list using a `for` loop.
