# Week 4, Day 5: Templates and Dynamic Content Rendering in Django

## Overview

Today’s lesson is focused on Django’s templating system—how to render dynamic content using templates. We will learn how to create, organize, and extend templates, pass context data from views, and use Django’s template language to build interactive, real-world web pages. This session is crucial for transforming your backend logic into attractive, user-friendly front-end pages.

> **Project-Based Note:**  
> Today's work is part of our ongoing mini-project (for example, a blog or store application). By the end of the day, you will be able to render dynamic content such as blog posts, product details, or user messages on your site. You will also learn to use template inheritance to create a consistent layout across multiple pages.

---

## Lesson Plan

### 1. Recap of Previous Lessons

- **Review:**
  - How we set up the Django project, created apps, and implemented URL routing and views (both FBVs and CBVs).
  - Today, we build on this foundation by connecting views to templates for dynamic content rendering.

### 2. Introduction to Django Templates

#### 2.1 What are Django Templates?

- **Definition:**  
  Django templates are HTML files with special syntax that allow you to embed dynamic data and control structures.
- **Purpose:**  
  They separate presentation from business logic, ensuring that your Python code (views) and HTML (presentation) remain decoupled.

#### 2.2 Template Syntax and Features

- **Variable Interpolation:**  
  Use double curly braces to render variables:
  ```html
  <h1>Welcome, {{ user_name }}!</h1>
  ```
- **Control Structures:**  
  Use `{% ... %}` tags for loops and conditionals:
  ```html
  {% if posts %}
  <ul>
    {% for post in posts %}
    <li>{{ post.title }}</li>
    {% endfor %}
  </ul>
  {% else %}
  <p>No posts available.</p>
  {% endif %}
  ```
- **Template Filters:**  
  Modify variables with filters like `|date:"F j, Y"`:
  ```html
  <p>Published on: {{ post.published_date|date:"F j, Y" }}</p>
  ```

### 3. Creating and Organizing Templates

#### 3.1 Template Directory Structure

- **Project Structure Example:**
  ```
  my_website/
  ├── my_website/
  │   ├── settings.py
  │   └── urls.py
  ├── blog/
  │   ├── templates/
  │   │   └── blog/
  │   │       ├── base.html
  │   │       ├── post_list.html
  │   │       └── post_detail.html
  │   └── views.py
  └── manage.py
  ```
- **Settings Configuration:**  
  Ensure your `settings.py` file includes the template directories:
  ```python
  TEMPLATES = [
      {
          'BACKEND': 'django.template.backends.django.DjangoTemplates',
          'DIRS': [],  # Use app directories by default
          'APP_DIRS': True,
          'OPTIONS': {
              'context_processors': [
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
              ],
          },
      },
  ]
  ```

#### 3.2 Template Inheritance and Reusability

- **Base Template (`base.html`):**
  ```html
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>{% block title %}My Website{% endblock %}</title>
      <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
    </head>
    <body>
      <header>
        <h1>My Website Header</h1>
      </header>
      <nav>
        <ul>
          <li><a href="{% url 'post_list' %}">Blog</a></li>
          <li><a href="{% url 'about' %}">About</a></li>
        </ul>
      </nav>
      <main>
        {% block content %}
        <!-- Page-specific content will go here -->
        {% endblock %}
      </main>
      <footer>
        <p>&copy; 2025 My Website</p>
      </footer>
    </body>
  </html>
  ```
- **Extending the Base Template (e.g., `post_list.html`):**

  ```html
  {% extends "blog/base.html" %} {% block title %}Blog Posts{% endblock %} {%
  block content %}
  <h2>Blog Posts</h2>
  {% if posts %}
  <ul>
    {% for post in posts %}
    <li>
      <a href="{% url 'post_detail' post_id=post.id %}">{{ post.title }}</a>
      <small>Published on: {{ post.published_date|date:"F j, Y" }}</small>
    </li>
    {% endfor %}
  </ul>
  {% else %}
  <p>No posts available at the moment.</p>
  {% endif %} {% endblock %}
  ```

### 4. Connecting Views to Templates

#### 4.1 Passing Context Data

