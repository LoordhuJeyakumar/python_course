# Week 7, Day 5: Bringing it Together - MongoDB Integration with Django and DRF

## Overview

This week, we've successfully delved into building REST APIs with Django REST Framework and explored the fundamentals of the NoSQL database MongoDB. Today, we'll connect these concepts by learning how to integrate MongoDB into your Django project. We will explore three primary approaches for this integration: **PyMongo** (the official driver), **MongoEngine** (a powerful ODM layer), and **Djongo** (an ORM transpiler). You will learn how to set up and configure each method, perform CRUD operations on your MongoDB data from within your Django application, and understand how to expose this data through DRF API endpoints using `pymongo`.

By the end of this lesson, you will be able to:

  - Understand the common reasons and specific use cases for integrating MongoDB into a Django project, often alongside a relational database.
  - Install and configure the `pymongo`, `mongoengine`, and `djongo` libraries for use in a Django project.
  - Connect to a MongoDB database from your Django application using `pymongo`, including managing the connection efficiently.
  - Define document schemas and interact with MongoDB using MongoEngine's ORM-like interface.
  - Configure Djongo to allow Django's built-in ORM to interact with MongoDB collections using standard Django models and query methods.
  - Perform CRUD operations (Create, Read, Update, Delete) on MongoDB collections from within your Django views using `pymongo`.
  - Understand the critical considerations and potential complexities when mixing relational database interactions (via Django ORM) with NoSQL database interactions (with MongoDB) in a single project (data consistency, transactions, modeling, querying, etc.).
  - Create a basic API endpoint using DRF to retrieve data from MongoDB (using `pymongo`) and serialize it for a JSON response.
  - Handle incoming data from DRF API requests and save it to MongoDB using `pymongo`.
  - Assess the trade-offs and choose the most suitable approach (PyMongo, MongoEngine, or Djongo) based on project requirements, complexity, performance needs, and team expertise.

> **Project-Based Note:**
> While your core blog data might reside in a relational database, you could integrate MongoDB to store supplementary data, like real-time user activity logs, unmoderated comments, or unstructured post metadata. Today's lesson provides the tools and understanding to implement this integration and expose that MongoDB data via your blog's API, showcasing a polyglot persistence approach.

-----

## Lesson Plan

### 1\. Recap of Week 7

  - **Brief Review:** This week, we covered:
      - Fundamentals of REST APIs and HTTP methods (Day 1).
      - Setting up Django REST Framework and creating serializers for data conversion and validation (Day 2).
      - Building API views and ViewSets for handling CRUD operations on Django Models and configuring URL routing with DRF Routers (Day 3).
      - Introduction to MongoDB, its concepts (databases, collections, documents), basic CRUD operations using the `mongo` shell, and the `pymongo` Python driver (Day 4).
        Today, we bridge the gap between Django/DRF and MongoDB by exploring different ways to connect and interact with MongoDB from within your Django application.

### 2\. Why Integrate MongoDB with Django? (Use Cases and Benefits)

While Django's ORM is primarily designed for relational databases, there are compelling reasons to integrate a NoSQL database like MongoDB into a Django project, often alongside the existing relational database (a pattern known as **polyglot persistence**):

  - **Handling Unstructured or Semi-Structured Data:** MongoDB's flexible, schema-less document model is ideal for storing data where the structure is not fixed or varies significantly from item to item (e.g., user preference settings, external API responses, flexible configuration settings, user activity streams, logging). You can evolve your data model without rigid schema migrations.
  - **High-Volume, High-Velocity Data:** For data that is generated rapidly or in very large volumes (e.g., real-time sensor data, large event logs, social media feeds), MongoDB's architecture and horizontal scalability (sharding) can be a better fit than scaling a traditional relational database.
  - **Specific Data Access Patterns:** MongoDB's document model is well-suited for data that is often retrieved as a single unit (e.g., a complete user session object, a product catalog item with all its variants and details embedded). Embedding related data can lead to faster read performance compared to multiple joins in a relational database.
  - **Caching Layer:** MongoDB can sometimes be used as a fast, document-based caching layer for data retrieved from a relational database or other sources that are expensive to compute or fetch.
  - **Real-time Features:** Its capabilities, particularly with change streams, can be beneficial for features requiring real-time data updates or streaming.
  - **Leveraging Django's Strengths:** You can still utilize Django's robust features for user authentication and authorization, URL routing, templating (for parts of the app), and the admin interface (for relational data), while delegating specific data storage needs to MongoDB.
  - **Rapid Development:** Using an ODM like MongoEngine or an ORM transpiler like Djongo can sometimes reduce the boilerplate code required for data modeling and interaction compared to managing SQL migrations manually for rapidly changing schemas.

### 3\. Integrating MongoDB with Django: Three Approaches

There are several ways to integrate MongoDB into your Django project. The most common approaches are:

1.  **PyMongo (Official Driver):** Directly using the official Python driver. This gives you the most control and flexibility but requires you to handle database interactions and data mapping manually in your Python code.
2.  **MongoEngine (ODM Layer):** An Object-Document Mapper (ODM) that provides a Pythonic, Django ORM-like way to define document schemas and interact with MongoDB. It abstracts away many of the low-level `pymongo` details.
3.  **Djongo (ORM Transpiler):** Allows you to use Django's built-in ORM and models directly with MongoDB. Djongo translates Django ORM queries into MongoDB queries.

Let's explore each approach:

#### Approach 1: PyMongo (Official Driver)

