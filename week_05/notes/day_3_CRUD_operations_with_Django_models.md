# Week 5, Day 3: Mastering Data Interaction - CRUD Operations with Django Models

## Overview

Yesterday, we solidified our understanding of Django models and relationships, and today, we delve into the fundamental ways to interact with the data stored in our database: **CRUD operations**. CRUD is an acronym for **Create, Read, Update, and Delete**, representing the four basic functions of persistent storage. Django's Object-Relational Mapper (ORM) provides a powerful and Pythonic way to perform these operations on your models. By the end of this lesson, you will be able to:

-   Comprehend the significance of CRUD operations in web application development.
-   Create new records in your database using Django models.
-   Retrieve specific records or collections of records using various querying techniques.
-   Modify existing records in your database.
-   Remove records from your database.
-   Perform CRUD operations involving related models seamlessly.
-   Understand and apply best practices for efficient and secure database interactions.

> **Project-Based Note:**
> For your ongoing project, today's lesson equips you with the essential skills to manage your application's data. Whether it's adding new blog posts, displaying product details, updating user profiles, or removing obsolete items, mastering CRUD operations is key to building dynamic and interactive web applications.

---

## Lesson Plan

### 1. Recap of Week 5, Days 1 & 2

-   **Brief Review:** Let's quickly recap the key concepts from the beginning of the week:
    -   Defining Django models as Python classes that map to database tables.
    -   Understanding different field types (CharField, IntegerField, ForeignKey, etc.) and their usage.
    -   Establishing relationships between models using `ForeignKey`, `OneToOneField`, and `ManyToManyField`.
    -   Managing database schema changes using Django migrations (`makemigrations` and `migrate`).

### 2. CRUD Operations Overview

-   **Understanding CRUD:**
    -   **Create:** The operation of adding new data records to your database.
    -   **Read:** The process of retrieving or viewing existing data records from the database.
    -   **Update:** The action of modifying existing data records in the database.
    -   **Delete:** The operation of removing data records from the database.
-   **The Core of Data Interaction:** CRUD operations are fundamental to almost every data-driven web application. They enable users and the application itself to interact with and manage the stored information effectively.

### 3. Creating New Model Instances (Create)

-   **Method 1: Instantiating and Saving**
    -   This involves creating an instance of your model class, setting the values for its fields as attributes, and then explicitly saving the instance to the database using the `.save()` method.
    -   **Example (using the `Book` model from previous exercises):**
        ```python
        from catalog.models import Author, Book

        # Assuming an author with the name "Jane Austen" exists
        jane_austen = Author.objects.get(name="Jane Austen")

        new_book = Book(
            title="Pride and Prejudice",
            author=jane_austen,
            publication_year=1813,
            isbn="978-0141439518",
            price=10.99,
            is_available=True
        )
        new_book.save()  # Saves the new book record to the database
        print(f"Book '{new_book.title}' created with ID: {new_book.id}")
        ```
    -   **Handling Relationships During Creation:**
        -   For `ForeignKey` fields, assign the related model instance directly to the field.
        -   For `ManyToManyField` fields, first create and save the main object, then use the `.add()` method on the field's manager to associate existing related objects.
        ```python
        from catalog.models import Genre

        fantasy_genre = Genre.objects.get(name="Fantasy")
        # Assuming book1 from previous exercises exists
        book1.genres.add(fantasy_genre) # Adds the "Fantasy" genre to the book
        ```
    -   **Handling File Uploads:** When your model includes file fields like `ImageField` or `FileField`, you typically handle their creation through Django forms, often using `ModelForm`. When a form with a file field is submitted, ensure the form has the attribute `enctype="multipart/form-data"`. The file data is then available in the `request.FILES` dictionary within your view and is automatically handled by Django when you save the form.

-   **Method 2: Using `objects.create()`**
    -   The `objects.create()` method provides a more concise way to create a new object and immediately save it to the database in a single step. This method is suitable when you have all the necessary data available directly.
    -   **Example:**
        ```python
        from catalog.models import Author, Book

        # Assuming an author with the name "Charles Dickens" exists
        charles_dickens = Author.objects.get(name="Charles Dickens")

        another_book = Book.objects.create(
            title="Oliver Twist",
            author=charles_dickens,
            publication_year=1838,
            isbn="978-0141439631",
            price=12.50,
            is_available=False
        )
        print(f"Book '{another_book.title}' created with ID: {another_book.id}")
        ```

