## Week 2, Day 2: Data Structures - Tuples and Sets - COMPLETE

**Lesson Plan:**

1.  **Introduction to Tuples and Sets**
    - Recap of Day 1 (Lists), Q\&A. Briefly review Lists and address any questions from Day 1 exercises or Week 1 assignment questions.
    - Introduction to Tuples:
      - Definition: Ordered, **immutable** collections of items. Emphasize the key difference from lists: immutability (cannot be changed after creation).
      - Why Tuples? Use cases: representing fixed collections of items (coordinates, records), data integrity (preventing accidental modification), as keys in dictionaries (upcoming topic).
      - Creating Tuples:
        - Using parentheses `()`: Empty tuple `()`, tuple with initial elements `(1, 2, 3)`, single-element tuple `(5,)` (note the trailing comma).
        - Tuple packing and unpacking: automatic packing of values into a tuple, and unpacking tuple elements into variables.
        - Using the `tuple()` constructor: `tuple()`, `tuple([1, 2, 3])` (from list), `tuple("string")` (from string).
    - Accessing Tuple Elements:
      - Indexing: Similar to lists, zero-based indexing. Accessing elements using positive and negative indices.
      - Slicing: Similar to lists, extracting subtuples using slicing `[:]`. Tuples are also sequences.
    - Tuple Immutability: Demonstrate attempts to modify tuples and show the resulting errors (TypeError). Emphasize that tuples cannot be changed after creation.
    - Tuple methods: `.count(item)`, `.index(item, [start, end])`. Point out that tuples have fewer methods than lists due to immutability.
    - Introduction to Sets:
      - Definition: **Unordered**, collections of **unique** items. Emphasize "unordered" (no guaranteed order, order may seem to change) and "unique" (no duplicate items).
      - Why Sets? Use cases: membership testing, removing duplicates, mathematical set operations (union, intersection, etc.).
      - Creating Sets:
        - Using curly braces `{}`: Set with initial elements `{1, 2, 3}`, empty set **cannot be created with `{}` (it creates an empty dictionary instead!)**.
        - Using the `set()` constructor: `set() # creates an empty set`, `set([1, 2, 2, 3])` (duplicates automatically removed), `set("hello")` (creates a set of unique characters).
    - Set Operations:
      - Adding and Removing items: `.add(item)`, `.update(iterable)`, `.remove(item)` (raises KeyError if not found), `.discard(item)` (no error if not found), `.pop()` (removes and returns an arbitrary element, error on empty set), `.clear()` (removes all elements).
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate tuple and set creation, access, and basic operations. Highlight the differences between tuples and lists, and the properties of sets. Encourage learners to experiment and observe.
2.  **Set Operations (Mathematical Sets) and Choosing Data Structures**
    - Mathematical Set Operations:
      - Union (`|` operator or `.union()` method): Combining elements from two or more sets.
      - Intersection (`&` operator or `.intersection()` method): Elements common to two or more sets.
      - Difference (`-` operator or `.difference()` method): Elements in the first set but not in the second set.
      - Symmetric Difference (`^` operator or `.symmetric_difference()` method): Elements in either set, but not in both.
      - Subset and Superset tests (`<=` or `.issubset()`, `>=` or `.issuperset()`): Checking if one set is a subset or superset of another.
    - Set Membership testing: `in` and `not in` operators for efficient membership checks.
    - Iterating through Sets: Using `for` loops to iterate over set elements (note: order is not guaranteed).
    - Choosing between Lists, Tuples, and Sets:
      - When to use Lists: Ordered collections that need to be modified frequently.
      - When to use Tuples: Ordered, immutable collections for data integrity, representing fixed records, dictionary keys.
      - When to use Sets: Collections of unique items, membership testing, removing duplicates, mathematical set operations.
    - **Hands-on Exercises:** Learners practice tuple and set operations and choose the appropriate data structure for given problems. Exercises should include tasks like:
      - Creating tuples and sets.
      - Accessing tuple elements and slicing tuples.
      - Performing set operations (union, intersection, difference, symmetric difference).
      - Testing set membership.
      - Writing programs that choose between lists, tuples, or sets to solve specific problems efficiently.
    - Example problem solving: Guide learners to solve problems like:
      - Finding common elements in two lists using sets.
      - Removing duplicate items from a list using sets.
      - Checking if all elements of one list are present in another list (using sets for efficiency).
      - Creating a program to analyze words in a sentence and find unique words, common words between two sentences, etc.
    - Q\&A and wrap-up: Address learner questions. Recap tuples, sets, their properties, operations, and when to use each data structure. Preview Day 3's topic: Dictionaries.