This is the most fundamental way to interact with MongoDB from Python and Django.

  - **Installation:**

    ```bash
    pip install pymongo
    ```

    For extra features (like DNS SRV connection strings or TLS/SSL support):

    ```bash
    pip install "pymongo[srv,tls]"
    ```

  - **Configuration & Utility Module for Connection Management:**
    It's best practice to manage the MongoDB client connection efficiently rather than creating a new connection for each request. A utility module is a good place for this.

    ```python
    # In your project's settings.py

    # MongoDB Settings
    # Replace with your actual connection string (local or Atlas)
    MONGODB_URI = "mongodb://localhost:27017/"
    # Replace with the name of the database you want to use
    MONGODB_DATABASE = "my_django_mongo_db"

    # In a utility file (e.g., my_app/mongo_utils.py) - create this file

    from pymongo import MongoClient
    from django.conf import settings
    import atexit # Import atexit to ensure connection is closed on exit

    _mongo_client = None

    def get_mongo_client():
        """Returns a MongoClient instance, reusing an existing one if available."""
        global _mongo_client
        if _mongo_client is None:
            try:
                # Use the connection string from settings
                _mongo_client = MongoClient(settings.MONGODB_URI)
                # Optional: The ismaster command is a cheap way to check connection.
                _mongo_client.admin.command('ismaster')
                print("MongoDB connection successful!") # For debugging
            except Exception as e:
                print(f"MongoDB connection error: {e}")
                _mongo_client = None # Ensure _mongo_client is None if connection fails
        return _mongo_client

    def get_mongo_database():
        """Returns the specified MongoDB database from settings."""
        client = get_mongo_client()
        if client:
            # Access the database using the name from settings
            return client[settings.MONGODB_DATABASE]
        return None # Return None if client connection failed

    def close_mongo_client():
        """Closes the MongoDB client connection on application exit."""
        global _mongo_client
        if _mongo_client:
            _mongo_client.close()
            print("MongoDB connection closed.") # For debugging

    # Register the close function to be called automatically on application exit
    atexit.register(close_mongo_client)
    ```

    You would then import `get_mongo_database` into your views or other parts of your application to interact with MongoDB.

  - **Using PyMongo in Django Views (Performing CRUD):**
    You can use `pymongo` methods directly within your Django view functions or class-based view methods to perform CRUD operations on MongoDB collections.

    ```python
    # my_app/views.py (example using the mongo_utils)

    from django.http import JsonResponse, HttpResponse # Use Django's response types
    from .mongo_utils import get_mongo_database # Import your utility function
    import datetime
    import json # Might need json if handling request.body manually (less common with DRF)
    from bson.objectid import ObjectId # Import ObjectId for looking up by _id
    from pymongo import DESCENDING # Import for sorting

    def log_list_view(request):
        db = get_mongo_database()
        if db:
            logs_collection = db.logs # Access the 'logs' collection
            # Retrieve all documents and convert the cursor to a list
            all_logs = list(logs_collection.find().sort('timestamp', DESCENDING)) # Example sorting

            # PyMongo returns ObjectId objects for _id. These are not JSON serializable.
            # Convert ObjectId to string before returning as JSON.
            for log in all_logs:
                log['_id'] = str(log['_id'])

            # Return as JsonResponse
            return JsonResponse(all_logs, safe=False) # safe=False allows serializing lists

        return HttpResponse("Failed to connect to MongoDB.", status=500)


    def add_log_view(request):
        if request.method == 'POST':
            db = get_mongo_database()
            if db:
                logs_collection = db.logs
                # Assuming data is sent as JSON in the request body
                try:
                    data = json.loads(request.body)
                except json.JSONDecodeError:
                    return HttpResponse("Invalid JSON.", status=400)

                # Optional: Add a timestamp if not provided
                if 'timestamp' not in data:
                    data['timestamp'] = datetime.datetime.utcnow()

                # Insert the document
                result = logs_collection.insert_one(data)

                # Return the inserted document's ID
                return JsonResponse({"inserted_id": str(result.inserted_id)}, status=201) # 201 Created

            return HttpResponse("Failed to connect to MongoDB.", status=500)
        return HttpResponse("Method not allowed.", status=405) # Method Not Allowed

    # Similar views could be implemented for update and delete operations
    # def update_log_view(request, log_id):
    #     if request.method == 'PUT':
    #         db = get_mongo_database()
    #         if db:
    #             logs_collection = db.logs
    #             try:
    #                 data = json.loads(request.body)
    #                 # Use ObjectId to query by _id
    #                 result = logs_collection.update_one(
    #                     {"_id": ObjectId(log_id)},
    #                     {"$set": data} # Update using $set operator
    #                 )
    #                 if result.matched_count:
    #                     return JsonResponse({"status": "updated", "matched_count": result.matched_count, "modified_count": result.modified_count})
    #                 return HttpResponse("Log not found.", status=404)
    #             except (json.JSONDecodeError, ObjectIdError):
    #                 return HttpResponse("Invalid data or ID.", status=400)
    #         return HttpResponse("Failed to connect to MongoDB.", status=500)
    #     return HttpResponse("Method not allowed.", status=405)

    # def delete_log_view(request, log_id):
    #      if request.method == 'DELETE':
    #          db = get_mongo_database()
    #          if db:
    #              logs_collection = db.logs
    #              try:
    #                 result = logs_collection.delete_one({"_id": ObjectId(log_id)})
    #                 if result.deleted_count:
    #                     return JsonResponse({"status": "deleted", "deleted_count": result.deleted_count}, status=204) # 204 No Content
    #                 return HttpResponse("Log not found.", status=404)
    #              except ObjectIdError:
    #                  return HttpResponse("Invalid ID.", status=400)
    #          return HttpResponse("Failed to connect to MongoDB.", status=500)
    #      return HttpResponse("Method not allowed.", status=405)

    ```

    This direct approach gives maximum control over MongoDB interactions and is suitable when you need fine-grained access or are working with complex MongoDB features not fully supported by ODMs/ORMs. However, it requires more manual data handling, validation, and serialization logic compared to DRF serializers or ODMs.

#### Approach 2: MongoEngine (ODM Layer)

