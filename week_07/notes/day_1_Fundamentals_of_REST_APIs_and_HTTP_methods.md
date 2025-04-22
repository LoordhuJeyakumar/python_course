# Week 7, Day 1: Understanding the Backbone of Modern Web - REST APIs and HTTP Methods

## Overview

Over the past few weeks, we've focused on building traditional web applications where Django renders HTML pages for the user's browser. Now, we're shifting gears to explore a different paradigm: building **REST APIs**. REST APIs are the standard way for different software systems to communicate with each other over the internet. Understanding REST and the underlying HTTP methods is fundamental to building modern web services, mobile application backends, and applications that interact with third-party services. By the end of this lesson, you will be able to:

  - Understand the concept of Application Programming Interfaces (APIs) and their role in software communication.
  - Define what a REST API is and describe the key principles and constraints of RESTful architecture.
  - Identify the benefits of using REST APIs for building scalable, flexible, and interoperable systems.
  - Understand the fundamental HTTP methods (GET, POST, PUT, PATCH, DELETE) and their conventions within the context of REST APIs, including their idempotency and safety characteristics.
  - Interpret common HTTP status codes used in API responses to understand the outcome of a request.
  - Grasp the core design principles of REST APIs, including resources, endpoints, and representations.
  - Recognize JSON as the prevalent data format for REST API requests and responses and understand its structure.
  - Understand the importance of API documentation and have a brief introduction to tools like OpenAPI/Swagger.
  - Design simple REST API endpoints and understand how HTTP methods map to CRUD operations.

> **Project-Based Note:**
> While our blog project initially focused on rendering HTML, we will soon learn how to expose our blog data (posts, authors, comments) as a REST API. This will allow other applications (like a mobile app or a separate front-end framework like React or Vue.js) to interact with our blog's content programmatically. This is a crucial step towards building full-stack applications where the backend (Django API) and the frontend (built with another technology) are decoupled.

-----

## Lesson Plan

### 1\. Recap of Previous Weeks (Relevant Concepts)

  - **Brief Review:** We've built web applications where the server sends HTML responses to the browser, handling the HTTP request/response cycle (Week 4). We also learned about HTTP methods GET and POST when handling forms (Week 6). Today, the "response" will often be data (like JSON) instead of HTML, consumed by another application rather than a human user's browser rendering a webpage. We'll revisit and expand on HTTP methods and status codes in the context of APIs. We've built and deployed full-stack Django apps and handled forms and validations in prior lessons, which provides a foundation for building the backend of an API.

### 2\. Introduction to APIs (Application Programming Interfaces)

  - **What is an API?**
      - An API is a set of rules, protocols, and tools that allows different software applications to communicate with each other.
      - Think of it as a contract or an agreement between two pieces of software, defining how they can interact and exchange information.
      - APIs abstract away the complexity of one system, allowing another system to use its functionality without needing to know the internal details of how it works.
  - **Real-World Analogy:**
      - Imagine a restaurant. The waiter is the API. You (the client) tell the waiter what you want to order (make a request). The waiter takes your order to the kitchen (the system providing the service). The kitchen prepares the food and gives it back to the waiter (the response). The waiter delivers the food to you. You don't need to know how the kitchen works, just how to communicate with the waiter.
  - **Examples of APIs in Use:**
      - Weather apps, social media logins (Google, Facebook APIs), payment gateways (Stripe, PayPal APIs), mapping services (Google Maps API), and many more.

### 3\. What are REST APIs? - Principles of RESTful Architecture

  - **REST:** Stands for **Re**presentational **S**tate **T**ransfer. It's an architectural style and a set of constraints for designing networked applications. APIs that adhere to the principles of REST are called RESTful APIs.
  - **Key Principles/Constraints of RESTful Architecture:**
      - **Client-Server:** Separation of concerns between the client (requesting information) and the server (providing information). They communicate over a network, allowing for independent development and scaling.
      - **Stateless:** Each request from a client to the server must contain all the information needed to understand and process the request. The server does not store any client context or state between requests. This improves scalability, reliability, and visibility.
      - **Cacheable:** Responses from the server can be cached by clients or intermediaries to improve performance. Responses must implicitly or explicitly label themselves as cacheable or non-cacheable.
      - **Uniform Interface:** This is the most important principle, simplifying the overall system architecture through standardization. Key aspects include:
          * **Identification of Resources:** Resources are uniquely identified (e.g., using URLs).
          * **Manipulation of Resources through Representations:** Clients interact with resources by exchanging representations of the resource's state.
          * **Self-descriptive Messages:** Messages include enough information to describe how to process them.
          * **Hypermedia as the Engine of Application State (HATEOAS) (Optional):** Resources can include links to related resources to guide the client on possible next actions.
      - **Layered System:** Clients cannot ordinarily tell whether they are connected directly to the end server, or to an intermediary like a proxy or load balancer. This allows for adding layers (like security or caching) without affecting clients.
      - **Code on Demand (Optional):** Servers can temporarily extend or customize client functionality by transferring executable code (e.g., JavaScript).

