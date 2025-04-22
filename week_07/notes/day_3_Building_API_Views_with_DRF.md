# Week 7, Day 3: Bringing Your API to Life - Building Views with Django REST Framework

## Overview

Yesterday, we set up Django REST Framework and learned how to use serializers to convert our Django models into formats suitable for API responses and to handle incoming data. Today, we will connect these serializers to URLs by building **API views**. DRF provides powerful view classes that make it easy to handle different HTTP methods (GET, POST, PUT, PATCH, DELETE) and implement the logic for your API endpoints. You'll learn various approaches to creating views, from simple function-based views to the highly efficient ViewSets, and how to configure URL routing for them. By the end of this lesson, you will be able to:

  - Understand the role and purpose of API views in Django REST Framework.
  - Differentiate between Function-Based Views (FBVs) and Class-Based Views (CBVs) in DRF and understand the benefits of CBVs, including DRF's specific `APIView`.
  - Utilize DRF's generic views (like `ListCreateAPIView`, `RetrieveUpdateDestroyAPIView`) for common API patterns.
  - Leverage the powerful `ViewSet` classes (especially `ModelViewSet`) and `Router`s to quickly build RESTful API endpoints with minimal code.
  - Create API endpoints that respond appropriately to GET, POST, PUT, PATCH, and DELETE requests.
  - Access and handle request data (including JSON) using `request.data` in DRF views.
  - Configure URLs to route requests to your DRF API views, making use of DRF's routers.
  - Understand how to apply view-level security like permissions and throttling.
  - Test your API endpoints using the DRF browsable API and command-line tools like `curl` or GUI tools like Postman/Insomnia.

> **Project-Based Note:**
> Today, you will start creating the actual API endpoints for your blog project. You'll build views that allow clients to fetch lists of blog posts, retrieve individual posts, create new posts, update existing ones, and delete posts, all using your previously defined models and serializers. This is a core step in making your blog application accessible programmatically.

-----

## Lesson Plan

### 1\. Recap of Week 7, Day 2

  - **Brief Review:** Yesterday, we successfully installed and set up Django REST Framework (`pip install djangorestframework`, added `'rest_framework'` to `INSTALLED_APPS`). We then learned about serializers, particularly `ModelSerializer`, and how to use them to convert Django model instances and QuerySets into Python native datatypes suitable for JSON output (serialization) and how they are used to validate incoming data (deserialization). We also saw how to serialize single objects (`Serializer(instance=...)`) and lists (`Serializer(instance=..., many=True)`) and explored nesting serializers.

### 2\. Introduction to DRF API Views and Request Handling

  - **The Role of API Views:** In the MVT (Model-View-Template) pattern of traditional Django, views handle the request/response logic and typically render templates. In a DRF API, views still handle the request/response logic, but instead of rendering HTML templates, they typically interact with serializers to process data from your models and return API responses (like JSON).
  - **Handling API Logic:** API views are responsible for:
      - Receiving incoming HTTP requests.
      - Accessing and parsing request data (especially the request body).
      - Interacting with your models (using the ORM) to fetch, create, update, or delete data based on the request.
      - Using serializers to validate incoming data (deserialization) and format outgoing data (serialization).
      - Applying authentication, permissions, and throttling.
      - Returning appropriate HTTP responses, including status codes and serialized data.
  - **Accessing Request Data (`request.data`):**
      - In DRF API views (both FBVs and CBVs enhanced by DRF), the `request` object is an instance of DRF's `Request` class, which extends Django's standard `HttpRequest`.
      - `request.data`: This property of the `Request` object provides a unified way to access parsed request body data. It automatically handles various request body formats (like JSON, XML, form data) based on the `Content-Type` header of the request. This is generally preferred over `request.POST` or `request.body` in DRF views.
    <!-- end list -->
    ```python
    # Example of accessing request.data in a simple view
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    from rest_framework import status

    @api_view(['POST'])
    def process_json_data(request):
        if request.method == 'POST':
            data = request.data # Access the parsed request body data (e.g., a Python dictionary if JSON was sent)
            if 'name' in data and 'value' in data:
                print(f"Received: Name={data['name']}, Value={data['value']}")
                return Response({"received": "Data processed successfully"}, status=status.HTTP_200_OK)
            return Response({"error": "Missing 'name' or 'value' in request body"}, status=status.HTTP_400_BAD_REQUEST)
    ```