### 4. Retrieving Data (Read)

-   **The Django QuerySet API:** Django's ORM utilizes QuerySets to represent collections of objects retrieved from your database. You obtain these QuerySets through your model's **Manager**, which is named `objects` by default.

-   **Retrieving All Objects (`all()`):**
    ```python
    all_books = Book.objects.all()
    for book in all_books:
        print(book.title)
    ```

-   **Filtering Objects (`filter()`):**
    -   The `.filter()` method returns a new QuerySet containing objects that meet the specified conditions (lookup parameters).
    -   **Field Lookups:** Django offers a wide range of field lookups to define your filtering criteria:
        -   **Exact match:** `Book.objects.filter(title="Pride and Prejudice")`
        -   **Case-insensitive exact match:** `Book.objects.filter(title__iexact="pride and prejudice")`
        -   **Contains (case-sensitive):** `Book.objects.filter(title__contains="Pride")`
        -   **Contains (case-insensitive):** `Book.objects.filter(title__icontains="pride")`
        -   **Greater than/equal to, less than/equal to:** `Book.objects.filter(publication_year__gt=1900)`, `Book.objects.filter(pages__lte=500)`
        -   **In a list:** `Book.objects.filter(author__name__in=["Jane Austen", "Charles Dickens"])` (using `__` to traverse relationships)
        -   **Starts with/ends with (case-sensitive):** `Book.objects.filter(title__startswith="P")`, `Book.objects.filter(title__endswith="e")`
        -   **Range:** `Book.objects.filter(publication_year__range=(1800, 1850))`
        -   **Is null:** `Book.objects.filter(isbn__isnull=True)`
        -   Refer to the Django documentation for a complete list of available lookups.
    -   **Chaining Filters:** You can apply multiple `.filter()` calls sequentially to refine your query:
        ```python
        available_books_after_1900 = Book.objects.filter(is_available=True).filter(publication_year__gt=1900)
        ```

-   **Retrieving a Single Object (`get()`):**
    -   The `.get()` method retrieves exactly one object that matches the given lookup parameters.
    -   **Important:** It raises a `DoesNotExist` exception if no object matches the criteria and a `MultipleObjectsReturned` exception if more than one object is found.
    -   **Best Practice:** In Django views, it's often recommended to use `get_object_or_404` from `django.shortcuts` instead of `.get()` directly, as it handles the `DoesNotExist` exception by returning an HTTP 404 error, which is more appropriate for web requests.
    -   **Example:**
        ```python
        try:
            book = Book.objects.get(isbn="978-0141439518")
            print(f"Retrieved book: {book.title}")
        except Book.DoesNotExist:
            print("Book with that ISBN not found.")
        ```

-   **Retrieving the First or Last Object (`first()`, `last()`):**
    -   These methods return the first or last object from a QuerySet, respectively. They return `None` if the QuerySet is empty. Typically used after applying an ordering.
    ```python
    first_book_added = Book.objects.order_by('id').first()
    last_updated_book = Book.objects.order_by('-updated_at').last()
    ```

-   **Ordering Results (`order_by()`):**
    -   The `.order_by()` method allows you to sort the objects in a QuerySet based on one or more fields. Use a hyphen (`-`) before the field name to specify descending order.
    ```python
    books_by_year = Book.objects.order_by('publication_year')
    books_by_price_desc = Book.objects.order_by('-price', 'title') # Order by price descending, then by title ascending
    ```

-   **Retrieving Specific Field Values (`values()`, `values_list()`):**
    -   `.values()` returns a QuerySet of dictionaries. Each dictionary represents an object and contains the specified field names as keys and their corresponding values.
    -   `.values_list()` returns a QuerySet of tuples. Each tuple contains the values of the specified fields in the order they were listed. You can also pass `flat=True` if you are only retrieving a single field to get a flat list of values.
    ```python
    book_titles_and_authors = Book.objects.values('title', 'author__name') # Note querying across the 'author' ForeignKey
    for item in book_titles_and_authors:
        print(f"Title: {item['title']}, Author: {item['author__name']}")

    book_prices = Book.objects.values_list('title', 'price') # Returns tuples
    for title, price in book_prices:
        print(f"{title}: ${price}")

    all_titles = Book.objects.values_list('title', flat=True) # Returns a flat list of book titles
    for title in all_titles:
        print(title)
    ```

