-- Retrieve all courses
SELECT * FROM courses;


-- Retrieve student details (ID, name, GPA)
SELECT students.student_id, students.first_name, students.last_name, students.gpa FROM students;


-- Order students by GPA in ascending order where GPA is less than 4.00
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.gpa < 4.00
ORDER BY students.gpa ASC;


-- Order all students by GPA (default ascending)
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
ORDER BY students.gpa;


-- Get top 3 students with highest GPA
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
ORDER BY students.gpa DESC
LIMIT 3;


-- Find students with last names starting with 'D'
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.last_name LIKE "D%";


-- Find students with 'a' anywhere in their first name
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.first_name LIKE "%a%";


-- Find students with first name starting with 'J' followed by exactly 3 characters
SELECT students.student_id, students.first_name, students.last_name, students.gpa
FROM students
WHERE students.first_name LIKE "J___";


-- Count the total number of students
SELECT COUNT(*) FROM students;


-- Group students by course and count students in each course
SELECT students.course_id, COUNT(*) FROM students GROUP BY students.course_id;


-- Find courses with average GPA > 3.5
SELECT students.course_id, AVG(students.gpa)
FROM students
GROUP BY students.course_id
HAVING AVG(students.gpa) > 3.5;


-- Retrieve all student details
SELECT * FROM students;


-- Group students by course and find courses with more than 1 student
SELECT students.course_id, COUNT(*)
FROM students
GROUP BY students.course_id
HAVING COUNT(*) > 1;


-- INNER JOIN: Get student and course information where they match
SELECT students.student_id, students.first_name, students.last_name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.course_id;


-- LEFT JOIN: Get all students and their course info (if available)
SELECT students.first_name, students.last_name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id;


-- RIGHT JOIN: Get all courses and their student info (if available)
SELECT students.first_name, students.last_name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id;



-- FULL JOIN: Get all students and all courses, matching where possible
SELECT students.first_name, students.last_name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.course_id

UNION

SELECT students.first_name, students.last_name, courses.course_name
FROM students
RIGHT JOIN courses
ON students.course_id = courses.course_id;
