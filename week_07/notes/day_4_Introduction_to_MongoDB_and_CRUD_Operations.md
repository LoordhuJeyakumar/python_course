# Week 7, Day 4: Stepping into the NoSQL World - Introduction to MongoDB

## Overview

So far in this bootcamp, our database interactions have been primarily with relational databases using Django's ORM. Today, we're going to explore a different type of database: a **NoSQL database**, specifically **MongoDB**. NoSQL databases offer different advantages compared to traditional relational databases and are often used for handling large volumes of unstructured or semi-structured data, achieving higher scalability, and providing schema flexibility. We'll learn the fundamental concepts of MongoDB and how to perform basic data operations (CRUD) using its interactive shell and the `pymongo` Python driver. By the end of this lesson, you will be able to:

  - Understand the concept of NoSQL databases, their characteristics, and how they differ from relational databases.
  - Define what MongoDB is and recognize its key characteristics as a document database (using BSON).
  - Identify the benefits of using MongoDB, such as scalability, flexibility (schema-less), and performance.
  - Understand the basic architecture of MongoDB (databases, collections, documents).
  - Set up and connect to a MongoDB instance (locally or via a cloud service like Atlas).
  - Use the MongoDB shell (`mongo` / `mongosh`) to interact with your data.
  - Perform basic CRUD operations (Create, Read, Update, Delete) using the MongoDB shell commands, including filtering and basic update operators.
  - Use the `pymongo` Python driver to connect to MongoDB and perform basic CRUD operations from a Python script.
  - Understand basic best practices in MongoDB, including schema design approaches (embedding vs. referencing) and indexing.

> **Project-Based Note:**
> While our blog project primarily uses a relational database (like SQLite or PostgreSQL) with Django, understanding NoSQL databases like MongoDB is valuable for a full-stack developer. You might encounter projects where MongoDB is used for specific features (e.g., real-time data, logging, unstructured content) or as the primary database. Learning MongoDB now expands your toolkit and prepares you for integrating it with Django or using it in standalone Python applications.

-----

## Lesson Plan

### 1\. Recap of Week 7 (So far)

  - **Brief Review:** This week, we've transitioned into building REST APIs with Django REST Framework. We covered the fundamentals of RESTful architecture and HTTP methods (Day 1), set up DRF and learned about serializers for data conversion and validation (Day 2), and built API views using ViewSets and Routers to expose our Django models as API endpoints (Day 3). Today, we take a detour to explore a different data storage technology – MongoDB – which we will then integrate with our API knowledge later in the week.

### 2\. Introduction to NoSQL Databases

  - **What is NoSQL?**
      - NoSQL stands for "Not Only SQL". It's a broad category of databases that move away from the traditional relational model (fixed schemas, tables, SQL queries).
      - NoSQL databases offer alternative ways of storing and retrieving data, often designed for specific use cases that relational databases might not handle as efficiently, such as handling large volumes of data, high velocity data, or data with varying structures.
  - **Key Characteristics of NoSQL Databases:**
      - **Schema-less or Flexible Schema:** Data can be stored without a strict, predefined schema. Documents within the same collection can have different fields. This provides flexibility and faster development cycles for evolving data structures.
      - **Horizontal Scalability:** Many NoSQL databases are designed to scale out horizontally across many servers, making them suitable for handling massive volumes of data and high traffic loads by distributing the data.
      - **Varied Data Models:** NoSQL databases use different data models, including:
          - **Document-based:** Data is stored in documents (like JSON or BSON). MongoDB is a primary example.
          - **Key-Value:** Data is stored as simple key-value pairs. (e.g., Redis, DynamoDB).
          - **Column-Family:** Data is stored in columns families (e.g., Cassandra, HBase).
          - **Graph-based:** Data is stored as nodes and edges in a graph structure (e.g., Neo4j).
      - **Generally Non-Relational:** They typically do not use fixed tables and relationships with foreign keys like relational databases, although relationships can be handled through embedding or referencing documents.
      - **Different Consistency Models:** NoSQL databases often prioritize availability and partition tolerance over strong immediate consistency (ACID) in distributed environments, often offering eventual consistency.

### 3\. What is MongoDB? - Document Database

  - **MongoDB:** A popular, open-source, cross-platform **document-oriented database**.
  - **Document Database:** In a document database like MongoDB, data is stored in **documents**. A document is a collection of key-value pairs, similar to JSON objects. Documents are self-describing and can have nested structures (arrays, other documents).
  - **BSON:** MongoDB stores data in a binary representation of JSON called **BSON (Binary JSON)**. BSON extends JSON with additional data types like Date, Binary data, ObjectId, etc.