- **Example View Function:**

  ```python
  # In blog/views.py
  from django.shortcuts import render
  from .models import Post

  def post_list(request):
      posts = Post.objects.all()  # Retrieve all posts from the database
      context = {
          'posts': posts,
          'user_name': request.user.username if request.user.is_authenticated else "Guest"
      }
      return render(request, 'blog/post_list.html', context)
  ```

- **Explanation:**  
  The `render` function combines a template with context data and returns an HTTP response.

#### 4.2 Dynamic Detail Page

- **Example Detail View:**

  ```python
  # In blog/views.py
  from django.shortcuts import get_object_or_404

  def post_detail(request, post_id):
      post = get_object_or_404(Post, id=post_id)
      context = {'post': post}
      return render(request, 'blog/post_detail.html', context)
  ```

- **Corresponding Template (`post_detail.html`):**

  ```html
  {% extends "blog/base.html" %} {% block title %}{{ post.title }}{% endblock %}
  {% block content %}
  <article>
    <h2>{{ post.title }}</h2>
    <p><small>Published on: {{ post.published_date|date:"F j, Y" }}</small></p>
    <div>{{ post.content|safe }}</div>
    <a href="{% url 'post_list' %}">Back to Blog Posts</a>
  </article>
  {% endblock %}
  ```

### 5. Advanced Template Features

#### 5.1 Template Filters and Tags

- **Common Filters:**
  - `|date:"FORMAT"` for formatting dates.
  - `|lower` to convert text to lowercase.
  - `|safe` to mark a string as safe for HTML output.
- **Custom Template Tags (Optional):**  
  You can create custom tags for reusability. (This is advanced; we’ll cover it later if time permits.)

#### 5.2 Including Static Files

- **Static Files Setup:**  
  Ensure `STATIC_URL` is set in `settings.py`:
  ```python
  STATIC_URL = '/static/'
  ```
- **Usage in Templates:**
  ```html
  {% load static %}
  <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
  ```

### 6. Best Practices for Templating

- **Separation of Concerns:**  
  Keep logic in views, and let templates focus solely on presentation.
- **DRY Principle:**  
  Use template inheritance to avoid code repetition.
- **Clear Documentation:**  
  Document the purpose of each template and its sections.

---

## Detailed Exercises

### Exercise 1: Create a Base Template and Extend It

<details>
<summary><b>Solution for Exercise 1: Base and Extended Templates</b></summary>

1. **Create a Base Template (`blog/templates/blog/base.html`):**

   ```html
   <!DOCTYPE html>
   <html lang="en">
     <head>
       <meta charset="UTF-8" />
       <title>{% block title %}My Website{% endblock %}</title>
       {% load static %}
       <link rel="stylesheet" href="{% static 'css/styles.css' %}" />
     </head>
     <body>
       <header>
         <h1>My Website</h1>
       </header>
       <nav>
         <ul>
           <li><a href="{% url 'post_list' %}">Blog</a></li>
           <li><a href="{% url 'about' %}">About</a></li>
         </ul>
       </nav>
       <main>
         {% block content %}
         <!-- Page-specific content -->
         {% endblock %}
       </main>
       <footer>
         <p>&copy; 2025 My Website</p>
       </footer>
     </body>
   </html>
   ```

2. **Create an Extended Template (`blog/templates/blog/post_list.html`):**

   ```html
   {% extends "blog/base.html" %} {% block title %}Blog Posts{% endblock %} {%
   block content %}
   <h2>Blog Posts</h2>
   {% if posts %}
   <ul>
     {% for post in posts %}
     <li>
       <a href="{% url 'post_detail' post_id=post.id %}">{{ post.title }}</a>
       <small>Published on: {{ post.published_date|date:"F j, Y" }}</small>
     </li>
     {% endfor %}
   </ul>
   {% else %}
   <p>No posts available.</p>
   {% endif %} {% endblock %}
   ```

3. **Test the Templates:**  
   Run your server and navigate to the blog list page (configured in your view for `post_list`). Verify that the content renders within the layout defined in `base.html`.

</details>

### Exercise 2: Create a Dynamic Detail Template

<details>
<summary><b>Solution for Exercise 2: Dynamic Detail Page</b></summary>