### 5. Updating Existing Model Instances (Update)

-   **Method 1: Retrieving, Modifying, and Saving**
    -   Retrieve the specific object you want to update using one of the read operations, modify its attributes directly, and then call the `.save()` method on the instance to persist the changes to the database.
    -   **Example:**
        ```python
        try:
            book_to_update = Book.objects.get(title="Pride and Prejudice")
            book_to_update.price = 11.50
            book_to_update.is_available = False
            book_to_update.save()
            print(f"Updated price and availability for '{book_to_update.title}'")
        except Book.DoesNotExist:
            print("Book not found.")
        ```
    -   **Handling File Uploads:** When updating models with file fields through forms, the process is similar to creation. You'll use a form (often a `ModelForm` instantiated with the existing instance), and if the user provides a new file, it will be available in `request.FILES` and handled automatically upon saving the form. If the user doesn't upload a new file, the existing file associated with the model will typically be retained.

-   **Method 2: Using `objects.update()`**
    -   The `.objects.update()` method allows you to update multiple objects that match a specific filter in a single database query. It returns the number of objects that were updated. This method is efficient for bulk updates but doesn't trigger model signals.
    -   **Example:**
        ```python
        num_updated = Book.objects.filter(author__name="Jane Austen").update(is_available=False)
        print(f"Updated {num_updated} books by Jane Austen to be unavailable.")
        ```
    -   **Updating Related Objects:** You can also update attributes of related objects by accessing them through the relationships.
        ```python
        try:
            author = Author.objects.get(name="Jane Austen")
            author.bio = "A renowned English novelist known for her works set among the British landed gentry."
            author.save()
            print(f"Updated bio for {author.name}")
        except Author.DoesNotExist:
            print("Author not found.")
        ```

### 6. Deleting Model Instances (Delete)

-   **Method 1: Retrieving and Deleting**
    -   Retrieve the specific object you wish to delete and then call the `.delete()` method on that instance.
    -   **Example:**
        ```python
        try:
            book_to_delete = Book.objects.get(title="Oliver Twist")
            book_to_delete.delete()
            print(f"Deleted book: '{book_to_delete.title}'")
        except Book.DoesNotExist:
            print("Book not found.")
        ```
-   **Implications of `on_delete`:** Remember the `on_delete` option you defined when setting up `ForeignKey` and `OneToOneField` relationships. When you delete an object that is referenced by other objects through these relationships, Django will perform the action specified in `on_delete` (e.g., `CASCADE` to delete related objects, `SET_NULL` to set the foreign key to `NULL`).

-   **Method 2: Using `objects.filter().delete()`**
    -   You can delete multiple objects that match a specific filter using the `.filter().delete()` method. This is often more efficient for deleting multiple records.
    -   **Example:**
        ```python
        num_deleted = Book.objects.filter(publication_year__lt=1800).delete()
        print(f"Deleted {num_deleted[0]} books published before 1800.") # .delete() returns a tuple with the count of deleted objects.
        ```
    -   **Caution:** Exercise extreme care when using `.delete()` on a QuerySet, especially without any filtering conditions, as it will delete all records for that model in the database.

### 7. Best Practices for CRUD Operations

-   **Input Validation:** Always validate user inputs before creating or updating data. Django Forms and ModelForms are excellent tools for handling this automatically.
-   **Error Handling:** Implement proper error handling using `try-except` blocks, especially when retrieving single objects with `.get()` to manage `DoesNotExist` exceptions gracefully.
-   **Atomic Transactions:** For critical operations that involve multiple database changes, use Django's transaction management (`django.db.transaction`) to ensure that all operations succeed or fail together, maintaining data integrity.
-   **Efficient Querying:** Be mindful of the number of database queries your code generates. Use techniques like `.select_related()` and `.prefetch_related()` to optimize queries involving related models and avoid the "N+1" problem. Retrieve only the necessary fields using `.only()` or `.values()` when you don't need all the attributes of a model instance.

### 8. Hands-on Practical Real-World Exercises and Tasks with Solutions

### Exercise 1: Creating and Retrieving Books (Including View-Based Creation)

**Objective:** Practice creating `Book` objects using both the Django shell and a simple view with a ModelForm.

