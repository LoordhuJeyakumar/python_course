## Week 2, Day 5: Modules and Packages - COMPLETE

**Lesson Plan:**

1.  **Introduction to Modules**

    - Recap of Day 4 (Functions), Q\&A. Briefly review Functions, scope, arguments, return values, and address any questions from Day 4 exercises or function design principles.
    - Introduction to Modules:
      - Definition: A module is a **file** containing Python definitions and statements (functions, classes, variables). Essentially, any Python file (`.py`) is a module.
      - Why Modules?
        - Organization: Structuring large programs into multiple, manageable, and logically separated files (modules).
        - Reusability (Code Sharing): Write code in modules and reuse it across different projects.
        - Namespace Management: Modules create separate namespaces, preventing naming conflicts between different parts of a large project.
        - Modularity and Maintainability: Easier to develop, test, and maintain individual modules compared to a single monolithic script.
        - Code Distribution and Collaboration: Facilitates sharing and collaboration by creating self-contained, distributable units of code.
    - Built-in Modules:
      - Python's Standard Library: Vast collection of pre-built modules that come with Python installation.
      - Examples of Useful Built-in Modules (and brief overview of what they do):
        - `math`: Mathematical functions (e.g., `sqrt`, `sin`, `cos`, `pi`).
        - `random`: Random number generation, random choices (e.g., `random()`, `randint()`, `choice()`, `shuffle()`).
        - `datetime`: Date and time manipulation (e.g., `datetime`, `date`, `time`, `timedelta`).
        - `os`: Operating system interactions (e.g., file system operations, environment variables - use with caution when demonstrating OS operations in a learning context).
        - `sys`: System-specific parameters and functions (e.g., `sys.path`, `sys.version`, `sys.argv`).
    - Importing Modules:
      - `import module_name`: Imports the entire module. Access functions/variables using `module_name.function_name` or `module_name.variable_name`. Namespace prefix.
      - `import module_name as alias`: Imports module with a shorter alias. `alias.function_name`. Namespace prefix with alias.
      - `from module_name import function_name1, function_name2, ...`: Imports specific functions/variables directly into the current namespace. Access directly as `function_name1()`. No namespace prefix for imported items.
      - `from module_name import *` : Imports all names from a module into the current namespace. **Generally discouraged** because it can lead to namespace pollution and naming conflicts, making code harder to read and maintain. Explain the dangers of `import *`.
    - Module Search Path (`sys.path`):
      - Explanation of how Python finds modules when you import them.
      - `sys.path` list: List of directories where Python looks for modules. First, current directory, then directories in `PYTHONPATH` environment variable, then standard library directories, etc.
      - Demonstrate inspecting `sys.path` in Python interpreter.
      - Briefly mention how to add directories to `sys.path` (though usually not necessary for basic module usage).
    - Creating Your Own Modules:
      - Simple process: Just create a Python file (`.py`) and put function, class, variable definitions inside it. File name becomes the module name.
      - Example: Create a simple module `my_module.py` with a function and a variable.
      - Demonstrate importing and using `my_module` from another Python script in the same directory.
    - Examples and live coding in the IDE (VS Code/PyCharm) to demonstrate importing built-in modules, using different import styles, exploring `sys.path`, and creating and importing custom modules. Emphasize best practices for module organization and import styles. Encourage learners to experiment and observe.

