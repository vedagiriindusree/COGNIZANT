from contextlib import asynccontextmanager

from fastapi import BackgroundTasks, Depends, FastAPI, HTTPException, Response, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import create_tables, get_db
from models import Course,Student, Enrollment
from schemas import CourseCreate, CourseResponse, CourseUpdate,StudentCreate,StudentResponse,EnrollmentCreate, EnrollmentResponse

def send_confirmation_email(student_email: str):
    print(f"Sending confirmation to {student_email}")
    
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield


app = FastAPI(
    title="Course Management API",
    description="REST API for managing Courses, Students, and Enrollments using FastAPI.",
    version="1.0.0",
    contact={
        "name": "Indu",
        "email": "indu@example.com"
    },
    lifespan=lifespan
)


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Courses"],
    summary="Create a new course",
    response_description="Course created successfully"
)
async def create_course(
    course: CourseCreate,
    db: AsyncSession = Depends(get_db),
):
    new_course = Course(**course.model_dump())

    db.add(new_course)
    await db.commit()
    await db.refresh(new_course)

    return new_course


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
    tags=["Courses"]
)
async def get_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse,
)
async def update_course(
    course_id: int,
    updated_course: CourseUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    for key, value in updated_course.model_dump(exclude_unset=True).items():
        setattr(course, key, value)

    await db.commit()
    await db.refresh(course)

    return course


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_course(
    course_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Course).where(Course.id == course_id)
    )

    course = result.scalar_one_or_none()

    if course is None:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    await db.delete(course)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.post(
    "/api/students/",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_student(
    student: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    new_student = Student(**student.model_dump())

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student


@app.get(
    "/api/students/{student_id}",
    response_model=StudentResponse,
    tags=["Students"]
)
async def get_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


@app.put(
    "/api/students/{student_id}",
    response_model=StudentResponse,
)
async def update_student(
    student_id: int,
    student_data: StudentCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.email = student_data.email

    await db.commit()
    await db.refresh(student)

    return student


@app.delete(
    "/api/students/{student_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_student(
    student_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Student).where(Student.id == student_id)
    )

    student = result.scalar_one_or_none()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    await db.delete(student)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)

# ---------------- ENROLLMENT CRUD ----------------

@app.post(
    "/api/enrollments/",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_enrollment(
    enrollment: EnrollmentCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    new_enrollment = Enrollment(**enrollment.model_dump())

    db.add(new_enrollment)
    await db.commit()
    await db.refresh(new_enrollment)

    result = await db.execute(
        select(Student).where(Student.id == enrollment.student_id)
    )
    student = result.scalar_one()

    background_tasks.add_task(
        send_confirmation_email,
        student.email
    )

    return new_enrollment

@app.get(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
    tags=["Enrollments"]
)
async def get_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    return enrollment


@app.put(
    "/api/enrollments/{enrollment_id}",
    response_model=EnrollmentResponse,
)
async def update_enrollment(
    enrollment_id: int,
    enrollment_data: EnrollmentCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    enrollment.student_id = enrollment_data.student_id
    enrollment.course_id = enrollment_data.course_id

    await db.commit()
    await db.refresh(enrollment)

    return enrollment


@app.delete(
    "/api/enrollments/{enrollment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_enrollment(
    enrollment_id: int,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Enrollment).where(Enrollment.id == enrollment_id)
    )

    enrollment = result.scalar_one_or_none()

    if enrollment is None:
        raise HTTPException(
            status_code=404,
            detail="Enrollment not found"
        )

    await db.delete(enrollment)
    await db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)