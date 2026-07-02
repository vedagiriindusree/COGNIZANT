from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db, create_tables
from models import Course
from schemas import CourseCreate, CourseUpdate

@asynccontextmanager
async def lifespan(app):
    await create_tables()
    yield
app = FastAPI(
    title="Course Management API",
    version="1.0",
    lifespan=lifespan
)
courses = [
    {"id": 1, "name": "Python", "code": "CS101", "credits": 4, "department_id": 1},
    {"id": 2, "name": "Java", "code": "CS102", "credits": 4, "department_id": 1},
    {"id": 3, "name": "AI", "code": "CS103", "credits": 3, "department_id": 2},
    {"id": 4, "name": "Cloud", "code": "CS104", "credits": 3, "department_id": 2},
]


@app.get("/")
async def root():
    return {"message": "API running"}


# @app.post("/api/courses/")
# async def create_course(course: CourseCreate):
#     new_course = {
#         "id": len(courses) + 1,
#         **course.model_dump()
#     }
#     courses.append(new_course)
#     return new_course
@app.post("/api/courses/")
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db)
):

    new_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(new_course)

    await db.commit()

    await db.refresh(new_course)

    return new_course


# @app.get("/api/courses/{course_id}")
# async def get_course(course_id: int):
#     for course in courses:
#         if course["id"] == course_id:
#             return course
#     return {"message": "Course not found"}

# @app.get("/api/courses/")
# async def get_courses(
#     skip: int = 0,
#     limit: int = 10,
#     department_id: int | None = None,
# ):
#     result = courses

#     if department_id is not None:
#         result = [c for c in result if c["department_id"] == department_id]

#     return result[skip: skip + limit]

# @app.get("/api/courses/")
# async def get_courses(
#     skip: int = 0,
#     limit: int = 10,
#     department_id: int | None = None,
#     db: AsyncSession = Depends(get_db),
# ):
#     result = courses

#     if department_id is not None:
#         result = [c for c in result if c["department_id"] == department_id]

#     return result[skip: skip + limit]
@app.get("/api/courses/")
async def get_courses(
    skip: int = 0,
    limit: int = 10,
    department_id: int | None = None,
    db: AsyncSession = Depends(get_db)
):

    stmt = select(Course)

    if department_id:
        stmt = stmt.where(Course.department_id == department_id)

    stmt = stmt.offset(skip).limit(limit)

    result = await db.execute(stmt)

    return result.scalars().all()

@app.get("/api/courses/{course_id}")
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    return result.scalar_one_or_none()
@app.put("/api/courses/{course_id}")
async def update_course(
    course_id: int,
    course: CourseUpdate,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if not db_course:
        return {"message": "Course not found"}

    for key, value in course.model_dump(exclude_unset=True).items():
        setattr(db_course, key, value)

    await db.commit()

    await db.refresh(db_course)

    return db_course
@app.delete("/api/courses/{course_id}")
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    db_course = result.scalar_one_or_none()

    if not db_course:
        return {"message": "Course not found"}

    await db.delete(db_course)

    await db.commit()

    return {"message": "Deleted"}