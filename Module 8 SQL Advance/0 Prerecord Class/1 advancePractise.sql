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

