## Week 2, Day 3: Data Structures - Dictionaries - COMPLETE

**Lesson Plan:**

1.  **Introduction to Dictionaries**

    - Recap of Day 2 (Tuples & Sets), Q\&A. Briefly review Tuples and Sets and address any questions from Day 2 exercises or related to data structure choices.
    - Introduction to Dictionaries:
      - Definition: **Unordered**, **mutable** collections of **key-value pairs**. Emphasize "key-value pairs" and "unordered" nature.
      - Why Dictionaries? Use cases: representing structured data (configurations, records, JSON-like data), mapping keys to values, efficient lookups by key.
      - Dictionary Keys and Values:
        - Keys must be **immutable** (strings, numbers, tuples - _cannot be lists or sets as keys_). Must be unique within a dictionary.
        - Values can be of any data type (mutable or immutable), and can be duplicated within a dictionary.
      - Creating Dictionaries:
        - Using curly braces `{}`: Empty dictionary `{}`, dictionary with initial key-value pairs `{key1: value1, key2: value2, ...}`.
        - Using the `dict()` constructor: `dict()`, `dict([(key1, value1), (key2, value2)])` (list of tuples), `dict(key1=value1, key2=value2)` (keyword arguments), `dict(zip(keys_list, values_list))`.
    - Accessing Dictionary Items:
      - Accessing values by key using square brackets `[]`: `dictionary[key]`.
      - Using the `.get(key, default_value)` method: Returns value for key if key exists, otherwise returns `default_value` (or `None` if default not specified). Preferred way to avoid `KeyError`.
      - Handling `KeyError`: What happens when you try to access a key that is not in the dictionary (using `[]` without checking). Importance of using `.get()` or checking for key existence beforehand using `in`.
    - Dictionary Mutability: Demonstrate how dictionaries are mutable and key-value pairs can be modified.
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate dictionary creation, access methods, and basic modifications. Emphasize the key-value pair concept and the unordered nature. Encourage learners to experiment and observe.

2.  **Dictionary Methods, Iteration, and Nesting**
    - Dictionary Methods (in detail with demonstrations):
      - `.keys()`: Returns a view object that displays a list of all keys in the dictionary (not a list itself, but iterable).
      - `.values()`: Returns a view object that displays a list of all values in the dictionary (iterable).
      - `.items()`: Returns a view object that displays a list of dictionary's key-value pairs (as tuples) (iterable).
      - `.update(other_dictionary)`: Updates the dictionary with key-value pairs from `other_dictionary`. Overwrites existing keys if they are also in `other_dictionary`.
      - `.pop(key, default_value)`: Removes the key and returns its value. If key not found, returns `default_value` (or raises `KeyError` if default not specified).
      - `.popitem()`: Removes and returns an arbitrary last inserted key-value pair (in versions before Python 3.7, behavior was undefined, now guaranteed last-in-first-out in insertion order). Raises `KeyError` on empty dictionary.
      - `.clear()`: Removes all items from the dictionary (empties the dictionary).
      - `.copy()`: Returns a shallow copy of the dictionary.
    - Dictionary Iteration:
      - Iterating through keys: `for key in dictionary:`.
      - Iterating through values: `for value in dictionary.values():`.
      - Iterating through key-value pairs: `for key, value in dictionary.items():`.
    - Nested Dictionaries: Dictionaries within dictionaries. Representing hierarchical data. Accessing items in nested dictionaries.
    - Restrictions on Dictionary Keys: Recap that keys must be immutable. Show examples of valid and invalid key types.
    - Choosing Data Structures: Briefly review lists, tuples, sets, and now dictionaries. Discuss scenarios where dictionaries are the most appropriate data structure (when you need to associate keys with values and perform lookups by key).
    - **Hands-on Exercises:** Learners practice dictionary operations, methods, iteration, and nested dictionaries. Exercises should include tasks like:
      - Creating dictionaries and accessing values using different methods.
      - Modifying dictionaries by adding, updating, and removing key-value pairs.
      - Using various dictionary methods (`keys`, `values`, `items`, `update`, `pop`, `popitem`, `clear`, `copy`).
      - Iterating through dictionaries in different ways (keys, values, items).
      - Working with nested dictionaries to represent structured information.
      - Choosing appropriate data structures (lists, tuples, sets, or dictionaries) for given problems.
    - Example problem solving: Guide learners to solve problems like:
      - Counting word frequencies in a text using a dictionary.
      - Creating a phonebook or contact list using a dictionary.
      - Representing and accessing student grades for multiple subjects using nested dictionaries.
      - Implementing a simple data lookup or configuration system using dictionaries.
    - Q\&A and wrap-up: Address learner questions. Recap dictionaries, their properties, key-value pairs, methods, iteration, nesting, and when to use them. Preview Day 4's topic: Functions.