2.  **Packages, External Packages, and Virtual Environments**
    - Introduction to Packages:
      - Definition: A package is a way of structuring modules using "dotted module names". Essentially, a package is a directory (folder) that contains:
        - Modules (`.py` files).
        - Subpackages (other directories that are also packages).
        - A special file named `__init__.py` (can be empty, but its presence makes Python treat the directory as a package).
      - Why Packages?
        - Hierarchical Organization: Structuring large projects into a hierarchy of packages and subpackages for better organization of modules.
        - Namespace Hierarchy: Further namespace management within large projects, avoiding naming collisions between modules in different packages.
        - Improved Code Maintainability: Makes large codebases easier to navigate, maintain, and understand.
    - Creating Packages:
      - Create a directory for the package (e.g., `mypackage`).
      - Inside the directory, create an empty `__init__.py` file. This marks the directory as a Python package.
      - Place modules (`.py` files) inside the package directory (e.g., `module1.py`, `module2.py` inside `mypackage`).
      - Demonstrate importing modules from within a package using dot notation: `import mypackage.module1`, `from mypackage import module2`.
    - Importing from Packages:
      - `import package_name.module_name`: Imports a module within a package. Access using `package_name.module_name.function()`.
      - `from package_name import module_name`: Imports a module directly from a package. Access using `module_name.function()`.
      - `from package_name.module_name import function_name`: Imports a specific function from a module within a package. Access directly as `function_name()`.
    - External Packages and `pip`:
      - Introduction to the Python Package Index (PyPI): Vast repository of third-party packages created by the Python community.
      - `pip` (Package Installer for Python): Tool for installing, uninstalling, and managing Python packages from PyPI and other sources. Usually comes pre-installed with Python.
      - Installing packages using `pip install package_name` in the terminal/command prompt.
      - Examples of useful external packages (and brief overview):
        - `requests`: Making HTTP requests (web requests).
        - `NumPy`: Numerical computing, arrays, mathematical functions.
        - `Pandas`: Data analysis and manipulation (DataFrames).
        - `Matplotlib`: Plotting and data visualization.
        - `BeautifulSoup4` (bs4): Web scraping.
        - `Flask` / `Django`: Web frameworks.
      - Demonstrate installing `requests` using `pip install requests` and using it in a Python script.
    - Virtual Environments (brief introduction):
      - Why Virtual Environments? Isolating project dependencies. Avoid conflicts between package versions required by different projects. Keep project dependencies self-contained.
      - Briefly explain the concept of virtual environments and tools like `venv` (built-in) or `virtualenv`.
      - Demonstrate creating a virtual environment (e.g., `python -m venv venv_name` or `python3 -m venv venv_name`).
      - Activating a virtual environment (using `source venv_name/bin/activate` on Linux/macOS or `venv_name\Scripts\activate` on Windows).
      - Installing packages within a virtual environment using `pip install package_name` (packages are installed only within the environment).
      - Deactivating a virtual environment (using `deactivate`).
      - Emphasize the importance of using virtual environments for managing project dependencies, especially when working on multiple projects or collaborating.
    - **Hands-on Exercises:** Learners practice creating modules and packages, importing and using modules from packages, installing and using external packages, and working with virtual environments. Exercises should include tasks like:
      - Creating a simple package with multiple modules.
      - Importing and using functions from modules within packages.
      - Installing and using the `requests` package to make a simple web request (e.g., fetch data from a public API).
      - Creating a virtual environment for a project.
      - Installing packages within the virtual environment and demonstrating isolation from global Python environment.
    - Example problem solving: Guide learners to solve problems like:
      - Creating a package for geometric calculations (modules for circle, rectangle, triangle calculations).
      - Using the `random` module to simulate dice rolls or card shuffling.
      - Using the `datetime` module to work with dates and times, calculate time differences.
      - Fetching data from a web API using the `requests` package and printing parts of the response.
    - Q\&A and wrap-up: Address learner questions. Recap modules, packages, built-in and external modules, `pip`, virtual environments, and their importance for organizing and extending Python projects. Preview next week's topics.

---

**Study Material & Notes:**

### Week 2: Day 5: Modules and Packages

**Notes:**

#### 1. Modules

- **Definition:** A module is simply a **Python file** (`.py` file) that contains Python code – definitions of functions, classes, variables, and executable statements. Essentially, any Python file can be treated as a module.

- **Why Use Modules?**

  - **Organization:** Modules help you break down large Python programs into smaller, more manageable, and logically organized files. This makes your projects easier to navigate and understand.
  - **Reusability (Code Sharing):** Modules promote code reuse. You can write functions and classes in one module and then import and use them in other Python scripts or projects, without having to rewrite the same code. This saves time and reduces redundancy.
  - **Namespace Management:** Modules create separate **namespaces**. A namespace is a container that provides a naming context. When you import a module, it creates its own namespace. This helps prevent naming conflicts between variables, functions, or classes defined in different modules. If you have two functions with the same name in different modules, they won't clash because they belong to different namespaces.
  - **Modularity and Maintainability:** By dividing your code into modules, you achieve better modularity. Each module can be developed, tested, and maintained independently. This makes it easier to find and fix bugs, and to update or extend parts of your program without affecting other parts.
  - **Code Distribution and Collaboration:** Modules are the building blocks for creating libraries and packages, which are units of code that can be easily distributed and shared. This is essential for collaboration and for using code developed by others.