### 4\. Benefits of REST APIs

  - **Scalability:** The stateless nature of RESTful APIs makes horizontal scaling easier.
  - **Flexibility:** Decoupling client and server allows different technologies on both ends.
  - **Interoperability:** Based on standard web technologies (HTTP, URLs, JSON/XML).
  - **Ease of Use:** Generally simpler than other styles like SOAP.
  - **Performance:** Caching can improve performance.
  - **Language-Agnostic:** Can be built and consumed using any programming language.

### 5\. Understanding HTTP Methods in REST APIs (GET, POST, PUT, PATCH, DELETE - In Detail)

HTTP methods indicate the desired action to be performed on a resource. RESTful APIs use HTTP methods according to specific conventions to perform CRUD operations on resources.

| CRUD Operation | HTTP Verb | Endpoint Example           | Description                                       | Idempotent? | Safe? |
| :------------- | :-------- | :------------------------- | :------------------------------------------------ | :---------- | :---- |
| Create         | POST      | `/api/books/`              | Create a new book resource                        | No          | No    |
| Read (List)    | GET       | `/api/books/`              | Retrieve a list of books                          | Yes         | Yes   |
| Read (Detail)  | GET       | `/api/books/{id}/`         | Retrieve details of book `{id}`                   | Yes         | Yes   |
| Update (Full)  | PUT       | `/api/books/{id}/`         | Replace book `{id}` entirely                      | Yes         | No    |
| Update (Partial)| PATCH     | `/api/books/{id}/`         | Modify one or more fields of book `{id}`          | Yes         | No    |
| Delete         | DELETE    | `/api/books/{id}/`         | Remove book `{id}`                                | Yes         | No    |

  - **Idempotency:** An operation is idempotent if calling it multiple times has the same effect on the server's state as calling it once (assuming no external factors). GET, PUT, PATCH, and DELETE are generally idempotent. POST is generally not.
  - **Safety:** A safe operation does not change the state of the server. GET and HEAD are considered safe. POST, PUT, PATCH, and DELETE are not.
  - **Request Body:** POST, PUT, and PATCH requests typically include a request body containing the data to be sent to the server (e.g., JSON). GET and DELETE requests typically do not.

### 6\. HTTP Status Codes for REST APIs

HTTP status codes are three-digit numbers returned by the server, indicating the outcome of the client's request.

  - **2xx (Success):** The action was successfully received, understood, and accepted.
      - `200 OK`: The request was successful. (Common for successful GET, PUT, PATCH, DELETE).
      - `201 Created`: The request has been fulfilled and resulted in a new resource being created. (Common for successful POST). Includes `Location` header.
      - `204 No Content`: The server successfully processed the request, but is not returning any content. (Common for successful DELETE).
  - **4xx (Client Error):** The request contains bad syntax or cannot be fulfilled.
      - `400 Bad Request`: The server cannot process the request due to client error (e.g., malformed syntax, invalid data).
      - `401 Unauthorized`: Authentication is required and has failed or has not yet been provided.
      - `403 Forbidden`: The server understood the request but refuses to authorize it (authenticated but no permission).
      - `404 Not Found`: The server cannot find the requested resource.
      - `405 Method Not Allowed`: The HTTP method used is not allowed for the resource.
      - `409 Conflict`: Request conflicts with the current state of the resource (e.g., duplicate entry).
      - `422 Unprocessable Entity`: Server understands the request but cannot process it due to semantic errors (often used for validation errors in API data).
  - **5xx (Server Error):** The server failed to fulfill an apparently valid request.
      - `500 Internal Server Error`: Generic server error.
      - `503 Service Unavailable`: Server is not ready to handle the request (maintenance, overload).

