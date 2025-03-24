## Week 4, Day 2: Django Overview: MVT Architecture and Setup - Lesson Plan

**Lesson Plan:**

1.  **Recap of Day 1: Web Fundamentals**

    - Briefly review HTTP, client-server model, URLs, domains, DNS, and the HTTP request/response cycle.
    - Quick Q&A to ensure understanding of basic web concepts.

2.  **Introduction to Django: A High-Level Python Web Framework**

    - What is Django? Defining a web framework and its purpose.
    - Key benefits of using Django: Rapid development, security features, scalability, large community, "batteries-included" approach.
    - Use cases for Django: Content management systems, social networks, e-commerce platforms, APIs, etc.

3.  **Django's MVT (Model-View-Template) Architecture Explained**

    - Introduction to architectural patterns in web development.
    - Detailed explanation of the MVT pattern:
      - **Model:** The data layer - interacting with databases, data validation.
      - **View:** The business logic layer - handling HTTP requests, interacting with models, and preparing data for templates.
      - **Template:** The presentation layer - defining the structure and display of the user interface using HTML and template language.
    - The flow of data in an MVT application: User request -> URL routing -> View -> Model (optional) -> View -> Template -> HTTP response.
    - Analogy to help understand MVT (e.g., a restaurant: Model = ingredients, View = chef, Template = plate).
    - Brief comparison with the MVC (Model-View-Controller) architecture (mentioning similarities and key differences).

