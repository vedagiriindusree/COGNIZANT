from pydantic import BaseModel
from typing import Optional

class CourseBase(BaseModel):
    name: str
    code: str
    credits: int
    department_id: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    credits: Optional[int] = None
    department_id: Optional[int] = None


class CourseResponse(CourseBase):
    id: int

    model_config = {
        "from_attributes": True
    }


class StudentBase(BaseModel):
    name: str
    email: str


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    model_config = {
        "from_attributes": True
    }

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int


class EnrollmentCreate(EnrollmentBase):
    pass


class EnrollmentResponse(EnrollmentBase):
    id: int

    model_config = {
        "from_attributes": True
    }