---

**Study Material & Notes:**

### Week 2: Data Structures - Day 2: Tuples and Sets

**Notes:**

#### 1. Tuples

- **Definition:** Tuples are **ordered** and **immutable** sequences of items.

  - **Ordered:** Items in a tuple maintain their order.
  - **Immutable:** Once a tuple is created, you **cannot** change its contents (add, remove, or modify items). This is the main difference from lists.

- **Why Tuples?**

  - **Data Integrity:** Immutability ensures that the data in a tuple remains constant throughout the program. Prevents accidental modifications.
  - **Representing Fixed Collections:** Useful for representing collections of items that are not meant to change, like coordinates (x, y), RGB color values (red, green, blue), or database records.
  - **Dictionary Keys:** Tuples can be used as keys in dictionaries (upcoming topic), while lists cannot because lists are mutable.
  - **Slightly Faster than Lists:** In some cases, tuple operations can be slightly faster than list operations due to their immutability.

- **Creating Tuples:**

  1.  **Using Parentheses `()`:**

      - **Empty Tuple:**

        ```python
        empty_tuple = ()
        print(empty_tuple) # Output: ()
        print(type(empty_tuple)) # Output: <class 'tuple'>
        ```

      - **Tuple with Initial Elements:**

        ```python
        coordinates = (10, 20)
        print(coordinates) # Output: (10, 20)

        rgb_color = (255, 0, 0) # Red color
        print(rgb_color) # Output: (255, 0, 0)

        mixed_tuple = (1, "hello", 3.14, True) # Different data types
        print(mixed_tuple) # Output: (1, 'hello', 3.14, True)
        ```

      - **Single-Element Tuple:** To create a tuple with just one item, you **must** include a trailing comma `,` after the item.

        ```python
        single_item_tuple = (5,) # Note the comma!
        print(single_item_tuple) # Output: (5,)
        print(type(single_item_tuple)) # Output: <class 'tuple'>

        not_a_tuple = (5) # Without comma, Python interprets it as just an integer in parentheses
        print(not_a_tuple) # Output: 5
        print(type(not_a_tuple)) # Output: <class 'int'>
        ```

  2.  **Tuple Packing and Unpacking:**

      - **Tuple Packing:** Automatically creating a tuple by placing values separated by commas.

        ```python
        my_tuple = 1, 2, 3 # Tuple packing
        print(my_tuple) # Output: (1, 2, 3)
        ```

      - **Tuple Unpacking:** Assigning tuple elements to individual variables. The number of variables on the left side must match the number of elements in the tuple.

        ```python
        point = (10, 20)
        x, y = point # Tuple unpacking
        print(f"x = {x}, y = {y}") # Output: x = 10, y = 20

        rgb = (100, 150, 200)
        red, green, blue = rgb # Unpack into red, green, blue variables
        print(f"Red: {red}, Green: {green}, Blue: {blue}") # Output: Red: 100, Green: 150, Blue: 200
        ```

  3.  **Using the `tuple()` constructor:**

      - **Creating an empty tuple:**

        ```python
        another_empty_tuple = tuple()
        print(another_empty_tuple) # Output: ()
        ```

      - **Creating a tuple from an iterable (like a list or string):**

        ```python
        my_list = [1, 2, 3]
        tuple_from_list = tuple(my_list)
        print(tuple_from_list) # Output: (1, 2, 3)

        tuple_from_string = tuple("Python")
        print(tuple_from_string) # Output: ('P', 'y', 't', 'h', 'o', 'n')
        ```

