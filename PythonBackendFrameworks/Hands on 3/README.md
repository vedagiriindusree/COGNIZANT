# Hands-On 3

## Python Backend Frameworks

### Topic

Django REST Framework - API Views, ViewSets and Routers

---

## Objective

To develop RESTful APIs using Django REST Framework by implementing serializers, APIViews, ViewSets, routers, and custom actions.

---

## Software Used

- Python 3.x
- Django
- Django REST Framework
- SQLite
- Postman
- Visual Studio Code

---

# Task 1 - API Views

## Features Implemented

- Created ModelSerializers
- Implemented APIView for Course
- GET API
- POST API
- PUT API
- DELETE API

---

# Task 2 - ViewSets and Routers

## Features Implemented

- ModelViewSet
- DefaultRouter
- Automatic CRUD endpoints
- Custom Action using @action decorator
- Students endpoint for each course

---

## API Endpoints

| Method | Endpoint |
|---------|----------|
| GET | /api/courses/ |
| POST | /api/courses/ |
| GET | /api/courses/{id}/ |
| PUT | /api/courses/{id}/ |
| DELETE | /api/courses/{id}/ |
| GET | /api/v2/courses/ |
| GET | /api/v2/courses/{id}/students/ |

---

## Result

REST APIs were successfully developed using Django REST Framework. CRUD operations, ViewSets, Routers, and custom actions were implemented and tested successfully.