MongoEngine is a popular Object-Document Mapper (ODM) for Python and MongoDB. It provides a way to define document structures using Python classes and offers a query API similar to Django's ORM.

  - **Installation:**

    ```bash
    pip install mongoengine
    ```

  - **Configuration in `settings.py`:**
    You configure MongoEngine to connect to your MongoDB database, typically by calling `mongoengine.connect()` in your `settings.py` after Django has loaded.

    ```python
    # settings.py

    # ... other settings ...

    # MongoDB Settings (used by MongoEngine)
    MONGO_DB_NAME = "mydatabase"
    MONGO_HOST = os.getenv("MONGO_URI", "mongodb://localhost:27017/") # Use environment variable or default

    # --- Connect MongoEngine (can be placed at the end of settings.py) ---
    from mongoengine import connect
    import sys

    # Connect only if running a Django command or development server
    # Avoid connecting during certain management commands (like collectstatic)
    if 'runserver' in sys.argv or 'shell' in sys.argv or 'wsgi' in sys.argv or 'daphne' in sys.argv:
         try:
              connect(
                  db=MONGO_DB_NAME,
                  host=MONGO_HOST
              )
              print(f"MongoEngine connected to {MONGO_DB_NAME} at {MONGO_HOST}") # For debugging
         except Exception as e:
              print(f"MongoEngine connection error: {e}")


    ```

  - **Defining Document Schemas:**
    You define the structure of your MongoDB documents using Python classes that inherit from `mongoengine.Document` and use MongoEngine field types (like `StringField`, `IntField`, `DateTimeField`, `ListField`, `EmbeddedDocumentField`).

    ```python
    # my_app/documents.py (create this file for your MongoEngine documents)

    from mongoengine import Document, StringField, DateTimeField, EmbeddedDocument, ListField, ReferenceField
    import datetime

    # Example of an Embedded Document
    class Author(EmbeddedDocument):
        name = StringField(required=True)
        email = StringField()

    # Example of a Document
    class BlogPost(Document):
        title = StringField(required=True, max_length=200)
        content = StringField(required=True)
        # Embedded Author document
        author = EmbeddedDocumentField(Author)
        tags = ListField(StringField())
        published_date = DateTimeField(default=datetime.datetime.utcnow)
        is_published = StringField(choices=('yes', 'no', 'draft'), default='draft')

        meta = {
            'collection': 'blog_posts', # Specify the collection name in MongoDB
            'indexes': [
                'title', # Single field index
                '-published_date', # Descending index
                ('is_published', 'tags') # Compound index
            ]
        }

    # Example referencing another document (if authors were in a separate collection)
    # class AuthorDocument(Document):
    #     name = StringField(required=True)
    #     email = StringField()
    #
    # class BlogPostWithRef(Document):
    #      title = StringField(required=True)
    #      author = ReferenceField(AuthorDocument) # Reference to an AuthorDocument
    ```

  - **Using MongoEngine in Django Views:**
    You can interact with your MongoDB documents using the document classes, which provide a query API very similar to Django's ORM (`.objects`, `.filter()`, `.get()`, `.create()`, `.update()`, `.delete()`).

    ```python
    # my_app/views.py (example using MongoEngine)

    from django.shortcuts import render, redirect, get_object_or_404
    # Import your MongoEngine documents
    from .documents import BlogPost, Author # Assuming Author is embedded or defined

    def list_blog_posts(request):
        # Query all blog posts using MongoEngine
        posts = BlogPost.objects.order_by('-published_date')
        return render(request, 'blog_posts_list.html', {'posts': posts}) # Render a Django template

    def create_blog_post(request):
        if request.method == 'POST':
            # Get data from request (e.g., from a Django form or request.POST/request.data)
            title = request.POST.get('title') # Example from a form
            content = request.POST.get('content')
            author_name = request.POST.get('author_name')

            # Create an embedded Author document
            author_doc = Author(name=author_name)

            # Create a new BlogPost document
            new_post = BlogPost(
                title=title,
                content=content,
                author=author # Assign the embedded document
            )
            new_post.save() # Save the document to MongoDB

            return redirect('blog_posts_list') # Redirect after saving

        return render(request, 'create_blog_post.html') # Render a form template

    # Similar views for retrieving, updating, and deleting
    # def view_blog_post(request, post_id):
    #     # Retrieve a single blog post by its MongoDB _id
    #     try:
    #         post = BlogPost.objects.get(id=post_id) # Use 'id' for the _id field
    #         return render(request, 'blog_post_detail.html', {'post': post})
    #     except BlogPost.DoesNotExist:
    #         raise Http404

    # def update_blog_post(request, post_id):
    #      # ... get post by id ...
    #      if request.method == 'POST':
    #          # ... get data ...
    #          post.title = request.POST.get('title')
    #          post.save()
    #          return redirect('view_blog_post', post_id=post_id)
    #      # ... render update form ...

    # def delete_blog_post(request, post_id):
    #      # ... get post by id ...
    #      if request.method == 'POST':
    #          post.delete()
    #          return redirect('blog_posts_list')

    ```

    MongoEngine significantly reduces the boilerplate compared to raw `pymongo` and makes working with MongoDB feel more familiar to Django developers. It handles data type mapping, validation based on schema definition, and provides a powerful query builder.

#### Approach 3: Djongo (ORM Transpiler)

Djongo is a database backend for Django that allows you to use Django's standard ORM and model syntax with MongoDB as the database. It translates Django ORM queries into MongoDB queries.

  - **Installation:**

    ```bash
    pip install djongo
    ```

  - **Database Configuration in `settings.py`:**
    You configure Djongo in your `DATABASES` setting, specifying `djongo` as the engine.

    ```python
    # settings.py

    # ... other settings ...

    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'NAME': os.getenv("MONGO_DB_NAME", "mydjango_djongo_db"), # MongoDB database name
            'ENFORCE_SCHEMA': False, # Set to True to enforce schema validation based on Django models
            'CLIENT': {
                'host': os.getenv("MONGO_URI", "mongodb://localhost:27017/"),
                # 'port': 27017, # Optional if port is in URI
                # 'username': 'your_username', # Optional
                # 'password': 'your_password', # Optional
                # 'authSource': 'admin', # Optional
                # 'authMechanism': 'SCRAM-SHA-1' # Optional
            }
        }
    }

    # If you are using both relational and Djongo:
    # DATABASES = {
    #     'default': { # Your relational database
    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME': 'mydjangodb',
    #         # ... other relational settings ...
    #     },
    #     'mongodb': { # Your MongoDB using Djongo
    #         'ENGINE': 'djongo',
    #         'NAME': 'mydjango_djongo_db',
    #         'CLIENT': { 'host': 'mongodb://localhost:27017/' }
    #     }
    # }
    # You would then need to use database routing (DATABASE_ROUTERS) in settings.py
    # to direct model queries to the correct database.

    ```

  - **Defining Models Normally:**
    You define your models using standard `django.db.models.Model` and Django field types (`CharField`, `TextField`, etc.). Djongo handles the mapping to MongoDB document structures.

    ```python
    # my_app/models.py (Using standard Django models with Djongo)

    from django.db import models

    class Note(models.Model):
        title = models.CharField(max_length=200)
        content = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        # You can define embedded documents using models.JSONField or by creating
        # separate models and using relationships, although complex relationships
        # might have limitations in Djongo compared to relational ORM.
        # Example of embedding with JSONField:
        # author = models.JSONField(default=dict) # Stores a dictionary like {"name": "...", "email": "..."}

        def __str__(self):
            return self.title
    ```

  - **Using Djongo in Django Views:**
    You use Django's standard ORM query API (`.objects.all()`, `.filter()`, `.get()`, `.create()`, `.save()`, `.delete()`) as if you were working with a relational database. Djongo translates these operations to MongoDB queries.

    ```python
    # my_app/views.py (example using Djongo)

    from django.shortcuts import render, redirect, get_object_or_404
    from .models import Note # Import your standard Django model

    def list_notes(request):
        # Use standard Django ORM to query MongoDB
        notes = Note.objects.all().order_by('-created_at')
        return render(request, 'notes_list.html', {'notes': notes})

    def create_note(request):
        if request.method == 'POST':
            # Use standard Django ORM create
            Note.objects.create(
                title=request.POST.get('title'),
                content=request.POST.get('content')
            )
            return redirect('list_notes') # Redirect after saving

        return render(request, 'create_note.html') # Render a form template

    # Similar views for retrieve, update, and delete using standard ORM methods
    # def view_note(request, note_id):
    #     # Djongo maps Django model id to MongoDB _id
    #     note = get_object_or_404(Note, id=note_id)
    #     return render(request, 'note_detail.html', {'note': note})

    # def update_note(request, note_id):
    #     note = get_object_or_404(Note, id=note_id)
    #     if request.method == 'POST':
    #         note.title = request.POST.get('title')
    #         note.content = request.POST.get('content')
    #         note.save() # Use standard save
    #         return redirect('view_note', note_id=note_id)
    #     return render(request, 'update_note.html', {'note': note})

    # def delete_note(request, note_id):
    #     note = get_object_or_404(Note, id=note_id)
    #     if request.method == 'POST': # Or DELETE method in API
    #         note.delete() # Use standard delete
    #         return redirect('list_notes')

    ```

    Djongo's main advantage is allowing you to reuse existing Django ORM code and concepts with MongoDB. It handles the complexity of translating queries. However, its support for all Django ORM features and complex MongoDB-specific operations or schema design patterns might have limitations.

