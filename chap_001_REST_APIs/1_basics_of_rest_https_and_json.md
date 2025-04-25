## Basics of REST APIs and other Important Topics
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
### What is a Request?
In the context of FastAPI and web development, a Request is an object that represents an incoming HTTP request from a client (e.g., a browser, mobile app, or another service). It contains all the details of the request, such as:
  - **Headers** (e.g., authentication tokens, content type)
  - **HTTP Method** (e.g., GET, POST, PUT, DELETE)
  - URL Path and query parameters
  - **Body** (for methods like POST or PUT)
  - Cookies
  - Client information (e.g., IP address)

### Important Headers
  - `Authorization`: For authentication (often with Bearer tokens or API keys)
  - `Content-Type`: Specifies the media type of the data you're sending to the server. Some example are, `Content-Type: application/json`, `Content-Type: application/xml`, and `Content-Type: multipart/form-data` (for file uploads)
  - `Accept`: Specifies the media types the client can understand in the server's response. Some examples are, `Accept: application/json` (requests JSON response), `Accept: application/xml`, `Accept: text/html`.
  - `Content-Length`: The Content-Length in an API (or HTTP) response or request is an HTTP header that indicates the size of the message body in bytes. It helps the client or server know how much data to expect when transmitting or receiving information
  
### What is HTTP Protocol?
- HTTP (HyperText Transfer Protocol) is the foundation
  of communication on the web. It allows your browser (client) to request data (like web pages, images, etc.) from a server, and the server responds with the requested information
-  Each request is independent (the server doesn’t remember past requests).
- GET (fetch data) and POST (send data)
- Like 200 (OK), 404 (Not Found), 500 (Server Error).

### JSON Encoding
- JSON stands for JavaScript Object Notation
- REST API uses for JSON messages for communication