---

**Study Material & Notes:**

### Week 2: Data Structures - Day 3: Dictionaries

**Notes:**

#### 1. Dictionaries

- **Definition:** Dictionaries are **unordered**, **mutable** collections of **key-value pairs**.

  - **Unordered:** Dictionaries do not maintain any order of items. The order of key-value pairs is not guaranteed. (In Python 3.7+, dictionaries remember insertion order as an implementation detail, but you shouldn't rely on it for general dictionary behavior where order is not semantically important).
  - **Mutable:** You can change the contents of a dictionary after it's created. You can add, remove, or modify key-value pairs.
  - **Key-Value Pairs:** Each item in a dictionary is a pair of two parts: a **key** and a **value**. Keys are used to access their associated values, like words in a dictionary are used to look up definitions.

- **Why Dictionaries?**

  - **Representing Structured Data:** Dictionaries are excellent for organizing and representing data that has a clear structure, often in key-value relationships. Examples:
    - Configuration settings (e.g., `{"database_host": "localhost", "port": 5432}`).
    - Records (e.g., a student record: `{"name": "Alice", "age": 20, "major": "Physics"}`).
    - JSON-like data structures used in web development and APIs.
  - **Mapping Keys to Values:** Dictionaries allow you to efficiently associate arbitrary keys with corresponding values.
  - **Efficient Lookups by Key:** Retrieving a value based on its key is very fast in dictionaries, even for large dictionaries. This is a core strength of dictionaries.

- **Dictionary Keys and Values:**

  - **Keys:**

    - Must be **immutable** data types. This means keys can be:
      - Strings (`"name"`, `"city"`)
      - Numbers (integers, floats - though floats as keys are less common and can be problematic due to floating-point precision) (`1`, `3.14`)
      - Tuples (if they contain only immutable elements) `(1, 2)`, `("first", "last")`
    - **Cannot be:**
      - Lists, sets, or other mutable objects because keys need to be hashable (immutable).
    - **Must be unique** within a dictionary. If you use the same key multiple times when creating or updating a dictionary, the last value associated with that key will be kept.

  - **Values:**
    - Can be of **any data type**. Values can be mutable or immutable, and can be of different types within the same dictionary.
    - **Can be duplicated** within a dictionary. Multiple keys can have the same value.

- **Creating Dictionaries:**

  1.  **Using Curly Braces `{}`:**

      - **Empty Dictionary:**

        ```python
        empty_dict = {}
        print(empty_dict) # Output: {}
        print(type(empty_dict)) # Output: <class 'dict'>
        ```

      - **Dictionary with Initial Key-Value Pairs:**

        ```python
        student = {"name": "Alice", "age": 20, "major": "Computer Science"}
        print(student) # Output: {'name': 'Alice', 'age': 20, 'major': 'Computer Science'}

        config = {"host": "localhost", "port": 8080, "debug": True}
        print(config) # Output: {'host': 'localhost', 'port': 8080, 'debug': True}
        ```

  2.  **Using the `dict()` constructor:**

      - **Creating an Empty Dictionary:**

        ```python
        another_empty_dict = dict()
        print(another_empty_dict) # Output: {}
        ```

      - **From a List of Tuples (Key-Value Pairs):** Each tuple should have two elements: (key, value).

        ```python
        pairs = [("apple", 1), ("banana", 2), ("cherry", 3)]
        fruit_dict = dict(pairs)
        print(fruit_dict) # Output: {'apple': 1, 'banana': 2, 'cherry': 3}
        ```

      - **Using Keyword Arguments (Keyword-Value Pairs):** Keys must be valid Python identifiers (like variable names) when using this method.

        ```python
        person_dict = dict(name="Bob", city="New York", job="Engineer")
        print(person_dict) # Output: {'name': 'Bob', 'city': 'New York', 'job': 'Engineer'}
        ```

      - **Using `zip()` to Combine Keys and Values Lists:**

        ```python
        keys = ["a", "b", "c"]
        values = [10, 20, 30]
        combined_dict = dict(zip(keys, values))
        print(combined_dict) # Output: {'a': 10, 'b': 20, 'c': 30}
        ```

- **Accessing Dictionary Items:**

  - **Using Square Brackets `[]` with Keys:** Access the value associated with a key. If the key is not found in the dictionary, it raises a `KeyError`.

    ```python
    student = {"name": "Alice", "age": 20, "major": "Computer Science"}
    student_name = student["name"] # "Alice"
    student_age = student["age"] # 20
    # student_city = student["city"] # KeyError: 'city' (if key is not in dictionary)

    print(f"Student Name: {student_name}, Student Age: {student_age}")
    ```

  - **Using the `.get(key, default_value)` method:** A safer way to access values.

    - If the `key` is in the dictionary, it returns the corresponding value.
    - If the `key` is **not** in the dictionary, it returns the `default_value` if provided. If `default_value` is not provided, it returns `None`. **It does not raise a `KeyError`.**

    ```python
    student = {"name": "Alice", "age": 20, "major": "Computer Science"}
    student_major = student.get("major") # "Computer Science"
    student_city = student.get("city") # None (key 'city' not found, default is None)
    student_city_default = student.get("city", "Unknown City") # "Unknown City" (key 'city' not found, default provided)

    print(f"Student Major: {student_major}, Student City (get with None default): {student_city}, Student City (get with 'Unknown' default): {student_city_default}")
    ```

  - **Handling `KeyError` (when using `[]`):** If you are not sure if a key exists in a dictionary, you should either use `.get()` or check for key existence first using the `in` operator to avoid `KeyError` when using `[]`.

    ```python
    my_dict = {"a": 1, "b": 2}

    if "c" in my_dict:
        value_c = my_dict["c"] # Safe to access because we checked if 'c' is a key
        print(f"Value of 'c': {value_c}")
    else:
        print("'c' is not a key in the dictionary.")
    ```

- **Dictionary Mutability: Modifying Dictionaries**

  - **Adding New Key-Value Pairs:** Assign a value to a new key using square brackets `[]`. If the key is new, it's added to the dictionary.

    ```python
    person = {"name": "Charlie", "age": 30}
    person["city"] = "London" # Add a new key-value pair: "city": "London"
    print(person) # Output: {'name': 'Charlie', 'age': 30, 'city': 'London'}
    ```

  - **Updating Existing Values:** Assign a new value to an existing key using square brackets `[]`. If the key already exists, its value is updated.

    ```python
    person = {"name": "Charlie", "age": 30, "city": "London"}
    person["age"] = 31 # Update the value for the key "age"
    print(person) # Output: {'name': 'Charlie', 'age': 31, 'city': 'London'}
    ```

  - **Removing Key-Value Pairs:**

    - `del dictionary[key]`: Deletes the key-value pair associated with `key`. Raises `KeyError` if the key is not found.

      ```python
      person = {"name": "Charlie", "age": 31, "city": "London"}
      del person["city"] # Remove the key-value pair with key "city"
      print(person) # Output: {'name': 'Charlie', 'age': 31}
      # del person["country"] # KeyError: 'country' (if you try to delete a non-existent key)
      ```

    - `.pop(key, default_value)`: Removes and returns the value associated with `key`. If `key` is not found, returns `default_value` if provided, otherwise raises `KeyError`.

      ```python
      person = {"name": "Charlie", "age": 31, "city": "London"}
      removed_age = person.pop("age") # Remove and return the value for key "age"
      print(person) # Output: {'name': 'Charlie', 'city': 'London'}
      print(removed_age) # Output: 31

      removed_country = person.pop("country", "Country not found") # Key 'country' not found, returns default value
      print(removed_country) # Output: Country not found
      # person.pop("country") # KeyError: 'country' (if no default value is provided and key is missing)
      ```

    - `.popitem()`: Removes and returns an arbitrary last-inserted (key, value) pair as a tuple. In Python versions before 3.7, the item removed was arbitrary. Raises `KeyError` if the dictionary is empty.

      ```python
      items_dict = {"item1": 100, "item2": 200, "item3": 300}
      removed_item_pair = items_dict.popitem() # Removes and returns last inserted pair (e.g., might remove ('item3', 300))
      print(items_dict) # Output: (e.g.) {'item1': 100, 'item2': 200}
      print(removed_item_pair) # Output: (e.g.) ('item3', 300)
      # empty_dict = {}
      # empty_dict.popitem() # KeyError: 'popitem(): dictionary is empty'
      ```

    - `.clear()`: Removes all key-value pairs from the dictionary, making it an empty dictionary.

      ```python
      data_dict = {"a": 1, "b": 2, "c": 3}
      data_dict.clear()
      print(data_dict) # Output: {}
      ```

#### 2. Dictionary Methods:

- `.keys()`: Returns a **view object** that displays a list of all keys in the dictionary. It's not a static list, but dynamically reflects changes to the dictionary.

  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "Paris"}
  keys_view = my_dict.keys()
  print(keys_view) # Output: dict_keys(['name', 'age', 'city']) (order may vary)

  print(list(keys_view)) # Convert to a list if you need a list: ['name', 'age', 'city']

  my_dict["job"] = "Engineer" # Add a new key
  print(keys_view) # Output: dict_keys(['name', 'age', 'city', 'job']) (keys_view is updated)
  ```

- `.values()`: Returns a **view object** that displays a list of all values in the dictionary. Like `.keys()`, it's a dynamic view.

  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "Paris"}
  values_view = my_dict.values()
  print(values_view) # Output: dict_values(['Alice', 25, 'Paris'])

  print(list(values_view)) # Convert to list: ['Alice', 25, 'Paris']

  my_dict["age"] = 26 # Update a value
  print(values_view) # Output: dict_values(['Alice', 26, 'Paris']) (values_view is updated)
  ```