### 5\. Considerations when Mixing Django ORM (Relational) and MongoDB (NoSQL)

Integrating MongoDB into a Django project that also uses a relational database introduces complexities that require careful consideration:

  - **Data Consistency:** Ensuring data consistency and integrity across two different database systems (relational and NoSQL) can be challenging. If related data exists in both databases, you need a strategy to keep them synchronized during create, update, or delete operations. Unlike relational databases with foreign key constraints, there are no automatic cross-database integrity checks.
  - **Transactions:** While both relational databases and recent versions of MongoDB support transactions, their behavior and guarantees can differ, especially for multi-document transactions in distributed MongoDB setups. Performing operations that involve writing to both databases transactionally is complex and typically requires application-level coordination logic.
  - **Data Modeling:** You need to carefully decide which data belongs in the relational database and which belongs in MongoDB based on its structure, access patterns, scalability needs, and the strengths of each database. Avoid forcing data into a model that isn't a good fit.
  - **Querying and Joins:** You cannot perform direct joins between data stored in your relational database (using Django ORM) and data stored in MongoDB (using PyMongo, MongoEngine, or Djongo). If you need to combine data from both sources, you must retrieve data from each database separately and join/combine it in your Python code.
  - **Authentication and Authorization:** Django's built-in authentication and authorization system is tightly coupled with its ORM and the default database backend. If you store user-specific data only in MongoDB, you'll need to ensure your views properly check permissions based on the authenticated Django user when accessing or modifying that MongoDB data.
  - **Admin Interface:** Django's Admin interface is built for its ORM. Managing data stored solely in MongoDB would require building a custom admin interface within Django or using a separate MongoDB management tool (like MongoDB Compass or Atlas Data Explorer).
  - **Complexity:** Managing connections, data models, and queries for two different database technologies adds complexity to your project's codebase and deployment.

### 6\. Exposing MongoDB Data via DRF API Endpoints (using PyMongo)

