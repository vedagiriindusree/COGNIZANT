# Hands-On 6: FastAPI – Path Parameters, Pydantic & Async Endpoints

## Objective

The objective of this hands-on is to build a Course Management REST API using FastAPI. The application demonstrates Pydantic data validation, path and query parameters, asynchronous endpoints, dependency injection, async SQLAlchemy database access, automatic Swagger documentation, and pagination.

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
Handson6/
│
├── main.py
├── schemas.py
├── models.py
├── database.py
├── requirements.txt
├── README.md
├── Output Screenshot/
│   ├── Task 1/
│   └── Task 2/
└── venv/
```

---

## Task 1 – FastAPI Setup and Pydantic Schemas

Completed the following:

- Created FastAPI application.
- Configured root endpoint.
- Created Pydantic schemas:
  - CourseCreate
  - CourseUpdate
  - CourseResponse
  - DepartmentResponse
- Implemented POST endpoint using request validation.
- Verified Swagger documentation.
- Tested validation errors (HTTP 422).

---

## Task 2 – Path/Query Parameters and Async Database Access

Completed the following:

- Implemented path parameters.
- Implemented query parameters.
- Configured Async SQLAlchemy.
- Implemented Dependency Injection using Depends().
- Performed asynchronous CRUD operations.
- Implemented pagination using skip and limit.
- Implemented department-based filtering.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API Status |
| POST | /api/courses/ | Create Course |
| GET | /api/courses/ | List Courses |
| GET | /api/courses/{course_id} | Get Course by ID |
| PUT | /api/courses/{course_id} | Update Course |
| DELETE | /api/courses/{course_id} | Delete Course |

---

## Features Implemented

- FastAPI Project Setup
- Pydantic Request Validation
- Response Models
- Automatic Swagger Documentation
- Path Parameters
- Query Parameters
- Pagination
- Department Filtering
- Async SQLAlchemy
- Dependency Injection
- Async CRUD Operations

---

## Expected Outcome

- FastAPI application runs successfully.
- Swagger UI is generated automatically.
- Request validation returns HTTP 422 for invalid data.
- CRUD operations work asynchronously.
- Pagination returns limited records.
- Department filtering returns only matching courses.
- All endpoints return JSON responses.

---

## How to Run

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

The FastAPI application successfully demonstrates:

- Pydantic validation
- Async endpoints
- Async SQLAlchemy
- Dependency Injection
- Path parameters
- Query parameters
- Pagination
- Department filtering
- Automatic Swagger documentation