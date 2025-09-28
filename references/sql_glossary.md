# SQL Glossary

This glossary provides definitions for common SQL terms and concepts to help students understand the terminology used in database management.

## A

**Aggregate Function**: A function that performs a calculation on multiple values and returns a single value (e.g., AVG, COUNT, MAX, MIN, SUM).

**ALTER TABLE**: A DDL command used to add, modify, or delete columns in an existing table.

**ACID**: An acronym for Atomicity, Consistency, Isolation, and Durability - the four key properties that guarantee reliable processing of database transactions.

**Alias**: A temporary name given to a table or column in a query to make the query more readable or to simplify references to tables/columns.

## B

**BLOB**: Binary Large Object - a data type used to store binary data such as images, audio, or other multimedia files.

**BCNF**: Boyce-Codd Normal Form - a normal form used in database normalization that is slightly stronger than 3NF.

**Backup**: A copy of data that can be used to restore the original after a data loss event.

## C

**Cardinality**: The uniqueness of data values in a column. High cardinality means many unique values, low cardinality means few unique values.

**Cascade**: An option for foreign key constraints that automatically applies changes (like DELETE or UPDATE) to related rows in child tables.

**CHECK Constraint**: A rule that limits the values that can be placed in a column.

**Commit**: The action that makes database changes permanent.

**Composite Key**: A key that consists of two or more columns.

**Correlated Subquery**: A subquery that references columns from the outer query and is executed once for each row processed by the outer query.

**CTE (Common Table Expression)**: A temporary result set that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement.

**CRUD**: Create, Read, Update, Delete - the four basic functions of persistent storage.

## D

**Database**: An organized collection of structured information or data, typically stored electronically in a computer system.

**Data Type**: A classification that specifies which type of value a column can hold (e.g., INTEGER, TEXT, DATE).

**DDL (Data Definition Language)**: SQL commands that define the database structure (e.g., CREATE, ALTER, DROP).

**DML (Data Manipulation Language)**: SQL commands that manipulate data within the database (e.g., SELECT, INSERT, UPDATE, DELETE).

**DCL (Data Control Language)**: SQL commands that control access to data within the database (e.g., GRANT, REVOKE).

**Denormalization**: The process of adding redundant data to a normalized database to improve read performance.

**DISTINCT**: A keyword used to return only unique values in a result set.

## E

**Entity**: A person, place, thing, or event that is tracked in a database.

**Entity-Relationship Diagram (ERD)**: A graphical representation of entities and their relationships to each other.

**Execution Plan**: The sequence of operations that the database engine performs to execute a query.

## F

**Foreign Key**: A column or group of columns in a table that refers to the primary key in another table.

**Function**: A predefined operation that performs a specific task, such as mathematical calculations or string manipulations.

## G

**GROUP BY**: A clause used to group rows that have the same values in specified columns.

## H

**HAVING**: A clause used to filter groups based on a specified condition.

## I

**Index**: A database structure that improves the speed of data retrieval operations at the cost of additional writes and storage space.

**INNER JOIN**: A join operation that returns rows when there is at least one match in both tables.

**INSERT**: A DML command used to add new rows to a table.

**Integrity Constraint**: A rule that restricts the values that can be inserted into a table to maintain data integrity.

## J

**JOIN**: A SQL operation used to combine rows from two or more tables based on a related column.

**Junction Table**: A table used to connect two or more tables in a many-to-many relationship.

## K

**Key**: A column or group of columns used to identify a row or establish a relationship between tables.

## L

**LEFT JOIN**: A join operation that returns all rows from the left table and matched rows from the right table.

**LIKE**: An operator used in a WHERE clause to search for a specified pattern in a column.

**LIMIT**: A clause used to restrict the number of rows returned by a query.

## M

**Many-to-Many Relationship**: A relationship between two entities where each record in the first table can match many records in the second table and vice versa.

**Metadata**: Data that provides information about other data, such as table names, column names, data types, etc.

## N

**Normalization**: The process of organizing data in a database to reduce redundancy and improve data integrity.

**NULL**: A special marker used to indicate that a data value does not exist in the database.

## O

**One-to-Many Relationship**: A relationship between two entities where each record in the first table can match many records in the second table, but each record in the second table matches only one record in the first table.

**One-to-One Relationship**: A relationship between two entities where each record in the first table matches exactly one record in the second table.

**ORDER BY**: A clause used to sort the result set by one or more columns.

## P

**Primary Key**: A column or group of columns that uniquely identifies each row in a table.

**Projection**: The operation of selecting specific columns from a table.

## Q

**Query**: A request for data or information from a database.

**Query Optimization**: The process of improving the performance of a database query.

## R

**RDBMS**: Relational Database Management System - software that manages relational databases.

**Recursive Query**: A query that references itself.

**Referential Integrity**: A property that ensures relationships between tables remain consistent.

**RIGHT JOIN**: A join operation that returns all rows from the right table and matched rows from the left table.

**Rollback**: The operation of restoring the database to a previous state by discarding changes made in a transaction.

## S

**Schema**: The structure that represents the logical configuration of all or part of a relational database.

**SELECT**: A DML command used to retrieve data from one or more tables.

**Self Join**: A join in which a table is joined with itself.

**SQL Injection**: A code injection technique used to attack data-driven applications by inserting malicious SQL statements.

**Stored Procedure**: A prepared SQL code that can be saved and reused.

**Subquery**: A query nested inside another query.

## T

**Table**: A collection of related data organized in rows and columns.

**Transaction**: A sequence of one or more SQL operations treated as a single logical unit of work.

**Trigger**: A stored procedure that automatically executes when a specified event occurs in the database.

**TRUNCATE**: A DDL command that removes all rows from a table without logging individual row deletions.

## U

**UNION**: An operator used to combine the result sets of two or more SELECT statements.

**UNIQUE Constraint**: A constraint that ensures all values in a column are different.

**UPDATE**: A DML command used to modify existing records in a table.

## V

**View**: A virtual table based on the result set of a SQL statement.

## W

**WHERE**: A clause used to filter records based on a specified condition.

**Wildcard**: A special character used to substitute for any other character(s) in a string.

**Window Function**: A function that performs calculations across a set of table rows related to the current row.

## Symbols

**%**: In LIKE patterns, represents zero or more characters.

**_**: In LIKE patterns, represents exactly one character.

**!=** or **<>**: Not equal to operator.

**>=**: Greater than or equal to operator.

**<=**: Less than or equal to operator.

**;**: Statement terminator in SQL.

**--**: Single line comment indicator.

**/* */**: Multi-line comment indicators.