- `.items()`: Returns a **view object** that displays a list of all key-value pairs as tuples. Dynamic view.

  ```python
  my_dict = {"name": "Alice", "age": 25, "city": "Paris"}
  items_view = my_dict.items()
  print(items_view) # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'Paris')])

  print(list(items_view)) # Convert to list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')]

  my_dict["city"] = "London" # Update a value
  print(items_view) # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'London')]) (items_view updated)
  ```

- `.update(other_dictionary)`: Merges key-value pairs from `other_dictionary` into the current dictionary. If there are keys in common, the values from `other_dictionary` overwrite the values in the current dictionary.

  ```python
  dict1 = {"a": 1, "b": 2, "c": 3}
  dict2 = {"c": 30, "d": 4, "e": 5} # 'c' is a common key, 'd' and 'e' are new keys

  dict1.update(dict2) # Update dict1 with key-value pairs from dict2
  print(dict1) # Output: {'a': 1, 'b': 2, 'c': 30, 'd': 4, 'e': 5} # Value for 'c' is updated, new keys 'd', 'e' added
  ```

- `.copy()`: Returns a **shallow copy** of the dictionary. Changes to the copy will not affect the original dictionary, and vice-versa (for top-level immutable values).

  ```python
  original_dict = {"name": "Alice", "age": 25, "city": "Paris"}
  copied_dict = original_dict.copy()

  copied_dict["age"] = 26 # Modify the copy
  copied_dict["job"] = "Developer" # Add to the copy

  print(f"Original dictionary: {original_dict}") # Original is unchanged
  # Output: Original dictionary: {'name': 'Alice', 'age': 25, 'city': 'Paris'}
  print(f"Copied dictionary: {copied_dict}") # Copy is modified
  # Output: Copied dictionary: {'name': 'Alice', 'age': 26, 'city': 'Paris', 'job': 'Developer'}
  ```

