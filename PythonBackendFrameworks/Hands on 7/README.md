# Hands-On 7: FastAPI – Dependency Injection, CRUD & OpenAPI Documentation

## Objective

The objective of this hands-on is to implement complete CRUD operations using FastAPI, apply dependency injection, background tasks, proper HTTP status codes, exception handling, and customize the OpenAPI (Swagger) documentation.

---

## Technologies Used

- Python 3.x
- FastAPI
- Uvicorn
- SQLAlchemy
- Async SQLAlchemy
- SQLite
- Pydantic

---

## Project Structure

```text
Handson7/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── courses.db
├── requirements.txt
├── README.md
├── Output Screenshot/
│   ├── Task 1/
│   └── Task 2/
└── venv/
```

---

## Task 1 – Complete CRUD with Proper HTTP Conventions

Completed the following:

- Implemented Course CRUD APIs.
- Added proper HTTP status codes (201, 204, 404).
- Used response models for request/response validation.
- Implemented HTTPException for invalid IDs.
- Added Course → Students endpoint using JOIN query.
- Implemented CRUD operations for Students.
- Implemented CRUD operations for Enrollments.

---

## Task 2 – Background Tasks and OpenAPI Customization

Completed the following:

- Added FastAPI BackgroundTasks.
- Simulated email confirmation after enrollment.
- Customized OpenAPI metadata.
- Added endpoint tags.
- Added endpoint summary.
- Added response descriptions.
- Verified grouped Swagger documentation.

---

## API Endpoints

### Course

- POST `/api/courses/`
- GET `/api/courses/{id}`
- PUT `/api/courses/{id}`
- DELETE `/api/courses/{id}`
- GET `/api/courses/{id}/students`

### Student

- POST `/api/students/`
- GET `/api/students/{id}`
- PUT `/api/students/{id}`
- DELETE `/api/students/{id}`

### Enrollment

- POST `/api/enrollments/`
- GET `/api/enrollments/{id}`
- PUT `/api/enrollments/{id}`
- DELETE `/api/enrollments/{id}`

---

## Features Implemented

- FastAPI Dependency Injection
- Response Models
- Proper HTTP Status Codes
- HTTPException Handling
- CRUD Operations
- Background Tasks
- OpenAPI Customization
- Swagger Tags
- Endpoint Summary
- Response Description
- JOIN Queries

---

## Expected Outcome

- Complete asynchronous CRUD operations.
- Proper REST status codes.
- Automatic JSON error responses.
- Background tasks execute after sending the response.
- Swagger UI displays organized endpoints with tags and descriptions.
- APIs are fully documented using OpenAPI.

---

## Run the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Server

```bash
uvicorn main:app --reload
```

### Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

## Output

The application successfully demonstrates:

- Dependency Injection
- CRUD Operations
- Background Tasks
- OpenAPI Documentation
- HTTP Exception Handling
- Response Models
- Swagger API Documentation