### 7\. REST API Design Principles: Resources, Endpoints, Representations

  - **Resources:** The key abstractions in a REST API. Resources are typically nouns representing objects or concepts (e.g., a `book`, a `user`, an `order`).
  - **Endpoints:** The URLs used to identify and access resources. Endpoints should be resource-oriented (use nouns, not verbs in the URL path).
      - Examples: `/api/v1/posts`, `/api/v1/users/{id}`, `/api/v1/products/{id}/reviews`.
  - **Representations:** How the state of a resource is transferred between client and server. Common formats are JSON and XML.

### 8\. Request and Response Formats: JSON and XML (Focus on JSON)

  - **JSON (JavaScript Object Notation):**
      - Lightweight, human-readable, easy to parse.
      - Based on a subset of JavaScript, but language-independent.
      - The de facto standard for REST API data exchange.
      - **Example JSON Representation of a Blog Post:**
        ```json
        {
          "id": 123,
          "title": "Learning REST APIs",
          "slug": "learning-rest-apis",
          "content": "Today we learned about REST principles...",
          "publish_date": "2025-04-21T10:00:00Z",
          "author": {
            "id": 1,
            "name": "Alice Smith"
          },
          "categories": [
            {"id": 1, "name": "Technology"},
            {"id": 2, "name": "Web Development"}
          ]
        }
        ```
  - **XML (Extensible Markup Language):**
      - More verbose than JSON.
      - Supports schemas and namespaces.
      - Less common than JSON for new REST APIs but still used in some contexts (especially legacy systems or document-centric APIs).

### 9\. REST API Design Best Practices

  - **Resource-oriented URLs:** Use nouns (e.g., `/api/orders/`), avoid verbs in the path.
  - **Versioning:** Include version in the URL (`/api/v1/...`) or via headers to manage API evolution without breaking existing clients.
  - **Filtering, Sorting & Pagination:** Support these via query parameters (`?page=2&sort=-created_at&status=active`) for flexibility in retrieving data collections.
  - **Consistent Error Responses:** Return structured data (e.g., JSON object) for errors, including details like `code`, `message`, and optional `details` for specific validation errors.
  - **HATEOAS (Optional):** Embed hyperlinks to related resources in responses for discoverability, allowing clients to navigate the API without hardcoding URLs.

### 10\. Introduction to API Documentation (Swagger/OpenAPI - Brief Overview)

  - **Importance of Documentation:** Essential for developers using your API. Describes endpoints, methods, parameters, request/response formats, authentication, and errors.
  - **OpenAPI Specification (OAS):** A standardized, language-agnostic format (YAML or JSON) for describing REST APIs.
  - **Swagger:** A set of tools (Swagger UI for interactive docs, Swagger Editor) based on the OpenAPI Specification.
  - **Benefits:** Interactive documentation, client code generation, clear API contracts for teams.

-----

## Detailed Study Materials & Notes (Expanded Concepts)

  - **More Analogies for APIs:** Compare to electrical outlets, standard plugs allow different devices to use power without knowing the power plant's internal workings.
  - **REST Constraints Detailed:** Explain each constraint in more depth, discussing the reasoning and benefits (e.g., why statelessness aids scalability, how a uniform interface simplifies interaction).
  - **HTTP Methods Idempotency/Safety Technicality:** Reiterate that idempotency means `f(x) = f(f(x))`. Safety means no state change. Explain how these characteristics guide API design and client implementation.
  - **HTTP Status Codes Comprehensive List:** Provide a broader list including less common but still relevant codes. Discuss how to choose the most appropriate status code for various scenarios.
  - **Error Response Structure:** Show a common JSON structure for API error responses to provide consistent feedback to clients.
  - **Naming Conventions:** Provide more examples of good and bad endpoint design. Discuss singular vs. plural nouns for collections vs. specific resources.
  - **JSON Structure:** Revisit JSON structure with examples of nested objects and arrays. Discuss best practices for representing data in JSON for APIs.
  - **API Documentation Tools:** Briefly mention other popular tools like Postman documentation, RAML, API Blueprint. Discuss automatic generation from code or manual definition.

-----

## Practical Exercises with Solutions

### Exercise 1: Identifying Resources and Endpoints

1.  **Scenario:** Imagine you are interacting with a public API for managing books and authors (like a simplified Goodreads API).
2.  **Task:** Based on the following hypothetical endpoint URLs, identify the resources being accessed or manipulated:
      * `/api/books/`
      * `/api/books/456/`
      * `/api/authors/`
      * `/api/authors/123/books/`
      * `/api/genres/`
      * `/api/books/456/reviews/`