1.  **Task (Shell):** Create two new `Book` objects in your `catalog` app using the Django shell, with different titles, authors, publication years, and ISBNs. Ensure at least one author already exists, and for the other, create a new `Author` object.
2.  **Task (View-Based):**
    a.  **Create a Model Form for Book:**

        ```python
        # In catalog/forms.py
        from django import forms
        from .models import Book

        class BookForm(forms.ModelForm):
            class Meta:
                model = Book
                fields = ['title', 'author', 'publication_year', 'isbn', 'price', 'is_available', 'cover_image']
        ```
    b.  **Create a View to Handle the Form:**

        ```python
        # In catalog/views.py
        from django.shortcuts import render, redirect
        from .forms import BookForm

        def create_book_view(request):
            if request.method == 'POST':
                form = BookForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    return redirect('book_list') # Assuming a view named 'book_list' exists
            else:
                form = BookForm()
            return render(request, 'catalog/create_book.html', {'form': form})
        ```
    c.  **Create the Template (`catalog/templates/catalog/create_book.html`):**

        ```html
        {% extends "base.html" %}
        {% block title %}Add New Book{% endblock %}
        {% block content %}
        <h2>Add a New Book</h2>
        <form method="post" enctype="multipart/form-data">
            {% csrf_token %}
            {{ form.as_p }}
            <button type="submit">Submit</button>
        </form>
        {% endblock %}
        ```
    d.  **Add a URL pattern in `catalog/urls.py`:**

        ```python
        from django.urls import path
        from . import views

        urlpatterns = [
            # ... other patterns
            path('books/create/', views.create_book_view, name='create_book'),
        ]
        ```
    e.  **Explanation:** This setup allows users to add a new book, including a cover image, through a web form. The `BookForm` handles validation and saving of the book data, including the uploaded image file.
3.  **Task (Shell):** Retrieve all books published after the year 1900.
4.  **Task (Shell):** Retrieve the book with a specific ISBN. Handle the case where the book might not exist.

<details>
<summary><b>Solution for Exercise 1</b></summary>
```python
from catalog.models import Author, Book
from catalog.forms import BookForm # Import for the view-based task
from django.shortcuts import render, redirect # Import for the view-based task
from django.urls import path # Import for the view-based task
from . import views # Import for the view-based task

# 1. Creating books (Shell)
author_rowling = Author.objects.create(name="J.K. Rowling")
book6 = Book.objects.create(title="Harry Potter and the Sorcerer's Stone", author=author_rowling, publication_year=1997, isbn="978-0590353403", price=10.50, is_available=True)
# Assuming author_asimov from previous exercise exists
book7 = Book.objects.create(title="I, Robot", author=Author.objects.get(name="Isaac Asimov"), publication_year=1950, isbn="978-0553803729", price=9.00, is_available=True)

# 2. View-Based Creation (Code provided in the task description - ensure you have 'base.html' or modify the template accordingly)

# 3. Retrieving books after 1900 (Shell)
post_1900_books = Book.objects.filter(publication_year__gt=1900)
print("Books published after 1900:")
for book in post_1900_books:
    print(book.title)

# 4. Retrieving a book by ISBN (Shell)
isbn_to_find = "978-0590353403"
try:
    book_found = Book.objects.get(isbn=isbn_to_find)
    print(f"\nBook with ISBN '{isbn_to_find}': {book_found.title}")
except Book.DoesNotExist:
    print(f"\nBook with ISBN '{isbn_to_find}' not found.")
```
</details>

### Exercise 2: Updating and Deleting Books

1.  **Task:** Retrieve the book titled "The Hobbit" and update its price to 12.99 and set `is_available` to `False`.
2.  **Task:** Delete all books published before the year 1950.

<details>
<summary><b>Solution for Exercise 2</b></summary>
```python
from catalog.models import Book

# 1. Updating "The Hobbit"
try:
    hobbit = Book.objects.get(title="The Hobbit")
    hobbit.price = 12.99
    hobbit.is_available = False
    hobbit.save()
    print(f"Updated '{hobbit.title}'. Price: ${hobbit.price}, Available: {hobbit.is_available}")
except Book.DoesNotExist:
    print("Book 'The Hobbit' not found.")

# 2. Deleting books before 1950
books_deleted = Book.objects.filter(publication_year__lt=1950).delete()
print(f"\nDeleted {books_deleted[0]} books published before 1950.")
```
</details>