### 4\. Advantages of MongoDB

  - **Flexibility (Schema-less):** You can add new fields, remove fields, or change the structure of documents within a collection without needing to perform complex schema migrations across the entire database. This is ideal for agile development.
  - **Scalability:** MongoDB is designed for horizontal scalability using techniques like sharding (distributing data across multiple servers) and replica sets (providing data redundancy and high availability).
  - **High Performance:** MongoDB can offer high performance for reads and writes, particularly for operations on single documents or when accessing embedded data, as related information can be retrieved in a single query.
  - **Rich Query Language:** MongoDB provides a powerful, JSON-like query language that supports a wide range of operations, including filtering, sorting, aggregation, geospatial queries, and text search.
  - **Developer Productivity:** Working with JSON-style documents in MongoDB often maps naturally to objects and data structures used in application code, simplifying development.
  - **Community and Ecosystem:** MongoDB has a large and active community, extensive documentation, and a rich ecosystem of drivers for various programming languages (like `pymongo` for Python).

### 5\. MongoDB vs. Relational Databases (Comparison)

| Feature          | Relational Databases (e.g., PostgreSQL, MySQL)      | MongoDB (NoSQL - Document)                         |
| :--------------- | :-------------------------------------------------- | :------------------------------------------------- |
| **Data Model** | Tables with rows and columns, fixed schema.         | Collections of documents, flexible schema.         |
| **Schema** | Strict and predefined; schema changes often require migrations. | Dynamic and flexible (schema-less); documents can have varying structures. |
| **Relationships**| Defined using foreign keys and joins between tables. | Typically handled by **embedding** related documents within a parent document or using **references** (storing the `_id` of a related document). |
| **Query Language**| SQL (Structured Query Language).                    | MongoDB Query Language (document-based queries).     |
| **Scalability** | Traditionally scales vertically (more powerful server); horizontal scaling (sharding) can be complex. | Designed for horizontal scaling (sharding) and built-in replication (replica sets). |
| **Data Type** | Primarily structured data.                          | Structured, semi-structured, and can handle unstructured data within documents. |
| **Transactions** | Strong ACID compliance for multi-operation transactions. | Supports ACID transactions within a single document; multi-document transactions were introduced in later versions with different considerations. |

  - **When to Choose Which:**
      - **Relational Databases:** Best for applications requiring strong data integrity and complex transactions across multiple entities (ACID), applications with highly structured data and well-defined relationships, and when extensive analytical reporting with complex joins is needed.
      - **MongoDB:** Excellent for handling large volumes of data with high velocity, applications requiring flexibility in data structure, content management systems, catalogs, real-time data feeds, logging, and scenarios where related data can be effectively embedded within a single document to minimize read operations.
      - **Hybrid Approaches:** In large-scale systems, it's increasingly common to use both relational and NoSQL databases, leveraging the strengths of each for different parts of the application (e.g., relational for core business logic, MongoDB for user activity or a product catalog).

### 6\. Basic MongoDB Architecture: Databases, Collections, Documents

  - **Database:** A container for collections. A single MongoDB server can host multiple databases. You typically create a separate database for each application.
  - **Collection:** A group of documents. Collections are analogous to tables in relational databases, but they do not enforce a rigid schema. Documents within the same collection can have different structures. Collections reside within a database.
  - **Document:** The basic unit of data in MongoDB. A document is a BSON (or JSON-like) object containing key-value pairs. Documents are schema-less, meaning a document in a collection does not need to have the same fields as other documents in the same collection.
    ```json
    {
      "_id": ObjectId("65c8d7c1a1b2c3d4e5f67890"),  // Unique identifier generated by MongoDB
      "title": "Introduction to MongoDB",
      "content": "MongoDB stores data in flexible, JSON-like documents...",
      "author": {           // Embedded Document
        "name": "Alice Wonderland",
        "email": "alice@example.com"
      },
      "tags": ["mongodb", "nosql", "database", "bson"], // Array Field
      "published": true,
      "created_at": ISODate("2025-04-21T10:00:00.000Z"), // Date Field
      "views": 150          // Number Field
    }
    ```
      - `_id`: A unique identifier for each document within a collection. If you insert a document without an `_id` field, MongoDB automatically adds one with a unique `ObjectId` value.