### 3\. Function-Based Views (FBVs) vs. Class-Based Views (CBVs) in DRF

DRF allows you to build API views using both Function-Based Views and Class-Based Views, each with its own advantages.

  - **Function-Based Views (FBVs):**

      - You can write API views as simple Python functions. DRF provides the `@api_view` decorator to enhance FBVs with API functionalities like request parsing, returning `Response` objects, and providing the browsable API.
      - **Example:**
        ```python
        from rest_framework.decorators import api_view
        from rest_framework.response import Response
        from rest_framework import status
        from blog.models import BlogPost
        from .serializers import BlogPostSerializer

        @api_view(['GET', 'POST']) # Specify allowed HTTP methods
        def blog_post_list_create_fbv(request):
            if request.method == 'GET':
                posts = BlogPost.objects.all()
                serializer = BlogPostSerializer(posts, many=True)
                return Response(serializer.data) # Return DRF's Response object

            elif request.method == 'POST':
                serializer = BlogPostSerializer(data=request.data) # Use request.data
                if serializer.is_valid():
                    serializer.save() # Save the new object
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Return validation errors
        ```
      - **Use Case:** Suitable for simple, highly customized endpoints where the logic is straightforward and contained within a single function. Provides explicit control over the request and response handling.

  - **Class-Based Views (CBVs):**

      - Django's Class-Based Views offer advantages like code reusability through inheritance and mixing, and better organization by dispatching different HTTP methods to different class methods (`.get()`, `.post()`, `.put()`, etc.). DRF extends this with a powerful hierarchy of CBVs tailored for APIs.
      - **`rest_framework.views.APIView`:** This is the basic building block for DRF's CBVs. It extends Django's `View` but provides DRF-specific functionality like the `Request` object, handling authentication/permissions/throttling, and returning `Response` objects. You implement methods corresponding to HTTP verbs.
      - **Example:**
        ```python
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework import status
        from blog.models import BlogPost
        from .serializers import BlogPostSerializer
        from django.http import Http404 # Import for handling object not found

        class BlogPostListCreateAPIView(APIView):
            def get(self, request, format=None): # format=None is common practice
                posts = BlogPost.objects.all()
                serializer = BlogPostSerializer(posts, many=True)
                return Response(serializer.data)

            def post(self, request, format=None):
                serializer = BlogPostSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        class BlogPostDetailAPIView(APIView):
            def get_object(self, pk): # Helper method to get the object or raise 404
                try:
                    return BlogPost.objects.get(pk=pk)
                except BlogPost.DoesNotExist:
                    raise Http404

            def get(self, request, pk, format=None):
                post = self.get_object(pk)
                serializer = BlogPostSerializer(post)
                return Response(serializer.data)

            def put(self, request, pk, format=None):
                post = self.get_object(pk)
                serializer = BlogPostSerializer(post, data=request.data) # Pass instance and data for updates
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            def delete(self, request, pk, format=None):
                post = self.get_object(pk)
                post.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
        ```
      - **Benefits:** Better organization of code compared to large FBVs, easier to apply mixins and inherit from base classes.

### 4\. Generic Class-Based Views (Reducing Boilerplate)

