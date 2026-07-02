USE college_db;
SELECT * FROM students;
SELECT * FROM students
WHERE enrollment_year = 2022;
SELECT * FROM courses
WHERE credits > 3;
SELECT * FROM professors
WHERE salary > 80000;
SELECT * FROM students
ORDER BY last_name;
SELECT * FROM students
WHERE first_name LIKE 'A%';
SELECT
s.first_name,
s.last_name,
d.dept_name
FROM students s
JOIN departments d
ON s.department_id = d.department_id;
SELECT
s.first_name,
c.course_name,
e.grade
FROM enrollments e
JOIN students s
ON e.student_id = s.student_id
JOIN courses c
ON e.course_id = c.course_id;
SELECT
p.prof_name,
d.dept_name
FROM professors p
JOIN departments d
ON p.department_id = d.department_id;
SELECT
department_id,
COUNT(*) AS total_students
FROM students
GROUP BY department_id;
SELECT AVG(salary) AS average_salary
FROM professors;
SELECT MAX(budget) AS highest_budget
FROM departments;
SELECT SUM(credits) AS total_credits
FROM courses;
SELECT
enrollment_year,
COUNT(*) AS total_students
FROM students
GROUP BY enrollment_year;