4.  **Setting up a Python Virtual Environment for Django Projects**

    - Importance of virtual environments for isolating project dependencies.
    - Step-by-step instructions on creating a virtual environment using `venv` (for Python 3):
      - Navigating to the desired project directory in the terminal.
      - Running the command: `python -m venv venv` (or `python3 -m venv venv` on some systems).
      - Activating the virtual environment:
        - On Windows: `venv\Scripts\activate`
        - On macOS/Linux: `source venv/bin/activate`
      - Visual confirmation of virtual environment activation (the `(venv)` prefix in the terminal).
    - Mentioning alternative tools like `conda` for environment management (optional, for more advanced learners or if it fits the bootcamp's broader scope).

5.  **Installing Django**

    - Ensuring the virtual environment is activated.
    - Using `pip`, the Python package installer, to install Django.
    - Running the command: `pip install Django`
    - Explaining that `pip` will download and install Django and its dependencies.
    - Verifying the Django installation:
      - Running `python -m django --version` in the terminal.
      - Understanding the output (the installed Django version).

6.  **Creating Your First Django Project**

    - Explaining the concept of a Django project as a collection of settings and applications.
    - Using the `django-admin` command-line utility.
    - Navigating to the directory where you want to create your project (outside the virtual environment directory is a common practice).
    - Running the command: `django-admin startproject myfirstproject` (emphasize choosing a meaningful project name).
    - Understanding the project directory structure created by this command.

7.  **Understanding the Django Project Structure**

    - Navigating into the newly created project directory: `cd myfirstproject`.
    - Explaining the purpose of the key files and directories:
      - `manage.py`: A command-line utility for administrative tasks (running the server, creating apps, running migrations, etc.).
      - `myfirstproject/` (inner directory with the same name): The actual Python package for your project.
        - `__init__.py`: An empty file that tells Python this directory is a package.
        - `settings.py`: Contains all the configuration settings for your Django project (database settings, installed apps, middleware, etc.). This will be explored in detail later.
        - `urls.py`: Defines the URL patterns for your project, mapping URLs to views. This is the project-level URL configuration.
        - `asgi.py`: Entry-point for ASGI-compatible web servers to serve your project. ASGI is a successor to WSGI and is used for asynchronous web applications.
        - `wsgi.py`: Entry-point for WSGI-compatible web servers to serve your project. WSGI is a standard interface between web servers and Python web applications.

8.  **Running the Django Development Server**

    - Explaining that Django comes with a built-in lightweight development server, suitable for testing and development.
    - Ensuring you are in the project's root directory (the one containing `manage.py`).
    - Running the command: `python manage.py runserver`
    - Understanding the output in the terminal (server address, port number).
    - Explaining how to access the development server in a web browser (usually at `http://127.0.0.1:8000/`).
    - Mentioning how to stop the server (usually by pressing `Ctrl + C` in the terminal).

9.  **Exploring the Default Django Project**

    - Describing what you should see in the browser when you access `http://127.0.0.1:8000/`: A default "It worked!" page, often with a Django logo.
    - Explaining that this confirms that Django is installed correctly and your project is set up and running.

10. **Troubleshooting Common Setup Issues**

    - Common problems beginners might encounter:
      - Python not being recognized as a command (ensure Python is added to the system's PATH environment variable).
      - `pip` command not found (ensure `pip` is installed correctly; it usually comes with Python installations).
      - Virtual environment not activated (double-check the activation steps for your operating system).
      - Incorrect directory when running `django-admin` or `manage.py` commands.
      - Port 8000 already in use (you can specify a different port using `python manage.py runserver 8080`).
    - Suggesting resources for troubleshooting (official Django documentation, online forums like Stack Overflow).

11. **Wrap-up and Q&A**
    - Review key concepts: Django as a web framework, MVT architecture (Model, View, Template), the setup process (virtual environment, installation, project creation), and running the development server.
    - Discuss the importance of each step in the setup process.
    - Open the floor for learner questions on Django overview and setup.
    - Briefly preview the next day's topic: Creating Django projects and apps.

---

# Day 2: Django Overview: MVT Architecture and Setup - Study Material & Notes

## Recap of Day 1: Web Fundamentals

Welcome back to Week 4! Yesterday, we laid the foundation by understanding the core concepts of the web. We learned about how the internet works, the role of HTTP in communication between clients (like your browser) and servers, and the structure of URLs. Remember the HTTP request/response cycle? Today, we'll build upon that knowledge by diving into Django, a powerful tool for building web applications with Python.

## 2. Introduction to Django: A High-Level Python Web Framework

So, what exactly is **Django**?

At its heart, Django is a **high-level Python web framework**. Think of a framework as a set of pre-written code, tools, and conventions that help you structure and build complex applications more efficiently. Instead of starting from scratch for every web project, Django provides the essential building blocks you need, allowing you to focus on the unique features of your application.

**Key Benefits of Using Django:**

- **Rapid Development:** Django follows conventions and provides many built-in features, which significantly speeds up the development process. This is often summarized by its motto: "The web framework for perfectionists with deadlines."
- **Security Features:** Security is a top priority in Django. It comes with built-in protection against common web vulnerabilities like cross-site scripting (XSS) and SQL injection.
- **Scalability:** Django is designed to handle high traffic and can be scaled to accommodate growing applications.
- **Large and Active Community:** Django has a vibrant and supportive community of developers. This means you can easily find help, tutorials, and third-party packages to extend Django's functionality.
- **"Batteries-Included" Approach:** Django comes with many essential features built-in, such as an ORM (Object-Relational Mapper) for database interaction, an admin interface, a templating engine, and more. This reduces the need to find and integrate external libraries for common tasks.

**What Can You Build with Django?**

Django's versatility allows it to be used for a wide range of web applications, including:

- **Content Management Systems (CMS):** Platforms like Wagtail are built on Django.
- **Social Networks:** While large platforms might use more complex architectures, Django is suitable for building many types of social networking sites.
- **E-commerce Platforms:** Django can handle the complexities of online stores.
- **RESTful APIs:** Django REST Framework, which we'll learn about later, makes building robust APIs easy.
- **Data Analysis and Visualization Tools:** Django can be used to create web interfaces for data-driven applications.

## 3. Django's MVT (Model-View-Template) Architecture Explained

Django follows an architectural pattern called **MVT**, which stands for **Model-View-Template**. This pattern helps to organize your code and separate different concerns within your application, making it more maintainable and easier to understand.

Let's break down each component:

- **Model:**

  - The **Model** is responsible for managing the application's data.
  - It interacts with the database (or other data storage mechanisms).
  - Models define the structure of your data (e.g., a "User" model might have fields like username, email, password).
  - Django's ORM (Object-Relational Mapper) allows you to interact with the database using Python code instead of writing raw SQL queries.
  - Models also often include logic for validating data.

- **View:**

  - The **View** contains the business logic of your application.
  - It receives HTTP requests from users.
  - It processes these requests, often by interacting with the **Model** to retrieve or update data.
  - The **View** then decides which **Template** to use to generate the response and prepares the data that the template will display.
  - In Django, "views" are typically Python functions or classes.

- **Template:**
  - The **Template** is the presentation layer of your application.
  - It's responsible for defining how the user interface will be displayed.
  - Templates are usually written in HTML, often with special syntax (Django's template language) that allows you to dynamically insert data passed from the **View**.
  - Templates focus on the structure and visual presentation, while the logic of what data to display is handled by the **View**.

**The Flow of Data in an MVT Application:**

Imagine a user wants to view a specific blog post on your Django website:

1.  **User Request:** The user clicks a link or types a URL in their browser, sending an HTTP request to your Django server.
2.  **URL Routing:** Django's URL dispatcher examines the requested URL and matches it to a specific **View** function or class that is responsible for handling that URL.
3.  **View:** The matched **View** is executed.
4.  **Model (Optional):** The **View** might need to retrieve data from the database to display the blog post. In this case, it will interact with the **Model** to fetch the necessary information.
5.  **View:** After retrieving the data (if needed), the **View** prepares this data to be displayed. This data is often passed to a **Template**.
6.  **Template:** The **View** selects an appropriate **Template** file. The template then uses the data passed by the view to dynamically generate the HTML content for the blog post.
7.  **HTTP Response:** Django sends the generated HTML back to the user's browser as an HTTP response.
8.  **Browser Rendering:** The user's browser receives the HTML and renders it, displaying the blog post to the user.

**MVT Analogy: The Restaurant**

Think of building a web page like ordering food at a restaurant:

- **Model (Ingredients):** The raw materials – the data stored in your database (like blog post content, user information, etc.).
- **View (Chef):** The chef takes your order (the HTTP request), gets the necessary ingredients (interacts with the Model), prepares the dish (processes the data), and decides how it should be presented (chooses the Template and prepares the data for it).
- **Template (Plate):** The plate is how the final dish (the web page) is presented to you. The chef (View) arranges the ingredients (data) on the plate (Template) to make it appealing.

**Brief Comparison with MVC (Model-View-Controller):**

You might have heard of the **MVC (Model-View-Controller)** architecture, which is similar to MVT. The key difference in Django's MVT is the role of the "Controller." In MVC, the Controller acts as an intermediary between the View and the Model, handling user input and updating the Model or selecting a View. In Django's MVT, the "View" essentially takes on the responsibilities of both the traditional View and the Controller from the MVC pattern. The "Template" in MVT corresponds to the "View" in MVC.

While the terminology differs slightly, the underlying principle of separating concerns remains the same. Django's MVT is well-suited for its design philosophy and has proven to be effective for building web applications.

## 4. Setting up a Python Virtual Environment for Django Projects

Before we start working with Django, it's crucial to set up a **virtual environment**. A virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting other Python projects on your system. This helps prevent conflicts between different project requirements.

Here's how to create and activate a virtual environment using `venv` (which comes built-in with Python 3):

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory where you plan to create your Django project.** This could be a folder on your desktop or a dedicated projects directory.
3.  **Run the following command:**

    ```bash
    python -m venv venv
    ```

    (On some systems, you might need to use `python3` instead of `python`.)

    This command will create a new directory named `venv` (you can choose a different name if you prefer) within your current directory. This `venv` directory will contain a copy of the Python interpreter and the `pip` package installer.

4.  **Activate the virtual environment.** You need to activate the environment to start using the Python interpreter and packages within it. The activation command varies depending on your operating system:

    - **On Windows:**

      ```bash
      venv\Scripts\activate
      ```

    - **On macOS and Linux:**

      ```bash
      source venv/bin/activate
      ```

5.  **Verify Activation:** Once the virtual environment is activated, you should see the name of your environment (usually `(venv)`) displayed at the beginning of your terminal prompt. This indicates that you are now working within the isolated environment.

**Why Use a Virtual Environment?**

- **Isolation:** Keeps project dependencies separate, avoiding conflicts between different projects that might require different versions of the same libraries.
- **Reproducibility:** Makes it easier to share your project with others, as you can provide a list of the exact dependencies required (using `pip freeze > requirements.txt`).
- **Clean System:** Prevents cluttering your global Python installation with project-specific packages.

**Alternative: Conda Environments (Optional)**

If you are using Anaconda or Miniconda, you can create virtual environments using `conda`:

1.  **Open your Anaconda Prompt or terminal.**
2.  **Navigate to your project directory.**
3.  **Run the command:**

    ```bash
    conda create --name myenv python=3.x
    ```

    (Replace `myenv` with your desired environment name and `3.x` with your preferred Python version).

4.  **Activate the conda environment:**

    ```bash
    conda activate myenv
    ```

## 5. Installing Django

Now that you have your virtual environment activated, you can install Django.

1.  **Ensure your virtual environment is active** (you should see the `(venv)` prefix in your terminal).
2.  **Run the following command using `pip`:**

    ```bash
    pip install Django
    ```

    This command will connect to the Python Package Index (PyPI), download the latest stable version of Django, and install it along with any necessary dependencies within your active virtual environment.

3.  **Verify the Installation:** You can check if Django has been installed correctly by running the following command:

    ```bash
    python -m django --version
    ```

    This should output the version of Django that you have just installed (e.g., `4.2.x`).

## 6. Creating Your First Django Project

With Django installed, you can now create your first Django project. A Django project is a collection of settings and applications that work together to build your web application.

1.  **Open your terminal or command prompt.**
2.  **Navigate to the directory where you want to create your Django project.** It's generally a good practice to create a new directory for each project, and you should be one level above where you want your project's main directory to be created (e.g., if you want a folder named `myfirstproject`, navigate to the directory that will contain it). **Make sure you are outside of your virtual environment directory when running the `startproject` command.**
3.  **Run the following command:**

    ```bash
    django-admin startproject myfirstproject
    ```

    Replace `myfirstproject` with the desired name for your project. Django will create a new directory with this name, containing the basic structure for your project. It's common to use lowercase letters and underscores for project names.

## 7. Understanding the Django Project Structure

Let's take a look at the directory structure that Django created:

```
myfirstproject/
├── manage.py
└── myfirstproject/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

Let's understand the purpose of each of these files and directories:

- **`manage.py`:** This is a powerful command-line utility that allows you to interact with your Django project. You'll use it for various tasks like running the development server, creating applications, running database migrations, and more.

- **`myfirstproject/` (inner directory):** This is the actual Python package for your project. Its name is the same as your project name.

  - **`__init__.py`:** This is an empty file that tells Python that the `myfirstproject` directory should be treated as a Python package.

  - **`settings.py`:** This file contains all the configuration settings for your Django project. Here you'll configure things like your database connection, installed applications, middleware, security settings, template locations, and much more. We'll explore this file in detail later.

  - **`urls.py`:** This file defines the URL patterns for your project. It maps incoming web requests (URLs) to the appropriate Django views that will handle them. This is the project-level URL configuration.

  - **`asgi.py`:** This file serves as the entry point for ASGI (Asynchronous Server Gateway Interface) compatible web servers to serve your Django project. ASGI is a standard for Python asynchronous web applications and is becoming increasingly important for modern web development.

  - **`wsgi.py`:** This file serves as the entry point for WSGI (Web Server Gateway Interface) compatible web servers to serve your Django project. WSGI is a standard interface between web servers and Python web applications and is widely used.

## 8. Running the Django Development Server

Django comes with a lightweight development server that you can use for testing and development without needing to set up a full-fledged web server like Apache or Nginx.

1.  **Open your terminal or command prompt.**
2.  **Navigate into your project's root directory** (the one containing `manage.py`). You can do this using the `cd` command:

    ```bash
    cd myfirstproject
    ```

3.  **Run the development server using `manage.py`:**

    ```bash
    python manage.py runserver
    ```

    You should see output in your terminal similar to this:

    ```
    Watching for file changes with StatReloader
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations: admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.

    March 17, 2025 - 21:45:00
    Django version 4.2.x, using settings 'myfirstproject.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ```

    This indicates that the Django development server has started and is running on your local machine at the address `http://127.0.0.1:8000/`.

4.  **Access the Server in Your Browser:** Open your web browser (Chrome, Firefox, Safari, etc.) and navigate to the address provided in the terminal (`http://127.0.0.1:8000/`).

5.  **Stop the Server:** To stop the development server, go back to your terminal and press `Ctrl + C` (Control key + C key).

## 9. Exploring the Default Django Project

When you access `http://127.0.0.1:8000/` in your browser, you should see a default welcome page from Django. This page typically includes a message like "It worked!" and a Django logo. This simple page confirms that you have successfully installed Django, created a project, and started the development server.

This default page is a good sign that your basic setup is working correctly. In the coming days, we'll learn how to create our own web pages and applications within this Django project.

## 10. Troubleshooting Common Setup Issues

Setting up a development environment can sometimes be tricky. Here are some common issues you might encounter and how to address them:

- **`python` command not found:** This usually means that Python is not added to your system's PATH environment variable. You might need to reinstall Python and make sure the "Add Python to PATH" option is checked during installation. You can also manually add it to your system's environment variables.
- **`pip` command not found:** `pip` should come bundled with recent versions of Python. If you encounter this issue, you might need to reinstall Python or ensure that the Python installation directory's `Scripts` subdirectory is in your PATH.
- **`(venv)` not appearing in the terminal:** This means your virtual environment is not activated. Double-check the activation command for your operating system and make sure you ran it correctly from within your project directory.
- **Error: "No module named django":** This usually indicates that Django is not installed in your active virtual environment. Ensure your virtual environment is activated and then try running `pip install Django` again.
- **Running `django-admin` or `manage.py` in the wrong directory:** Make sure you are running `django-admin startproject` from a directory _outside_ of your project directory. For `python manage.py runserver`, you need to be inside your project's root directory (the one containing `manage.py`).
- **Port 8000 already in use:** If another application is already using port 8000 on your machine, Django might fail to start the development server. You can try running the server on a different port by specifying it in the command: `python manage.py runserver 8080`. Then, access your application in the browser at `http://127.0.0.1:8080/`.

If you encounter any other issues, don't hesitate to ask for help! The official Django documentation ([https://docs.djangoproject.com/](https://docs.djangoproject.com/)) and online communities like Stack Overflow ([https://stackoverflow.com/questions/tagged/django](https://stackoverflow.com/questions/tagged/django)) are excellent resources for troubleshooting.

## Summary of Day 2: Django Overview and Setup

Today, we took our first steps into the world of Django! We learned:

- What Django is and its key benefits for web development.
- The fundamental **MVT (Model-View-Template)** architecture that Django follows.
- How to set up a **virtual environment** to isolate our project dependencies.
- How to **install Django** using `pip`.
- How to **create a new Django project** using `django-admin startproject`.
- The basic **structure of a Django project** and the purpose of key files like `manage.py`, `settings.py`, and `urls.py`.
- How to **run the Django development server** and access the default project page in a browser.
- Some common **troubleshooting steps** for setup issues.

You've now successfully set up your development environment and created your first Django project! This is a significant step towards becoming a Python Full-Stack Web Developer. Tomorrow, we'll delve deeper into creating applications within our Django project.

## Exercises

**Exercise 1: Create a New Django Project**

1.  Open your terminal or command prompt.
2.  Navigate to a directory where you want to store your Django projects.
3.  Create a new virtual environment named `my_django_env` using the appropriate command for your system (`python -m venv my_django_env` or `python3 -m venv my_django_env`).
4.  Activate the `my_django_env` virtual environment.
5.  Install Django within the activated environment.
6.  Navigate to a directory _outside_ of your virtual environment.
7.  Create a new Django project named `my_website`.
8.  Navigate into the `my_website` directory.
9.  Run the Django development server.
10. Open your web browser and go to `http://127.0.0.1:8000/`. You should see the default Django welcome page.
11. Stop the development server in your terminal.
12. Deactivate the virtual environment (usually by typing `deactivate` in the terminal).

**Exercise 2: Explore the Project Files**

1.  Navigate into the `my_website` directory you created in Exercise 1.
2.  List the files and directories within this directory.
3.  Open the `my_website` subdirectory.
4.  List the files within this inner `my_website` directory.
5.  For each of the `.py` files (`__init__.py`, `asgi.py`, `settings.py`, `urls.py`, `wsgi.py`) in the inner `my_website` directory, try to write a brief sentence or two describing its purpose based on what you learned today. You can open the files in a text editor to get a glimpse of their content, but don't worry about understanding everything inside them yet.

**Exercise 3: Try a Different Port**

1.  Navigate to the root directory of your `my_website` project (the one containing `manage.py`).
2.  Run the development server on port `8080` instead of the default port `8000` using the command: `python manage.py runserver 8080`.
3.  Open your web browser and go to `http://127.0.0.1:8080/`. You should still see the default Django welcome page.
4.  Stop the development server.

## Daily Task

**Task: Document Your Setup**

1.  Create a simple Markdown file (e.g., `django_setup.md`) in your `my_website` project directory.
2.  In this file, document the steps you took to set up your Django project today:
    - How you created and activated the virtual environment.
    - The command you used to install Django.
    - The command you used to create your Django project.
    - The command you used to run the development server.
    - The URL you used to access the default Django page.
3.  Briefly explain in your own words the purpose of the `manage.py` file.

This exercise will help you solidify the setup process and practice your Markdown skills.

---

**End of Day 2 Study Material & Notes**

---

## Exercises

<details>
<summary><b>Solution for Exercise 1: Create a New Django Project</b></summary>

```bash
# 1. Open your terminal or command prompt.
# (Assume you have your terminal open)

# 2. Navigate to a directory for your Django projects (replace 'path/to/your/projects' accordingly).
cd path/to/your/projects

# 3. Create a new virtual environment named 'my_django_env'.
python -m venv my_django_env

# 4. Activate the 'my_django_env' virtual environment.
# On Windows:
my_django_env\Scripts\activate
# On macOS/Linux:
source my_django_env/bin/activate

# (You should now see '(my_django_env)' at the beginning of your terminal prompt)

# 5. Install Django within the activated environment.
pip install Django

# 6. Navigate to a directory outside of your virtual environment (e.g., back to 'path/to/your/projects').
cd ..

# 7. Create a new Django project named 'my_website'.
django-admin startproject my_website

# 8. Navigate into the 'my_website' directory.
cd my_website

# 9. Run the Django development server.
python manage.py runserver

# (Open your browser and go to http://127.0.0.1:8000/)

# 10. Stop the development server in your terminal (Ctrl + C).

# 11. Deactivate the virtual environment.
deactivate

# (The '(my_django_env)' prefix should disappear from your terminal prompt)
```

</details>

<details>
<summary><b>Solution for Exercise 2: Explore the Project Files</b></summary>

1.  Navigate into the `my_website` directory: `cd my_website`
2.  List files and directories: `ls` (on macOS/Linux) or `dir` (on Windows) - You should see `manage.py` and another directory named `my_website`.
3.  Open the inner `my_website` directory: `cd my_website`
4.  List files: `ls` or `dir` - You should see `__init__.py`, `asgi.py`, `settings.py`, `urls.py`, and `wsgi.py`.
5.  Brief descriptions:
    - `__init__.py`: An empty file indicating that this directory is a Python package.
    - `asgi.py`: Entry point for ASGI-compatible web servers.
    - `settings.py`: Contains configuration settings for the Django project.
    - `urls.py`: Defines URL patterns for the project.
    - `wsgi.py`: Entry point for WSGI-compatible web servers.

</details>

<details>
<summary><b>Solution for Exercise 3: Try a Different Port</b></summary>

1.  Navigate to the root directory of `my_website`: `cd ..` (if you are currently in the inner `my_website` directory).
2.  Run the server on port 8080: `python manage.py runserver 8080`
3.  Open browser and go to `http://127.0.0.1:8080/`.
4.  Stop the server: `Ctrl + C` in the terminal.

</details>

## Daily Task

<details>
<summary><b>Solution for Daily Task: Document Your Setup</b></summary>

# Django Setup Documentation - my_website Project

This document outlines the steps taken to set up the Django project "my_website" on [Your Date].

## Virtual Environment Creation and Activation

1.  Navigated to the directory where I wanted to store my Django projects.
2.  Created a new virtual environment named `my_django_env` using the command:
    ```bash
    python -m venv my_django_env
    ```
3.  Activated the virtual environment using the command:
    ```bash
    # On Windows:
    my_django_env\Scripts\activate
    # On macOS/Linux:
    source my_django_env/bin/activate
    ```

## Django Installation

1.  With the virtual environment activated, I installed Django using pip:
    ```bash
    pip install Django
    ```

## Django Project Creation

1.  Navigated back to the directory where I wanted to create the project.
2.  Created the Django project named `my_website` using the command:
    ```bash
    django-admin startproject my_website
    ```

## Running the Development Server

1.  Navigated into the `my_website` project directory:
    ```bash
    cd my_website
    ```
2.  Started the development server using the command:
    ```bash
    python manage.py runserver
    ```
3.  Accessed the default Django page in my web browser by navigating to `http://127.0.0.1:8000/`.

## Purpose of `manage.py`

The `manage.py` file is a command-line utility that helps with various administrative tasks for the Django project. It acts as a wrapper around the `django-admin` tool and is specific to your project. You can use it to run the development server, create and manage applications, run database migrations, and perform many other useful operations within the context of your Django project.