DRF provides a set of generic views that are pre-written to handle common API patterns like listing objects, creating objects, retrieving a single object, updating an object, and deleting an object. They combine `GenericAPIView` with mixins.

  - **`GenericAPIView` + Mixins:**

      - `GenericAPIView` provides core functionality like specifying the `queryset` and `serializer_class`.
      - Mixin classes (e.g., `ListModelMixin`, `CreateModelMixin`, `RetrieveModelMixin`, `UpdateModelMixin`, `DestroyModelMixin`) provide the methods for specific actions. You combine them with `GenericAPIView` and explicitly define the HTTP method handlers (`.get()`, `.post()`, etc.) to call the mixin methods.
      - **Example (List and Create):**
        ```python
        from rest_framework import generics, mixins
        from blog.models import BlogPost
        from .serializers import BlogPostSerializer

        class BlogPostListCreateGeneric(mixins.ListModelMixin,
                                        mixins.CreateModelMixin,
                                        generics.GenericAPIView):
            queryset = BlogPost.objects.all()
            serializer_class = BlogPostSerializer

            def get(self, request, *args, **kwargs):
                return self.list(request, *args, **kwargs) # Call the list mixin method

            def post(self, request, *args, **kwargs):
                return self.create(request, *args, **kwargs) # Call the create mixin method
        ```
      - **Use Case:** When you need a custom view that performs only a subset of standard actions or requires significant customization alongside the standard actions.

  - **Concrete Generic Views:**

      - DRF provides pre-built classes that combine `GenericAPIView` and specific mixins into a single class, offering a very concise way to define common API endpoints.
      - **Examples:**
          - `ListAPIView`: Read-only endpoint for listing objects.
          - `CreateAPIView`: Endpoint for creating objects.
          - `ListCreateAPIView`: Combines listing and creating objects.
          - `RetrieveAPIView`: Read-only endpoint for retrieving a single object.
          - `UpdateAPIView`: Endpoint for updating a single object (PUT and PATCH).
          - `DestroyAPIView`: Endpoint for deleting a single object.
          - `RetrieveUpdateAPIView`: Combines retrieving and updating.
          - `RetrieveDestroyAPIView`: Combines retrieving and deleting.
          - `RetrieveUpdateDestroyAPIView`: Provides retrieve, update (PUT/PATCH), and delete actions.
      - **Example (List/Create and Retrieve/Update/Destroy):**
        ```python
        from rest_framework import generics
        from blog.models import BlogPost
        from .serializers import BlogPostSerializer

        # API endpoint for listing and creating blog posts
        class BlogPostListCreateAPIView(generics.ListCreateAPIView):
            queryset = BlogPost.objects.all()
            serializer_class = BlogPostSerializer

        # API endpoint for retrieving, updating, and deleting a single blog post
        class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
            queryset = BlogPost.objects.all() # Note: Using .all() here is fine; the generic view will filter by pk
            serializer_class = BlogPostSerializer
            lookup_field = 'pk' # Default lookup field is 'pk', can change to 'slug' etc.
        ```
      - **Benefit:** Minimal code for standard CRUD endpoints. Handles boilerplate like querying, serialization, validation, and returning appropriate responses automatically. Includes built-in support for pagination, filtering, authentication, and permissions via class attributes.

