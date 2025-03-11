SELECT *FROM courses;

SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students;


--OEDER BY
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.gpa < 4.00
ORDER BY students.gpa ASC
;


SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
ORDER BY students.gpa
;


-- LIMIT
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
ORDER BY students.gpa DESC
LIMIT 3
;


-- LIKE (specific pattern in a column)
-- any string starting with "D"
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.last_name LIKE "D%" 
;--"%D" ending with D


--"a" anywhere in its value.
SELECT
    students.student_id,
    students.first_name,
    students.last_name,
    students.gpa
FROM students
WHERE students.first_name like "%a%" 
;


-- "J" followed by exactly three more characters.
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.first_name like "J___"
;


-- Count
SELECT COUNT(*)
FROM students
;


--Grouping
SELECT students.course_id, COUNT(*)
FROM students
GROUP BY students.course_id
;

-- Having(Filters groups after aggregation- count, sum, avg)
SELECT students.course_id, AVG(students.gpa)
FROM students
GROUP BY students.course_id
HAVING AVG (students.gpa) > 3.5
;


SELECT *FROM students
;

SELECT students.course_id, COUNT(*)
FROM students
GROUP BY students.course_id
HAVING COUNT(*) > 1
;


-- INNER JOIN (combines rows with matching values in both tables.)
-- only common matches
SELECT
    students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id
;


-- LEFT JOIN
-- left er sob ashbe + right er comman gula ashbe
SELECT
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id
;


-- RIGHT JOIN
SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id
;



-- FULL JOIN
-- FULL JOIN
SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id

UNION --mysql dosen't support fulljoin, that's why we use UNION

SELECT
    -- students.student_id,
    students.first_name,
    students.last_name,
    courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id
;