#### 3. Dictionary Iteration:

- **Iterating through Keys (default iteration):** By default, when you iterate over a dictionary in a `for` loop, you iterate over its keys.

  ```python
  my_dict = {"a": 1, "b": 2, "c": 3}
  for key in my_dict: # Iterates over keys by default
      print(key) # Output: (order not guaranteed) a, b, c
      print(f"Key: {key}, Value: {my_dict[key]}") # Access value using the key
      # Output: Key: a, Value: 1, ...
  ```

- **Iterating through Values:** Use `.values()` method to iterate over the values.

  ```python
  my_dict = {"a": 1, "b": 2, "c": 3}
  for value in my_dict.values():
      print(value) # Output: (order not guaranteed) 1, 2, 3
  ```

- **Iterating through Key-Value Pairs:** Use `.items()` method to iterate over key-value pairs (as tuples).

  ```python
  my_dict = {"a": 1, "b": 2, "c": 3}
  for key, value in my_dict.items(): # Unpack key and value from each tuple
      print(f"Key: {key}, Value: {value}") # Output: (order not guaranteed) Key: a, Value: 1, ...
  ```

#### 4. Nested Dictionaries:

- Dictionaries can be nested, meaning you can have dictionaries as values within other dictionaries. This is useful for representing hierarchical data structures.

  ```python
  company = {
      "name": "TechCorp",
      "employees": {
          "employee1": {"name": "Alice", "role": "Developer"},
          "employee2": {"name": "Bob", "role": "Manager"},
          "employee3": {"name": "Charlie", "role": "Designer"}
      },
      "location": "Silicon Valley"
  }

  print(company) # Print the entire nested dictionary
  print(company["name"]) # Access company name: "TechCorp"
  print(company["employees"]["employee2"]["role"]) # Access role of employee2: "Manager"

  # Iterate through employees in the nested dictionary
  for employee_id, employee_data in company["employees"].items():
      print(f"Employee ID: {employee_id}")
      print(f"  Name: {employee_data['name']}")
      print(f"  Role: {employee_data['role']}")
  ```