### 5\. ViewSets & Routers (The Most Efficient Approach for RESTful APIs)

  - **ViewSets:** As introduced yesterday, ViewSets combine the logic for a set of related views into a single class (e.g., list, create, retrieve, update, destroy for a model). They don't provide method handlers like `.get()` or `.post()` directly, but rather actions like `.list()`, `.create()`, `.retrieve()`, etc.

  - **`rest_framework.viewsets.ModelViewSet`:** This is the most powerful and commonly used ViewSet for building model-based APIs. It automatically provides all the standard CRUD actions (`list`, `create`, `retrieve`, `update`, `partial_update`, `destroy`) for a given model. You primarily need to specify the `queryset` and `serializer_class`.

    ```python
    # api/views.py (or blog/views.py)

    from rest_framework import viewsets
    from blog.models import BlogPost
    from .serializers import BlogPostSerializer

    class BlogPostViewSet(viewsets.ModelViewSet):
        """
        API endpoint that allows blog posts to be viewed, created, updated, or deleted.
        """
        queryset = BlogPost.objects.all().order_by('-publish_date') # Specify the base QuerySet for retrieving objects
        serializer_class = BlogPostSerializer # Specify the serializer to use for data conversion and validation
        # permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Example: Only authenticated users can create/update/delete
    ```

    With this, the `BlogPostViewSet` class is ready to handle all the CRUD operations for the `BlogPost` model.

  - **Routers:** Routers are used to automatically generate URL patterns for `ViewSet` classes based on the actions they provide. This saves you from manually writing individual URL patterns for each action.

  - **`rest_framework.routers.DefaultRouter`:** A commonly used router that automatically generates URL patterns for a standard set of viewset actions, following RESTful conventions.

  - **Setup:**

    ```python
    # your_project/urls.py (main project urls.py)

    from django.contrib import admin
    from django.urls import path, include
    from rest_framework.routers import DefaultRouter
    # Import ViewSets from your app(s) - adjust import path as needed
    from api import views as api_views # Assuming your API views are in api/views.py
    # from blog import views as blog_views # If ViewSets are in blog/views.py

    # Create a router instance
    router = DefaultRouter()

    # Register your ViewSets with the router
    # Syntax: router.register(prefix, viewset, basename=None)
    # prefix: The URL prefix for this set of routes (e.g., 'blogposts' will create URLs like /api/blogposts/)
    # viewset: The ViewSet class
    # basename (optional): Used to name the URL patterns; required if the queryset does not have a .model attribute
    router.register(r'blogposts', api_views.BlogPostViewSet, basename='blogpost') # Register your BlogPostViewSet
    # router.register(r'users', api_views.UserViewSet, basename='user') # Register other ViewSets
    # router.register(r'categories', api_views.CategoryViewSet, basename='category')

    # The API URLs are now determined automatically by the router.
    # Include the router's URLs in your project's main urlpatterns
    urlpatterns = [
        path('admin/', admin.site.urls),
        # ... other traditional app URLs ...
        path('api/v1/', include(router.urls)), # Include DRF router URLs under a versioned prefix
        # path('api/', include(router.urls)), # Alternative without versioning prefix
    ]
    ```

    This router will automatically generate URLs like `/api/v1/blogposts/` (for list/create) and `/api/v1/blogposts/{pk}/` (for retrieve/update/delete), mapping them to the corresponding methods in your `BlogPostViewSet`.

### 6\. Authentication, Permissions & Throttling (Applied to Views)

While covered in more detail later, it's important to know that security and rate limiting are applied at the view level in DRF.

  - **Permissions:** Control *who* can access a view or perform an action. Set the `permission_classes` attribute on your view or ViewSet.
    ```python
    from rest_framework import viewsets, permissions
    # ...

    class BlogPostViewSet(viewsets.ModelViewSet):
        # ...
        permission_classes = [permissions.IsAuthenticatedOrReadOnly] # Allows authenticated users write access, others read-only
        # permission_classes = [permissions.IsAdminUser] # Only admin users can access
    ```
  - **Throttling:** Control the rate of requests clients can make to an API endpoint. Set the `throttle_classes` attribute.
    ```python
    from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
    # ...

    class BlogPostViewSet(viewsets.ModelViewSet):
        # ...
        throttle_classes = [UserRateThrottle, AnonRateThrottle] # Apply throttling based on user or anonymous status
    ```

### 7\. Testing API Endpoints using Tools