- **Accessing Tuple Elements: Indexing and Slicing**

  - Indexing and slicing work exactly the same way as with lists.

  ```python
  my_tuple = ('a', 'b', 'c', 'd', 'e')
  first_element = my_tuple[0] # 'a'
  last_element = my_tuple[-1] # 'e'
  sub_tuple = my_tuple[1:4] # ('b', 'c', 'd')

  print(f"First element: {first_element}, Last element: {last_element}, Sub-tuple: {sub_tuple}")
  ```

- **Tuple Immutability:** You cannot modify tuples after creation. Attempts to do so will result in errors.

  ```python
  my_tuple = (1, 2, 3)
  # my_tuple[0] = 10 # TypeError: 'tuple' object does not support item assignment (cannot change item)
  # my_tuple.append(4) # AttributeError: 'tuple' object has no attribute 'append' (no methods to add/remove items)
  ```

- **Tuple Methods:** Tuples have fewer methods than lists due to their immutability. The common ones are:

  - `.count(item)`: Returns the number of occurrences of `item` in the tuple.
  - `.index(item, [start, end])`: Returns the index of the first occurrence of `item`.

  ```python
  my_tuple = (1, 2, 2, 3, 2, 4)
  count_2_tuple = my_tuple.count(2) # 3
  index_3_tuple = my_tuple.index(3) # 3

  print(f"Count of 2 in tuple: {count_2_tuple}, Index of 3 in tuple: {index_3_tuple}")
  ```

#### 2. Sets

- **Definition:** Sets are **unordered** collections of **unique** items.

  - **Unordered:** Sets do not maintain any specific order of elements. The order in which you add items may not be the order in which they are stored or retrieved. Order is not guaranteed.
  - **Unique:** Sets only store unique items. Duplicate items are automatically removed. If you try to add an item that is already in the set, it has no effect.
  - Sets are **mutable**, you can add or remove items after creation.

- **Why Sets?**

  - **Membership Testing:** Sets are very efficient for checking if an item is present in a collection (using the `in` operator). Membership tests are faster in sets than in lists or tuples, especially for large collections.
  - **Removing Duplicates:** Sets automatically eliminate duplicate values. Useful for getting unique items from a list or other sequence.
  - **Mathematical Set Operations:** Sets support standard mathematical set operations like union, intersection, difference, symmetric difference, etc., which are very useful in various algorithms and data processing tasks.

- **Creating Sets:**

  1.  **Using Curly Braces `{}`:**

      - **Set with Initial Elements:**

        ```python
        my_set = {1, 2, 3, 2, 4} # Duplicate '2' will be automatically removed
        print(my_set) # Output: {1, 2, 3, 4} (order may vary)
        print(type(my_set)) # Output: <class 'set'>

        string_set = {"apple", "banana", "apple", "orange"} # Duplicate "apple" removed
        print(string_set) # Output: {'banana', 'apple', 'orange'} (order may vary)
        ```

      - **Important:** You **cannot** create an empty set using `{}`. `{}` creates an empty dictionary instead (dictionaries are covered next day).

  2.  **Using the `set()` constructor:**

      - **Creating an Empty Set:** Use `set()` to create an empty set.

        ```python
        empty_set = set()
        print(empty_set) # Output: set()
        print(type(empty_set)) # Output: <class 'set'>
        ```

      - **Creating a set from an iterable (list, tuple, string):** Duplicates will be removed.

        ```python
        my_list = [1, 2, 2, 3, 4, 4, 4]
        set_from_list = set(my_list) # Remove duplicates
        print(set_from_list) # Output: {1, 2, 3, 4}

        set_from_string = set("Mississippi") # Unique characters from the string
        print(set_from_string) # Output: {'M', 'i', 's', 'p'} (order may vary)
        ```