You can build DRF API endpoints that interact with MongoDB data retrieved using `pymongo`. This allows you to expose your MongoDB data alongside your relational data through a unified API.

  - **API View using `APIView` or Generic Views:** You'll typically use DRF's class-based views (`APIView`, `ListAPIView`, etc.) to handle the request/response logic.

  - **Retrieving Data with PyMongo:** Inside the view method (`.get()`, `.post()`, etc.), you use your `pymongo` connection utility to get the database and collection objects and then perform `find()` or `find_one()` operations.

  - **Serialization for DRF Response:**

      - You can directly return the Python dictionaries (or lists of dictionaries) retrieved by `pymongo` in a DRF `Response`. DRF will automatically render them as JSON.
      - **Handling `_id`:** Remember that MongoDB's `_id` field is an `ObjectId`. You need to convert it to a string (`str(document['_id'])`) before returning it in a JSON response, as `ObjectId` is not a standard JSON serializable type. You can do this manually in the view or using a DRF serializer.
      - **Using DRF Serializers for MongoDB Data:** While direct return works, defining a DRF `serializers.Serializer` (not `ModelSerializer`) that matches your MongoDB document structure allows you to leverage DRF's validation and representation features.

    <!-- end list -->

    ```python
    # my_app/serializers.py (Define a Serializer for your MongoDB documents)

    from rest_framework import serializers

    class LogEntrySerializer(serializers.Serializer):
        _id = serializers.CharField(read_only=True) # To serialize ObjectId as string
        user_id = serializers.IntegerField()
        action = serializers.CharField()
        timestamp = serializers.DateTimeField()
        # Define other fields matching your MongoDB document structure
        # data = serializers.JSONField() # For flexible fields within a document

    ```

    ```python
    # my_app/views.py (API View using DRF and PyMongo)

    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from .mongo_utils import get_mongo_database # Your connection utility
    from .serializers import LogEntrySerializer # Your serializer for MongoDB data
    from bson.objectid import ObjectId # For retrieving by _id

    class LogListCreateAPIView(APIView):
        """
        API endpoint to list and create log entries in MongoDB.
        """
        def get(self, request, format=None):
            db = get_mongo_database()
            if db:
                logs_collection = db.logs
                # Retrieve documents (e.g., limit or filter for performance)
                # Using .find() returns a cursor; convert to a list
                log_entries = list(logs_collection.find().sort('timestamp', DESCENDING))

                # Using a Serializer (recommended for structure and potential validation)
                # The serializer will handle converting ObjectId to string if defined as CharField
                serializer = LogEntrySerializer(log_entries, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

                # Alternative: Return list directly (requires manual _id conversion if not using serializer)
                # for entry in log_entries:
                #     entry['_id'] = str(entry['_id'])
                # return Response(log_entries, status=status.HTTP_200_OK)

            return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        def post(self, request, format=None):
            db = get_mongo_database()
            if db:
                logs_collection = db.logs
                # Use the serializer to validate incoming data
                serializer = LogEntrySerializer(data=request.data)
                if serializer.is_valid():
                    validated_data = serializer.validated_data
                    # Insert the validated data into MongoDB
                    insert_result = logs_collection.insert_one(validated_data)
                    # Include the generated _id in the response
                    validated_data['_id'] = str(insert_result.inserted_id)
                    return Response(validated_data, status=status.HTTP_201_CREATED)
                # Return validation errors
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    class LogDetailAPIView(APIView):
        """
        API endpoint to retrieve, update, or delete a single log entry by _id.
        """
        def get_object(self, log_id):
            db = get_mongo_database()
            if db:
                logs_collection = db.logs
                try:
                    # Find the document by its ObjectId
                    return logs_collection.find_one({"_id": ObjectId(log_id)})
                except Exception as e: # Catching potential errors like InvalidId
                    print(f"Error finding log: {e}")
                    return None # Or raise Http404

            return None # Indicate connection failure

        def get(self, request, log_id, format=None):
            log_entry = self.get_object(log_id)
            if log_entry:
                serializer = LogEntrySerializer(log_entry)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "Log entry not found or DB error."}, status=status.HTTP_404_NOT_FOUND) # 404 if not found

        def put(self, request, log_id, format=None):
             log_entry = self.get_object(log_id)
             if log_entry:
                 db = get_mongo_database()
                 if db:
                     logs_collection = db.logs
                     # Use serializer to validate incoming data for update
                     serializer = LogEntrySerializer(log_entry, data=request.data)
                     if serializer.is_valid():
                         validated_data = serializer.validated_data
                         # Update the document in MongoDB
                         update_result = logs_collection.update_one(
                             {"_id": ObjectId(log_id)},
                             {"$set": validated_data}
                         )
                         # Retrieve the updated document to return in the response
                         updated_log = logs_collection.find_one({"_id": ObjectId(log_id)})
                         serializer = LogEntrySerializer(updated_log) # Serialize the updated doc
                         return Response(serializer.data, status=status.HTTP_200_OK)
                     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                 return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             return Response({"error": "Log entry not found."}, status=status.HTTP_404_NOT_FOUND)

        def delete(self, request, log_id, format=None):
            log_entry = self.get_object(log_id) # Check if exists first (optional but good practice)
            if log_entry:
                db = get_mongo_database()
                if db:
                    logs_collection = db.logs
                    delete_result = logs_collection.delete_one({"_id": ObjectId(log_id)})
                    if delete_result.deleted_count:
                        return Response(status=status.HTTP_204_NO_CONTENT) # 204 No Content on successful delete
                    return Response({"error": "Log entry not found."}, status=status.HTTP_404_NOT_FOUND) # Should not happen if get_object worked
                return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            return Response({"error": "Log entry not found."}, status=status.HTTP_404_NOT_FOUND)


    ```

  - **Mapping the DRF Views to URLs:**

    ```python
    # your_project/urls.py (main project urls.py)

    from django.urls import path
    # Import views from your app that interact with MongoDB
    from my_app import views as my_app_views

    urlpatterns = [
        # ... other URL patterns (including DRF router for relational models) ...
        # Map your MongoDB API views to URLs
        path('api/mongo/logs/', my_app_views.LogListCreateAPIView.as_view(), name='mongo_log_list_create_api'),
        path('api/mongo/logs/<str:log_id>/', my_app_views.LogDetailAPIView.as_view(), name='mongo_log_detail_api'),
        # Note: Using <str:log_id> in the URL pattern because ObjectId is represented as a string
    ]
    ```

### 7\. Practical Real-World Exercises and Tasks with Solutions

### Exercise 1: Setting up `pymongo` and Connection in Django

1.  **Task:** Install the `pymongo` library.
2.  **Task:** Add your MongoDB connection URI and database name to your project's `settings.py`. Use environment variables for credentials in a real project.
3.  **Task:** Create a utility file (e.g., `my_app/mongo_utils.py`) to handle the MongoDB client connection using the settings, ensuring the client is reused and closed on application exit, as shown in the lesson plan.

\<details\>
\<summary\>\<b\>Solution for Exercise 1\</b\>\</summary\>

1.  In your terminal, with your virtual environment active:

    ```bash
    pip install pymongo python-dotenv # Install python-dotenv for environment variables
    ```

2.  In your `settings.py`:

    ```python
    # settings.py

    import os
    from dotenv import load_dotenv # Import load_dotenv

    # Load environment variables from .env file (if it exists)
    load_dotenv()

    # ... other settings ...

    # MongoDB Settings
    # Get connection string from environment variable, with a local default
    MONGODB_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
    # Get database name from environment variable, with a default
    MONGODB_DATABASE = os.getenv("MONGO_DB_NAME", "my_django_mongo_db")

    # ... rest of settings ...
    ```

    Create a `.env` file in your project root (same directory as `manage.py`) to store sensitive connection details:

    ```dotenv
    # .env
    MONGO_URI="mongodb+srv://<your_atlas_user>:<your_password>@<your_cluster>.mongodb.net/?retryWrites=true&w=majority"
    MONGO_DB_NAME="your_atlas_database_name"
    # Or for local:
    # MONGO_URI="mongodb://localhost:27017/"
    # MONGO_DB_NAME="my_local_mongo_db"
    ```

3.  In a new file like `my_app/mongo_utils.py` (replace `my_app` with one of your app names):

    ```python
    # my_app/mongo_utils.py

    from pymongo import MongoClient
    from django.conf import settings
    import atexit
    import pymongo # Import pymongo to catch exceptions like ConnectionFailure

    _mongo_client = None

    def get_mongo_client():
        """Returns a MongoClient instance, reusing an existing one if available."""
        global _mongo_client
        if _mongo_client is None:
            try:
                # Use the connection string from settings
                _mongo_client = MongoClient(settings.MONGODB_URI)
                # The ismaster command is a cheap way to check connection and auth.
                _mongo_client.admin.command('ismaster')
                print("MongoDB connection successful!") # For debugging in development
            except pymongo.errors.ConnectionFailure as e:
                print(f"MongoDB connection error: {e}")
                _mongo_client = None # Ensure _mongo_client is None if connection fails
            except Exception as e: # Catch other potential errors during connection setup
                 print(f"An unexpected error occurred during MongoDB connection: {e}")
                 _mongo_client = None
        return _mongo_client

    def get_mongo_database():
        """Returns the specified MongoDB database from settings."""
        client = get_mongo_client()
        if client:
            # Access the database using the name from settings
            return client[settings.MONGODB_DATABASE]
        return None # Return None if client connection failed

    def close_mongo_client():
        """Closes the MongoDB client connection on application exit."""
        global _mongo_client
        if _mongo_client:
            _mongo_client.close()
            print("MongoDB connection closed.") # For debugging

    # Register the close function to be called automatically on application exit
    atexit.register(close_mongo_client)

    ```