Once you have created your API views and configured your URLs, you can test them using various tools.

  - **Browsable API (DRF's Default):**

      - If you access your API endpoints in a web browser, DRF by default provides a human-friendly HTML page. This browsable API is extremely useful during development for inspecting responses and interacting with your API using automatically generated forms for POST, PUT, and PATCH requests.
      - Navigate your browser to the URL handled by your router (e.g., `http://127.0.0.1:8000/api/v1/blogposts/`).

  - **`curl` (Command Line):** A versatile command-line tool for making HTTP requests.

    ```bash
    # GET request to list blog posts
    curl http://127.0.0.1:8000/api/v1/blogposts/

    # GET request for a specific blog post (replace 1 with a valid ID)
    curl http://127.0.0.1:8000/api/v1/blogposts/1/

    # POST request to create a new blog post (example JSON - adjust fields as needed based on your serializer)
    # Make sure to replace {author_id} and {category_id} with actual IDs from your database
    curl -X POST -H "Content-Type: application/json" -d '{"title": "My API Created Post", "content": "This post was created via the API.", "author": {author_id}, "category": {category_id}, "publish_date": "2025-04-21T15:00:00Z", "slug": "api-created-post-slug"}' http://127.0.0.1:8000/api/v1/blogposts/

    # PUT request to update a specific blog post (replace {post_id} with a valid ID)
    # Provide the *complete* data for the post
    curl -X PUT -H "Content-Type: application/json" -d '{"id": {post_id}, "title": "My Updated API Post", "content": "Content has been updated via PUT.", "author": {author_id}, "category": {category_id}, "publish_date": "2025-04-21T16:00:00Z", "slug": "updated-api-post-slug"}' http://127.0.0.1:8000/api/v1/blogposts/{post_id}/

    # PATCH request to partially update a specific blog post (replace {post_id} with a valid ID)
    # Provide only the fields you want to update
    curl -X PATCH -H "Content-Type: application/json" -d '{"content": "Content updated partially via PATCH."}' http://127.0.0.1:8000/api/v1/blogposts/{post_id}/

    # DELETE request for a specific blog post (replace {post_id} with a valid ID)
    curl -X DELETE http://127.0.0.1:8000/api/v1/blogposts/{post_id}/
    ```

  - **Postman or Insomnia (GUI Tools):** These are popular desktop applications with a user-friendly interface for making HTTP requests, managing environments, setting headers, sending various request body types, and inspecting responses. They are excellent for testing, debugging, and documenting APIs.

### 8\. Practical Real-World Exercises and Tasks with Solutions

### Exercise 1: Creating a `ModelViewSet` for Blog Posts

1.  **Task:** In your API app's `views.py` (or your blog app's `views.py`, depending on your structure), define a `ModelViewSet` named `BlogPostViewSet` for your `BlogPost` model.
2.  **Task:** Specify the `queryset` to retrieve all `BlogPost` objects you want to expose via the API and the `serializer_class` to be your `BlogPostSerializer` (the one you created yesterday, ideally with nested author/category).

\<details\>
\<summary\>\<b\>Solution for Exercise 1\</b\>\</summary\>

```python
# api/views.py (or blog/views.py)

from rest_framework import viewsets
from blog.models import BlogPost, Author, Category # Import your models
from .serializers import BlogPostSerializer, AuthorSerializer, CategorySerializer # Import your serializers
from rest_framework import permissions # Import permissions if you want to add them

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be viewed, created, updated, or deleted.
    """
    # Define the base queryset for this viewset
    # You might filter this queryset depending on your needs (e.g., only published posts)
    queryset = BlogPost.objects.all().order_by('-publish_date')
    # Specify the serializer class to use for this viewset
    serializer_class = BlogPostSerializer
    # Optional: Add permission classes to control access
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny] # Allow anyone access (often the default)
```

\</details\>

### Exercise 2: Configuring URLs with a Router

1.  **Task:** In your project's main `urls.py`, import `DefaultRouter` from `rest_framework.routers` and your `BlogPostViewSet` from your app's views.
2.  **Task:** Create an instance of `DefaultRouter`.
3.  **Task:** Register your `BlogPostViewSet` with the router. Choose a meaningful prefix for the URLs (e.g., `'blogposts'`).
4.  **Task:** Include the router's URLs in your project's `urlpatterns`, preferably under a versioned path like `/api/v1/`.