- **Set Operations (Mutability and Methods):** Sets are mutable, and have methods for modification and set algebra.

  - **Adding Items:**

    - `.add(item)`: Adds a single `item` to the set. If the item is already present, it has no effect.

      ```python
      my_set = {1, 2, 3}
      my_set.add(4) # Add 4 to the set
      print(my_set) # Output: {1, 2, 3, 4}
      my_set.add(2) # Adding 2 again has no effect (duplicates are ignored)
      print(my_set) # Output: {1, 2, 3, 4}
      ```

    - `.update(iterable)`: Adds multiple items from an `iterable` (like a list, tuple, or another set) to the set. Duplicates are automatically handled.

      ```python
      set1 = {1, 2, 3}
      set2 = {3, 4, 5}
      my_list = [5, 6, 7]

      set1.update(set2) # Add elements from set2 to set1
      print(set1) # Output: {1, 2, 3, 4, 5}

      set1.update(my_list) # Add elements from list to set1
      print(set1) # Output: {1, 2, 3, 4, 5, 6, 7}
      ```

  - **Removing Items:**

    - `.remove(item)`: Removes `item` from the set. If `item` is not in the set, it raises a `KeyError`.

      ```python
      my_set = {1, 2, 3, 4}
      my_set.remove(3) # Remove 3
      print(my_set) # Output: {1, 2, 4}
      # my_set.remove(5) # KeyError: 5 (if you try to remove an item not in the set)
      ```

    - `.discard(item)`: Removes `item` from the set if it is present. If `item` is not in the set, it does nothing (no error).

      ```python
      my_set = {1, 2, 3, 4}
      my_set.discard(3) # Remove 3
      print(my_set) # Output: {1, 2, 4}
      my_set.discard(5) # Discarding 5 (which is not in set) has no effect, no error
      print(my_set) # Output: {1, 2, 4}
      ```

    - `.pop()`: Removes and returns an **arbitrary** element from the set. Because sets are unordered, you don't know which element will be removed. Raises `KeyError` if the set is empty.

      ```python
      my_set = {10, 20, 30, 40}
      removed_item = my_set.pop() # Remove and return an arbitrary item (e.g., might remove 10)
      print(my_set) # Output: {20, 30, 40} (order may vary, and which element is popped is arbitrary)
      print(removed_item) # Output: (e.g.) 10
      # empty_set = set()
      # empty_set.pop() # KeyError: 'pop from an empty set'
      ```

    - `.clear()`: Removes all elements from the set, making it an empty set.

      ```python
      data_set = {1, 2, 3, 4, 5}
      data_set.clear()
      print(data_set) # Output: set()
      ```

