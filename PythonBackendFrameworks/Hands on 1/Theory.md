# Python Backend Frameworks

# Hands-On 1

## Web Framework Foundations & Django Project Setup

**Name:** Indu

**Technology:** Django

---

# Task 1

## 1. Request–Response Cycle

### Definition

The Request–Response Cycle is the process by which a web application receives an HTTP request from a client, processes it, and sends back an HTTP response.

### Flow

```text
Browser
   ↓
URL Router (urls.py)
   ↓
Middleware
   ↓
View (views.py)
   ↓
Model (models.py)
   ↓
Database
   ↓
Model
   ↓
View
   ↓
Middleware
   ↓
HTTP Response
   ↓
Browser
```

### Explanation

1. The browser sends an HTTP request.
2. The URL router matches the requested URL to the appropriate view.
3. Middleware processes the request before it reaches the view.
4. The view contains the business logic.
5. If data is required, the model communicates with the database.
6. The model returns the requested data to the view.
7. The view prepares an HTTP response.
8. Middleware processes the response before it is sent back.
9. The browser receives and displays the response.

---

## 2. Middleware

### Definition

Middleware is software that processes requests before they reach the Django view and processes responses before they are returned to the client.

### Built-in Middleware Examples

#### SessionMiddleware

- Maintains user session data.
- Allows users to remain logged in across multiple requests.

#### AuthenticationMiddleware

- Identifies the currently logged-in user.
- Provides authentication and user information during request processing.

---

## 3. WSGI vs ASGI

| WSGI | ASGI |
|------|------|
| Web Server Gateway Interface | Asynchronous Server Gateway Interface |
| Supports synchronous requests only | Supports both synchronous and asynchronous requests |
| Suitable for traditional web applications | Suitable for real-time and asynchronous applications |
| Default interface used by Django | Used when async features such as WebSockets are required |

### Django Default

Django uses **WSGI** by default.

### When to Use ASGI

- Chat applications
- WebSockets
- Live notifications
- Streaming applications
- Real-time dashboards

---

## 4. MVC vs MVT

### MVC Architecture

- **Model** – Manages application data and database operations.
- **View** – Displays the user interface.
- **Controller** – Handles business logic and user requests.

### Django MVT Architecture

- **Model** – Handles data and database operations.
- **View** – Contains business logic and processes requests.
- **Template** – Displays the user interface.

### MVC to MVT Mapping

| MVC | Django MVT |
|------|------------|
| Model | Model |
| View | Template |
| Controller | View |

---

## Conclusion

In this task, the basic concepts of the Django web framework were studied, including the Request–Response Cycle, Middleware, WSGI vs ASGI, and the MVC to MVT architecture. These concepts form the foundation for developing Django web applications.