\<details\>
\<summary\>\<b\>Solution for Exercise 2\</b\>\</summary\>

```python
# your_project/urls.py (main project urls.py)

from django.contrib import admin
from django.urls import path, include
from rest\_framework.routers import DefaultRouter

# Import your ViewSets from your app(s) - adjust import path as needed

from api import views as api\_views \# Assuming your API views are in api/views.py

# from blog import views as blog\_views \# Alternative if ViewSets are in blog/views.py

# Create a router instance

router = DefaultRouter()

# Register your ViewSets with the router

# The first argument is the URL prefix (e.g., 'blogposts'),

# the second argument is the ViewSet class.

# basename is optional but good practice if queryset doesn't have a .model attribute

router.register(r'blogposts', api\_views.BlogPostViewSet, basename='blogpost')

# Example: Registering other ViewSets if you have them

# router.register(r'authors', api\_views.AuthorViewSet, basename='author')

# router.register(r'categories', api\_views.CategoryViewSet, basename='category')

# The API URLs are now determined automatically by the router.

# Include the router's URLs in your project's main urlpatterns

urlpatterns = [
path('admin/', admin.site.urls),
\# ... other URL patterns for your traditional views or other apps ...
path('api/v1/', include(router.urls)), \# Include DRF router URLs under /api/v1/
\# path('api/', include(router.urls)), \# Alternative: include directly under /api/
]

```

</details>

### Exercise 3: Testing Your API Endpoints

1.  **Task:** Run your Django development server: `python manage.py runserver`.
2.  **Task:** Open your web browser and navigate to the root URL handled by your router (e.g., `http://127.0.0.1:8000/api/v1/`). You should see a page listing the registered API endpoints (e.g., 'blogposts').
3.  **Task:** Navigate to the specific endpoint for blog posts (e.g., `http://127.0.0.1:8000/api/v1/blogposts/`). You should see the browsable API for your blog posts, listing any existing posts.
4.  **Task:** Use the browsable API, `curl`, or Postman/Insomnia to perform the following requests against your `/api/v1/blogposts/` and `/api/v1/blogposts/{id}/` endpoints:
      - **GET** `/api/v1/blogposts/` to get the list of all blog posts.
      - **POST** `/api/v1/blogposts/` with valid JSON data in the request body to create a new blog post. (Remember to include all required fields based on your serializer).
      - **GET** `/api/v1/blogposts/{id}/` (replace `{id}` with the ID of a post you created or know exists) to retrieve the details of a specific post.
      - **PUT** `/api/v1/blogposts/{id}/` with valid *complete* JSON data to update a specific post.
      - **PATCH** `/api/v1/blogposts/{id}/` with valid *partial* JSON data to update only specific fields of a post.
      - **DELETE** `/api/v1/blogposts/{id}/` to delete a specific post.
5.  **Task:** Observe the HTTP status codes and response bodies for each request to confirm that the operations are working as expected.

<details>
<summary><b>Solution for Exercise 3 (Conceptual Testing Steps)</b></summary>

**Conceptual Steps:**

1.  **Start Server:** `python manage.py runserver`
2.  **Access Root:** Open browser to `http://127.0.0.1:8000/api/v1/` (or your configured root). Verify you see links to registered ViewSets.
3.  **Access BlogPost Endpoint:** Open browser to `http://127.0.0.1:8000/api/v1/blogposts/`.
      * **Browsable API:** See a list of posts if any exist. You'll see a form to create new posts (POST).
      * **cURL/Postman:** Make a GET request. You should receive a JSON array of post objects.
4.  **Create Post (POST):**
      * **Browsable API:** Fill out the form with valid data and submit.
      * **cURL/Postman:** Send a POST request to `/api/v1/blogposts/` with a JSON body. Example cURL provided in Lesson Plan section 7. You should get `201 Created` and the new post's data back, including its ID.
