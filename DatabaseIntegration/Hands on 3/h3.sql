USE college_db;

SELECT s.student_id,
       s.first_name,
       s.last_name
FROM students s
JOIN enrollments e
ON s.student_id = e.student_id
GROUP BY s.student_id, s.first_name, s.last_name
HAVING COUNT(e.course_id) >
(
    SELECT AVG(course_count)
    FROM
    (
        SELECT COUNT(*) AS course_count
        FROM enrollments
        GROUP BY student_id
    ) AS avg_table
);
SELECT c.course_name
FROM courses c
WHERE NOT EXISTS
(
    SELECT *
    FROM enrollments e
    WHERE e.course_id = c.course_id
    AND e.grade <> 'A'
);
SELECT p.prof_name,
       p.department_id,
       p.salary
FROM professors p
WHERE salary =
(
    SELECT MAX(p2.salary)
    FROM professors p2
    WHERE p2.department_id = p.department_id
);
SELECT d.dept_name,
       avg_salary.avg_sal
FROM departments d
JOIN
(
    SELECT department_id,
           AVG(salary) AS avg_sal
    FROM professors
    GROUP BY department_id
) AS avg_salary
ON d.department_id = avg_salary.department_id
WHERE avg_salary.avg_sal > 85000;
USE college_db;

CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    d.dept_name,
    COUNT(e.course_id) AS total_enrollments,
    ROUND(AVG(
        CASE
            WHEN e.grade='A+' THEN 10
            WHEN e.grade='A' THEN 9
            WHEN e.grade='B+' THEN 8
            WHEN e.grade='B' THEN 7
            WHEN e.grade='C' THEN 6
            ELSE 0
        END
    ),2) AS avg_gpa
FROM students s
JOIN departments d
ON s.department_id=d.department_id
LEFT JOIN enrollments e
ON s.student_id=e.student_id
GROUP BY s.student_id,s.first_name,s.last_name,d.dept_name;
CREATE VIEW vw_course_stats AS
SELECT
    c.course_name,
    c.course_code,
    COUNT(e.student_id) AS total_enrollments,
    ROUND(AVG(
        CASE
            WHEN e.grade='A+' THEN 10
            WHEN e.grade='A' THEN 9
            WHEN e.grade='B+' THEN 8
            WHEN e.grade='B' THEN 7
            WHEN e.grade='C' THEN 6
            ELSE 0
        END
    ),2) AS avg_gpa
FROM courses c
LEFT JOIN enrollments e
ON c.course_id=e.course_id
GROUP BY c.course_id,c.course_name,c.course_code;
SELECT * FROM vw_student_enrollment_summary;

SELECT * FROM vw_course_stats;
UPDATE vw_student_enrollment_summary
SET dept_name='Computer Science'
WHERE student_id=1;
DROP VIEW vw_student_enrollment_summary;
CREATE VIEW vw_student_enrollment_summary AS
SELECT
    s.student_id,
    CONCAT(s.first_name,' ',s.last_name) AS student_name,
    d.dept_name
FROM students s
JOIN departments d
ON s.department_id=d.department_id
WHERE d.dept_name='Computer Science'
WITH CHECK OPTION;
SELECT * FROM vw_student_enrollment_summary;
USE college_db;

DELIMITER $$

CREATE PROCEDURE enroll_student(
    IN p_student_id INT,
    IN p_course_id INT,
    IN p_enrollment_date DATE
)
BEGIN

    DECLARE cnt INT;

    SELECT COUNT(*)
    INTO cnt
    FROM enrollments
    WHERE student_id = p_student_id
      AND course_id = p_course_id;

    IF cnt > 0 THEN
        SELECT 'Student is already enrolled in this course' AS Message;
    ELSE
        INSERT INTO enrollments(student_id, course_id, enrollment_date, grade)
        VALUES(p_student_id, p_course_id, p_enrollment_date, NULL);

        SELECT 'Enrollment Successful' AS Message;
    END IF;

END $$

DELIMITER ;
CALL enroll_student(3,5,'2024-07-01');
CALL enroll_student(3,5,'2024-07-01');
START TRANSACTION;

UPDATE students
SET department_id = 2
WHERE student_id = 1;

INSERT INTO departments(dept_name, hod_name, budget)
VALUES('AI','Dr. Kumar',500000);

COMMIT;
SELECT * FROM students;
SELECT * FROM departments;
START TRANSACTION;

UPDATE students
SET department_id = 3
WHERE student_id = 2;

INSERT INTO enrollments(student_id, course_id)
VALUES(999,1);

ROLLBACK;
SELECT * FROM students;
START TRANSACTION;

INSERT INTO departments(dept_name, hod_name, budget)
VALUES('Cyber Security','Dr. John',700000);

SAVEPOINT sp1;

INSERT INTO enrollments(student_id, course_id)
VALUES(999,2);

ROLLBACK TO sp1;

COMMIT;
SELECT * FROM departments;
SELECT * FROM enrollments;