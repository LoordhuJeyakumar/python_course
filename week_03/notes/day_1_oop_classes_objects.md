## Week 3, Day 1: Introduction to Object-Oriented Programming (OOP) - DETAILED

**Lesson Plan:**

1.  **Introduction to Object-Oriented Programming (OOP) Concepts**

    - **Recap of Week 2, Day 5 (Modules and Packages), Q&A**

      - Briefly review Modules and Packages, their benefits for code organization, reusability, and namespace management.
      - Address any questions or difficulties learners faced in the Week 2, Day 5 exercises or while studying modules and packages.
      - Quickly revisit importing modules, creating packages, using `pip` for external packages, and the purpose of virtual environments.

    - **Introduction to Object-Oriented Programming (OOP)**

      - **What is Object-Oriented Programming?**

        - Definition: OOP is a programming paradigm centered around "objects" rather than actions, and data rather than logic.
        - Contrast with Procedural Programming: Briefly explain how procedural programming focuses on functions or procedures that perform operations on data, while OOP focuses on objects that contain both data (attributes) and operations (methods).
        - Analogy: Relate OOP to real-world objects. Examples: `Car` (object) has attributes (color, model, speed) and methods (start, accelerate, brake). `Dog` (object) has attributes (breed, age, name) and methods (bark, eat, sleep).
        - Key Principles of OOP: Briefly introduce the four pillars of OOP that will be covered in detail:
          - **Encapsulation:** Bundling data (attributes) and methods that operate on the data into a single unit (an object). Hiding internal implementation details and exposing only necessary interfaces.
          - **Abstraction:** Simplifying complex reality by modeling classes appropriate to the problem. Focusing on essential features and hiding unnecessary details.
          - **Inheritance:** Creating new classes (derived or child classes) based on existing classes (base or parent classes), inheriting their attributes and methods. Promoting code reuse and establishing "is-a" relationships.
          - **Polymorphism:** The ability of different classes to respond to the same method call in their own specific ways. "Many forms" - one interface, multiple implementations.

      - **Objects and Classes:**

        - **Class Definition:**

          - Definition: A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (behavior) that objects of that class will have.
          - Syntax in Python: Introduce the `class` keyword, class name conventions (PascalCase), and the basic structure of a class definition.
          - Example: Define a simple `Dog` class with attributes like `breed`, `age`, `name` and methods like `bark()`, `description()`.
          - Explain the `__init__` method (constructor):
            - Purpose: Special method automatically called when an object is created. Used to initialize the object's attributes.
            - `self` parameter: Explain `self` as a reference to the instance of the class. It's used to access and modify the object's attributes within the class methods.
            - Demonstrate defining `__init__` in the `Dog` class to initialize `breed`, `age`, and `name` when a `Dog` object is created.

        - **Object (Instance) Creation:**
          - Definition: An object is a specific instance of a class. Created based on the blueprint provided by the class.
          - Instantiation: Explain how to create objects (instances) of a class by calling the class name like a function, passing arguments to the `__init__` method.
          - Example: Create `Dog` objects like `my_dog = Dog("Golden Retriever", 3, "Buddy")`, `another_dog = Dog("Labrador", 5, "Lucy")`.
          - Accessing Attributes: Demonstrate accessing object attributes using dot notation (`object_name.attribute_name`). Example: `my_dog.name`, `my_dog.breed`, `my_dog.age`.
          - Calling Methods: Demonstrate calling object methods using dot notation (`object_name.method_name()`). Example: `my_dog.bark()`, `my_dog.description()`.

      - **Encapsulation in Detail:**

        - Definition: Bundling of data (attributes) and methods that operate on that data within a class. Restricting direct access to some of the object's components.
        - Purpose: Data protection, preventing accidental modification of data from outside the object, code organization, and managing complexity.
        - Access Modifiers (Briefly mention, Python's approach is different):
          - Public, Private, Protected (Conceptually introduce, but emphasize Python's lack of strict enforcement).
          - Naming Conventions in Python for Encapsulation:
            - Public attributes and methods: Standard names (e.g., `name`, `bark()`).
            - "Private" attributes and methods: Naming convention using a single underscore prefix (`_attribute`, `_method()`). Indicate they are intended for internal use, but Python doesn't strictly prevent external access (convention, not enforcement).
            - "Name mangling" for stronger privacy (less common for beginners, but introduce for awareness): Double underscore prefix (`__attribute`, `__method()`). Python mangles these names to make them harder to access from outside the class, but still not truly private.
        - Getter and Setter Methods (Properties in Python - introduce later if time permits, or in Day 2):
          - Concept: Provide controlled access to "private" attributes through getter methods (to retrieve the value) and setter methods (to modify the value).
          - Example: For the `Dog` class, demonstrate creating a getter method `get_age()` to retrieve the `age` and a setter method `set_age(new_age)` to update the `age`, even if `age` is conceptually treated as "internal".

      - **Abstraction in Detail:**
        - Definition: Simplifying complex systems by modeling classes that represent essential features without including low-level details. Hiding complex implementation and exposing only necessary information.
        - Purpose: Managing complexity, making code easier to use and understand, focusing on "what" an object does rather than "how" it does it.
        - Abstract Classes and Methods (Introduce concept, Python's `abc` module - might be slightly advanced for Day 1, can be touched upon briefly or moved to later):
          - Abstract Class: A class that cannot be instantiated directly. Designed to be a base class for other classes. May contain abstract methods.
          - Abstract Method: A method declared in an abstract class but without an implementation. Subclasses must provide concrete implementations for abstract methods.
          - Python's `abc` module (`from abc import ABC, abstractmethod`): Briefly show how to define abstract classes and methods in Python using `ABC` and `@abstractmethod` decorator. Example: Create an abstract class `Shape` with an abstract method `area()`, and then subclasses like `Circle`, `Rectangle` must implement `area()`.
        - Interface (Conceptually related to abstraction, might be introduced later):
          - Interface: A contract that defines a set of methods that a class must implement. Python doesn't have explicit interfaces like some languages (e.g., Java, C#), but the concept is important in OOP.

    - **Live coding and examples in the IDE (VS Code/PyCharm) throughout the lecture.**
      - Create `Dog` class and objects, demonstrate attribute access, method calls, encapsulation using naming conventions, and basic abstraction examples.
      - Encourage learners to follow along, experiment, and ask questions.

2.  **Inheritance and Polymorphism (Hands-on & Exercises)**

    - **Inheritance in Detail**

      - Definition: A mechanism where a new class (child class or derived class) inherits properties (attributes and methods) from an existing class (parent class or base class).
      - "Is-a" Relationship: Inheritance represents an "is-a" relationship. Example: A `GoldenRetriever` "is-a" `Dog`. A `Car` "is-a" `Vehicle`.
      - Benefits of Inheritance:
        - Code Reusability: Child classes inherit code from parent classes, reducing code duplication.
        - Extensibility: Child classes can extend or modify the behavior of parent classes.
        - Organization and Hierarchy: Creates a class hierarchy, making code more organized and easier to understand.
        - Polymorphism (Facilitates polymorphism, explained later).
      - Types of Inheritance (Single, Multiple, Multilevel - focus on Single and Multilevel for Day 1):
        - Single Inheritance: A class inherits from only one parent class. (Most common and easiest to understand initially). Example: `class GoldenRetriever(Dog):`.
        - Multiple Inheritance: A class inherits from multiple parent classes. (Mention briefly, can be more complex, potential for diamond problem - may defer detailed discussion). Example: `class HybridDog(GoldenRetriever, Poodle):`.
        - Multilevel Inheritance: Inheritance through multiple levels of classes. Example: `class Animal -> class Mammal -> class Dog -> class GoldenRetriever`.
      - Syntax for Inheritance in Python:
        - `class ChildClassName(ParentClassName):`
        - Demonstrate creating a `GoldenRetriever` class that inherits from the `Dog` class.
        - Inheriting `__init__` method:
          - If the child class doesn't define its own `__init__`, it inherits the parent's `__init__`.
          - If the child class needs its own `__init__` (to add new attributes or modify initialization), it can define its own `__init__`.
          - Using `super().__init__(...)` in the child's `__init__` to call the parent's `__init__` to initialize inherited attributes. Explain the importance of `super()` for proper inheritance and avoiding code duplication.
        - Method Overriding:
          - Definition: Child class can redefine a method that is already defined in its parent class.
          - Purpose: To provide a specialized implementation of a method in the child class while keeping the same method name.
          - Example: Override the `bark()` method in the `GoldenRetriever` class to have a specific bark sound different from the generic `Dog` bark.
          - Using `super().method_name()` to call the parent class's implementation of the overridden method from within the child class's overridden method (if needed to extend parent behavior).
        - Adding New Methods and Attributes in Child Class:
          - Demonstrate adding new attributes (e.g., `is_good_with_kids` in `GoldenRetriever`) and new methods (e.g., `fetch()` in `GoldenRetriever`) that are specific to the child class and not present in the parent class.

    - **Polymorphism in Detail**

      - Definition: "Many forms." The ability of different classes to respond to the same method call in their own unique ways. Allows objects of different classes to be treated as objects of a common type (often through inheritance or interfaces).
      - "One interface, many implementations."
      - Types of Polymorphism (Focus on Method Overriding and Duck Typing for Day 1):
        - Method Overriding (already introduced with Inheritance): Polymorphism achieved through method overriding. Child classes provide their own implementations of methods inherited from parent classes.
        - Duck Typing (Python's dynamic typing): "If it walks like a duck and quacks like a duck, then it must be a duck." In Python, polymorphism is often achieved through duck typing. The type or class of an object is less important than the methods it supports. If an object has the necessary methods, it can be used where an object of a certain type is expected.
        - Method Overloading (Python has limited built-in support for traditional method overloading based on argument types, might skip for Day 1 or mention briefly as different from other languages).
      - Example of Polymorphism with `Dog` and `Cat` classes:
        - Create a base class `Animal` with a method `speak()`.
        - Create subclasses `Dog` and `Cat` that inherit from `Animal` and override the `speak()` method to make a "Woof!" and "Meow!" sound respectively.
        - Demonstrate calling `speak()` on objects of `Dog` and `Cat` classes. The appropriate `speak()` method is called based on the object's class (polymorphic behavior).
        - Example with a function that takes an `Animal` object and calls `speak()`. This function will work correctly with both `Dog` and `Cat` objects due to polymorphism.

    - **Hands-on Exercises:** Learners practice creating classes, objects, inheritance hierarchies, method overriding, and simple polymorphism examples. Exercises should include tasks like:

      - Creating a base class `Shape` with methods like `area()` and `perimeter()` (returning 0 for base class). Create subclasses `Rectangle`, `Circle`, `Triangle` that inherit from `Shape` and override these methods to calculate the respective areas and perimeters.
      - Creating a class hierarchy for `Vehicle` -> `Car`, `Bicycle`, `Motorcycle`. `Vehicle` class can have attributes like `color`, `model`, `speed` and methods like `start_engine()`, `stop_engine()`. Subclasses can override or extend these methods and add their own attributes and methods (e.g., `Car` can have `number_of_doors`, `Bicycle` can have `has_basket`).
      - Demonstrating polymorphism by creating a list of different `Shape` objects (Rectangle, Circle, Triangle) and iterating through the list, calling the `area()` method on each object. Show that the correct `area()` method for each shape is executed.
      - Create a simple `BankAccount` class with methods `deposit()`, `withdraw()`, `get_balance()`. Create subclasses `SavingsAccount` and `CheckingAccount` that inherit from `BankAccount`. `SavingsAccount` might have an additional method `calculate_interest()` and `CheckingAccount` might have a method to `order_checks()`.

    - **Example problem solving:** Guide learners to solve problems using OOP principles:

      - Model a simple Library Management System using OOP. Classes could be `Book`, `Library`, `Patron`. `Book` objects have attributes like `title`, `author`, `ISBN`, `is_checked_out`. `Library` can have methods to `add_book()`, `remove_book()`, `checkout_book()`, `return_book()`. `Patron` objects can represent library members.
      - Design classes to represent different types of employees in a company (e.g., `Employee`, `Manager`, `Engineer`, `Salesperson`). `Employee` can be a base class with common attributes like `name`, `employee_id`, `salary` and methods like `calculate_pay()`. Subclasses can override `calculate_pay()` to implement salary calculation logic specific to their roles.

    - **Q&A and wrap-up:** Address learner questions. Recap OOP concepts: classes, objects, encapsulation, abstraction, inheritance, polymorphism. Emphasize the benefits of OOP for code organization, reusability, and maintainability in larger projects. Preview Day 2 topics (more OOP concepts, class methods, static methods, properties, etc.).

---

**Study Material & Notes:**

### Week 3: Day 1: Introduction to Object-Oriented Programming (OOP)

**Notes:**

#### 1. Introduction to Object-Oriented Programming (OOP)

- **What is Object-Oriented Programming?**

  - **Paradigm Shift:** Object-Oriented Programming (OOP) is a fundamental shift from procedural programming. Instead of focusing on procedures or functions, OOP emphasizes **objects**. Think of objects as self-contained entities that bundle together both data and the actions that can be performed on that data.
  - **Objects as Building Blocks:** In OOP, you design your programs around objects. Each object is an instance of a **class**, which acts as a blueprint. Classes define the _type_ of object, specifying what kind of data it can hold and what actions it can perform.
  - **Real-World Analogy:** Imagine the real world. It's full of objects: cars, dogs, people, buildings, etc. Each object has characteristics (attributes) and can perform actions (behaviors). OOP tries to model this real-world approach in programming.
    - **Example: A `Dog` Object:**
      - **Attributes (Data):** Breed (e.g., "Labrador"), age (e.g., 3 years), name (e.g., "Buddy"), color (e.g., "Golden").
      - **Methods (Behaviors/Actions):** `bark()`, `eat()`, `sleep()`, `fetch()`, `wag_tail()`.
  - **Key Advantages of OOP:**
    - **Modularity:** OOP breaks down complex problems into smaller, self-contained objects. This makes code easier to manage, understand, and debug. Each object is like a module with its own data and functionality.
    - **Reusability:** OOP promotes code reuse through concepts like inheritance. You can create new classes based on existing ones, inheriting and extending their functionality. This saves development time and reduces redundancy.
    - **Maintainability:** OOP code tends to be more maintainable because of its modular structure and encapsulation. Changes in one part of the system are less likely to have unintended side effects in other parts.
    - **Abstraction:** OOP allows you to hide complex implementation details and expose only essential information. This simplifies the interface and makes it easier to use objects without needing to know their inner workings.
    - **Flexibility and Extensibility:** OOP designs are often more flexible and extensible. You can easily add new features or modify existing ones by creating new objects or modifying existing classes without disrupting the entire system.
    - **Team Collaboration:** OOP principles facilitate team collaboration by providing clear interfaces and modular components. Different developers can work on different objects or classes with less risk of conflicts.

- **Four Pillars of OOP:** These are the core principles that define object-oriented programming:

  1.  **Encapsulation:**
      - **Bundling:** Encapsulation is the principle of bundling data (attributes) and methods (functions) that operate on that data into a single unit called an **object**. Think of it as a capsule that contains both data and code.
      - **Data Hiding:** Encapsulation also involves hiding the internal implementation details of an object and protecting its data from unauthorized access or modification from outside the object. You interact with objects through well-defined interfaces (methods).
      - **Analogy:** A car engine is encapsulated. You interact with it through controls like the accelerator and brake (methods), but you don't need to know the complex internal workings of the engine to drive the car.
  2.  **Abstraction:**
      - **Simplification:** Abstraction means simplifying complex reality by modeling classes that represent only the essential features and behaviors relevant to a particular problem or context.
      - **Hiding Complexity:** It involves hiding unnecessary implementation details from the user and presenting a simplified, high-level interface. You focus on _what_ an object does, not _how_ it does it.
      - **Analogy:** When you use a smartphone, you interact with apps through icons and touch gestures. You don't need to understand the intricate electronics and software code running in the background. The smartphone provides an abstract interface to complex functionalities.
  3.  **Inheritance:**
      - **"Is-a" Relationship:** Inheritance is a powerful mechanism that allows you to create new classes (child or derived classes) that are based on existing classes (parent or base classes). The child class inherits attributes and methods from the parent class.
      - **Code Reusability:** Inheritance promotes code reuse. You can define common attributes and behaviors in a parent class and then reuse them in multiple child classes.
      - **Extending Functionality:** Child classes can extend the functionality of parent classes by adding new attributes and methods or by modifying inherited ones.
      - **Hierarchy:** Inheritance establishes a class hierarchy, representing "is-a" relationships. For example, "a `Dog` is an `Animal`," "a `Car` is a `Vehicle`."
  4.  **Polymorphism:**
      - **"Many Forms":** Polymorphism means "many forms." It's the ability of different classes to respond to the same method call in their own specific ways. It allows objects of different types to be treated as objects of a common type.
      - **One Interface, Multiple Implementations:** Polymorphism enables you to write code that can work with objects of different classes in a uniform way, as long as they support a common interface (e.g., have a method with the same name).
      - **Example:** Consider a `speak()` method. A `Dog` object's `speak()` might produce "Woof!", while a `Cat` object's `speak()` might produce "Meow!". Both are "speaking," but they do it differently. You can call `speak()` on either a `Dog` or a `Cat` object, and the appropriate sound will be produced based on the object's actual type.

#### 2. Objects and Classes in Python

- **Classes: Blueprints for Objects**

  - **Definition:** A class is a blueprint or a template that defines the characteristics (attributes) and behaviors (methods) that objects of that class will possess. It's like a cookie cutter – it defines the shape, but you need to use it to create actual cookies (objects).
  - **Syntax:** In Python, you define a class using the `class` keyword, followed by the class name (by convention, use PascalCase - e.g., `ClassName`). The class body contains attributes (variables) and methods (functions).

    ```python
    class ClassName:
        # Class attributes (variables shared by all objects of the class)
        class_attribute = "This is a class attribute"

        # Constructor - special method to initialize objects
        def __init__(self, attribute1, attribute2):
            # Instance attributes (unique to each object)
            self.attribute1 = attribute1
            self.attribute2 = attribute2

        # Methods (functions that objects of this class can perform)
        def method1(self):
            # Method implementation
            pass

        def method2(self, parameter):
            # Method implementation with parameters
            pass
    ```

  - **Example: `Dog` Class**

    ```python
    class Dog:
        """Represents a dog.""" # Docstring to describe the class

        species = "Canis familiaris" # Class attribute, common to all Dog objects

        def __init__(self, breed, age, name):
            """Constructor to initialize Dog objects."""
            self.breed = breed      # Instance attribute: breed of the dog
            self.age = age          # Instance attribute: age of the dog
            self.name = name        # Instance attribute: name of the dog

        def bark(self):
            """Makes the dog bark."""
            return "Woof!"

        def description(self):
            """Returns a description of the dog."""
            return f"{self.name} is a {self.age}-year-old {self.breed}."
    ```

    - **`class Dog:`**: Starts the class definition. `Dog` is the name of the class.
    - **`"""Represents a dog."""`**: Docstring - good practice to document your classes.
    - **`species = "Canis familiaris"`**: A **class attribute**. It's defined at the class level and is shared by all `Dog` objects. All dogs are of the same species.
    - **`def __init__(self, breed, age, name):`**: The **constructor** (initializer). It's a special method named `__init__`. It's automatically called when you create a new `Dog` object.
      - **`self`**: The first parameter of instance methods (including `__init__`) is always `self`. It's a reference to the current instance of the class (the object being created or operated on).
      - **`breed, age, name`**: Parameters for the constructor. When you create a `Dog` object, you'll pass values for these.
      - **`self.breed = breed`**, **`self.age = age`**, **`self.name = name`**: Inside `__init__`, these lines create **instance attributes**. `self.breed`, `self.age`, `self.name` are attributes that will be unique to each `Dog` object. They store the breed, age, and name of _this specific dog_.
    - **`def bark(self):`** and **`def description(self):`**: These are **methods** of the `Dog` class. Methods are functions defined within a class that operate on objects of that class.
      - Like `__init__`, the first parameter is `self`.
      - `bark()` method returns the string "Woof!".
      - `description()` method returns a formatted string using the dog's `name`, `age`, and `breed` attributes.

- **Objects (Instances) of a Class**

  - **Definition:** An object is a concrete instance of a class. A class is the blueprint, and an object is the actual entity created based on that blueprint. You can create multiple objects from the same class, each with its own set of attribute values.
  - **Instantiation (Creating Objects):** To create an object of a class, you call the class name like a function, passing any necessary arguments to the constructor (`__init__` method).

    ```python
    # Creating Dog objects (instances of the Dog class)
    my_dog = Dog("Golden Retriever", 3, "Buddy")  # Create a Dog object, call __init__
    another_dog = Dog("Labrador", 5, "Lucy")      # Create another Dog object
    ```

    - **`my_dog = Dog("Golden Retriever", 3, "Buddy")`**: This line creates a `Dog` object and assigns it to the variable `my_dog`.
      - `Dog("Golden Retriever", 3, "Buddy")` is calling the `Dog` class like a function. This triggers the `__init__` method.
      - The arguments `"Golden Retriever"`, `3`, and `"Buddy"` are passed to the `__init__` method's parameters `breed`, `age`, and `name` respectively.
      - Inside `__init__`, `self` refers to the newly created `Dog` object, and the attributes `breed`, `age`, and `name` are set for this specific `Dog` object.
    - **`another_dog = Dog("Labrador", 5, "Lucy")`**: Creates another `Dog` object with different attribute values.

  - **Accessing Attributes:** You access the attributes of an object using dot notation (`object_name.attribute_name`).

    ```python
    print(my_dog.name)   # Output: Buddy
    print(my_dog.breed)  # Output: Golden Retriever
    print(my_dog.age)    # Output: 3
    print(another_dog.name) # Output: Lucy
    ```

  - **Calling Methods:** You call methods of an object using dot notation as well (`object_name.method_name()`).

    ```python
    print(my_dog.bark())         # Output: Woof!
    print(another_dog.description()) # Output: Lucy is a 5-year-old Labrador.
    ```

#### 3. Encapsulation in Detail

- **Bundling and Hiding:** Encapsulation is about bundling data (attributes) and methods that operate on that data together within a class. It also involves controlling access to the internal workings of an object and hiding implementation details.
- **Purpose of Encapsulation:**
  - **Data Protection:** Prevents accidental or unauthorized modification of an object's data from outside the object. You control how data is accessed and changed through methods.
  - **Code Organization:** Keeps data and related operations together, making code more organized and easier to understand.
  - **Abstraction and Simplicity:** Hides complex internal implementation details from the user of the object. Users interact with objects through a simplified interface (methods).
  - **Maintainability and Flexibility:** Allows you to change the internal implementation of a class without affecting code that uses it, as long as the public interface (methods) remains the same.
- **Access Modifiers and Naming Conventions in Python:**

  - **Python's Approach:** Python doesn't have strict access modifiers like `private`, `public`, or `protected` as in some other languages (e.g., Java, C++). Instead, it relies on naming conventions to indicate the intended level of access.
  - **Public Attributes and Methods:**
    - Names with no special prefixes are considered public. They are intended to be accessed and used from outside the class.
    - Example: In the `Dog` class, `breed`, `age`, `name`, `bark()`, `description()` are public.
  - **"Private" Attributes and Methods (Naming Convention):**

    - Use a single underscore prefix `_` in front of the name (e.g., `_attribute`, `_method()`).
    - **Convention, Not Enforcement:** This is a convention to indicate that an attribute or method is intended for internal use within the class and its subclasses. Python does _not_ prevent external access to single-underscore names. It's a signal to other programmers to treat them as internal.
    - Example:

      ```python
      class BankAccount:
          def __init__(self, account_number, balance):
              self.account_number = account_number # Public attribute
              self._balance = balance          # "Private" attribute (by convention)

          def deposit(self, amount):
              if amount > 0:
                  self._balance += amount
              else:
                  print("Deposit amount must be positive.")

          def get_balance(self): # Public method to access balance
              return self._balance
      ```

      - `_balance` is intended to be treated as "internal." You should ideally access and modify it through methods like `deposit()` and `get_balance()`, not directly from outside the class. However, you _can_ still access it directly (e.g., `account._balance`), but it's against the convention.

  - **"Name Mangling" for Stronger Privacy (Double Underscore):**

    - Use a double underscore prefix `__` (e.g., `__attribute`, `__method()`).
    - **Name Mangling:** Python performs "name mangling" on double-underscore names. It changes the name to make it harder (but not impossible) to access from outside the class. The name is effectively renamed to `_ClassName__attribute`.
    - **Intended for More Robust Privacy:** Provides a slightly stronger level of privacy compared to single underscore, but it's still not true private access restriction like in some other languages.
    - Example:

      ```python
      class MyClass:
          def __init__(self):
              self.__private_attribute = 10 # Name mangled attribute

          def get_private_attribute(self):
              return self.__private_attribute

      obj = MyClass()
      # print(obj.__private_attribute) # This will raise an AttributeError
      print(obj.get_private_attribute()) # Access through public method (OK)
      print(obj._MyClass__private_attribute) # Accessing mangled name (still possible, but discouraged)
      ```

      - `__private_attribute` is name-mangled. You cannot directly access it as `obj.__private_attribute` from outside the class. You should use the public method `get_private_attribute()` to access it. However, you _can_ still access it using the mangled name `obj._MyClass__private_attribute`, but it's highly discouraged and considered breaking encapsulation.

  - **Getter and Setter Methods (Properties - Advanced, might introduce later):**

    - **Controlled Access:** Getter methods (accessors) are used to retrieve the value of a "private" attribute. Setter methods (mutators) are used to modify the value of a "private" attribute, often with validation or logic.
    - **Example with `Dog` Class (using getter and setter for `age`)**:

      ```python
      class Dog:
          def __init__(self, breed, age, name):
              self.breed = breed
              self._age = age  # "Private" attribute for age (using single underscore)
              self.name = name

          def get_age(self): # Getter method for age
              return self._age

          def set_age(self, new_age): # Setter method for age
              if isinstance(new_age, int) and new_age >= 0:
                  self._age = new_age
              else:
                  print("Invalid age. Age must be a non-negative integer.")

          def bark(self):
              return "Woof!"

          def description(self):
              return f"{self.name} is a {self._age}-year-old {self.breed}."

      my_dog = Dog("Pug", 2, "Max")
      print(my_dog.get_age()) # Get age using getter: Output: 2
      my_dog.set_age(4)       # Set age using setter
      print(my_dog.get_age()) # Output: 4
      my_dog.set_age(-1)      # Try to set invalid age: Output: Invalid age. Age must be a non-negative integer.
      print(my_dog.get_age()) # Age remains unchanged: Output: 4
      # print(my_dog._age)     # Still possible to access directly, but discouraged
      ```

      - `_age` is treated as "private."
      - `get_age()` is the getter method – it returns the value of `_age`.
      - `set_age(new_age)` is the setter method – it allows you to update `_age`, but with validation (ensuring age is a non-negative integer). This provides controlled modification.

        **Simple Practice Task: Encapsulation - `Book` Class**

             Create a class `Book` with:
             1.  A "private" instance attribute `_title` (using single underscore convention) and a public instance attribute `author`.
             2.  A getter method `get_title()` to access the book's title.
             3.  A setter method `set_title(new_title)` to modify the title, including a simple validation to ensure the new title is not empty.
             4.  In your main script, create a `Book` object, set its author and title (using the setter), then access and print the title using the getter method and the author attribute directly.

#### 4. Abstraction in Detail

- **Simplifying Complexity:** Abstraction is about hiding complex implementation details and exposing only the essential features of an object. It allows you to work with objects at a higher level of abstraction, focusing on _what_ they do rather than _how_ they do it.
- **Purpose of Abstraction:**
  - **Managing Complexity:** In complex systems, abstraction helps to manage complexity by breaking down the system into simpler, more manageable parts. You can focus on the interactions between objects without getting bogged down in their internal workings.
  - **Ease of Use:** Makes objects easier to use. Users don't need to understand the intricate details of how an object is implemented to use its functionalities. They interact with it through a simplified interface.
  - **Flexibility to Change Implementation:** Abstraction allows you to change the internal implementation of a class without affecting the code that uses it, as long as the abstract interface (public methods) remains consistent. This provides flexibility for future modifications and improvements.
- **Abstract Classes and Methods (Python's `abc` module):**

  - **Abstract Class:**
    - A class that is designed to be a blueprint for other classes but cannot be instantiated directly. You cannot create objects of an abstract class itself.
    - Abstract classes serve as base classes to define a common interface for a group of related subclasses.
    - In Python, you create abstract classes using the `abc` module (`abc` stands for Abstract Base Classes).
    - To make a class abstract, you inherit from `ABC` (Abstract Base Class) from the `abc` module.
  - **Abstract Method:**
    - A method declared in an abstract class but without an implementation in the abstract class itself. It's like a placeholder method.
    - Subclasses of an abstract class are _required_ to provide concrete implementations for all abstract methods inherited from the abstract class. If a subclass fails to implement an abstract method, it will also become an abstract class and cannot be instantiated.
    - You declare abstract methods using the `@abstractmethod` decorator from the `abc` module.
  - **Example: Abstract `Shape` Class and Concrete Subclasses**

    ```python
    from abc import ABC, abstractmethod

    class Shape(ABC): # Shape is an abstract class (inherits from ABC)
        """Abstract base class for shapes."""

        @abstractmethod # Decorator to declare abstract method
        def area(self):
            """Abstract method to calculate area. Subclasses must implement this."""
            pass # No implementation in abstract class

        @abstractmethod
        def perimeter(self):
            """Abstract method to calculate perimeter. Subclasses must implement this."""
            pass

    class Rectangle(Shape): # Rectangle inherits from Shape
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self): # Concrete implementation of area for Rectangle
            return self.width * self.height

        def perimeter(self): # Concrete implementation of perimeter for Rectangle
            return 2 * (self.width + self.height)

    class Circle(Shape): # Circle inherits from Shape
        import math # Import math module within the class (or at the top)
        def __init__(self, radius):
            self.radius = radius

        def area(self): # Concrete implementation of area for Circle
            return math.pi * self.radius**2

        def perimeter(self): # Concrete implementation of perimeter for Circle
            return 2 * math.pi * self.radius

    # shape = Shape() # Error! Cannot instantiate abstract class Shape
    rect = Rectangle(5, 10) # OK, Rectangle is concrete
    circ = Circle(3)       # OK, Circle is concrete

    print(f"Rectangle area: {rect.area()}, perimeter: {rect.perimeter()}") # Output: Rectangle area: 50, perimeter: 30
    print(f"Circle area: {circ.area():.2f}, perimeter: {circ.perimeter():.2f}") # Output: Circle area: 28.27, perimeter: 18.85

    # class IncompleteShape(Shape): # If you don't implement abstract methods in subclass
    #     pass # IncompleteShape is also abstract, cannot be instantiated

    # incomplete = IncompleteShape() # Error! Cannot instantiate abstract class IncompleteShape
    ```

    - **`from abc import ABC, abstractmethod`**: Imports necessary classes and decorators from the `abc` module.
    - **`class Shape(ABC):`**: Defines `Shape` as an abstract class by inheriting from `ABC`.
    - **`@abstractmethod`**: Decorator used to mark `area()` and `perimeter()` as abstract methods in the `Shape` class. These methods have no implementation (`pass`) in the abstract class.
    - **`class Rectangle(Shape):`** and **`class Circle(Shape):`**: `Rectangle` and `Circle` are concrete subclasses of `Shape`. They _must_ provide implementations for the abstract methods `area()` and `perimeter()`. If they don't, they would also become abstract classes.
    - **`shape = Shape()`**: Raises an error because you cannot create an object of an abstract class directly.
    - **`rect = Rectangle(5, 10)`** and **`circ = Circle(3)`**: You can create objects of concrete subclasses like `Rectangle` and `Circle`.

    **Simple Practice Task: Abstraction - `AnimalSound` Abstract Class**

            1.  Create an abstract class `AnimalSound` with an abstract method `make_sound()`.
            2.  Create two concrete classes, `DogSound` and `CatSound`, that inherit from `AnimalSound`.
            3.  Implement the `make_sound()` method in `DogSound` to return "Woof!" and in `CatSound` to return "Meow!".
            4.  Attempt to instantiate `AnimalSound` directly (should result in an error).
            5.  Create instances of `DogSound` and `CatSound` and call the `make_sound()` method on each, printing the result.



#### 5. Inheritance in Detail

- **"Is-a" Relationship and Code Reuse:** Inheritance is a fundamental OOP concept that allows you to create a new class (child class or derived class) based on an existing class (parent class or base class). The child class inherits attributes and methods from the parent class. It represents an "is-a" relationship (e.g., "a `Dog` is an `Animal`"). Inheritance promotes code reusability and helps in organizing classes in a hierarchical manner.
- **Benefits of Inheritance:**
  - **Code Reusability:** Child classes inherit attributes and methods from parent classes, reducing the need to rewrite code. Common functionalities can be defined in the parent class and reused by multiple child classes.
  - **Extensibility:** Child classes can extend the functionality of parent classes by adding new attributes and methods or by overriding inherited methods to provide specialized behavior.
  - **Organization and Hierarchy:** Inheritance creates a clear class hierarchy, making code more organized, easier to understand, and maintain. It reflects real-world hierarchies and relationships.
  - **Polymorphism (Enables Polymorphism):** Inheritance is essential for achieving polymorphism. Polymorphic behavior often relies on inheritance hierarchies where different subclasses provide different implementations of methods inherited from a common parent class.
- **Types of Inheritance (Focus on Single and Multilevel):**

  - **Single Inheritance:** A child class inherits from only one parent class. This is the simplest and most common form of inheritance.

    ```python
    class Animal: # Parent class
        def speak(self):
            return "Generic animal sound"

    class Dog(Animal): # Dog inherits from Animal (single inheritance)
        def speak(self): # Method overriding
            return "Woof!"
    ```

  - **Multiple Inheritance:** A child class inherits from multiple parent classes. Python supports multiple inheritance, but it can introduce complexity (e.g., the "diamond problem" if there are conflicting names in parent classes).

    ```python
    class Flyer: # Parent class 1
        def fly(self):
            return "Can fly"

    class Swimmer: # Parent class 2
        def swim(self):
            return "Can swim"

    class Duck(Flyer, Swimmer): # Duck inherits from both Flyer and Swimmer (multiple inheritance)
        pass # Duck inherits fly() and swim() methods
    ```

  - **Multilevel Inheritance:** Inheritance extends through multiple levels. A class inherits from a parent, which in turn inherits from its parent, and so on.

    ```python
    class Animal: # Base class
        def breathe(self):
            return "Breathes air"

    class Mammal(Animal): # Mammal inherits from Animal
        def give_birth(self):
            return "Gives birth to live young"

    class Dog(Mammal): # Dog inherits from Mammal (and indirectly from Animal) - multilevel inheritance
        def bark(self):
            return "Woof!"
    ```

- **Syntax for Inheritance in Python:**

  - To make a class inherit from another, you specify the parent class name in parentheses after the child class name in the class definition:

    ```python
    class ChildClassName(ParentClassName):
        # Class body (attributes and methods of child class)
        pass
    ```

  - **Example: `GoldenRetriever` inheriting from `Dog`**

    ```python
    class Dog: # Parent class (already defined earlier)
        species = "Canis familiaris"
        def __init__(self, breed, age, name):
            self.breed = breed
            self.age = age
            self.name = name
        def bark(self):
            return "Woof!"
        def description(self):
            return f"{self.name} is a {self.age}-year-old {self.breed}."

    class GoldenRetriever(Dog): # GoldenRetriever inherits from Dog
        """Represents a Golden Retriever dog, a specific breed of Dog."""
        def __init__(self, age, name, coat_color): # Child class constructor
            # Initialize attributes inherited from Dog class using super()
            super().__init__("Golden Retriever", age, name) # Call parent's __init__
            self.coat_color = coat_color # Add new attribute specific to GoldenRetriever

        def bark(self): # Method overriding - Golden Retrievers bark differently
            return "Soft Woof!" # Override bark() method

        def fetch(self): # New method specific to GoldenRetriever
            return "Golden Retriever loves to fetch!"

        def description(self): # Overriding description to include coat color
            parent_description = super().description() # Get parent's description first
            return f"{parent_description} and has a {self.coat_color} coat."

    golden = GoldenRetriever(4, "Goldie", "Golden") # Create GoldenRetriever object
    print(golden.breed)       # Inherited attribute: Output: Golden Retriever
    print(golden.name)        # Inherited attribute: Output: Goldie
    print(golden.coat_color)  # New attribute: Output: Golden
    print(golden.bark())        # Overridden method: Output: Soft Woof!
    print(golden.fetch())       # New method: Output: Golden Retriever loves to fetch!
    print(golden.description()) # Overridden description: Output: Goldie is a 4-year-old Golden Retriever. and has a Golden coat.
    ```

    - **`class GoldenRetriever(Dog):`**: `GoldenRetriever` class inherits from `Dog`.
    - **`def __init__(self, age, name, coat_color):`**: Child class constructor. It takes `age`, `name`, and `coat_color` as parameters.
      - **`super().__init__("Golden Retriever", age, name)`**: Crucial use of `super()`. `super()` is used to call a method from the parent class. Here, `super().__init__(...)` calls the `__init__` method of the `Dog` class (parent class) to initialize the inherited attributes `breed`, `age`, and `name`. We _hardcode_ `"Golden Retriever"` for `breed` because all `GoldenRetriever` objects are of that breed. We reuse the parent class's initialization logic, avoiding code duplication.
      - **`self.coat_color = coat_color`**: Initializes a new attribute `coat_color` that is specific to `GoldenRetriever` objects.
    - **`def bark(self):`**: **Method Overriding**. `GoldenRetriever` class overrides the `bark()` method inherited from `Dog`. Now, when you call `bark()` on a `GoldenRetriever` object, it will execute this overridden version, not the one in the `Dog` class.
    - **`def fetch(self):`**: **Adding a New Method**. `GoldenRetriever` class adds a new method `fetch()` that is not present in the `Dog` class.
    - **`def description(self):`**: Overriding `description()` to extend parent behavior.
      - **`parent_description = super().description()`**: Uses `super().description()` to call the `description()` method of the parent `Dog` class and get its result. This reuses the parent's description logic.
      - Then, it extends the parent's description by adding information about the `coat_color`.

#### 6. Polymorphism in Detail

- **"Many Forms" and Flexibility:** Polymorphism, meaning "many forms," is a key OOP principle that allows objects of different classes to respond to the same method call in their own specific ways. It provides flexibility and allows you to write code that can work with objects of different types in a uniform manner.
- **"One Interface, Many Implementations":** Polymorphism is often described as "one interface, many implementations." It means you can define a common interface (e.g., a method name) in a parent class, and then different subclasses can implement this interface in their own way, according to their specific needs.
- **Types of Polymorphism (Focus on Method Overriding and Duck Typing):**

  - **Method Overriding (Polymorphism through Inheritance):**
    - Method overriding, which we discussed with inheritance, is a primary way to achieve polymorphism.
    - When a child class overrides a method of its parent class, it provides its own specific implementation of that method.
    - When you call this overridden method on an object of the child class, the child class's version of the method is executed, not the parent class's version.
    - Example: `Dog` and `Cat` classes overriding the `speak()` method of an `Animal` base class.
  - **Duck Typing (Python's Polymorphism):**

    - **"If it walks like a duck and quacks like a duck...":** Duck typing is a concept particularly relevant in dynamically typed languages like Python. It states, "If an object has the methods and attributes I need, I'll treat it as being of the type I want." The actual class or type of the object is less important than whether it supports the required operations.
    - **Focus on Behavior, Not Type:** Python emphasizes behavior over type. If an object has a `speak()` method, you can call `speak()` on it, regardless of whether it's a `Dog`, a `Cat`, or something else entirely.
    - Example:

      ```python
      class Dog:
          def speak(self):
              return "Woof!"

      class Cat:
          def speak(self):
              return "Meow!"

      class Duck: # Not related by inheritance to Dog or Cat
          def speak(self):
              return "Quack!"

      def animal_sound(animal): # Function that takes any 'animal' object
          return animal.speak() # Calls the 'speak' method

      my_dog = Dog()
      my_cat = Cat()
      my_duck = Duck()

      print(animal_sound(my_dog)) # Output: Woof!
      print(animal_sound(my_cat)) # Output: Meow!
      print(animal_sound(my_duck)) # Output: Quack!
      ```

      - The `animal_sound()` function doesn't care if the `animal` argument is a `Dog`, `Cat`, or `Duck`. It only cares that the object has a `speak()` method. This is duck typing in action. Any object that has a `speak()` method can be passed to `animal_sound()` and the code will work.

  - **Method Overloading (Limited in Python):**
    - In some languages, method overloading allows you to define multiple methods in the same class with the same name but different parameters (different number or types of arguments).
    - **Python's Approach:** Python has limited built-in support for traditional method overloading based on argument types. If you define multiple methods with the same name in a class, the last one defined will override the earlier ones.
    - You can achieve a form of method overloading in Python using default argument values or variable arguments (`*args`, `**kwargs`) to handle different numbers or types of arguments within a single method definition, but it's not overloading in the classic sense.

**Exercises:**

1.  **Create a `Rectangle` class:**

    - It should have attributes `width` and `height`, initialized in the `__init__` method.
    - Add methods `area()` (calculates and returns the area) and `perimeter()` (calculates and returns the perimeter).
    - Create `Rectangle` objects, set their attributes, and test the `area()` and `perimeter()` methods.

2.  **Create a `Student` class:**

    - Attributes: `name` (string), `student_id` (integer), `courses` (list of strings, initially empty).
    - Methods:
      - `enroll_in_course(course_name)`: Adds a course name to the `courses` list.
      - `drop_course(course_name)`: Removes a course name from the `courses` list.
      - `get_courses()`: Returns the list of enrolled courses.
      - `get_student_info()`: Returns a string with student's name, ID, and enrolled courses.
    - Create `Student` objects, enroll them in courses, drop courses, and display their information.

3.  **Create a class hierarchy for shapes:**

    - Base class: `Shape` (abstract class) with abstract methods `area()` and `perimeter()`.
    - Subclasses: `Circle`, `Square`, `Triangle` inheriting from `Shape`.
    - Implement `__init__`, `area()`, and `perimeter()` methods for each subclass with appropriate formulas. For `Triangle`, assume it's a right-angled triangle and take base and height as input.
    - Demonstrate polymorphism: Create a list of different shape objects and calculate the total area of all shapes in the list by iterating through it and calling the `area()` method on each object.

4.  **Inheritance and Method Overriding:**
    - Create a base class `Vehicle` with attributes `model_name`, `color`, `engine_type` and methods `start_engine()`, `stop_engine()`, `get_vehicle_info()`.
    - Create subclasses `Car`, `Motorcycle`, `Bus` inheriting from `Vehicle`.
    - Override the `start_engine()` method in `Car` and `Motorcycle` to print specific start engine messages for each type.
    - Add a new attribute `number_of_wheels` to the `Vehicle` class and initialize it in the `__init__` method of `Vehicle`. Ensure that the `__init__` methods of `Car`, `Motorcycle`, and `Bus` call the parent class's `__init__` using `super()`. Set appropriate values for `number_of_wheels` in the subclasses (e.g., 4 for `Car`, 2 for `Motorcycle`, 4 or 6 for `Bus`).
    - Test creating objects of each vehicle type and calling their methods.

**Daily Tasks:**

1.  **Review today's notes and study material thoroughly.**
2.  **Complete all the exercises.**
3.  **Experiment with creating your own classes and objects. Try to model real-world objects or scenarios using OOP concepts.**
4.  **Read more about OOP principles and Python's implementation of OOP from online resources (links provided in study material).**
5.  **Think about how you can apply OOP principles in your future projects to improve code organization and reusability.**

**Assignments:**

1.  **Design a system for a simple online store using OOP.**

    - Classes to consider: `Product`, `ShoppingCart`, `Customer`, `Order`.
    - `Product` attributes: `product_id`, `name`, `description`, `price`, `category`. Methods: `get_price()`, `get_description()`.
    - `ShoppingCart` attributes: `items` (list of `Product` objects). Methods: `add_item(product)`, `remove_item(product)`, `view_cart()`, `calculate_total()`.
    - `Customer` attributes: `customer_id`, `name`, `shipping_address`, `billing_information`. Methods: `place_order(shopping_cart)`.
    - `Order` attributes: `order_id`, `customer`, `items` (list of `Product` objects), `order_date`, `total_amount`, `order_status`. Methods: `get_order_details()`, `update_status(new_status)`.
    - Implement the classes with basic attributes and methods. You don't need to implement full functionality (e.g., payment processing, database interaction), just focus on class design and relationships. Demonstrate creating objects, adding products to a shopping cart, and placing an order.

2.  **Create a text-based game using OOP concepts.**
    - Choose a simple game like "Text Adventure," "Guess the Number," or "Rock Paper Scissors."
    - Identify the key objects and actions in the game.
    - Design classes to represent these objects (e.g., `Player`, `Room`, `Item`, `Game` for a Text Adventure; `Player`, `Computer`, `Game` for Rock Paper Scissors).
    - Implement the game logic using methods within the classes. For example, a `Player` class might have methods like `move_to_room(room)`, `take_item(item)`, `use_item(item)`. A `Room` class might have attributes like `description`, `items`, `exits`.
    - Focus on using OOP principles to structure your game code.

**Solutions to Exercises and Assignments will be provided in Week 3, Day 2 materials.**

---

**(To be continued in Week 3, Day 2 with more advanced OOP topics, class methods, static methods, properties, decorators, etc.)**
