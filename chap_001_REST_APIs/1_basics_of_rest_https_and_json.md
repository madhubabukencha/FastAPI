## Basics of REST APIs, HTTP Protocol, and JSON Encoding
FAST API is commonly used to build RESTful APIs, but it's not limited to just REST.
It provides tools and features that make implementing REST principles easier and 
more efficient.

**Key Relationships between REST API and FAST API**
- **REST Implementation**: FAST API makes it simple to create REST-compliant endpoints
  with proper HTTP methods (GET, POST, PUT, DELETE)

- **Beyond REST**: FAST API also supports other paradigms like:
  - WebSockets (for real-time communication)
  - GraphQL (through extensions)
  - RPC-style APIs

- **Enhanced Features**: While adhering to REST principles, FAST API adds:
  - Automatic data validation
  - Automatic documentation (OpenAPI/Swagger)
  - Async support
  - Dependency injection

So, in this document you will understand about:
- What is REST APIs
- HTTP Protocol
- JSON Encoding
### What is REST API?
- REST API stands for Representation State Transfer Application Programming Interface
- FAST API is a modern Python web framework for building APIs, while REST is an architectural style
- REST API performs actions like Create, Retrieve, Update and Delete. These operations also know as CRUD.
- REST API usually goes through the HTTP transport layer and it uses JSON as encoding.
- CRUD and HTTP verbs
    |  CRUD   | HTTP  |
    |---------|-------|
    | Create  | POST  |
    | Retrieve| GET   |
    | Update  | PUT/PATCH|
    | Delete  | DELETE|
- Basic GET implementation in Python. Below API request tells you a Joke
  ```python
  import requests
  
  data = requests.get("https://official-joke-api.appspot.com/random_joke", 
                       headers={"Authorization": "",
                                "Content-Type": "application/json",
                                "Accept": "application/json"})
  print(data.json())
  ```
- **Important Headers**
  - `Authorization`: For authentication (often with Bearer tokens or API keys)
  - `Content-Type`: Specifies the media type of the data you're sending to the server. Some example are, `Content-Type: application/json`, `Content-Type: application/xml`, and `Content-Type: multipart/form-data` (for file uploads)
  - `Accept`: Specifies the media types the client can understand in the server's response. Some examples are, `Accept: application/json` (requests JSON response), `Accept: application/xml`, `Accept: text/html`.
  
### What is HTTP Protocol?
- HTTP (HyperText Transfer Protocol) is the foundation
  of communication on the web. It allows your browser (client) to request data (like web pages, images, etc.) from a server, and the server responds with the requested information
-  Each request is independent (the server doesn’t remember past requests).
- GET (fetch data) and POST (send data)
- Like 200 (OK), 404 (Not Found), 500 (Server Error).

### JSON Encoding
- JSON stands for JavaScript Object Notation
- REST API uses for JSON messages for communication