\</details\>

### Exercise 2: Performing MongoDB CRUD in a Django View

1.  **Task:** Create a simple view function (e.g., `mongo_test_view`) in one of your apps' `views.py`.
2.  **Task:** Inside this view, use your `get_mongo_database()` utility function to get a database object.
3.  **Task:** Get a collection named `test_data`.
4.  **Task:** Perform the following operations using `pymongo` methods on the `test_data` collection:
      - Insert a document with fields like `message`, `timestamp`, and `source`.
      - Find all documents and print them to the console.
      - Find one document by a filter.
      - Update a document using `$set` to add a `status` field.
      - Delete the document you just updated.
5.  **Task:** Return an `HttpResponse` indicating the operations were performed (check the console for output).
6.  **Task:** Add a URL pattern in your project's `urls.py` to map a URL (e.g., `/mongo-test/`) to this view.
7.  **Task:** Run your server and access the URL in your browser to trigger the view and observe the console output.

\<details\>
\<summary\>\<b\>Solution for Exercise 2\</b\>\</summary\>

```python
# my_app/views.py (assuming you created my_app and mongo_utils.py in it)

from django.shortcuts import render
from django.http import HttpResponse
# Import your utility function
from .mongo_utils import get_mongo_database
import datetime
import pymongo # Import pymongo for sorting constants if needed (e.g., DESCENDING)
from bson.objectid import ObjectId # Required for querying by _id


def mongo_test_view(request):
    """
    A simple view to test MongoDB connection and basic CRUD operations.
    """
    db = get_mongo_database()

    if db:
        test_collection = db.test_data # Access the 'test_data' collection
        print("\n--- Performing MongoDB CRUD in Django View ---")

        # --- Create (Insert) ---
        print("Inserting document...")
        doc_to_insert = {
            "message": "Hello from Django!",
            "timestamp": datetime.datetime.utcnow(),
            "source": "django_view_test",
            "value": 100
        }
        insert_result = test_collection.insert_one(doc_to_insert)
        inserted_id = insert_result.inserted_id
        print(f"Inserted doc ID: {inserted_id}")

        # --- Read (Find) ---
        print("\nFinding all documents:")
        # Find all documents where source is 'django_view_test'
        all_docs_cursor = test_collection.find({"source": "django_view_test"})
        all_docs_list = list(all_docs_cursor) # Convert cursor to list
        for doc in all_docs_list:
            print(doc)

        print("\nFinding one document:")
        single_doc = test_collection.find_one({"_id": inserted_id}) # Find by the inserted ID
        print(single_doc)

        # --- Update ---
        print("\nUpdating document...")
        if single_doc: # Ensure the document was found
             update_result = test_collection.update_one(
                 {"_id": inserted_id}, # Filter by _id
                 {"$set": {"status": "processed", "updated_at": datetime.datetime.utcnow(), "value": 150}} # Update using $set
             )
             print(f"Documents matched for update: {update_result.matched_count}, Documents modified: {update_result.modified_count}")
        else:
             print("Document not found for update.")

        # --- Verify update (Optional) ---
        # updated_doc = test_collection.find_one({"_id": inserted_id})
        # print("\nDocument after update:", updated_doc)


        # --- Delete ---
        print("\nDeleting document...")
        delete_result = test_collection.delete_one({"_id": inserted_id}) # Delete by _id
        print(f"Documents deleted: {delete_result.deleted_count}")

        # --- Verify deletion (Optional) ---
        # deleted_doc = test_collection.find_one({"_id": inserted_id})
        # print("\nDocument after deletion (should be None):", deleted_doc)


        return HttpResponse("MongoDB CRUD operations performed (check server console).")

    else:
        return HttpResponse("Failed to connect to MongoDB. Check settings and ensure MongoDB is running.", status=500)

```

**Add a URL pattern in your project's `urls.py`:**

```python
# your_project/urls.py

from django.contrib import admin
from django.urls import path, include
# Import your test view
from my_app import views as my_app_views # Adjust import as needed

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... other urls ...
    path('mongo-test/', my_app_views.mongo_test_view, name='mongo_test'), # Map the test view
]
```

\</details\>

### Exercise 3: Creating a DRF API Endpoint for MongoDB Data (List and Create)

1.  **Task:** Create a simple DRF Serializer (not `ModelSerializer`) in `my_app/serializers.py` that matches the structure of your `test_data` documents from Exercise 2. Include fields like `_id` (CharField, read\_only), `message` (CharField), `timestamp` (DateTimeField), and any other fields you added.
2.  **Task:** Create a DRF API view class (e.g., `TestLogAPIView`) that inherits from `APIView` in `my_app/views.py`.
3.  **Task:** Implement the `get` method in `TestLogAPIView` to retrieve *all* documents from the `test_data` collection using `pymongo`. Use your serializer to serialize the list of documents (remember `many=True`) and return a `Response` with the data (ensuring `_id` is handled).
4.  **Task:** Implement the `post` method in `TestLogAPIView` to handle incoming API data (`request.data`). Use your serializer to validate the incoming data. If valid, insert the data into the `test_data` collection using `pymongo`. Return a `Response` with the created document's data, including the generated `_id`.
5.  **Task:** Add a URL pattern in your project's `urls.py` to map an API endpoint (e.g., `/api/mongo/testlogs/`) to this view.
6.  **Task:** Run your server and test the API endpoint using your browser (for GET and browsable API) and a tool like `curl` or Postman/Insomnia (for GET and POST).

\<details\>
\<summary\>\<b\>Solution for Exercise 3\</b\>\</summary\>

