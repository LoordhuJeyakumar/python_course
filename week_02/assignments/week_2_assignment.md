## Week 2 Assignment: Data Structures and Functions

**Topics Covered:** Lists, Tuples, Sets, Dictionaries, Functions, Modules, and Packages.

**Purpose:** This assignment is designed to assess your understanding of data structures (lists, tuples, sets, dictionaries) and functions in Python. You will be challenged to apply these concepts to solve practical problems, demonstrating your ability to choose the right data structure for a given task and to write modular and reusable code using functions and modules.

**Instructions:**

- For each problem, write Python code to solve the task.
- Ensure your code is well-commented and readable.
- Test your code thoroughly with the provided examples and consider edge cases.
- Submit your solutions as separate files for each problem, and make folder in your name then add each problems.
- For problems involving module creation, submit both the module file (`.py`) and the main script that uses it.

---

**Problems:**

**1. Inventory Management with Dictionaries:**

A store needs to manage its inventory. You are tasked with creating a system to track the quantity of each item in stock and its price.

- **Task:**

  - Create a dictionary named `inventory` where keys are item names (strings) and values are dictionaries themselves. Each inner dictionary should have two keys: `"quantity"` (integer representing stock quantity) and `"price"` (float representing the price per item).
  - Initialize the `inventory` with at least 5 different items (e.g., "Laptop", "Headphones", "Mouse", "Keyboard", "Monitor"). Set initial quantities and prices for each.
  - Write a function called `update_inventory(item_name, quantity_change)` that takes an `item_name` (string) and a `quantity_change` (integer). This function should update the quantity of the `item_name` in the `inventory`. If `quantity_change` is positive, it increases the stock; if negative, it decreases it. Ensure that the quantity does not become negative. If the item is not in the inventory, print a message "Item not found in inventory."
  - Write a function called `get_item_price(item_name)` that takes an `item_name` (string) and returns the price of the item from the `inventory`. If the item is not found, return `None`.
  - Write a function called `calculate_total_value()` that calculates and returns the total value of all items currently in the inventory (sum of quantity \* price for all items).

**2. Student Grade Analysis with Lists and Functions:**

You have a list of student names and their grades in a class. You need to perform some analysis on this data.

- **Task:**

  - Create a list of tuples named `student_grades`. Each tuple should contain a student's name (string) and their grade (integer). Example: `[("Alice", 88), ("Bob", 75), ("Charlie", 92), ...]`. Include at least 8-10 student records.
  - Write a function called `calculate_average_grade(grades_list)` that takes the `student_grades` list as input and returns the average grade of all students.
  - Write a function called `get_top_students(grades_list, top_n=3)` that takes the `student_grades` list and an optional parameter `top_n` (defaulting to 3). This function should return a list of the names of the top `top_n` students with the highest grades. If there are ties in grades, include all students with grades equal to or above the nth top student's grade.
  - Write a function called `get_failing_students(grades_list, passing_grade=60)` that takes the `student_grades` list and an optional `passing_grade` (defaulting to 60). This function should return a list of names of students who have a grade below the `passing_grade`.

**3. Set Operations for Data Analysis:**

You have two lists of keywords related to different marketing campaigns. You need to analyze the overlap and differences between these keyword sets.

- **Task:**

  - Create two lists of strings, `campaign_keywords_A` and `campaign_keywords_B`, each containing at least 10-15 keywords. Some keywords should be common to both lists to demonstrate set operations effectively. Include duplicate keywords within each list to test set conversion.
  - Write a function called `analyze_keywords(keywords_list_A, keywords_list_B)` that takes two lists of keywords as input. Inside the function:
    - Convert both input lists into sets to automatically remove duplicate keywords.
    - Calculate and return a dictionary containing the following:
      - `"common_keywords"`: A set of keywords present in both campaigns (intersection).
      - `"unique_to_A"`: A set of keywords that are only in campaign A (difference: A - B).
      - `"unique_to_B"`: A set of keywords that are only in campaign B (difference: B - A).
      - `"all_keywords"`: A set of all unique keywords from both campaigns (union).

**4. Module for Geometry Calculations:**

Create a module to perform basic geometric calculations for rectangles and triangles.

- **Task:**

  - Create a module file named `geometry_module.py`.
  - In `geometry_module.py`, define the following functions:
    - `rectangle_area(length, width)`: Calculates and returns the area of a rectangle.
    - `rectangle_perimeter(length, width)`: Calculates and returns the perimeter of a rectangle.
    - `triangle_area(base, height)`: Calculates and returns the area of a triangle.
    - `triangle_perimeter(side1, side2, side3)`: Calculates and returns the perimeter of a triangle.
  - In your main script (e.g., `main.py`), import the `geometry_module`.
  - Use functions from `geometry_module` to:
    - Calculate and print the area and perimeter of a rectangle with length 10 and width 5.
    - Calculate and print the area and perimeter of a triangle with base 8, height 6, and sides 7, 8, 9.

---

**Bonus Challenges (Optional, for extra practice):**

**5. Advanced Inventory Management:**

Extend the inventory management system from Problem 1.

- **Bonus Tasks:**
  - Add a function `add_new_item(item_name, initial_quantity, price)` to add a new item to the `inventory`. Ensure that you check if an item with the same name already exists; if it does, print a message indicating the item already exists and do not add it again.
  - Write a function `get_low_stock_items(threshold=10)` that returns a list of item names that have a quantity below a given `threshold` (defaulting to 10).
  - Write a function `calculate_category_value(inventory, category_keywords)` where `category_keywords` is a list of keywords (strings). This function should calculate the total inventory value for items whose names contain at least one of the keywords in `category_keywords` (case-insensitive matching). Assume item names are descriptive enough to categorize them using keywords.

**6. Text Analysis using Dictionaries and Sets:**

Write a program that analyzes a given text (e.g., a paragraph of text).

- **Bonus Tasks:**
  - Write a function `analyze_text(text)` that takes a text string as input and returns a dictionary with the following analysis:
    - `"word_count"`: Total number of words in the text.
    - `"unique_word_count"`: Number of unique words in the text (case-insensitive).
    - `"average_word_length"`: Average length of words in the text (excluding punctuation and spaces).
    - `"most_frequent_words"`: A list of the top 5 most frequent words (case-insensitive, excluding common punctuation like commas, periods, etc.). If there are ties in frequency, include all tied words within the top 5 limit.

**Submission:**

Submit your Python code files (`.py` files) for each problem, including `geometry_module.py` and `main.py` for Problem 4, and any files you create for the bonus challenges if you attempt them. Ensure your code is well-organized and easy to understand.

---

**Good luck with your Week 2 Assignment!**
