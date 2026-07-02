# Hands-On 2

## Python Backend Frameworks

### Topic

Django Models, ORM & Admin Interface

---

## Objective

To create Django models for the Course Management System, perform database operations using the Django ORM, and manage data through the Django Admin Interface.

---

## Software Used

- Python 3.x
- Django
- Visual Studio Code
- SQLite

---

# Task 1 - Define Models and Run Migrations

## Models Created

- Department
- Course
- Student
- Enrollment

### Features Implemented

- Created Django models
- Added `__str__()` methods
- Used `ForeignKey` relationships
- Added `unique_together` constraint in the Enrollment model
- Generated migrations
- Applied migrations successfully

### Commands Used

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

---

# Task 2 - Django ORM Queries

## Operations Performed

- Created Departments
- Created Courses
- Created Students
- Filtered courses using ForeignKey lookup
- Counted courses using `annotate()`
- Retrieved related objects using `select_related()`
- Updated department budget using `F()` expressions

### Commands Used

```python
Course.objects.filter(department__name="Computer Science")

Department.objects.annotate(
    course_count=Count("course")
)

Student.objects.select_related("department")

Department.objects.update(
    budget=F("budget") * 1.1
)
```

---

# Task 3 - Django Admin Interface

## Features Implemented

- Created Django Superuser
- Registered all models
- Customized CourseAdmin
- Displayed multiple columns using `list_display`
- Added search functionality using `search_fields`
- Added filtering using `list_filter`
- Created records through Django Admin

---

## Admin Customization

```python
list_display = [
    "name",
    "code",
    "credits",
    "department"
]

search_fields = [
    "name",
    "code"
]

list_filter = [
    "department"
]
```

---

## Output

### Task 1

- Models created successfully.
- Database tables generated.
- Migrations applied successfully.

### Task 2

- ORM queries executed successfully.
- Course count displayed for each department.
- Budget updated using `F()` expressions.

### Task 3

- Django Admin displayed all registered models.
- Search and filter functionality worked successfully.
- Course details displayed with Name, Code, Credits, and Department.

---

## Result

The Django models were successfully created, database migrations were applied, ORM operations were performed, and the Django Admin Interface was configured successfully with search, filtering, and customized list display.

---

## Screenshots

### Task 1

- Models Created
- Makemigrations
- Migrate
- Show Migrations

### Task 2

- ORM Queries
- F() Update

### Task 3

- Admin Dashboard
- Course Admin