### 7\. Setting up MongoDB Locally or Using Cloud Services

  - **Local Installation:** You can download and install MongoDB Community Server on your own machine. The installation process is OS-specific (Windows, macOS, Linux). After installation, you need to start the MongoDB server process (`mongod`).
      - **Common Commands (Linux/macOS):**
        ```bash
        # Start the MongoDB daemon (server)
        mongod
        # or using a package manager service
        # brew services start mongodb-community@6.0 # macOS Homebrew
        # sudo systemctl start mongod # Ubuntu/Debian
        ```
  - **Cloud Services (MongoDB Atlas):** MongoDB Atlas is the official cloud database service for MongoDB. It offers a managed, hosted MongoDB instance in various cloud providers (AWS, Google Cloud, Azure). It's often the easiest way to get started and provides a free tier for learning and small projects.
      - **Benefits of Atlas:** Easy setup, automated tasks (backups, patching), scaling options, built-in monitoring and security features.
  - **Connecting:** Once MongoDB is running (locally or on Atlas), you can connect to it using the MongoDB shell or a driver like `pymongo`. The connection details (hostname, port, database name, credentials) will be provided by your local setup or Atlas.

### 8\. MongoDB Shell and Basic Commands (`mongo` / `mongosh`)

  - **MongoDB Shell:** MongoDB provides an interactive JavaScript shell (`mongosh` for recent versions, `mongo` for older versions) for interacting with MongoDB instances from the command line. It's a powerful tool for administration, querying, and scripting.
  - **Connecting to the Shell:** Open your terminal and type `mongosh` (or `mongo`). By default, it connects to a local MongoDB server running on `localhost:27017`. To connect to a different instance (including Atlas), you'll provide a connection string as an argument.
  - **Basic Shell Commands:**
      - `show dbs`: Lists all databases on the connected MongoDB instance.
      - `use <database_name>`: Switches the current database context to `<database_name>`. If the database doesn't exist, MongoDB creates it implicitly when you first insert data into a collection within that database.
      - `db`: Displays the name of the current database you are using.
      - `show collections`: Lists all collections in the current database.

### 9\. CRUD Operations in MongoDB Shell

The MongoDB shell provides methods attached to the `db` object (representing the current database) and then to collection objects (e.g., `db.mycollection`).

  - **Create (Insert):**

      - `db.collection.insertOne(document)`: Inserts a single document into a collection.
      - `db.collection.insertMany([document1, document2, ...])`: Inserts multiple documents into a collection.

    <!-- end list -->

    ```javascript
    // In the mongo/mongosh shell, after using a database (e.g., `use mydatabase`)

    // Insert a single user document
    db.users.insertOne({
      name: "Charlie Brown",
      age: 8,
      city: "Sparkyville"
    });

    // Insert multiple product documents
    db.products.insertMany([
      { name: "T-Shirt", price: 20, colors: ["Red", "Blue"] },
      { name: "Jeans", price: 50, size: "M" },
      { name: "Hat", price: 15 }
    ]);
    ```

  - **Read (Find):**

      - `db.collection.find(query document)`: Retrieves documents from a collection. The optional query document specifies filtering criteria. Returns a cursor to the matching documents.
      - `db.collection.findOne(query document)`: Retrieves the first document that matches the query.

    <!-- end list -->

    ```javascript
    // Find all documents in the users collection
    db.users.find(); // Use .pretty() to format output: db.users.find().pretty();

    // Find users older than 7
    db.users.find({ age: { $gt: 7 } }); // Using the $gt operator (greater than)

    // Find products with the name "Jeans"
    db.products.find({ name: "Jeans" });

    // Find products that have the color "Red" in their colors array
    db.products.find({ colors: "Red" }); // MongoDB can query array elements directly

    // Find a single user named Charlie Brown
    db.users.findOne({ name: "Charlie Brown" });
    ```

  - **Update:**

      - `db.collection.updateOne(filter document, update document)`: Updates the first document that matches the filter.
      - `db.collection.updateMany(filter document, update document)`: Updates all documents that match the filter.
      - **Update Operators:** Update operations use operators (like `$set`, `$inc`, `$push`, `$unset`) in the `update document` to specify how to modify the existing document fields.
          - `$set`: Sets the value of a field.
          - `$inc`: Increments the value of a field.
          - `$push`: Appends an element to an array field.
          - `$unset`: Removes a field from a document.

    <!-- end list -->

    ```javascript
    // Update Charlie Brown's city
    db.users.updateOne(
      { name: "Charlie Brown" },
      { $set: { city: "Peanuts Town" } } // Set the city field
    );

    // Increment the age of all users by 1
    db.users.updateMany(
      {}, // Empty filter matches all documents
      { $inc: { age: 1 } } // Increment the age field
    );

    // Add "Green" to the colors array of the T-Shirt document
    db.products.updateOne(
      { name: "T-Shirt" },
      { $push: { colors: "Green" } } // Push "Green" into the colors array
    );
    ```

  - **Delete:**

      - `db.collection.deleteOne(filter document)`: Deletes the first document that matches the filter.
      - `db.collection.deleteMany(filter document)`: Deletes all documents that match the filter.

    <!-- end list -->

    ```javascript
    // Delete the document for Charlie Brown
    db.users.deleteOne({ name: "Charlie Brown" });

    // Delete all products with a price less than 10
    db.products.deleteMany({ price: { $lt: 10 } });
    ```