<details>
  <summary\><b>Solution for Exercise 1</b></summary>

  * `/api/books/`: The collection of **Books**.
  * `/api/books/456/`: A specific **Book** resource (the one with ID 456).
  * `/api/authors/`: The collection of **Authors**.
  * `/api/authors/123/books/`: The collection of **Books** resource belonging to the Author with ID 123. This is a sub-resource.
  * `/api/genres/`: The collection of **Genres**.
  * `/api/books/456/reviews/`: The collection of **Reviews** resource belonging to the Book with ID 456. This is a sub-resource.

</details>

### Exercise 2: Matching HTTP Methods to Actions

1.  **Scenario:** You are designing the API endpoints for a simple task management application.
2.  **Task:** Match the following actions to the most appropriate standard HTTP method in a RESTful API context:
      * Get a list of all tasks.
      * Create a new task.
      * Update the details of a specific task.
      * Delete a specific task.
      * Get the details of a specific task.
      * Mark a task as completed (partial update).

\<details\>
\<summary\>\<b\>Solution for Exercise 2\</b\>\</summary\>

  * Get a list of all tasks: **GET** (`/tasks/`)
  * Create a new task: **POST** (`/tasks/`)
  * Update the details of a specific task: **PUT** (`/tasks/{id}/`) - For a full replacement.
  * Delete a specific task: **DELETE** (`/tasks/{id}/`)
  * Get the details of a specific task: **GET** (`/tasks/{id}/`)
  * Mark a task as completed (partial update): **PATCH** (`/tasks/{id}/`) - More specific for partial updates than PUT.

\</details\>

### Exercise 3: Interpreting HTTP Status Codes

1.  **Scenario:** You are making requests to a REST API and receive different HTTP status codes in the responses.
2.  **Task:** Explain what each of the following status codes likely indicates about the outcome of your API request:
      * `200 OK`
      * `201 Created`
      * `204 No Content`
      * `400 Bad Request`
      * `401 Unauthorized`
      * `403 Forbidden`
      * `404 Not Found`
      * `405 Method Not Allowed`
      * `500 Internal Server Error`
      * `422 Unprocessable Entity`