```python
# my_app/serializers.py (add this serializer)

from rest_framework import serializers
# If you used ObjectId in your documents and need to serialize it directly,
# you might need a custom field, but CharField(read_only=True) is often sufficient
# for serializing the string representation of _id.
# from bson.objectid import ObjectId

class TestLogEntrySerializer(serializers.Serializer):
    # Define fields that match your MongoDB document structure
    _id = serializers.CharField(read_only=True) # MongoDB's _id will be converted to a string
    message = serializers.CharField(max_length=255)
    timestamp = serializers.DateTimeField(required=False, allow_null=True) # Make optional if added automatically
    source = serializers.CharField(max_length=50, required=False)
    value = serializers.IntegerField(required=False, allow_null=True)
    status = serializers.CharField(max_length=50, required=False, allow_null=True)
    updated_at = serializers.DateTimeField(required=False, allow_null=True)
    # Add any other fields present in your test_data documents

    # Optional: Add validation methods if needed
    # def validate_message(self, value):
    #     if len(value) < 5:
    #         raise serializers.ValidationError("Message must be at least 5 characters long.")
    #     return value

    def create(self, validated_data):
         # This method is needed if you use serializer.save() for creating,
         # but here we will handle insertion manually in the view.
         raise NotImplementedError("Create method not implemented directly in serializer.")

    def update(self, instance, validated_data):
         # This method is needed if you use serializer.save() for updating,
         # but here we will handle update manually in the view.
         raise NotImplementedError("Update method not implemented directly in serializer.")


```

```python
# my_app/views.py (add this APIView class)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mongo_utils import get_mongo_database
# Import your serializer for MongoDB data
from .serializers import TestLogEntrySerializer
# Import ObjectId if you need to work with it directly (e.g., querying by _id string)
from bson.objectid import ObjectId, InvalidId # Import InvalidId for error handling
import datetime # Import datetime for timestamps
from pymongo import DESCENDING # For sorting

class TestLogAPIView(APIView):
    """
    API endpoint to list and create log entries in MongoDB.
    """
    def get(self, request, format=None):
        """
        List all test log entries from MongoDB.
        """
        db = get_mongo_database()
        if db:
            test_collection = db.test_data # Access the 'test_data' collection
            try:
                # Retrieve documents (e.g., add filtering or pagination for large collections)
                # Sorting by timestamp descending
                log_entries = list(test_collection.find().sort('timestamp', DESCENDING))

                # Use the serializer to format the output data
                # The serializer's CharField for _id handles ObjectId conversion
                serializer = TestLogEntrySerializer(log_entries, many=True)

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Exception as e: # Catch potential errors during find operation
                print(f"Error retrieving logs from MongoDB: {e}")
                return Response({"error": "Error retrieving log entries."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        """
        Create a new test log entry in MongoDB.
        """
        db = get_mongo_database()
        if db:
            test_collection = db.test_data # Access the 'test_data' collection
            # Use the serializer to validate incoming data from request.data
            serializer = TestLogEntrySerializer(data=request.data)

            if serializer.is_valid():
                validated_data = serializer.validated_data
                # Add a timestamp if not provided in the validated data
                if 'timestamp' not in validated_data or validated_data['timestamp'] is None:
                    validated_data['timestamp'] = datetime.datetime.utcnow()

                try:
                    # Insert the validated data into MongoDB
                    insert_result = test_collection.insert_one(validated_data)
                    # Include the generated _id in the response data
                    validated_data['_id'] = str(insert_result.inserted_id)
                    # Return the created document data with 201 Created status
                    return Response(validated_data, status=status.HTTP_201_CREATED)

                except Exception as e: # Catch potential errors during insertion
                    print(f"Error inserting log into MongoDB: {e}")
                    return Response({"error": "Error creating log entry."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # If serializer is not valid, return validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Optional: Add methods for retrieving, updating, deleting a single log entry by _id
    # class TestLogDetailAPIView(APIView):
    #     def get_object(self, log_id_str):
    #         db = get_mongo_database()
    #         if db:
    #             test_collection = db.test_data
    #             try:
    #                 # Convert the string log_id to MongoDB ObjectId for querying
    #                 object_id = ObjectId(log_id_str)
    #                 return test_collection.find_one({"_id": object_id})
    #             except InvalidId:
    #                 return None # Indicate invalid ObjectId format
    #             except Exception as e:
    #                 print(f"Error finding log by ID: {e}")
    #                 return None
    #         return None

    #     def get(self, request, log_id_str, format=None):
    #         log_entry = self.get_object(log_id_str)
    #         if log_entry:
    #             serializer = TestLogEntrySerializer(log_entry)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         return Response({"error": "Log entry not found or invalid ID."}, status=status.HTTP_404_NOT_FOUND)

    #     # ... similar put and delete methods ...

```

**Add URL patterns in your project's `urls.py`:**

```python
# your_project/urls.py

from django.contrib import admin
from django.urls import path, include
# Import your new API views
from my_app import views as my_app_views # Adjust import as needed

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... other urls (including your DRF router for relational models) ...
    # Map your MongoDB API views to URLs
    path('api/mongo/testlogs/', my_app_views.TestLogAPIView.as_view(), name='test_log_api'),
    # Optional: URL for detail view
    # path('api/mongo/testlogs/<str:log_id_str>/', my_app_views.TestLogDetailAPIView.as_view(), name='test_log_detail_api'),
]
```

\</details\>

-----

## Detailed Daily Task

**Task: Implement and Document MongoDB Integration using One Approach**

1.  **Scenario:** Choose one of the three integration approaches discussed today (PyMongo, MongoEngine, or Djongo) to implement basic CRUD functionality for a new type of data you want to store in MongoDB within your Django project (e.g., user activity logs, product reviews, unstructured notes).
2.  **Instructions:**
      - **Choose one integration approach** (PyMongo, MongoEngine, or Djongo).
      - **Set up and configure** the chosen library in your Django project as demonstrated in the lesson.
      - **Define the data structure** for your chosen data type.
          - If using PyMongo, just decide on the dictionary structure.
          - If using MongoEngine, define a `Document` class.
          - If using Djongo, define a standard `django.db.models.Model`.
      - **Implement Django views** (can be simple function views or DRF API views) that perform **Create** and **Read (List)** operations for this new data type using your chosen integration approach.
      - **Configure URLs** to access these views.
      - **Test your implementation** by creating and retrieving data.
      - **Document your process** in your `daily_task.md` file. Include:
          - Which integration approach you chose and why.
          - The setup steps and configuration code.
          - The code for your data structure definition (if using MongoEngine or Djongo).
          - The code for your Create and Read (List) views.
          - The URL configuration.
          - A brief explanation of how it works.
          - Note any challenges encountered.
3.  **Optional:** Implement Update and Delete operations as well. If using DRF, create API endpoints for these operations.

\<details\>
\<summary\>\<b\>Solution for Daily Task: Implement and Document MongoDB Integration\</b\>\</summary\>

**Example `daily_task.md` Content (Using PyMongo and DRF for User Activity Logs):**

````markdown
# Daily Task: MongoDB Integration - PyMongo Approach for User Activity Logs