- **Mathematical Set Operations:**

  - **Union (`|` or `.union()`):** Returns a new set containing all elements from both sets.

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1 | set2 # or set1.union(set2)
    print(union_set) # Output: {1, 2, 3, 4, 5}
    ```

  - **Intersection (`&` or `.intersection()`):** Returns a new set containing only the elements that are common to both sets.

    ```python
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    intersection_set = set1 & set2 # or set1.intersection(set2)
    print(intersection_set) # Output: {3, 4}
    ```

  - **Difference (`-` or `.difference()`):** Returns a new set containing elements that are in the first set but not in the second set.

    ```python
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 5, 6, 7}
    difference_set = set1 - set2 # or set1.difference(set2)
    print(difference_set) # Output: {1, 2, 4} (elements in set1 but not in set2)
    ```

  - **Symmetric Difference (`^` or `.symmetric_difference()`):** Returns a new set containing elements that are in either of the sets, but not in their intersection (i.e., elements that are in exactly one of the sets).

    ```python
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 5, 6, 7}
    symmetric_difference_set = set1 ^ set2 # or set1.symmetric_difference(set2)
    print(symmetric_difference_set) # Output: {1, 2, 4, 6, 7} (elements in set1 or set2, but not both)
    ```

  - **Subset (`<=` or `.issubset()`):** Checks if the first set is a subset of the second set (i.e., all elements of the first set are also in the second set).

    ```python
    set1 = {1, 2}
    set2 = {1, 2, 3, 4}
    is_subset = set1 <= set2 # or set1.issubset(set2)
    print(is_subset) # Output: True (set1 is a subset of set2)
    ```

  - **Superset (`>=` or `.issuperset()`):** Checks if the first set is a superset of the second set (i.e., the first set contains all elements of the second set).

    ```python
    set1 = {1, 2, 3, 4}
    set2 = {2, 3}
    is_superset = set1 >= set2 # or set1.issuperset(set2)
    print(is_superset) # Output: True (set1 is a superset of set2)
    ```

- **Set Membership Testing:** Use `in` and `not in` operators to check if an element is present in a set. Very efficient operation for sets.

  ```python
  my_set = {"apple", "banana", "cherry"}
  is_apple_present = "apple" in my_set # True
  is_grape_present = "grape" in my_set # False
  is_orange_not_present = "orange" not in my_set # True

  print(f"Is 'apple' in set? {is_apple_present}, Is 'grape' in set? {is_grape_present}, Is 'orange' NOT in set? {is_orange_not_present}")
  ```

- **Iterating through a Set:** You can use a `for` loop to iterate over the elements of a set. However, remember that the order of iteration is not guaranteed to be the order of insertion or any specific order.

  ```python
  my_set = {"red", "green", "blue"}
  for color in my_set: # Iterate over elements in set
      print(color) # Output order is not guaranteed, might be e.g., blue, green, red
  ```

- **Other Useful Set Methods:**

  - `len(set)`: Returns the number of elements in the set (cardinality).
  - `.copy()`: Creates a shallow copy of the set.

---

**Exercises:**

### Week 2: Data Structures - Day 2: Exercises

1.  **Tuple Creation and Access:**

    - Create a tuple named `student_info` to store the following information about a student: name (string), age (integer), and major (string). For example: `("Alice", 20, "Computer Science")`.
    - Print the tuple.
    - Print the student's name from the tuple using indexing.
    - Print the student's major from the tuple using negative indexing.

2.  **Tuple Packing and Unpacking:**

    - Create a tuple by packing the values `100`, `200`, and `300` into a tuple named `values`.
    - Unpack the `values` tuple into three variables named `x`, `y`, and `z`.
    - Print the values of `x`, `y`, and `z`.

3.  **Set Creation and Basic Operations:**

    - Create two sets:
      - `set1` with elements `{1, 2, 3, 4, 5}`.
      - `set2` with elements `{4, 5, 6, 7, 8}`.
    - Print both sets.
    - Add the element `6` to `set1`.
    - Remove the element `2` from `set2` using `.discard()`.
    - Try to remove the element `1` from `set2` using `.remove()`. Handle the potential `KeyError` using a `try-except` block (or `.discard()` for no error if missing).
    - Print the modified `set1` and `set2`.

4.  **Set Operations (Mathematical Sets):**

    - Using `set1 = {1, 2, 3, 4, 5}` and `set2 = {4, 5, 6, 7, 8}` from the previous exercise:
      - Calculate and print the union of `set1` and `set2`.
      - Calculate and print the intersection of `set1` and `set2`.
      - Calculate and print the difference of `set1` from `set2` (elements in `set1` but not in `set2`).
      - Calculate and print the symmetric difference of `set1` and `set2`.
      - Check if `set1` is a subset of `set2`. Print the boolean result.

5.  **Choosing Data Structures:**

    - For each of the following scenarios, decide whether a **list**, a **tuple**, or a **set** would be the most appropriate data structure and explain _why_. No code is needed for this exercise, just your reasoning.
      - a) Storing a collection of student names where the order matters and names might be repeated.
      - b) Representing the days of the week.
      - c) Storing unique error codes encountered in a program.
      - d) Representing the coordinates of a point in 2D space (x, y).
      - e) A collection of tasks that need to be maintained in the order they were added, and tasks might be added or removed frequently.

---

**Daily Simple Task:**

### Daily Simple Task - Day 2, Week 2

Create a set of vowels (a, e, i, o, u). Ask the user to input a word. Convert the word to lowercase and then find the set of vowels present in the word. Print the vowels found.