\<details\>
\<summary\>\<b\>Solution for Exercise 3\</b\>\</summary\>

  * `200 OK`: The request was successful.
  * `201 Created`: A new resource was successfully created (usually in response to a POST request).
  * `204 No Content`: The request was successful, but there is no content to return (often used for successful DELETE or PUT operations that don't return data).
  * `400 Bad Request`: The client sent a request that the server could not understand or process due to incorrect syntax or invalid data (e.g., missing required fields in a request body).
  * `401 Unauthorized`: The client needs to authenticate to access the resource, but authentication failed or was not provided.
  * `403 Forbidden`: The client is authenticated, but they do not have permission to access the requested resource or perform the requested action.
  * `404 Not Found`: The server could not find the resource at the requested URL.
  * `405 Method Not Allowed`: The HTTP method used in the request (e.g., PUT) is not allowed for the requested resource (e.g., trying to PUT to a collection endpoint that only supports POST).
  * `500 Internal Server Error`: Something went wrong on the server side while processing the request. This is a generic server-side error.
  * `422 Unprocessable Entity`: The server understands the request but cannot process it due to semantic errors within the data provided (often used for validation errors in API data).

\</details\>

### Exercise 4: Design CRUD Endpoints for a “User” Resource

1.  **Task:** Write the HTTP method and URL for each standard CRUD operation on a "User" resource, assuming your API endpoints start with `/api/v1/`.
2.  **Task:** For each endpoint, briefly describe the expected action.

\<details\>
\<summary\>\<b\>Solution for Exercise 4\</b\>\</summary\>

  * **Create User:** `POST /api/v1/users/` - Creates a new user resource with data provided in the request body.
  * **List Users:** `GET /api/v1/users/` - Retrieves a list of all user resources.
  * **Get User (Detail):** `GET /api/v1/users/{user_id}/` - Retrieves the details of the user resource with the specified `user_id`.
  * **Update User (Full):** `PUT /api/v1/users/{user_id}/` - Replaces the entire user resource with the specified `user_id` with the data provided in the request body.
  * **Update User (Partial):** `PATCH /api/v1/users/{user_id}/` - Applies partial updates to the user resource with the specified `user_id` using data provided in the request body.
  * **Delete User:** `DELETE /api/v1/users/{user_id}/` - Removes the user resource with the specified `user_id`.

\</details\>

### Exercise 5: Draft a Minimal OpenAPI Definition Snippet

1.  **Task:** Create a minimal OpenAPI (YAML format) snippet that documents the `GET /api/v1/users/{id}/` endpoint, including parameters and a basic 200 OK response with a simple User schema.

\<details\>
\<summary\>\<b\>Solution for Exercise 5\</b\>\</summary\>

```yaml
openapi: 3.0.0
info:
  title: User API Example
  version: '1.0'
paths:
  /api/v1/users/{id}/:
    get:
      summary: Retrieve a single user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
          description: The ID of the user to retrieve.
      responses:
        '200':
          description: A user object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found
components:
  schemas:
    User:
      type: object
      properties:
        id:
          type: integer
          description: The unique identifier for the user.
        username:
          type: string
          description: The user's username.
        email:
          type: string
          format: email
          description: The user's email address.
```

\</details\>

-----

## Detailed Daily Task

**Option 1: Analyze a Public API's Endpoints and Methods**

1.  **Scenario:** Choose a public API that you can access (examples: JSONPlaceholder - a fake online REST API for testing and prototyping, or explore APIs from services like GitHub, Twitter, or a weather service if you have access/keys).
2.  **Instructions:**
      - **Visit the documentation page** for the public API you chose.
      - **Identify at least 5 different endpoints** (URLs) that the API provides.
      - For each identified endpoint, determine which **HTTP methods** (GET, POST, PUT, DELETE, etc.) are supported for that endpoint.
      - For each method, try to understand what action that method performs on the resource at that endpoint (e.g., GET `/users` retrieves all users).
      - Note down the likely **resource(s)** represented by each endpoint.
3.  **Write down your findings** in a text file or Markdown file (e.g., `api_analysis.md`), listing the endpoints, supported methods, the actions they perform, and the resources they represent.

\<details\>
\<summary\>\<b\>Solution for Daily Task (Option 1 - Example based on JSONPlaceholder)\</b\>\</summary\>

**Example `api_analysis.md` Content (Based on JSONPlaceholder):**

```markdown
# Public API Analysis - JSONPlaceholder

Analyzing the JSONPlaceholder API (https://jsonplaceholder.typicode.com/guide/)

**Endpoint 1:** `/posts`
- **Supported Methods:** GET, POST
- **Action (GET):** Retrieve a list of all posts.
- **Action (POST):** Create a new post.
- **Resource:** Collection of Posts.

**Endpoint 2:** `/posts/{id}` (e.g., `/posts/1`)
- **Supported Methods:** GET, PUT, PATCH, DELETE
- **Action (GET):** Retrieve details of a specific post.
- **Action (PUT):** Update all fields of a specific post.
- **Action (PATCH):** Update some fields of a specific post.
- **Action (DELETE):** Delete a specific post.
- **Resource:** A specific Post.

**Endpoint 3:** `/users`
- **Supported Methods:** GET
- **Action (GET):** Retrieve a list of all users.
- **Resource:** Collection of Users.

**Endpoint 4:** `/users/{id}/posts` (e.g., `/users/1/posts`)
- **Supported Methods:** GET
- **Action (GET):** Retrieve a list of posts written by a specific user.
- **Resource:** Collection of Posts belonging to a specific User (Sub-resource).

**Endpoint 5:** `/comments`
- **Supported Methods:** GET, POST
- **Action (GET):** Retrieve a list of all comments.
- **Action (POST):** Create a new comment.
- **Resource:** Collection of Comments.
```

**To Complete This Task:**

1.  Visit the documentation for your chosen API (e.g., [https://jsonplaceholder.typicode.com/guide/](https://www.google.com/search?q=https://jsonplaceholder.jsonplaceholder.typicode.com/guide/)).
2.  Read the documentation to find different URL endpoints.
3.  For each endpoint, look for which HTTP methods (GET, POST, PUT, DELETE, etc.) are listed as supported.
4.  Based on the method and the endpoint URL, infer or find in the documentation what action is performed (e.g., "GET /users/ will list all users").
5.  Identify what resource(s) (Users, Posts, Orders, etc.) the endpoint relates to.
6.  Record your findings in your analysis file.

\</details\>

**Option 2: Plan and Document a "Post" API**

1.  **Scenario:** Plan the core API endpoints for a simple blogging platform where you need to manage blog posts.
2.  **Instructions:**
      - **Define the structure/schema** of a "Post" resource (e.g., what fields it would have: title, body, author\_id, creation date). You can represent this as a JSON object.
      - **Design the API endpoints and specify the HTTP methods** for the standard CRUD operations (Create, Read List, Read Detail, Update Full, Update Partial, Delete) for the "Post" resource. Assume your API endpoints are versioned, starting with `/api/v1/`.
      - **Specify the appropriate HTTP status codes** you would expect for successful responses for each method (e.g., 200, 201, 204) and common client errors (e.g., 400, 404).
      - **Draft a minimal OpenAPI (YAML) snippet** that documents the `POST /api/v1/posts/` endpoint, including the expected request body schema (referencing a component schema) and the expected successful response status code (201 Created). Include the definition for the `PostInput` schema.
3.  **Document your plan** in a Markdown file (`daily_task.md`), including the resource schema, endpoint designs, status codes, and the OpenAPI snippet.

\<details\>
\<summary\>\<b\>Solution for Daily Task (Option 2 - Plan and Document a "Post" API)\</b\>\</summary\>

````markdown
# Daily Task: Planning and Documenting a "Post" API

Planning the core API endpoints for managing blog posts.

1. **"Post" Resource Schema (Example JSON):**
```json
{
  "id": 1,
  "title": "My First API Post",
  "body": "This is the content of my first API post.",
  "author_id": 42,
  "created_at": "2025-04-21T10:00:00Z"
}
````

2.  **API Endpoints and HTTP Methods (Versioning: /api/v1/):**

<!-- end list -->

  - **Create Post:** `POST /api/v1/posts/`
  - **List Posts:** `GET /api/v1/posts/`
  - **Retrieve Post (Detail):** `GET /api/v1/posts/{id}/`
  - **Update Post (Full):** `PUT /api/v1/posts/{id}/`
  - **Update Post (Partial):** `PATCH /api/v1/posts/{id}/`
  - **Delete Post:** `DELETE /api/v1/posts/{id}/`

<!-- end list -->

3.  **Expected HTTP Status Codes:**

<!-- end list -->

  - **Successful Responses:**
      - `GET`: 200 OK
      - `POST`: 201 Created
      - `PUT`/`PATCH`: 200 OK or 204 No Content (if no body returned)
      - `DELETE`: 200 OK or 204 No Content (if no body returned)
  - **Common Client Errors:**
      - 400 Bad Request (e.g., invalid request body format)
      - 404 Not Found (e.g., trying to access a post that doesn't exist)
      - 401 Unauthorized (if authentication is required)
      - 403 Forbidden (if authenticated but no permission)
      - 405 Method Not Allowed (e.g., trying to POST to `/posts/{id}/`)
      - 422 Unprocessable Entity (if validation fails on the provided data)

<!-- end list -->

4.  **Minimal OpenAPI Snippet for POST /api/v1/posts/ (YAML):**

<!-- end list -->

```yaml
/api/v1/posts/:
  post:
    summary: Create a new post
    description: Creates a new blog post resource.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/PostInput'
    responses:
      '201':
        description: Post created successfully
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Post' # Assuming a Post schema exists
      '400':
        description: Bad Request - Invalid input
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                errors:
                  type: object # Details about validation errors
components:
  schemas:
    PostInput:
      type: object
      required:
        - title
        - body
        - author_id
      properties:
        title:
          type: string
          description: The title of the blog post.
          example: "Introduction to REST APIs"
        body:
          type: string
          description: The main content of the blog post (can be Markdown or HTML).
          example: "This post explains the basics of REST..."
        author_id:
          type: integer
          description: The ID of the author creating the post.
          example: 1
```

```markdown
# Note: A full OpenAPI document would include the base 'info' section,
# potentially security schemes, and definitions for all schemas like 'Post'.
```

\</details\>

-----

## Final Wrap-up for Day 1 of Week 7

  - **Summary of Key Learnings:** Today, you've been introduced to the fundamental concepts of REST APIs and the crucial role of HTTP methods and status codes in API communication. You now understand how APIs enable different software systems to interact and the basic principles that guide the design of RESTful services, including resources, endpoints, representations, and key design best practices like versioning and consistent error handling.
  - **Next Steps:** This foundational knowledge is crucial for building APIs with Django. Tomorrow, we will start putting this knowledge into practice by introducing the **Django REST Framework (DRF)**. We'll learn how to set up DRF in our Django project and how to use **serializers** to convert our Django models into formats suitable for API responses (like JSON) and to handle incoming data.

*End of Week 7, Day 1 Study Material & Notes*

-----