Today, I integrated MongoDB into my Django project using the `pymongo` driver to store user activity logs and exposed a read-only API endpoint for these logs using DRF.

**1. Chosen Approach and Rationale:**
I chose the `pymongo` approach because it provides direct control over MongoDB interactions. For a simple logging scenario, I don't need a full ODM or ORM layer, and direct PyMongo allows flexibility for log document structure. Integrating with DRF was straightforward using `APIView`.

**2. Setup and Configuration:**
- Installed `pymongo`: `pip install pymongo`.
- Added MongoDB connection settings to `settings.py`:

```python
# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

# ... other settings ...

MONGODB_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGODB_DATABASE = os.getenv("MONGO_DB_NAME", "my_django_logs_db")
````

  - Created a `mongo_utils.py` file in my `users` app to manage the MongoDB connection:

<!-- end list -->

```python
# users/mongo_utils.py
from pymongo import MongoClient
from django.conf import settings
import atexit
import pymongo

_mongo_client = None

def get_mongo_client():
    global _mongo_client
    if _mongo_client is None:
        try:
            _mongo_client = MongoClient(settings.MONGODB_URI)
            _mongo_client.admin.command('ismaster')
            print("MongoDB connection successful!")
        except pymongo.errors.ConnectionFailure as e:
            print(f"MongoDB connection error: {e}")
            _mongo_client = None
        except Exception as e:
             print(f"An unexpected error occurred: {e}")
             _mongo_client = None
    return _mongo_client

def get_mongo_database():
    client = get_mongo_client()
    if client:
        return client[settings.MONGODB_DATABASE]
    return None

def close_mongo_client():
    global _mongo_client
    if _mongo_client:
        _mongo_client.close()
        print("MongoDB connection closed.")

atexit.register(close_mongo_client)
```

**3. Data Structure Definition:**
The structure for user activity log documents will be flexible but typically includes:

```json
{
  "_id": ObjectId("..."),
  "user_id": 123,
  "action": "view_post",
  "details": {
    "post_id": 5,
    "post_title": "API Basics"
  },
  "timestamp": ISODate("...")
}
```

**4. Views Implementation (DRF API Views):**
Created a serializer for the log data and a DRF API view.

  - `users/serializers.py`:

<!-- end list -->

```python
# users/serializers.py
from rest_framework import serializers

class UserActivityLogSerializer(serializers.Serializer):
    _id = serializers.CharField(read_only=True)
    user_id = serializers.IntegerField()
    action = serializers.CharField(max_length=100)
    details = serializers.JSONField(required=False) # Use JSONField for flexible details
    timestamp = serializers.DateTimeField()

    # No create/update methods needed in the serializer as we use pymongo directly

```

  - `users/views.py`:

<!-- end list -->

```python
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mongo_utils import get_mongo_database
from .serializers import UserActivityLogSerializer
from pymongo import DESCENDING
import datetime

class UserActivityLogListCreateAPIView(APIView):
    """
    API endpoint to list and create user activity log entries in MongoDB.
    """
    def get(self, request, format=None):
        db = get_mongo_database()
        if db:
            logs_collection = db.user_activity_logs # Access the collection
            try:
                # Retrieve logs, sort by timestamp descending
                log_entries = list(logs_collection.find().sort('timestamp', DESCENDING))
                serializer = UserActivityLogSerializer(log_entries, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                print(f"Error retrieving logs: {e}")
                return Response({"error": "Error retrieving logs."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        db = get_mongo_database()
        if db:
             logs_collection = db.user_activity_logs
             serializer = UserActivityLogSerializer(data=request.data)
             if serializer.is_valid():
                  validated_data = serializer.validated_data
                  if 'timestamp' not in validated_data:
                       validated_data['timestamp'] = datetime.datetime.utcnow()
                  try:
                       insert_result = logs_collection.insert_one(validated_data)
                       validated_data['_id'] = str(insert_result.inserted_id)
                       return Response(validated_data, status=status.HTTP_201_CREATED)
                  except Exception as e:
                       print(f"Error inserting log: {e}")
                       return Response({"error": "Error creating log."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "Failed to connect to MongoDB."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


```

**5. URL Configuration:**
Added a URL pattern in the project's main `urls.py`:

```python
# your_project/urls.py
from django.urls import path, include
from users import views as users_views # Import your views

urlpatterns = [
    # ... other urls ...
    # API endpoint for user activity logs
    path('api/user-activity/', users_views.UserActivityLogListCreateAPIView.as_view(), name='user_activity_log_api'),
]
```

**6. Testing:**

  - Ran the server.
  - Used browser to GET `http://127.0.0.1:8000/api/user-activity/` to see existing logs (empty initially).
  - Used `curl` to POST a new log entry:

<!-- end list -->

```bash
curl -X POST -H "Content-Type: application/json" -d '{"user_id": 1, "action": "view_homepage", "details": {}, "timestamp": "2025-04-21T19:00:00Z"}' [http://127.0.0.1:8000/api/user-activity/](http://127.0.0.1:8000/api/user-activity/)
```

Expected 201 Created response with the inserted document.

  - Used browser/curl again to GET and verify the new log entry appeared.

**Challenges:**

  - Ensuring the `mongo_utils` connection logic handled potential errors and connection reuse correctly.
  - Remembering to convert `ObjectId` to string in the DRF response.
  - Using `serializers.Serializer` for validation and structuring MongoDB data instead of `ModelSerializer`.

<!-- end list -->

```
</details>

---

## Final Wrap-up for Week 7

- **Summary of Key Learnings:** Congratulations on completing Week 7! You've successfully ventured into the exciting world of REST APIs and NoSQL databases. You learned the fundamentals of REST and HTTP, mastered Django REST Framework for building API endpoints for your relational models, explored MongoDB basics and CRUD operations in the shell and with `pymongo`. Today, you integrated MongoDB with your Django project using `pymongo`, learned about other approaches like MongoEngine and Djongo, understood the considerations when mixing database types, performed CRUD operations from views, and exposed MongoDB data via DRF.
- **Next Steps:** This week has provided a strong foundation in building modern backends. Next week, we'll cover **Advanced Topics, Deployment, and introduce the Capstone Project**. This will include more advanced Django concepts (authentication, middleware, caching), advanced MongoDB queries, deployment basics (getting your application live!), and the exciting start of your Capstone Project where you'll apply and integrate all the skills you've learned over the past seven weeks to build a complete full-stack application!

*End of Week 7 Study Material & Notes*

---