### 10\. Python Integration with `pymongo`

  - **`pymongo`:** This is the official Python driver for MongoDB, allowing you to interact with MongoDB databases programmatically from your Python applications, including Django.

  - **Installation:**

    ```bash
    pip install pymongo
    ```

  - **Connecting to MongoDB from Python:** Use the `MongoClient` class.

    ```python
    from pymongo import MongoClient

    # Connect to a local MongoDB instance
    client = MongoClient("mongodb://localhost:27017/")

    # Connect to a MongoDB Atlas instance (replace with your connection string)
    # client = MongoClient("mongodb+srv://<username>:<password>@<cluster-url>/mydatabase?retryWrites=true&w=majority")

    # Access a database
    db = client.mydatabase # Access the database named 'mydatabase'

    # Access a collection
    users_collection = db.users # Access the collection named 'users'

    # Or using dictionary-style access
    db = client['mydatabase']
    users_collection = db['users']
    ```

    The `MongoClient` manages connection pooling and thread safety automatically.

  - **Performing Basic CRUD with `pymongo`:** The `pymongo` methods for collections mirror the shell commands.

    ```python
    from pymongo import MongoClient
    from datetime import datetime

    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client.mydatabase # Replace with your database name
    posts_collection = db.posts # Replace with your collection name

    # --- Create ---
    post_document = {
        "title": "First PyMongo Post",
        "content": "Inserting documents with Python.",
        "published_date": datetime.utcnow()
    }
    insert_result = posts_collection.insert_one(post_document)
    print(f"Inserted document ID: {insert_result.inserted_id}")

    posts_list = [
        {"title": "Post 2", "content": "Second post."},
        {"title": "Post 3", "content": "Third post."}
    ]
    insert_many_result = posts_collection.insert_many(posts_list)
    print(f"Inserted document IDs: {insert_many_result.inserted_ids}")

    # --- Read ---
    # Find all documents
    print("\nFinding all posts:")
    for post in posts_collection.find():
        print(post)

    # Find documents matching a filter
    print("\nFinding post with title 'Post 2':")
    post_two = posts_collection.find_one({"title": "Post 2"})
    print(post_two)

    # --- Update ---
    # Update one document
    update_result = posts_collection.update_one(
        {"title": "First PyMongo Post"},
        {"$set": {"content": "Content updated via PyMongo."}}
    )
    print(f"\nMatched {update_result.matched_count}, Modified {update_result.modified_count} document(s).")

    # --- Delete ---
    # Delete one document
    delete_result = posts_collection.delete_one({"title": "Post 3"})
    print(f"\nDeleted {delete_result.deleted_count} document(s).")

    # --- Close the connection (good practice in longer scripts) ---
    # client.close() # Not strictly necessary if the script ends, but good to know

    ```

  - **Integration with Django:** While `pymongo` is used, directly embedding complex database interaction logic in Django views can make them less maintainable. Tomorrow, we will discuss strategies for integrating MongoDB with Django more effectively, potentially within dedicated modules or helper functions, and how to expose this data via DRF.