- **Built-in Modules (Python Standard Library):**

  - Python comes with a vast collection of pre-built modules known as the **Python Standard Library**. These modules provide a wide range of functionalities for common programming tasks, without you having to write them from scratch.
  - **Examples of Useful Built-in Modules:**

    - **`math` Module:** Provides mathematical functions and constants.
      - `math.sqrt(x)`: Square root of `x`.
      - `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Trigonometric functions (sine, cosine, tangent).
      - `math.pi`: Mathematical constant π (pi).
      - `math.log(x, [base])`: Logarithm of `x` to the given base (default base is `e` - natural logarithm).
      - `math.pow(x, y)`: `x` raised to the power of `y` (`x**y`).
    - **`random` Module:** For generating pseudo-random numbers and making random choices.
      - `random.random()`: Returns a random float number between 0.0 and 1.0.
      - `random.randint(a, b)`: Returns a random integer N such that `a <= N <= b`.
      - `random.choice(sequence)`: Returns a randomly selected element from a non-empty sequence (like a list or tuple).
      - `random.shuffle(list)`: Shuffles the elements of a list in place (modifies the original list randomly).
    - **`datetime` Module:** For working with dates and times.
      - `datetime.datetime`: Represents a specific date and time (year, month, day, hour, minute, second, microsecond).
      - `datetime.date`: Represents a date (year, month, day).
      - `datetime.time`: Represents a time (hour, minute, second, microsecond).
      - `datetime.timedelta`: Represents a duration, a difference between two dates or times.
      - `datetime.datetime.now()`: Get the current date and time.
    - **`os` Module:** Provides functions for interacting with the operating system. **Use with caution when demonstrating, as some operations can be system-specific or potentially dangerous if not used carefully.**
      - `os.getcwd()`: Get the current working directory.
      - `os.listdir(path)`: List directory contents at `path`.
      - `os.path.join(path1, path2, ...)`: Join path components in a platform-independent way.
      - `os.mkdir(path)`: Create a directory.
      - `os.remove(path)`: Delete a file.
    - **`sys` Module:** Provides access to system-specific parameters and functions.
      - `sys.path`: A list of strings specifying the search path for modules. Python looks in these directories when you try to import a module.
      - `sys.version`: String containing Python version information.
      - `sys.argv`: List of command-line arguments passed to the Python script.

- **Importing Modules:** To use modules in your Python code, you need to import them. Python offers several ways to import modules:

  1.  **`import module_name`:** This is the most common way to import a module. It imports the entire module. To access items (functions, variables, classes) from the module, you need to use the module name as a prefix, followed by a dot `.`, and then the item name. This is called **namespace prefixing**.

      ```python
      import math # Import the entire math module

      result_sqrt = math.sqrt(16) # Use math.sqrt() to access the sqrt function
      print(f"Square root of 16: {result_sqrt}") # Output: Square root of 16: 4.0

      pi_value = math.pi # Access the math.pi constant
      print(f"Value of pi: {pi_value}") # Output: Value of pi: 3.141592653589793
      ```

  2.  **`import module_name as alias`:** This imports the entire module but assigns it a shorter **alias** (an alternative name). This can be useful for long module names to make your code more concise and readable.

      ```python
      import datetime as dt # Import datetime module and give it alias 'dt'

      current_datetime = dt.datetime.now() # Use dt.datetime.now()
      print(f"Current date and time: {current_datetime}")
      ```

  3.  **`from module_name import item_name1, item_name2, ...`:** This allows you to import specific items (functions, variables, classes) directly from a module into your current namespace. After importing this way, you can use the imported items directly, without the module name prefix.

      ```python
      from random import randint, choice # Import randint and choice functions from random module

      random_integer = randint(1, 100) # Use randint directly
      print(f"Random integer between 1 and 100: {random_integer}")

      colors = ["red", "green", "blue"]
      random_color = choice(colors) # Use choice directly
      print(f"Randomly chosen color: {random_color}")
      ```

  4.  **`from module_name import *`:** This imports **all** public names (functions, variables, classes) defined in a module directly into your current namespace. **This is generally discouraged** and considered bad practice in most cases.

      - **Why Avoid `import *`?**

        - **Namespace Pollution:** It imports a large number of names into your namespace, potentially overwriting existing names or introducing naming conflicts, making your code harder to understand and debug.
        - **Reduced Readability:** It becomes unclear where a particular name (function, variable) is coming from. You have to look up the module to know its origin.
        - **Maintenance Issues:** If the module changes and adds or removes names, your code that uses `import *` might break unexpectedly or behave differently.

      - **When `import *` Might Be Considered (Rare Cases, e.g., Interactive Sessions, Very Specific Modules):** In very rare scenarios, like interactive sessions in a Python interpreter or for very specific modules that are designed to be used this way (and are well-documented), `import *` might be used for convenience. However, for most regular code, it's best to avoid `import *` and use more explicit import methods (`import module_name` or `from module_name import item_name1, ...`).

  **Best Practice for Importing:** It is generally recommended to use `import module_name` or `from module_name import item_name1, ...` to keep your namespaces clean and code readable and maintainable. `import as alias` can be useful for long module names or to avoid name clashes. Avoid `from module_name import *` in most situations.

- **Module Search Path (`sys.path`):**

  - When you use an `import` statement, Python needs to find the module you are trying to import. Python searches for modules in a list of directories called the **module search path**. You can see this path by inspecting `sys.path`:

    ```python
    import sys
    print(sys.path) # Prints a list of directory paths
    ```

  - `sys.path` is a list of directory paths. When you try to import a module named `mymodule`, Python looks in these directories in the following order:

    1.  **Current Directory:** The directory where your current Python script is running.
    2.  **Directories in `PYTHONPATH` Environment Variable:** If you have set the `PYTHONPATH` environment variable, Python will look in the directories listed in it.
    3.  **Installation-Dependent Default Directories:** These are standard directories where Python libraries and modules are installed when you install Python itself and when you install packages using tools like `pip`.
    4.  **(And potentially other paths based on Python installation and environment).**

  - Python searches these directories in order. The first directory in the list is searched first. If the module is found in a directory, Python loads and imports it. If it's not found after searching all directories in `sys.path`, Python raises an `ImportError`.

  - **Adding Directories to `sys.path` (Usually Not Necessary for Basic Usage):** In some advanced scenarios, you might need to add your own directories to `sys.path` if your modules are located in non-standard locations. You can modify `sys.path` list in your Python script, but for most cases, placing your modules in the same directory as your main script or in standard package locations is sufficient.

- **Creating Your Own Modules:** Creating your own modules in Python is very simple.

  1.  **Create a Python File:** Just create a new file with a `.py` extension (e.g., `my_module.py`).
  2.  **Write Python Code in the File:** Inside this `.py` file, write any valid Python code you want to include in your module: function definitions, class definitions, variable assignments, etc.
  3.  **Example: `my_module.py`**

      ```python
      # my_module.py
      """This is a simple example module."""

      MODULE_VERSION = "1.0" # Module-level variable

      def greet(name): # Function definition
          """Greets a person."""
          return f"Hello, {name}! Welcome to my module."

      def square_list(numbers): # Another function
          """Squares each number in a list and returns a new list."""
          squared_numbers = [n**2 for n in numbers]
          return squared_numbers
      ```

  4.  **Using Your Module in Another Script:** Save `my_module.py` in the same directory as your main Python script (or in a directory that is in Python's module search path). Then, you can import and use your module:

      ```python
      # main_script.py
      import my_module # Import your custom module

      message = my_module.greet("User") # Call function from module using namespace prefix
      print(message) # Output: Hello, User! Welcome to my module.

      numbers_to_square = [1, 2, 3, 4, 5]
      squared_list = my_module.square_list(numbers_to_square)
      print(f"Squared numbers: {squared_list}") # Output: Squared numbers: [1, 4, 9, 16, 25]

      module_version = my_module.MODULE_VERSION # Access module-level variable
      print(f"Module version: {module_version}") # Output: Module version: 1.0
      ```

#### 2. Packages

- **Definition:** A package is a way to **organize Python modules into a hierarchy of directories**. A package can contain:

  - Modules (`.py` files).
  - Subpackages (directories that are themselves packages).
  - Special `__init__.py` files that mark directories as packages.

- **Why Use Packages?**

  - **Hierarchical Organization:** Packages provide a way to structure very large Python projects into a logical hierarchy of modules and subpackages, just like you organize files into folders and subfolders in a file system. This greatly improves code organization and makes large projects more manageable.
  - **Namespace Hierarchy (Avoid Name Clashes in Large Projects):** Packages extend namespace management. Modules within different packages can have the same name without conflict because they reside in different package namespaces. This is crucial for large projects and libraries to avoid name collisions.
  - **Improved Code Maintainability:** Packages make it easier to navigate, understand, and maintain large codebases by grouping related modules together in a structured way.

- **Creating Packages:** To create a Python package, you essentially create a directory structure and add `__init__.py` files.

  1.  **Create a Package Directory:** Create a directory (folder) that will be your package's top-level directory. Let's say you want to create a package named `mypackage`.

      ```
      mypackage/  # Package directory
      ```

  2.  **Add `__init__.py` File:** Inside the `mypackage` directory, create an empty file named `__init__.py`. This file is what tells Python that this directory should be treated as a package. `__init__.py` can be empty, or it can contain initialization code for the package (e.g., setting up package-level variables or importing modules that should be readily available when the package is imported). For simple packages, it's often just an empty file.

      ```
      mypackage/
          __init__.py   # Empty file, marks directory as package
      ```

  3.  **Add Modules (`.py` files) to the Package:** Place your module files (`.py` files) inside the `mypackage` directory. For example, let's create two modules: `module1.py` and `module2.py`.

      ```
      mypackage/
          __init__.py
          module1.py   # Module file 1
          module2.py   # Module file 2
      ```

      - **Example `module1.py`:**

        ```python
        # mypackage/module1.py
        def function_module1():
            return "Function from module1 in mypackage"
        ```

      - **Example `module2.py`:**

        ```python
        # mypackage/module2.py
        def function_module2():
            return "Function from module2 in mypackage"
        ```

  4.  **Using Modules from Your Package:** Now, you can import and use modules from your `mypackage` in other Python scripts, using dot notation to specify the package and module hierarchy. Make sure the directory containing `mypackage` is in Python's module search path (e.g., by running your main script from the directory containing `mypackage`, or by ensuring the parent directory of `mypackage` is in `sys.path`).

      ```python
      # main_script.py (in the directory *containing* mypackage)
      import mypackage.module1 # Import module1 from package mypackage
      from mypackage import module2 # Import module2 from package mypackage

      result1 = mypackage.module1.function_module1() # Access function using package.module.function
      print(result1) # Output: Function from module1 in mypackage

      result2 = module2.function_module2() # Access function from module2 (imported directly)
      print(result2) # Output: Function from module2 in mypackage
      ```

  5.  **Subpackages:** You can further structure your packages by creating subdirectories within a package, and making those subdirectories into packages as well by adding `__init__.py` files to them. This allows for deeper hierarchical organization.

      ```
      mypackage/
          __init__.py
          module1.py
          subpackage1/         # Subpackage directory
              __init__.py   # Marks subpackage1 as a package
              submodule1.py # Module within subpackage1
          subpackage2/         # Another subpackage
              __init__.py
              submodule2.py
      ```

      To import `submodule1` from `subpackage1`, you would use: `import mypackage.subpackage1.submodule1` or `from mypackage.subpackage1 import submodule1`.

- **Importing from Packages:**

  - **`import package_name.module_name`:** Imports a module from within a package. You need to use the full dotted path (package name, then module name) to access items within the module.

    ```python
    import mypackage.module1

    result = mypackage.module1.function_module1() # Full dotted path
    ```

  - **`from package_name import module_name`:** Imports a module directly from a package. You can then use the module name directly (without the package prefix) to access items within it.

    ```python
    from mypackage import module2

    result = module2.function_module2() # Module name directly
    ```

  - **`from package_name.module_name import item_name`:** Imports a specific item (function, class, variable) from a module within a package directly into your current namespace. You can then use the item name directly.

    ```python
    from mypackage.module1 import function_module1

    result = function_module1() # Function name directly
    ```

#### 3. External Packages and `pip` (Package Installer for Python)

- **Python Package Index (PyPI):** A vast online repository of third-party Python packages. It's the central repository where the Python community publishes and shares packages that extend Python's capabilities beyond the standard library. Thousands of packages are available on PyPI, covering a wide range of domains (web development, data science, machine learning, networking, etc.). [https://pypi.org/](https://pypi.org/)

- **`pip` (Package Installer for Python):** The standard package manager for Python. It's used to install, uninstall, and manage Python packages from PyPI and other package indexes. `pip` usually comes pre-installed with most modern Python installations.

- **Installing Packages using `pip`:** You typically use `pip` from your command line or terminal. The basic command to install a package is:

  ```bash
  pip install package_name
  ```

  - Replace `package_name` with the name of the package you want to install (e.g., `requests`, `numpy`, `pandas`).
  - `pip` will connect to PyPI, download the package and its dependencies, and install them in your Python environment.
  - **Example: Installing the `requests` package:**

    ```bash
    pip install requests
    ```

- **Uninstalling Packages using `pip`:**

  ```bash
  pip uninstall package_name
  ```

- **Listing Installed Packages:** To see a list of packages you have installed in your Python environment:

  ```bash
  pip list
  ```

- **Examples of Useful External Packages:**

  - **`requests`:** For making HTTP requests (fetching data from web servers, interacting with web APIs). Example:

    ```python
    import requests

    response = requests.get("[https://api.github.com/events](https://www.google.com/search?q=https://api.github.com/events)") # Make a GET request to GitHub API
    print(f"Status code: {response.status_code}") # Print HTTP status code (e.g., 200 for success)
    # print(response.content) # Print the raw content of the response (bytes)
    # print(response.text) # Print the response content as text (if it's text-based, e.g., JSON, HTML)
    data = response.json() # If the response is JSON, parse it into Python data structures (list, dict)
    print(data[0]['repo']['name']) # Example: Access data from the JSON response
    ```

  - **`NumPy` (Numerical Python):** Fundamental package for numerical computing in Python. Provides powerful array objects (ndarrays) and mathematical functions for working with arrays efficiently. Essential for scientific computing, data analysis, machine learning, etc.

  - **`Pandas`:** Provides high-performance, easy-to-use data structures and data analysis tools, especially the DataFrame (for tabular data). Widely used for data manipulation, cleaning, analysis, and preparation.

  - **`Matplotlib`:** A 2D plotting library for creating static, interactive, and animated visualizations in Python. Used for creating graphs, charts, plots, histograms, etc.

  - **`BeautifulSoup4` (bs4):** For web scraping - parsing HTML and XML documents to extract data from web pages.

  - **`Flask` / `Django`:** Popular web frameworks for building web applications in Python. Flask is a microframework (simple and flexible), Django is a more full-featured framework (for larger, more complex web projects).

#### 4. Virtual Environments

- **Why Virtual Environments?** When you work on Python projects, especially if you have multiple projects, you might need to use different versions of packages for different projects. Also, you might want to keep your project dependencies isolated from your system-wide Python installation. Virtual environments solve these problems.

- **Virtual Environment Concept:** A virtual environment is a self-contained directory that contains a Python installation and a set of installed packages that are specific to a particular project. When you activate a virtual environment, any `pip install` commands will install packages within that environment, not in your global Python installation. This isolates your project's dependencies.

- **Using `venv` (Built-in Module):** Python has a built-in module called `venv` for creating virtual environments.

  1.  **Create a Virtual Environment:** Open your terminal or command prompt, navigate to your project directory (or where you want to create the virtual environment), and run:

      ```bash
      python -m venv venv_name    # On some systems, use python3 instead of python
      ```

      - `venv` is the module name.
      - `venv_name` is the name you want to give to your virtual environment directory (e.g., `myenv`, `venv`, `.venv`). It will create a directory with this name in your current location.

  2.  **Activate the Virtual Environment:** You need to activate the virtual environment to use it. The activation script is in the virtual environment's directory.

      - **On Linux/macOS:**

        ```bash
        source venv_name/bin/activate
        ```

      - **On Windows (Command Prompt):**

        ```bash
        venv_name\Scripts\activate
        ```

      - **On Windows (PowerShell):**

        ```powershell
        venv_name\Scripts\Activate.ps1
        ```

      - After activation, you'll typically see the virtual environment's name in parentheses at the beginning of your command prompt, indicating that the virtual environment is active (e.g., `(venv_name) $`).

  3.  **Install Packages within the Virtual Environment:** Once activated, any `pip install package_name` command will install packages **only** within the active virtual environment. These packages will be isolated from your system-wide Python packages and packages in other virtual environments.

      ```bash
      (venv_name) $ pip install requests numpy pandas
      ```

  4.  **Deactivate the Virtual Environment:** When you are done working in the virtual environment, you can deactivate it to return to your base Python environment. Simply run:

      ```bash
      deactivate
      ```

      The virtual environment name will disappear from your command prompt, indicating deactivation.

- **Why are Virtual Environments Important?**
  - **Dependency Isolation:** Keeps project dependencies separate. Project A can use version 1.0 of a package, while Project B can use version 2.0, without conflicts.
  - **Reproducibility:** Makes it easier to reproduce project environments. You can create a `requirements.txt` file (using `pip freeze > requirements.txt`) listing all packages and their versions in your virtual environment, and share this file with others. They can then recreate the same environment using `pip install -r requirements.txt`.
  - **Clean System Environment:** Keeps your global Python installation clean and uncluttered. You install project-specific packages only within virtual environments, not globally.
  - **Collaboration:** Facilitates collaboration because everyone working on a project can use the same virtual environment setup, ensuring consistent dependencies and avoiding "it works on my machine" issues.

---

**Exercises:**

### Week 2: Day 5: Exercises

1.  **Using the `math` module:**

    - Import the `math` module.
    - Calculate and print the square root of 144 using `math.sqrt()`.
    - Calculate and print the sine of 30 degrees (remember `math.sin()` takes radians, convert degrees to radians using `math.radians()`).
    - Print the value of `math.pi`.

2.  **Using the `random` module:**

    - Import the `random` module.
    - Generate and print a random integer between 1 and 10 (inclusive) using `random.randint()`.
    - Create a list of colors: `colors = ["red", "green", "blue", "yellow"]`.
    - Randomly choose and print one color from the `colors` list using `random.choice()`.
    - Shuffle the `colors` list randomly in place using `random.shuffle()`. Print the shuffled list.

3.  **Creating and Importing a Custom Module:**

    - Create a new Python file named `greeting_module.py` in the same directory as your script.
    - In `greeting_module.py`, define a function `greet_message(name)` that returns a personalized greeting message (e.g., "Hello, \[name]!").
    - In your main script, import the `greeting_module`.
    - Call the `greet_message()` function from `greeting_module` and print the returned greeting for a name of your choice.

4.  **Working with Packages:**

    - Create a package named `my_utils_package`.
    - Inside `my_utils_package`, create an empty `__init__.py` file.
    - Inside `my_utils_package`, create two modules: `string_utils.py` and `math_utils.py`.
      - In `string_utils.py`, define a function `reverse_string(text)` that returns the reversed string.
      - In `math_utils.py`, define a function `factorial(n)` that calculates the factorial of a number `n`.
    - In your main script, import and use functions from both `string_utils` and `math_utils` modules from the `my_utils_package`.

5.  **Installing and Using an External Package (`requests`):**

    - **(Ensure you have internet connection).**
    - Open your terminal or command prompt and install the `requests` package using `pip install requests`.
    - In your Python script, import the `requests` package.
    - Use `requests.get()` to make a request to a public API endpoint (e.g., `https://api.chucknorris.io/jokes/random`).
    - Print the HTTP status code of the response (`response.status_code`).
    - If the status code is 200 (success), parse the JSON response using `response.json()` and print the "value" of the joke from the JSON data.

---

**Daily Simple Task:**

### Daily Simple Task - Day 5, Week 2

Create a module named `circle_module.py` that contains two functions: `circle_area(radius)` which calculates and returns the area of a circle, and `circle_circumference(radius)` which calculates and returns the circumference of a circle. In your main script, import this module and use both functions to calculate and print the area and circumference of a circle with a radius of 7.