### Exercise 3: Working with Relationships

1.  **Task:** Retrieve the author named "J.R.R. Tolkien". Then, retrieve all books written by this author.
2.  **Task:** Assuming you have `Genre` objects (e.g., "Fantasy", "Science Fiction"), retrieve the book titled "Foundation" and add the "Science Fiction" genre to it.

<details>
<summary><b>Solution for Exercise 3</b></summary>
```python
from catalog.models import Author, Book, Genre

# 1. Retrieving author and their books
try:
    tolkien = Author.objects.get(name="J.R.R. Tolkien")
    tolkien_books = Book.objects.filter(author=tolkien)
    print(f"\nBooks by {tolkien.name}:")
    for book in tolkien_books:
        print(book.title)
except Author.DoesNotExist:
    print("Author 'J.R.R. Tolkien' not found.")

# 2. Adding a genre to a book
try:
    foundation = Book.objects.get(title="Foundation")
    science_fiction_genre = Genre.objects.get(name="Science Fiction")
    foundation.genres.add(science_fiction_genre)
    print(f"\nAdded genre 'Science Fiction' to '{foundation.title}'.")
except Book.DoesNotExist:
    print("Book 'Foundation' not found.")
except Genre.DoesNotExist:
    print("Genre 'Science Fiction' not found.")
```
</details>

---

## Detailed Daily Task

**Task: Implement CRUD Operations for Your Blog Application (Using Django Shell)**

1.  **Scenario:** Using the `Author`, `Category`, and `BlogPost` models you defined in yesterday's daily task (or a similar blog model structure in your `blog` app), implement the following operations directly in the Django shell:

    -   **Create:** Create a new `Author`, a new `Category`, and a new `BlogPost` associated with that author and category.
    -   **Read:** Retrieve all blog posts that belong to a specific category (e.g., "Technology").
    -   **Update:** Retrieve a specific blog post by its title and update its content.
    -   **Delete:** Delete a specific blog post by its title.

2.  **Document the exact Python code you used in the Django shell to perform each of these operations.**

<details>
<summary><b>Solution for Daily Task</b></summary>
```python
from blog.models import Author, Category, BlogPost
from django.utils import timezone

# Create
new_author = Author.objects.create(name="Alice Smith", email="alice.smith@example.com")
new_category = Category.objects.create(name="Technology")
new_post = BlogPost.objects.create(
    title="Introduction to Django ORM",
    slug="introduction-to-django-orm",
    author=new_author,
    category=new_category,
    content="This is a detailed introduction to the Django ORM...",
    publish_date=timezone.now()
)
print(f"Created Post: {new_post.title}")

# Read
try:
    tech_category = Category.objects.get(name="Technology")
    tech_posts = BlogPost.objects.filter(category=tech_category)
    print("\nPosts in 'Technology' category:")
    for post in tech_posts:
        print(post.title)
except Category.DoesNotExist:
    print("Category 'Technology' not found.")

# Update
try:
    post_to_update = BlogPost.objects.get(title="Introduction to Django ORM")
    post_to_update.content = "This is an updated and even more detailed introduction to the Django ORM..."
    post_to_update.save()
    print(f"\nUpdated content for '{post_to_update.title}'.")
except BlogPost.DoesNotExist:
    print("Post 'Introduction to Django ORM' not found.")

# Delete
try:
    post_to_delete = BlogPost.objects.get(title="Introduction to Django ORM")
    post_to_delete.delete()
    print(f"\nDeleted post: '{post_to_delete.title}'.")
except BlogPost.DoesNotExist:
    print("Post 'Introduction to Django ORM' not found.")
```
</details>

---

## Final Wrap-up for Day 3 of Week 5

-   **Summary of Key Learnings:** Today, you've gained a solid understanding of how to perform the core CRUD operations on your Django models using the ORM. You can now create, retrieve, update, and delete data, as well as work with relationships during these operations. You've also learned how Django handles file uploads with forms and seen an example of integrating the ORM create operation within a view. You are now equipped with essential best practices for writing efficient and maintainable database interaction code.
-   **Next Steps:** Tomorrow, we will explore the Django Admin interface, a powerful built-in tool that automatically provides a user-friendly interface for managing your application's data based on your models. This will significantly simplify data management tasks during development and for content administrators.

*End of Week 5, Day 3 Study Material & Notes*