1. **Detail View Function:**

   ```python
   # In blog/views.py
   from django.shortcuts import get_object_or_404, render
   from .models import Post

   def post_detail(request, post_id):
       post = get_object_or_404(Post, id=post_id)
       return render(request, 'blog/post_detail.html', {'post': post})
   ```

2. **Detail Template (`blog/templates/blog/post_detail.html`):**

   ```html
   {% extends "blog/base.html" %} {% block title %}{{ post.title }}{% endblock
   %} {% block content %}
   <article>
     <h2>{{ post.title }}</h2>
     <p><small>Published on: {{ post.published_date|date:"F j, Y" }}</small></p>
     <div>{{ post.content|safe }}</div>
     <a href="{% url 'post_list' %}">Back to Blog Posts</a>
   </article>
   {% endblock %}
   ```

3. **Test the Detail Page:**  
   Navigate to a specific post URL (e.g., `/blog/post/1/`) to verify that the details render correctly.

</details>

### Exercise 3: Pass Context Data to a Template

<details>
<summary><b>Solution for Exercise 3: Context Data Rendering</b></summary>

1. **View Function Example:**
   ```python
   # In blog/views.py
   def post_list(request):
       posts = Post.objects.all()  # Retrieve all posts from the database
       context = {
           'posts': posts,
           'user_name': request.user.username if request.user.is_authenticated else "Guest"
       }
       return render(request, 'blog/post_list.html', context)
   ```
2. **Template Usage:**  
   In `post_list.html`, use the `user_name` variable:
   ```html
   <p>Welcome, {{ user_name }}!</p>
   ```
3. **Test:**  
 Ensure the dynamic greeting appears along with the list of posts.
</details>

---

## Detailed Daily Task

<details>
<summary><b>Solution for Daily Task: Build and Test a Dynamic Feedback Form with Templates</b></summary>

1.  **Task Description:**  
    Create a new view that renders a feedback form using a template. The form should display on a GET request and process user input on a POST request.

2.  **Steps:**

    - **Step 1:** Create a template for the feedback form (`blog/templates/blog/feedback.html`):

      ```html
      {% extends "blog/base.html" %} {% block title %}Feedback{% endblock %} {%
      block content %}
      <h2>Submit Your Feedback</h2>
      <form method="post">
        {% csrf_token %}
        <input type="text" name="feedback" placeholder="Your feedback" />
        <button type="submit">Submit</button>
      </form>
      {% endblock %}
      ```

    - **Step 2:** Create a view to handle feedback in `blog/views.py`:

      ```python
      from django.http import HttpResponse

      def feedback_view(request):
          if request.method == 'POST':
              feedback = request.POST.get('feedback', 'No feedback provided')
              return HttpResponse(f"Thank you for your feedback: {feedback}")
          return render(request, 'blog/feedback.html')
      ```

    - **Step 3:** Add a URL pattern in `blog/urls.py`:
      ```python
      urlpatterns += [
          path('feedback/', feedback_view, name='feedback'),
      ]
      ```
    - **Step 4:** Run the server and navigate to `/blog/feedback/`.
      - Verify the form is displayed.
      - Submit the form and check the response message.
    - **Step 5:** **Documentation:**  
       Update your `daily_task.md` file with an entry like:
      ```markdown # Daily Task: Dynamic Feedback Form

           Today, I created a feedback form using Django templates. The form is rendered via a GET request and processes user input on a POST request. This exercise helped me understand context passing, CSRF protection, and template rendering.
           ```

      </details>

---

## Final Wrap-Up and Key Takeaways

- **Templates & Inheritance:**

  - Learn how to create a base template and extend it for consistent layouts.
  - Use the `{% block %}` tags to define placeholders for dynamic content.

- **Dynamic Content Rendering:**

  - Pass context data from views to templates using the `render` function.
  - Use Django’s template language to iterate over data, conditionally render content, and format variables.

- **Real-World Relevance:**

  - Building dynamic pages (such as blog lists, post details, and feedback forms) is essential for creating interactive web applications.
  - Template inheritance and context management are best practices that lead to maintainable and scalable code.

- **Next Steps:**
  - In upcoming lessons, we will further integrate models with templates, add forms with validation, and ultimately combine everything into a comprehensive mini-project.

_End of Week 4, Day 5 Study Material & Notes_

```

```