### 11\. Best Practices and Patterns

  - **Indexing:** Create indexes on fields that are frequently queried to improve read performance.
    ```javascript
    // In the mongo/mongosh shell
    db.posts.createIndex({ title: 1 }); // Create an ascending index on the 'title' field
    db.users.createIndex({ age: -1, city: 1 }); // Compound index (descending age, ascending city)
    ```
  - **Schema Design (Embedding vs. Referencing):** This is a critical decision in MongoDB.
      - **Embedding:** Store related data within a single document. Ideal for one-to-one relationships or one-to-many relationships where the "many" side is not too large and is frequently accessed with the "one" side (e.g., embedding comments within a blog post if comments are always viewed with the post). Reduces the number of queries needed.
      - **Referencing:** Store related data in separate collections and include references (usually the `_id`) in documents. Ideal for many-to-many relationships, one-to-many relationships where the "many" side is very large, or when the related data is frequently accessed independently (e.g., referencing an Author from a BlogPost). Requires multiple queries (or using `$lookup` in aggregation) to retrieve related data.
      - The choice depends on the relationship type, data access patterns, and data size.
  - **Error Handling and Connection Pooling:** In `pymongo`, use `try...except` blocks to handle potential database errors. `MongoClient` automatically handles connection pooling, which is efficient for managing connections in applications.

### 12\. Wrap-up and Q\&A

  - **Summary of Key Learnings:** Today, you've successfully stepped into the world of NoSQL databases by learning the fundamental concepts of MongoDB. You understand how it differs from relational databases, its key benefits, and its basic architecture (databases, collections, documents). You've also gained practical experience using the MongoDB shell to perform the essential CRUD operations (insert, find, update, delete) and learned how to connect to MongoDB and perform CRUD using the `pymongo` Python driver. You were introduced to important best practices like indexing and schema design considerations.
  - **Next Steps:** Tomorrow, we will bring together what we've learned about Django (models, views, DRF) and MongoDB. We'll discuss strategies for integrating MongoDB into our Django application using the `pymongo` driver to store and retrieve data from MongoDB collections within our Django views and potentially expose that data via a DRF API, demonstrating how to work with different database technologies in a single project.

-----

## Practical Exercises with Solutions

### Exercise 1: Setting up and Connecting to MongoDB

