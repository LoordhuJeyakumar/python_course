# Week 5, Day 1: Diving Deep into Django Models & Databases with the ORM

## Overview

Today marks the beginning of our exploration into how Django handles data persistence using its powerful **Object-Relational Mapper (ORM)**. We will move beyond just displaying static or dynamically generated content and learn how to define the structure of our application's data and interact with a database using Python code. By the end of this lesson, you will have a strong foundation in:

- Understanding what an ORM is and its significance in modern web development.
- Recognizing the advantages of using Django's ORM.
- Identifying the key components of the Django ORM: Models, Fields, and Queries.
- Configuring your Django project to connect to a database.
- Setting up a development database using SQLite.
- Defining your own Django models in the `models.py` file of your app.
- Utilizing the various field types available in Django models to represent different types of data.
- Understanding the purpose and basic usage of Django migrations.
- Grasping best practices for designing effective database models.
- Performing basic queries to retrieve data from your models.

> **Project-Based Note:**
> As we continue to develop our blog project (or any other mini-project you're working on), today's lesson is absolutely crucial. You will learn how to translate the entities of your application (like blog posts, categories, authors, comments) into Django models. This will enable you to store, retrieve, and manipulate data efficiently, forming the backbone of your web application's functionality.

---

## Lesson Plan

### 1. Recap of Week 4 (Relevant Parts)

-   **Brief Review:** Before we dive into databases, let's quickly remember the process of creating a Django project and apps using `django-admin startproject` and `python manage.py startapp`. Ensure you have a Django project set up and at least one app created where we can define our models.

### 2. Introduction to Django ORM: Bridging the Gap Between Objects and Databases

-   **What is an ORM (Object-Relational Mapper)?**
    -   An ORM acts as an intermediary layer between your object-oriented programming language (Python in our case) and a relational database. It allows you to interact with your database using Python objects and methods, abstracting away the need to write raw SQL queries.
    -   Think of the ORM as a translator that converts Python objects into database records (rows in tables) when you want to store data, and converts database records back into Python objects when you want to retrieve data.
-   **Benefits of Using the Django ORM:**
    -   **Database Abstraction:** You write Python code, and the ORM handles the specifics of interacting with your chosen database. This makes your code more readable and less dependent on a particular database system. Switching databases in the future becomes less daunting (though careful planning is still required).
    -   **Security:** The ORM helps prevent common security vulnerabilities like SQL injection by automatically escaping user inputs in queries.
    -   **Increased Productivity:** Developers can focus on the application's business logic using familiar Python syntax, rather than spending time writing and debugging SQL queries.
    -   **Code Portability:** Your model definitions are largely database-agnostic, making it easier to adapt your application to different database systems if needed.
-   **Django ORM Overview:**
    -   The Django ORM centers around three core concepts:
        -   **Models:** Python classes defined in your app's `models.py` file. Each model represents a table in your database. An instance of a model corresponds to a row in that table.
        -   **Fields:** Attributes of your model class. Each field represents a column in your database table and has a specific data type (e.g., text, integer, date).
        -   **Queries:** The Django ORM provides a high-level API to perform database operations (Create, Retrieve, Update, Delete - CRUD) using Python code. You typically won't need to write raw SQL.

### 3. Configuring Your Database in `settings.py`

-   **The `DATABASES` Setting:**
    -   Django uses the `DATABASES` dictionary in your project's `settings.py` file to store the connection details for your application's database.
    -   The `DATABASES` setting is a dictionary where each key represents a database connection. By default, Django configures a single connection named `'default'`.
-   **Supported Database Backends:**
    -   Django has built-in support for several popular relational database systems:
        -   **SQLite (`django.db.backends.sqlite3`):** A lightweight, file-based database ideal for development and smaller production projects. It requires no separate server setup and is often the default choice for beginners.
        -   **PostgreSQL (`django.db.backends.postgresql`):** A powerful, highly scalable, and feature-rich open-source relational database. Often preferred for production environments due to its robustness and advanced features.
        -   **MySQL (`django.db.backends.mysql`):** A widely used open-source relational database management system.
        -   **Oracle (`django.db.backends.oracle`):** A commercial relational database management system.
-   **Setting up a Development Database (SQLite Example):**
    -   Open your project's `settings.py` file. You will find the `DATABASES` dictionary pre-configured for SQLite:
        ```python
        import os

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
        ```
        -   **`ENGINE`:** Specifies the database backend. Here, `'django.db.backends.sqlite3'` tells Django to use SQLite.
        -   **`NAME`:** Specifies the name of the database. For SQLite, this is the path to the database file. `os.path.join(BASE_DIR, 'db.sqlite3')` ensures the database file (`db.sqlite3`) will be created in the root directory of your project. Django will automatically create this file when you run your first migration.
-   **Setting up Other Databases (Example - PostgreSQL):**
    -   If you decide to use a different database like PostgreSQL for your production environment (or even for development), you'll need to:
        1.  **Install the Database Adapter:** For PostgreSQL, you'll need the `psycopg2` library:
            ```bash
            pip install psycopg2-binary
            ```
            Similarly, you'd install `mysqlclient` for MySQL or `cx_Oracle` for Oracle.
        2.  **Configure `DATABASES`:** Update the `DATABASES` setting in `settings.py` with your database connection details:
            ```python
            DATABASES = {
                'default': {
                    'ENGINE': 'django.db.backends.postgresql',
                    'NAME': 'your_database_name',
                    'USER': 'your_username',
                    'PASSWORD': 'your_password',
                    'HOST': 'localhost',
                    'PORT': '5432',
                }
            }
            ```
            Replace `'your_database_name'`, `'your_username'`, `'your_password'` with your actual PostgreSQL credentials. `'HOST'` and `'PORT'` usually default to `localhost` and `5432` respectively for a local PostgreSQL installation.

### 4. Defining Your First Django Model (`models.py`)

-   **Models as Blueprints for Database Tables:**
    -   Django models are Python classes that act as blueprints for the tables in your database. Each model you define will eventually be translated into a database table with specific columns.
-   **Location of `models.py`:**
    -   You define your models within the `models.py` file of each Django app that needs to store data. For our blog example, we would define models like `Post`, `Author`, and `Category` in the `blog/models.py` file.
-   **Inheriting from `models.Model`:**
    -   Every Django model must inherit from the `django.db.models.Model` class. This base class provides all the necessary functionality for interacting with the database.
-   **Fields as Model Attributes:**
    -   The attributes you define within your model class represent the columns in your database table. Each attribute is an instance of a specific Django **field type**, which determines the kind of data that can be stored in that column (e.g., text, numbers, dates).
-   **Example Model:** Let's create a simple model for a `BlogPost`:
    ```python
    # In your app's models.py (e.g., blog/models.py)
    from django.db import models

    class BlogPost(models.Model):
        title = models.CharField(max_length=255)
        content = models.TextField()
        publish_date = models.DateTimeField()

        def __str__(self):
            return self.title
    ```
    -   `BlogPost` is the name of our model class. Django will typically create a database table named something like `appname_blogpost` (Django automatically adds a prefix based on your app name).
    -   `title`, `content`, and `publish_date` are fields of our model.
    -   `models.CharField`, `models.TextField`, and `models.DateTimeField` are the field types, indicating the type of data each field will store.
    -   The `__str__` method is a special Python method that defines how an instance of the `BlogPost` model will be represented as a string. This is very useful for debugging and in the Django admin interface.

### 5. Understanding Django Model Field Types

Django provides a wide variety of field types to accommodate different kinds of data. Here are some of the most commonly used ones with explanations and examples:

-   **`CharField(max_length=None, **options)`:** Used for storing strings of a fixed maximum length. You **must** specify the `max_length` argument, which defines the maximum number of characters allowed in the database column.
    ```python
    name = models.CharField(max_length=100, verbose_name="Author's Name")
    ```
-   **`TextField(**options)`:** Used for storing large, potentially unlimited amounts of text. It maps to a `TEXT` column in most databases.
    ```python
    body = models.TextField(verbose_name="Post Content")
    ```
-   **`IntegerField(**options)`:** Used for storing integer numbers.
    ```python
    age = models.IntegerField(verbose_name="Age")
    ```
-   **`FloatField(**options)`:** Used for storing floating-point numbers.
    ```python
    rating = models.FloatField(verbose_name="User Rating")
    ```
-   **`DecimalField(max_digits=None, decimal_places=None, **options)`:** Used for storing decimal numbers with a fixed precision. You **must** provide `max_digits` (total number of digits allowed, including decimal places) and `decimal_places` (number of digits after the decimal point).
    ```python
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Product Price")
    ```
-   **`BooleanField(default=False, **options)`:** Used for storing boolean (True/False) values. You can set a default value using the `default` argument.
    ```python
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    ```
-   **`DateField(auto_now=False, auto_now_add=False, **options)`:** Used for storing dates (year, month, day).
    -   `auto_now=True`: Automatically sets the field to the current date every time the model is saved. Useful for "last modified" timestamps.
    -   `auto_now_add=True`: Automatically sets the field to the current date when the model is first created. Useful for "creation date" timestamps.
    ```python
    publish_date = models.DateField(verbose_name="Publication Date")
    created_on = models.DateField(auto_now_add=True, verbose_name="Date Created")
    updated_on = models.DateField(auto_now=True, verbose_name="Date Updated")
    ```
-   **`DateTimeField(auto_now=False, auto_now_add=False, **options)`:** Used for storing dates and times. Similar `auto_now` and `auto_now_add` options are available.
    ```python
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Timestamp")
    ```
-   **`EmailField(max_length=254, **options)`:** Used for storing email addresses. It performs basic validation to ensure the input has a valid email format.
    ```python
    email = models.EmailField(verbose_name="Email Address")
    ```
-   **`URLField(max_length=200, **options)`:** Used for storing URLs. It performs basic validation to ensure the input is a valid URL.
    ```python
    website = models.URLField(verbose_name="Website URL")
    ```
-   **`SlugField(max_length=50, unique=False, **options)`:** A short label containing only letters, numbers, underscores or hyphens. Often used for SEO-friendly URLs. You can make it `unique=True` to ensure no two records have the same slug.
    ```python
    slug = models.SlugField(unique=True, verbose_name="URL Slug")
    ```
-   **Relationship Fields (Introduction - More on Day 2):**
    -   **`ForeignKey(to, on_delete, related_name=None, **options)`:** Represents a one-to-many relationship. The `to` argument specifies the model it's related to. `on_delete` specifies what happens when the referenced object is deleted (e.g., `models.CASCADE` to delete the current object as well, `models.SET_NULL` to set the field to `NULL` if allowed). `related_name` allows you to easily access the set of related objects from the "one" side of the relationship.
    -   **`ManyToManyField(to, related_name=None, **options)`:** Represents a many-to-many relationship.
    -   **`OneToOneField(to, on_delete, related_name=None, parent_link=False, **options)`:** Represents a one-to-one relationship.

### 6. Django Migrations: Evolving Your Database Schema

-   **Purpose of Migrations:** When you make changes to your Django models (e.g., adding a new field, deleting a field, changing a field type), these changes need to be reflected in your database schema (the structure of your database tables). **Migrations** are Django's way of propagating these changes to your database in a controlled and organized manner.
-   **Creating Migrations (`makemigrations`):** When you modify your `models.py` file, you need to tell Django to create migration files that describe how to update your database. You do this using the `makemigrations` management command:
    ```bash
    python manage.py makemigrations your_app_name
    ```
    If you don't specify an app name, Django will look for changes in all your apps. Django will then generate migration files (usually located in a `migrations` subdirectory within your app) that contain the Python code to apply the changes to your database schema.
-   **Applying Migrations (`migrate`):** Once the migration files are created, you need to apply them to your actual database using the `migrate` management command:
    ```bash
    python manage.py migrate
    ```
    This command executes the SQL statements defined in your migration files (and Django's built-in migrations for things like user management) to create or modify the tables in your database to match your current model definitions. **You need to run `migrate` every time you run `makemigrations` to actually apply the changes.**

### 7. Model Meta Options: Configuring Model Behavior

-   Within your model class, you can define an inner class named `Meta` to provide additional metadata and configuration options for your model.
-   **`verbose_name`:** A human-readable, singular name for your model. This is used in the Django admin interface and in other messages.
-   **`verbose_name_plural`:** The plural version of `verbose_name`.
-   **`ordering`:** A list or tuple of field names that specifies the default order in which objects of this model should be retrieved from the database. You can use a hyphen (`-`) before a field name to indicate descending order.
-   **Example:**
    ```python
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=8, decimal_places=2)

        class Meta:
            verbose_name = "Product Item"
            verbose_name_plural = "Product Items"
            ordering = ['name', '-price'] # Order by name ascending, then by price descending

        def __str__(self):
            return self.name
    ```

### 8. Best Practices for Modeling Data

-   **Keep Models Focused and Simple:** Each model should represent a single, clear concept or entity in your application. Avoid putting too much unrelated information into a single model.
-   **Use Meaningful Field Names and `verbose_name`:** Choose field names that clearly indicate the purpose of the data they store. Use the `verbose_name` option in your field definitions to provide human-readable names that will be used in the Django admin and forms.
-   **Plan Relationships Carefully:** Think about how different entities in your application relate to each other (one-to-one, one-to-many, many-to-many) and use the appropriate Django relationship fields (`ForeignKey`, `ManyToManyField`, `OneToOneField`). We will delve deeper into relationships tomorrow.
-   **Consider Data Types Carefully:** Choose the most appropriate field type for each piece of data you need to store. This helps ensure data integrity and efficiency. For example, use `IntegerField` for whole numbers, `DecimalField` for precise decimal values (like currency), and `EmailField` for email addresses.
-   **Think About Uniqueness and Indexing:** If a field should have unique values across all records (e.g., a username or an email address), set `unique=True`. For fields that you will frequently use to filter or search your data, consider adding database indexes to improve query performance (Django often handles this automatically for unique fields and foreign keys, but you might need to add explicit indexes in some cases).
-   **Document Your Models:** Add comments to your `models.py` file to explain the purpose of each model and its fields. This makes your code easier to understand and maintain.

### 9. Basic Querying with the Django ORM

-   **The `objects` Manager:** Every Django model automatically gets a manager called `objects`. This manager provides methods for performing database queries on your model.
-   **Retrieving All Objects (`all()`):** To get all instances of a model, you can use the `all()` method:
    ```python
    # Example: Retrieve all BlogPost objects
    all_posts = BlogPost.objects.all()
    ```
-   **Filtering Objects (`filter()`):** The `filter()` method allows you to retrieve a subset of objects that match specific conditions. You provide the conditions as keyword arguments where the key is the name of the field you want to filter on, and the value is the value you're looking for. You can also use "field lookups" (e.g., `__icontains` for case-insensitive containment).
    ```python
    # Example: Retrieve all blog posts with the title containing "Django"
    django_posts = BlogPost.objects.filter(title__icontains="Django")

    # Example: Retrieve all blog posts published after a specific date
    from datetime import datetime
    recent_posts = BlogPost.objects.filter(publish_date__gte=datetime(2023, 1, 1))
    ```
-   **Retrieving a Single Object (`get()`):** The `get()` method is used to retrieve a single object that matches the given conditions. **Be careful when using `get()` as it will raise an error (`Model.DoesNotExist`) if no object matches the criteria, or if multiple objects match.** It's often safer to use `get_object_or_404` (which we saw in the views lesson) in your views.
    ```python
    # Example: Retrieve the blog post with the ID equal to 1
    first_post = BlogPost.objects.get(id=1)
    ```
-   **Other Useful QuerySet Methods:** The `objects` manager and the `QuerySet` objects returned by methods like `all()` and `filter()` provide many other useful methods for interacting with your data, such as:
    -   `order_by()`: To specify the order of the results.
    -   `exclude()`: To retrieve objects that do *not* match the given conditions.
    -   `count()`: To get the number of objects in the QuerySet.
    -   `first()`: To get the first object in the QuerySet (returns `None` if the QuerySet is empty).
    -   `last()`: To get the last object in the QuerySet.

### 10. Wrap-up and Q&A

-   **Review Key Concepts:**
    -   The definition and benefits of the Django ORM.
    -   How to configure your database in `settings.py`.
    -   The role of `models.py` in defining your application's data structure.
    -   How to define models using various field types and their options.
    -   The purpose of Django migrations and the basic commands (`makemigrations` and `migrate`).
    -   The concept of Model Meta options for configuring model behavior.
    -   Best practices for designing effective database models.
    -   Basic querying using the `objects` manager and methods like `all()`, `filter()`, and `get()`.
-   **Discussion:** Encourage learners to ask questions about any aspect of the lesson. Discuss the importance of careful data modeling and the power of the ORM in simplifying database interactions.
-   **Preview Next Topic:** Tomorrow, we will delve deeper into defining relationships between models (one-to-one, one-to-many, many-to-many) and explore more advanced querying techniques.

---

## Detailed Study Materials & Notes

(This section provides more in-depth explanations and code examples for the topics covered above.)

### 1. Recap of Week 4

-   As a reminder, to create a Django project and an app, you would typically run commands like:
    ```bash
    django-admin startproject myproject
    cd myproject
    python manage.py startapp blog
    ```
    And then ensure `'blog'` is added to `INSTALLED_APPS` in `myproject/settings.py`.

### 2. Introduction to Django ORM (Expanded)

-   Explain with a simple analogy, like thinking of models as classes in Python, and instances of those models as objects. These objects hold data that needs to be stored persistently, and the ORM helps translate these objects into rows in database tables.

### 3. Configuring Databases in Django (More Detail)

-   Provide links to the official Django documentation for detailed instructions on setting up PostgreSQL, MySQL, and Oracle. Mention the specific database adapter libraries required for each.
    -   PostgreSQL: [https://docs.djangoproject.com/en/stable/ref/databases/#postgresql](https://www.google.com/search?q=https://docs.djangoproject.com/en/stable/ref/databases/%23postgresql)
    -   MySQL: [https://docs.djangoproject.com/en/stable/ref/databases/#mysql](https://www.google.com/search?q=https://docs.djangoproject.com/en/stable/ref/databases/%23mysql)
    -   SQLite: [https://docs.djangoproject.com/en/stable/ref/databases/#sqlite](https://www.google.com/search?q=https://docs.djangoproject.com/en/stable/ref/databases/%23sqlite)
    -   Oracle: [https://docs.djangoproject.com/en/stable/ref/databases/#oracle](https://www.google.com/search?q=https://docs.djangoproject.com/en/stable/ref/databases/%23oracle)

### 4. Introduction to Django Model Definition (`models.py`) (Expanded)

-   Reiterate that each model typically maps to a single database table. Django handles the creation of these tables based on your model definitions when you run migrations.

### 5. Understanding Django Model Field Types (Detailed Explanations and Options)

-   For each field type, provide examples of common options and their usage:
    -   `null=True`: Allows the database column to accept `NULL` values.
        ```python
        optional_bio = models.TextField(null=True, blank=True)
        ```
    -   `blank=True`: Allows the field to be empty in Django forms.
        ```python
        optional_bio = models.TextField(null=True, blank=True)
        ```
    -   `unique=True`: Ensures that no two records in the table have the same value for this field.
        ```python
        username = models.CharField(max_length=150, unique=True)
        ```
    -   `choices`: A sequence of (value, human-readable name) tuples to limit the choices for this field.
        ```python
        STATUS_CHOICES = [
            ('draft', 'Draft'),
            ('published', 'Published'),
        ]
        status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
        ```
    -   `default`: Sets a default value for the field if one is not provided when creating a new object.
        ```python
        is_premium = models.BooleanField(default=False)
        ```
    -   `help_text`: A short description of the field, often displayed in Django forms and the admin interface.
        ```python
        email = models.EmailField(help_text="Enter your primary email address.")
        ```

### 6. Django Migrations (More Detail)

-   Explain that Django keeps track of which migrations have been applied to your database. When you run `python manage.py migrate`, Django looks at the migrations that haven't been applied yet and runs them in order.
-   Mention that you can also rollback migrations to a previous state if needed (though we won't cover the commands for that today).

### 7. Model Meta Options (More Examples)

-   Show an example of using `ordering` with multiple fields:
    ```python
    class Comment(models.Model):
        # ... fields ...
        class Meta:
            ordering = ['post', '-created_at'] # Order by post ascending, then by creation time descending
    ```

### 8. Best Practices for Modeling Data (Expanded)

-   Emphasize the importance of thinking about the relationships between your data entities before defining your models. A well-designed data model is crucial for building a scalable and maintainable application.

### 9. Basic Querying with the Django ORM (More Examples)

-   Show examples of using `exclude()`:
    ```python
    # Get all blog posts that are not drafts (assuming a 'status' field)
    published_posts = BlogPost.objects.exclude(status='draft')
    ```
-   Example of using `order_by()`:
    ```python
    # Get all blog posts ordered by their publication date (oldest first)
    oldest_first_posts = BlogPost.objects.order_by('publish_date')

    # Get all blog posts ordered by their title in reverse alphabetical order
    reverse_alphabetical_posts = BlogPost.objects.order_by('-title')
    ```
-   Example of using `count()`:
    ```python
    total_number_of_posts = BlogPost.objects.count()
    print(f"Total posts: {total_number_of_posts}")
    ```

---

## Practical Exercises with Detailed Solutions

### Exercise 1: Creating Models for a Bookstore App

1.  **Task:** Create a Django project named `bookstore` and an app named `catalog` (if you haven't already done so from the previous file's exercises).
2.  **Task:** In `catalog/models.py`, define the following models:
    -   **`Author`:**
        -   `first_name` (CharField, max_length=50)
        -   `last_name` (CharField, max_length=50)
        -   `email` (EmailField)
        -   Add a `__str__` method that returns the author's full name.
    -   **`Book`:**
        -   `title` (CharField, max_length=200)
        -   `author` (ForeignKey to the `Author` model, on_delete=models.CASCADE)
        -   `isbn` (CharField, max_length=13, unique=True)
        -   `publication_year` (IntegerField)
        -   `price` (DecimalField, max_digits=6, decimal_places=2)

<details>
<summary><b>Solution for Exercise 1</b></summary>
```python
# catalog/models.py
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    publication_year = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
```
</details>

### Exercise 2: Applying Migrations

1.  **Task:** After defining the models in Exercise 1, run the `makemigrations` command for the `catalog` app.
2.  **Task:** Then, run the `migrate` command to create the database tables.

<details>
<summary><b>Solution for Exercise 2</b></summary>
Open your terminal in your project directory and run:
```bash
python manage.py makemigrations catalog
python manage.py migrate
```
You should see output indicating that migrations were created and applied.
</details>

### Exercise 3: Basic Querying in the Django Shell

1.  **Task:** Open the Django shell: `python manage.py shell`
2.  **Task:** Import the `Author` and `Book` models from `catalog.models`.
3.  **Task:** Create a few `Author` objects and a few `Book` objects, linking them to the authors.
4.  **Task:** Use the `objects.all()`, `objects.filter()`, and `objects.get()` methods to retrieve data from the database. For example:
    -   Get all authors.
    -   Get all books by a specific author.
    -   Get a book with a specific ISBN.
    -   Try to get a book with an ISBN that doesn't exist and observe the error.

<details>
<summary><b>Solution for Exercise 3</b></summary>
```python
from catalog.models import Author, Book

# Create authors
author1 = Author.objects.create(first_name="Jane", last_name="Austen", email="jane.austen@example.com")
author2 = Author.objects.create(first_name="Leo", last_name="Tolstoy", email="leo.tolstoy@example.com")

# Create books
book1 = Book.objects.create(title="Pride and Prejudice", author=author1, isbn="9780141439518", publication_year=1813, price=9.99)
book2 = Book.objects.create(title="War and Peace", author=author2, isbn="9780140449604", publication_year=1869, price=15.50)
book3 = Book.objects.create(title="Emma", author=author1, isbn="9780141439570", publication_year=1815, price=10.25)

# Get all authors
all_authors = Author.objects.all()
print(all_authors)

# Get all books by Jane Austen
austen_books = Book.objects.filter(author=author1)
print(austen_books)

# Get a book with a specific ISBN
war_and_peace = Book.objects.get(isbn="9780140449604")
print(war_and_peace)

# Try to get a book with a non-existent ISBN (will raise Book.DoesNotExist error)
# non_existent_book = Book.objects.get(isbn="1234567890123")


</details>

---

## Detailed Daily Task

**Task: Define Models for a Simple Blog Application (Revisited and Expanded)**

1.  **Scenario:** Continue building the data model for your blog application. You need to define models for `Author`, `Category`, and `BlogPost` with more detail.

2.  **Instructions:** Open the `models.py` file in your `blog` app. Define or modify the following models:

    -   **`Author` Model:**
        -   `first_name`: A `CharField` with a maximum length of 50 characters.
        -   `last_name`: A `CharField` with a maximum length of 50 characters.
        -   `email`: An `EmailField` with a `unique` constraint.
        -   `bio`: A `TextField` (optional, allow it to be blank and set `null=True`).
        -   Add a `__str__` method that returns the author's full name.

    -   **`Category` Model:**
        -   `name`: A `CharField` with a maximum length of 50 characters, and it should be `unique`.
        -   `description`: A `TextField` (optional, allow it to be blank and set `null=True`).
        -   Add a `__str__` method that returns the category name.

    -   **`BlogPost` Model:**
        -   `title`: A `CharField` with a maximum length of 255 characters.
        -   `slug`: A `SlugField` (we'll learn more about generating slugs later). Make it `unique=True`.
        -   `author`: A `ForeignKey` that relates to the `Author` model. When an author is deleted, their blog posts should also be deleted (use `on_delete=models.CASCADE`). Add a `related_name='blog_posts'` to the `Author` model.
        -   `category`: A `ForeignKey` that relates to the `Category` model. If a category is deleted, set the `category` field of the associated posts to `NULL` (use `on_delete=models.SET_NULL` and allow `null=True`). Add a `related_name='posts'` to the `Category` model.
        -   `content`: A `TextField`.
        -   `publish_date`: A `DateTimeField` (allow it to be `null=True` and `blank=True` for posts that are not yet published).
        -   `created_at`: A `DateTimeField` that automatically sets the current date and time when the post is created (`auto_now_add=True`).
        -   `updated_at`: A `DateTimeField` that automatically updates to the current date and time every time the post is saved (`auto_now=True`).
        -   Add a `__str__` method that returns the blog post's title.

<details>
<summary><b>Solution for Daily Task</b></summary>

```python
# blog/models.py
from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    content = models.TextField()
    publish_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```
</details>

---

## Final Wrap-up for Day 1 of Week 5

-   **Summary of Key Learnings:** Today, you've taken a significant step into the world of Django data management. You've learned about the Django ORM, how to configure your database, define models with various field types and options, and the importance of migrations. You've also started to explore basic querying and understand best practices for designing your data models.
-   **Next Steps:** Tomorrow, we will continue our journey with Django models by focusing on defining different types of relationships between models in more detail and learning more advanced querying techniques to retrieve and manipulate your application's data effectively.

*End of Week 5, Day 1 Study Material & Notes*