#### 5. Restrictions on Dictionary Keys:

- **Keys must be immutable:** Only immutable data types (strings, numbers, tuples) can be used as dictionary keys. Mutable types like lists or sets cannot be keys because their hash value can change if they are modified, which would break the dictionary's internal structure for efficient lookups.

  ```python
  valid_keys_dict = {
      "string_key": "value1",
      123: "value2",
      (1, 2): "value3" # Tuple as key
  }
  # invalid_key_dict = {
  #     ["list_key"]: "value" # TypeError: unhashable type: 'list' (Lists cannot be keys)
  #     {"set_key"}: "value" # TypeError: unhashable type: 'set' (Sets cannot be keys)
  # }
  ```

#### 6. Choosing Between Data Structures (Lists, Tuples, Sets, Dictionaries):

- **Lists:** Use when you need an **ordered** collection of items that **may change** (mutable). Order is important, and you may have duplicate items. Access items by index.
- **Tuples:** Use for **ordered**, **immutable** collections of items. Good for representing fixed data records, coordinates, when data integrity is important, and as dictionary keys. Access by index.
- **Sets:** Use when you need a collection of **unique** items, and **order is not important**. Efficient for membership testing, removing duplicates, and performing set operations. Access to items is based on membership, not index.
- **Dictionaries:** Use for collections of **key-value pairs** when you need to **associate keys with values** and perform **efficient lookups of values based on their keys**. Order is not guaranteed (though insertion order is remembered in Python 3.7+), and keys must be immutable.

---

**Exercises:**

### Week 2: Data Structures - Day 3: Exercises

1.  **Dictionary Creation and Access:**

    - Create a dictionary named `country_capitals` to store the capitals of three countries: "USA": "Washington D.C.", "France": "Paris", "Japan": "Tokyo".
    - Print the dictionary.
    - Print the capital of France using key-based access.
    - Print the capital of Germany using `.get()`. What is the output?
    - Print the capital of Germany using `.get()` with a default value of "Not found".

2.  **Dictionary Modification:**

    - Start with the `country_capitals` dictionary from Exercise 1.
    - Add a new country and capital: "India": "New Delhi".
    - Update the capital of "USA" to "Washington, D.C.".
    - Remove the entry for "France" using `del`.
    - Print the modified dictionary after each operation.

3.  **Dictionary Methods Practice:**

    - Create a dictionary `item_prices = {"apple": 1.0, "banana": 0.5, "orange": 0.8, "grape": 2.5}`.
    - Get and print a list of all keys in the dictionary using `.keys()`.
    - Get and print a list of all values in the dictionary using `.values()`.
    - Get and print a list of all key-value pairs (items) as tuples using `.items()`.
    - Remove the item "banana" and get its price using `.pop()`. Print the removed price.
    - Clear all items from the `item_prices` dictionary using `.clear()`. Print the dictionary to show it's empty.

4.  **Dictionary Iteration:**

    - Create a dictionary `student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}`.
    - Iterate through the dictionary and print each student's name and their grade (key and value).
    - Calculate and print the average grade of all students by iterating through the values.

5.  **Nested Dictionaries:**

    - Create a nested dictionary called `library` to represent books in a library. The main keys should be genres (e.g., "Fiction", "Science", "History"). Each genre key should have a value that is a list of dictionaries, where each dictionary represents a book with keys like "title", "author", and "year".
    - Add at least two books to each genre.
    - Print the entire `library` dictionary.
    - Access and print the title of the first book in the "Fiction" genre.
    - Iterate through the "Science" genre and print the title and author of each book in that genre.

---

**Daily Simple Task:**

### Daily Simple Task - Day 3, Week 2

Create a dictionary to store the number of days in each of the first six months of the year (January to June). Then, ask the user to enter a month name. Convert the month name to lowercase and check if it's in your dictionary. If yes, print the number of days in that month. If not, print "Month not found in the first six months."
