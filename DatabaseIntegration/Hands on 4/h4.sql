EXPLAIN
SELECT
    s.first_name,
    s.last_name,
    c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;
-- Before indexing:
-- PostgreSQL: Seq Scan on students.
-- MySQL: Full Table Scan.
CREATE INDEX idx_students_enrollment_year
ON students(enrollment_year);
CREATE UNIQUE INDEX idx_enrollments_student_course
ON enrollments(student_id, course_id);
CREATE INDEX idx_courses_course_code
ON courses(course_code);
EXPLAIN
SELECT s.first_name,
       s.last_name,
       c.course_name
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id
WHERE s.enrollment_year = 2022;