1.  **Task:** Install MongoDB Community Server locally OR sign up for a free tier on MongoDB Atlas.
2.  **Task:** Start your local MongoDB server (if installed locally) or get your connection string from Atlas.
3.  **Task:** Open your terminal and connect to your MongoDB instance using the `mongosh` (or `mongo`) shell.
4.  **Task:** Use the `show dbs` command to see the available databases.
5.  **Task:** Use a command to switch to a database named `mywebstore` (this database will be created if it doesn't exist when you first store data).

\<details\>
\<summary\>\<b\>Solution for Exercise 1\</b\>\</summary\>
The exact steps depend on your operating system for local installation or using Atlas.

1.  Follow the installation guides on the MongoDB website for your OS.
2.  Start the MongoDB server process (e.g., `sudo systemctl start mongod` on Linux, or as a service on Windows).
3.  In your terminal, run `mongosh`. If connecting to Atlas, use the connection string provided by Atlas (it will look something like `mongosh "mongodb+srv://<username>:<password>@<cluster-url>/mydatabase" --apiVersion 1 --username <username>`).
4.  In the shell, type:
    ```javascript
    show dbs
    ```
    You should see output listing databases like `admin`, `config`, `local`.
5.  In the shell, type:
    ```javascript
    use mywebstore
    ```
    The output should indicate that you've switched to the `mywebstore` database (e.g., `switched to db mywebstore`).

\</details\>

### Exercise 2: MongoDB Shell CRUD Practice

1.  **Task:** While in the `mywebstore` database in the MongoDB shell, insert three product documents into a collection named `products`. Each document should have at least `name`, `price`, and `in_stock` (boolean) fields. Include at least one document with an additional field not present in others (to demonstrate schema flexibility).
2.  **Task:** Query products with `price > 50`.
3.  **Task:** Update one product using `updateOne` to set a new field (e.g., `discount: 10`).
4.  **Task:** Update one product using `updateOne` and the `$inc` operator to increment its price by 5.
5.  **Task:** Delete any product where `in_stock` is `false` using `deleteMany`.
6.  **Task:** Delete one product by its `_id` (find an `_id` first using `find()`). Use `deleteOne`.

\<details\>
\<summary\>\<b\>Solution for Exercise 2\</b\>\</summary\>
While in the `mywebstore` database in the `mongosh` shell:

```javascript
// Make sure you are in the correct database: `use mywebstore`

// 1. Insert documents
db.products.insertMany([
  { name: "Widget Pro", price: 75, in_stock: true, tags: ["gadget", "tech"] },
  { name: "Basic Gadget", price: 45, in_stock: true },
  { name: "Legacy Doohickey", price: 120, in_stock: false, notes: "Old model" }
]);

// Verify insertion:
db.products.find().pretty();

// 2. Query
db.products.find({ price: { $gt: 50 } }).pretty();

// 3. Update one product to set a new field
db.products.updateOne(
  { name: "Widget Pro" },
  { $set: { discount: 10 } }
);
// Verify update:
db.products.find({ name: "Widget Pro" }).pretty();


// 4. Update one product to increment price
db.products.updateOne(
  { name: "Basic Gadget" },
  { $inc: { price: 5 } }
);
// Verify update:
db.products.find({ name: "Basic Gadget" }).pretty();


// 5. Delete products where in_stock is false
db.products.deleteMany({ in_stock: false });
// Verify deletion:
db.products.find().pretty();


// 6. Delete one product by _id
// First, find an _id (e.g., from the output of db.products.find().pretty())
// Let's assume an _id is ObjectId("abc123...") for the next step
// const productToDeleteId = ObjectId("abc123..."); // Replace with an actual _id

// To find an id to use:
const productToDelete = db.products.findOne({}); // Get any remaining product
if (productToDelete) {
  db.products.deleteOne({ _id: productToDelete._id });
  print("Deleted one product by _id:", productToDelete._id);
} else {
  print("No products left to delete by _id.");
}

// Verify final state:
db.products.find().pretty();
```

\</details\>

### Exercise 3: Python `pymongo` CRUD Script

1.  **Task:** Write a Python script (`mongo_crud.py`) using `pymongo`.
2.  **Task:** Connect to your local MongoDB instance (or Atlas using your connection string).
3.  **Task:** Access a database named `myblogdb` and a collection named `posts`.
4.  **Task:** Insert a document representing a blog post with fields like `title`, `content`, `author` (embedded document), and `date`.
5.  **Task:** Find and print all documents in the `posts` collection.
6.  **Task:** Find and print the document with the title you just inserted.
7.  **Task:** Update the content of the document you just inserted.
8.  **Task:** Delete the document you just updated.

\<details\>
\<summary\>\<b\>Solution for Exercise 3\</b\>\</summary\>

```python
# mongo_crud.py

from pymongo import MongoClient
from datetime import datetime

# Replace with your MongoDB connection string
# For local: "mongodb://localhost:27017/"
# For Atlas: "mongodb+srv://<username>:<password>@<cluster-url>/mydatabase?retryWrites=true&w=majority"
mongo_connection_string = "mongodb://localhost:27017/"

# Database and Collection names
database_name = "myblogdb"
collection_name = "posts"

try:
    # 2. Connect to MongoDB
    client = MongoClient(mongo_connection_string)

    # Check if the connection was successful (optional, but good practice)
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    print("MongoDB connection successful!")

    # 3. Access database and collection
    db = client[database_name]
    posts_collection = db[collection_name]
    print(f"Accessed database: {database_name}, collection: {collection_name}")

    # --- 4. Insert a document ---
    print("\n--- Inserting Document ---")
    post_to_insert = {
        "title": "PyMongo Basics",
        "content": "Learning CRUD operations with pymongo.",
        "author": {
            "name": "Coder McCodeface",
            "email": "coder@example.com"
        },
        "date": datetime.utcnow()
    }
    insert_result = posts_collection.insert_one(post_to_insert)
    print(f"Inserted document with ID: {insert_result.inserted_id}")

    # --- 5. Find and print all documents ---
    print("\n--- Finding All Documents ---")
    for post in posts_collection.find():
        print(post)

    # --- 6. Find and print the document with the specific title ---
    print("\n--- Finding Document by Title ---")
    found_post = posts_collection.find_one({"title": "PyMongo Basics"})
    print(found_post)

    # --- 7. Update the content of the document ---
    print("\n--- Updating Document ---")
    if found_post:
        update_result = posts_collection.update_one(
            {"_id": found_post["_id"]}, # Filter by _id is generally best
            {"$set": {"content": "Content has been updated using pymongo!"}}
        )
        print(f"Matched {update_result.matched_count}, Modified {update_result.modified_count} document(s).")
    else:
        print("Document not found for update.")

    # --- Verify the update ---
    # updated_post = posts_collection.find_one({"_id": found_post["_id"]})
    # print("Updated document:", updated_post)


    # --- 8. Delete the document ---
    print("\n--- Deleting Document ---")
    # We use the _id from the insertion result or the found_post
    if insert_result.inserted_id: # Or use if found_post and found_post.get("_id"):
        delete_result = posts_collection.delete_one({"_id": insert_result.inserted_id})
        print(f"Deleted {delete_result.deleted_count} document(s).")
    else:
         print("Could not find document ID to delete.")


    # --- Verify the deletion ---
    # deleted_post = posts_collection.find_one({"_id": insert_result.inserted_id})
    # print("Document after deletion:", deleted_post)


except Exception as e:
    print(f"An error occurred: {e}")
    # In a real application, you would handle specific exceptions (e.g., ConnectionFailure)
finally:
    # Close the connection (good practice)
    if 'client' in locals() and client:
        client.close()
        print("\nMongoDB connection closed.")

```

\</details\>

-----

## Detailed Daily Task

**Task: Explore Data Modeling Differences between Relational and Document Databases**

1.  **Scenario:** Consider how you would represent the data for a simple e-commerce order in a relational database versus a MongoDB document database. An order has an order ID, a customer, order date, and multiple items. Each item has a product (with name, price), quantity, and potentially options (like size, color).

2.  **Instructions:**

      - **Relational Database Design:** Sketch out the tables you would need, their columns, and the relationships between them (e.g., `Orders` table, `Customers` table, `OrderItems` table, `Products` table).
      - **MongoDB Document Database Design:** Sketch out the structure of a single document you would create in an `orders` collection to represent a complete order. Think about whether you would embed item details directly within the order document or reference product IDs from a separate `products` collection. Consider the pros and cons of each approach for this specific scenario.
      - **Compare and Contrast:** Write a brief comparison of the two approaches, noting the pros and cons for this specific e-commerce order scenario. Consider aspects like data retrieval (e.g., getting an order with all its items), flexibility for adding new item options, data duplication, and query complexity.

3.  **Write down your designs and comparison** in a text file or Markdown file (e.g., `data_modeling_comparison.md`).

\<details\>
\<summary\>\<b\>Solution for Daily Task: Explore Data Modeling Differences\</b\>\</summary\>

**Example `data_modeling_comparison.md` Content:**

````markdown
# Data Modeling Comparison: E-commerce Order

Comparing relational and document database design for a simple e-commerce order.

**Scenario:** Representing an order with Order ID, Customer, Order Date, and multiple Order Items (each item has Product details, Quantity, and potentially Options).

---

**Relational Database Design:**

We would likely need the following tables:

1.  **`Customers` Table:**
    - `customer_id` (Primary Key)
    - `name`
    - `email`
    - ... other customer details ...

2.  **`Orders` Table:**
    - `order_id` (Primary Key)
    - `customer_id` (Foreign Key to `Customers`)
    - `order_date`
    - `total_amount`
    - ... other order details (e.g., shipping address) ...

3.  **`Products` Table:**
    - `product_id` (Primary Key)
    - `name`
    - `current_price`
    - ... other product details ...

4.  **`OrderItems` Table:**
    - `order_item_id` (Primary Key)
    - `order_id` (Foreign Key to `Orders`)
    - `product_id` (Foreign Key to `Products`)
    - `quantity`
    - `purchased_price` (Crucial to store the price at the time of order)
    - ... fields for selected options (e.g., `size`, `color` - or a separate `OrderItemOptions` table linked by `order_item_id`) ...

**Relationships:**

- One Customer can have many Orders (One-to-Many: `Customers` to `Orders`).
- One Order can have many Order Items (One-to-Many: `Orders` to `OrderItems`).
- One Product can be in many Order Items (Many-to-Many conceptualized via `OrderItems` acting as the junction table).

---

**MongoDB Document Database Design:**

In MongoDB, we could store each order as a single document in an `orders` collection. A common pattern for Order Items is to **embed** them directly within the order document, capturing the state at the time of purchase.

**`orders` Collection Document Structure (Embedding):**

```json
{
  "_id": ObjectId("..."),         // MongoDB generated unique ID
  "order_id": "ORD12345",        // A business-level order ID
  "customer_id": ObjectId("..."),  // Reference to a customer document (if needed)
  "customer_details": {          // Or embed essential customer details for quick access
    "name": "John Doe",
    "email": "john@example.com"
  },
  "order_date": ISODate("2025-04-21T12:00:00Z"),
  "items": [                     // Array of embedded documents for each item
    {
      "product_id": ObjectId("..."), // Reference to a product document (if needed)
      "sku": "LAP-101",          // Embed product details at the time of purchase
      "name": "Laptop",
      "price_at_purchase": 1200.50,
      "quantity": 1,
      "options": {               // Embedded document for selected options
        "color": "Silver",
        "warranty": "3 years"
      }
    },
    {
      "product_id": ObjectId("..."),
      "sku": "MSE-205",
      "name": "Mouse",
      "price_at_purchase": 25.00,
      "quantity": 2,
      "options": {
        "color": "Black"
      }
    }
    // ... more items ...
  ],
  "total_amount": 1250.50,
  "status": "Completed",
  "shipping_address": { ... }
  // ... other order details ...
}
````

In this embedded approach, accessing a complete order with all its items is a single read operation on the `orders` collection. We embed product details like `name` and `price_at_purchase` because these should reflect the values at the time the order was placed, even if the product's current details change later.

-----

**Comparison and Contrast:**

**Relational Database Design Pros:**

  * **Data Integrity:** Strong consistency and adherence to schema rules and relationships.
  * **Reduced Duplication:** Customer and Product details are stored only once in their respective tables.
  * **Querying:** SQL is powerful for complex joins and aggregations across multiple tables.
  * **Transactions:** ACID compliance ensures data consistency for multi-step operations.

**Relational Database Design Cons:**

  * **Query Complexity:** Retrieving a complete order with all items requires joining multiple tables (`Orders`, `OrderItems`, `Products`, `Customers`).
  * **Schema Rigidity:** Adding new item options might require schema alterations or additional tables.

**MongoDB Document Database Design (Embedding) Pros:**

  * **Read Performance:** Retrieving a complete order with all its items is very fast (single document read).
  * **Flexibility:** Easily add different options to different order items without schema changes.
  * **Scalability:** Designed for horizontal scaling to handle high write/read volumes of orders.
  * **Natural Mapping:** Document structure often maps well to objects in application code.

**MongoDB Document Database Design (Embedding) Cons:**

  * **Data Duplication:** Product details (`name`, `price`, etc.) are duplicated across potentially many order documents. Updates to core product details do *not* automatically propagate to historical orders (though this is often desired for historical accuracy).
  * **Querying Embedded Data:** Querying or aggregating based on embedded fields (like finding all orders containing a specific product name) can be less straightforward or performant than joins in relational databases, sometimes requiring aggregation pipelines (`$match`, `$unwind`, `$group`, etc.).
  * **Document Size Limits:** MongoDB has a limit on the maximum document size (currently 16MB), which could be a concern if orders have an extremely large number of items (though usually not an issue for typical orders).

**Conclusion for this Scenario:**

The embedded MongoDB approach is highly effective for the primary use case of quickly retrieving complete order details for display. It offers flexibility for variable item options and scales well for high order volume. The relational approach is stronger for data integrity and complex analytical queries across products, customers, and orders. For this specific scenario focusing on order details retrieval, the embedded MongoDB design is often a strong choice, accepting the trade-offs in data duplication for read performance and flexibility. A production system might use a combination of embedding (for order items) and referencing (for customer and product IDs) depending on access patterns and consistency needs.

```
</details>

---

## Final Wrap-up for Day 4 of Week 7

- **Summary of Key Learnings:** Today, you've successfully stepped into the world of NoSQL databases by learning the fundamental concepts of MongoDB. You understand how it differs from relational databases, its key benefits, and its basic architecture (databases, collections, documents). You've gained practical experience using the MongoDB shell to perform the essential CRUD operations (insert, find, update, delete) and learned how to connect to MongoDB and perform CRUD using the `pymongo` Python driver. You were also introduced to important best practices like indexing and critical schema design considerations like embedding versus referencing, understanding the trade-offs involved.
- **Next Steps:** This foundational understanding of MongoDB is crucial for working with NoSQL data. Tomorrow, we will bring together what we've learned about Django (models, views, DRF) and MongoDB. We'll discuss strategies for integrating MongoDB into our Django application using the `pymongo` driver to store and retrieve data from MongoDB collections within our Django views and potentially expose that data via a DRF API, demonstrating how to work with different database technologies in a single project.

*End of Week 7, Day 4 Study Material & Notes*

---