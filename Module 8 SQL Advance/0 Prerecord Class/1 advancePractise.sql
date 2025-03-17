-- Active: 1741979921591@@127.0.0.1@3306@ecommerce_db


--Rename column
ALTER TABLE students  
CHANGE COLUMN course_id id INT;
-- Yes, ALTER is used to modify an existing table, such as renaming columns, changing data types, adding or dropping columns, etc.


--Rename Table
ALTER TABLE university 
RENAME TO uni
--another way to rename table
RENAME TABLE uni TO Diu
;   --       old table        new table

--comment


--Drop column
ALTER TABLE students
DROP COLUMN active
;


--Drop Talbe
DROP Table univeristy
;


--Drop Database
DROP DATABASE database_name
;


-- Constraints: rule that controls the data in a table to ensure accuracy and consistency

-- NOT NULL
            -- means that column cannot store Null values


--UNIQUE 
            -- Ensures all values in a column are distinct.


--PRIMARY KEY 
             --combination of NOT (NULL and UNIQUE). Uniquely identifies each row.


CREATE TABLE ramadan (
    id INT PRIMARY KEY,  -- Ensures each ID is unique
    name VARCHAR(50) NOT NULL,  -- Name cannot be empty
    email VARCHAR(100) UNIQUE,  -- No duplicate emails allowed
);



--FOREIGN KEY 
             -- Links tables by referencing a primary key.


--CHECK 
       -- Validates values against a condition.

CREATE TABLE students (
    age INT CHECK (age >= 18)  -- Ensures age is at least 18
);

CREATE TABLE enrollments (
    enroll_id INT PRIMARY KEY,
    student_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id)  -- Links to students table
);



--DEFAULT 
         -- Sets a default value if none is provided.

CREATE TABLE students (
    status VARCHAR(20) DEFAULT 'Active'  -- Sets 'Active' as the default value
);



--correlated subqueirs and common  table expression(CTEs)
--: they are two advanced techniques that help handle complex queries efficiently.


--A correlated subquery
  --: is a subquery that depends on the outer query and runs for each row.
SELECT student_id, first_name, gpa  
FROM students s  
WHERE gpa > (SELECT AVG(gpa) FROM students WHERE course_id = s.course_id);



--Common Table Expression (CTE):
       -- is a temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement.

WITH HighGPA AS (
    SELECT student_id, first_name, gpa  
    FROM students  
    WHERE gpa > 3.5
)  
SELECT * FROM HighGPA;
-- Here, HighGPA is a CTE storing students with gpa > 3.5, making queries more readable.