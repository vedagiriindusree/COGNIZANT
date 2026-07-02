# Hands-On 1

## Python Backend Frameworks

### Topic

Web Framework Foundations & Django Project Setup

---

## Objective

To understand the fundamentals of Django and create a basic Django project with a reusable application.

---

## Software Used

- Python 3.x
- Django
- Visual Studio Code

---

## Project Structure

```
coursemanager/
│
├── manage.py
├── coursemanager/
└── courses/
```

---

## Steps Performed

1. Created a virtual environment.
2. Installed Django.
3. Created a Django project named `coursemanager`.
4. Created a Django app named `courses`.
5. Registered the app in `INSTALLED_APPS`.
6. Created a function-based view.
7. Configured URL routing.
8. Ran the Django development server.

---

## Output

URL

```
http://127.0.0.1:8000/api/hello/
```

Output

```
Course Management API is running
```

---

## Result

The Django project was successfully created and the `/api/hello/` endpoint returned the expected response.