5.  **Get Specific Post (GET {id}):**
      * Use the ID from the created post (or an existing one).
      * **Browsable API:** Click on a post's URL or manually go to `/api/v1/blogposts/{id}/`.
      * **cURL/Postman:** Send a GET request to `/api/v1/blogposts/{id}/`. You should get `200 OK` and the specific post's data.
6.  **Update Post (PUT {id}):**
      * Use the same ID. Send a PUT request to `/api/v1/blogposts/{id}/` with the *complete* updated JSON data. Example cURL in Lesson Plan section 7. You should get `200 OK` and the updated post data.
7.  **Partial Update Post (PATCH {id}):**
      * Use the same ID. Send a PATCH request to `/api/v1/blogposts/{id}/` with only the fields you want to update. Example cURL in Lesson Plan section 7. You should get `200 OK` and the updated post data.
8.  **Delete Post (DELETE {id}):**
      * Use the same ID. Send a DELETE request to `/api/v1/blogposts/{id}/`. Example cURL in Lesson Plan section 7. You should get `204 No Content`.
9.  **Verify Deletion:** Attempt to GET the deleted post's ID (`/api/v1/blogposts/{id}/`). You should get `404 Not Found`.

This exercise requires your Django models, serializers, and the `BlogPostViewSet` and URL routing from previous exercises to be correctly set up and migrated.

</details>

-----

## Detailed Daily Task

**Task: Implement and Document Blog Post API Endpoints**

1.  **Scenario:** Your goal is to have functional API endpoints for your blog posts, usable by other applications.
2.  **Instructions:**
      - Ensure you have the `BlogPost` model defined (from Week 5) and the `BlogPostSerializer` created with nested Author/Category (from Week 7, Day 2 Daily Task).
      - **Create a `BlogPostViewSet`** in your API app's `views.py` (or your blog app's `views.py`).
      - **Configure your project's main `urls.py`** to use a `DefaultRouter` to include URLs for your `BlogPostViewSet` under an appropriate API path (e.g., `/api/v1/blogposts/`).
      - **(Optional but Recommended):** Add a basic permission class to your `BlogPostViewSet` (e.g., `permissions.IsAuthenticatedOrReadOnly` or `permissions.AllowAny`) and add `'rest_framework'` settings to your `settings.py` if you haven't already.
      - **Test your API endpoints thoroughly** using the DRF browsable API, `curl`, or Postman/Insomnia to confirm that GET (list and detail), POST, PUT, PATCH, and DELETE operations work correctly and return appropriate status codes and data.
      - **Document the process** in your `daily_task.md` file. Include:
          - The code for your `BlogPostViewSet`.
          - The relevant URL configuration in your project's `urls.py`.
          - Explain *why* you used a `ModelViewSet` and a `Router`.
          - Show example API requests (using `curl` or describing requests in Postman/Insomnia) for at least a GET (list) and a POST (create) request, including the expected status code and a snippet of the expected JSON response.
          - Describe any challenges you faced and how you resolved them.

<details>
<summary><b>Solution for Daily Task: Implement and Document Blog Post APIs</b></summary>

**Example `daily_task.md` Content:**

````markdown
# Daily Task: Implementing and Documenting Blog Post API Endpoints

Today, I implemented the core API endpoints for my blog posts using Django REST Framework's ViewSets and Routers.

**1. Blog Post ViewSet Implementation:**
- Created `BlogPostViewSet` in `api/views.py`.
- Defined the `queryset` to fetch all blog posts and set the `serializer_class` to `BlogPostSerializer`.

```python
# api/views.py

from rest_framework import viewsets, permissions # Imported permissions for optional step
from blog.models import BlogPost
from .serializers import BlogPostSerializer # Assuming BlogPostSerializer is in the same app

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be viewed, created, updated, or deleted.
    """
    queryset = BlogPost.objects.all().order_by('-publish_date')
    serializer_class = BlogPostSerializer
    # Optional: Added a permission class
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
````

**2. URL Configuration with Router:**

  - Updated the main `urls.py` to include the `api` app's URLs generated by a `DefaultRouter`.

<!-- end list -->

```python
# your_project/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views as api_views # Assuming views are in api/views.py

router = DefaultRouter()
router.register(r'blogposts', api_views.BlogPostViewSet, basename='blogpost')

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... other urls ...
    path('api/v1/', include(router.urls)), # Include API urls under /api/v1/
]
```

**Explanation of ViewSet and Router Usage:**
I used `ModelViewSet` because it automatically provides all the standard CRUD actions (list, retrieve, create, update, delete) with minimal code. By simply defining the `queryset` and `serializer_class`, DRF handles the underlying logic of interacting with the model and using the serializer for data conversion and validation.
Using a `DefaultRouter` simplifies URL configuration significantly. Instead of manually defining URL patterns for each action (e.g., a separate URL for list, detail, create), the router inspects the `BlogPostViewSet` and automatically generates the appropriate URL patterns (like `/api/v1/blogposts/` and `/api/v1/blogposts/{id}/`) that map to the viewset's actions. This makes the `urls.py` much cleaner and easier to maintain as the API grows.

**3. API Testing Examples:**

**GET List Request:**

```bash
curl [http://127.0.0.1:8000/api/v1/blogposts/](http://127.0.0.1:8000/api/v1/blogposts/)
```

Expected Status Code: `200 OK`
Expected JSON Response Snippet:

```json
[
    {
        "id": 1,
        "title": "Existing Post Title",
        "slug": "existing-post-slug",
        "author": { ... }, # Nested author data
        "category": { ... }, # Nested category data
        "content": "...",
        "publish_date": "..."
    },
    // ... more posts
]
```

**POST Create Request:**

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title": "New API Post", "content": "Content created via API.", "author": 1, "category": 1, "publish_date": "2025-04-21T18:00:00Z", "slug": "new-api-post"}' [http://127.0.0.1:8000/api/v1/blogposts/](http://127.0.0.1:8000/api/v1/blogposts/)
```

*Note: Replaced {author\_id} and {category\_id} with example IDs. Your JSON data might need to match your serializer fields.*
Expected Status Code: `201 Created`
Expected JSON Response Snippet:

```json
{
    "id": 5, # Example new ID
    "title": "New API Post",
    "slug": "new-api-post",
    "author": { ... }, # Nested author data
    "category": { ... }, # Nested category data
    "content": "Content created via API.",
    "publish_date": "2025-04-21T18:00:00Z"
}
```

**Challenges:**

  - Initially, I forgot to include the `many=True` when serializing a QuerySet in the shell during earlier testing, which caused errors. Understanding when to use `many=True` is crucial for lists of objects.
  - Ensuring the nested serializers were correctly configured and included in the `fields` list of the main serializer was important for the desired output format.
  - When testing POST/PUT requests, remembering to set the `Content-Type: application/json` header and provide valid JSON data in the request body was necessary.

\</details\>

-----

## Final Wrap-up for Day 3 of Week 7

  - **Summary of Key Learnings:** Today, you've successfully built your first API endpoints using Django REST Framework\! You gained hands-on experience with different view types (FBVs, CBVs, Generic Views) but focused on the most efficient approach for building RESTful APIs: using **ModelViewSets** combined with **Routers** to automatically handle CRUD operations and URL routing. You also learned how to access request data with `request.data`, briefly saw how to apply view-level security, and practiced testing your API using various tools.
  - **Next Steps:** This understanding of building API views is fundamental. Tomorrow, we will shift our focus to a new topic: an **Introduction to MongoDB and Basic CRUD Operations**. You'll learn about NoSQL databases and how to interact with MongoDB, which will prepare you for integrating it with your Django project later this week.

*End of Week 7, Day 3 Study Material & Notes*

-----