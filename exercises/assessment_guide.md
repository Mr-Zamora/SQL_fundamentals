# SQL Assessment Guide

This guide provides a framework for assessing students' SQL knowledge and skills. It includes both theoretical questions and practical tasks at different difficulty levels.

## Theoretical Assessment

### Basic Level (Understanding)

1. **Multiple Choice Questions**
   - What is a database?
   - What does SQL stand for?
   - Which SQL statement is used to retrieve data from a database?
   - What is a primary key?
   - In SQLite, what are the main data types?

2. **True/False Questions**
   - A table can have multiple primary keys.
   - The WHERE clause is used to filter records.
   - The INSERT statement is used to modify existing records.
   - NULL means the same as zero or an empty string.
   - SQLite requires a separate server process.

3. **Fill in the Blanks**
   - The _______ statement is used to add new records to a table.
   - To sort results in descending order, use the _______ keyword.
   - A _______ key is used to establish a relationship between two tables.
   - The _______ function returns the number of rows that match a specified criterion.
   - The _______ clause is used to filter groups in a GROUP BY query.

### Intermediate Level (Application)

1. **Short Answer Questions**
   - Explain the difference between a primary key and a foreign key.
   - What is the purpose of the JOIN clause in SQL?
   - Describe the difference between DELETE and DROP statements.
   - What is database normalization and why is it important?
   - Explain the concept of a transaction in a database.

2. **SQL Syntax Questions**
   - Write a SQL statement to create a table named "products" with columns for id, name, price, and category.
   - Write a SQL statement to retrieve all customers who have placed orders totaling more than $1000.
   - Write a SQL statement to update the price of all products in the "Electronics" category by increasing them by 10%.
   - Write a SQL statement to find the average order value for each customer.
   - Write a SQL statement to delete all orders placed before 2023.

### Advanced Level (Analysis)

1. **Case Study Questions**
   - Given a specific database schema, identify potential issues with the design and suggest improvements.
   - Analyze a complex SQL query and explain what it does, step by step.
   - Compare and contrast different approaches to solving a particular database problem.
   - Explain how you would optimize a slow-performing SQL query.
   - Discuss the trade-offs between different types of joins in a specific scenario.

## Practical Assessment

### Basic Level Tasks

1. **Database Creation and Simple Queries**
   - Create a database with at least two related tables
   - Insert at least 5 records into each table
   - Write queries to:
     - Select all records from each table
     - Select records that match a specific condition
     - Order results by a specific column

2. **Data Manipulation**
   - Update records based on a condition
   - Delete records based on a condition
   - Use basic filtering with WHERE
   - Use basic sorting with ORDER BY

### Intermediate Level Tasks

1. **Multi-table Operations**
   - Write queries using different types of JOINs
   - Use subqueries
   - Implement aggregate functions with GROUP BY
   - Filter grouped results with HAVING

2. **Data Analysis**
   - Calculate summary statistics (averages, counts, etc.)
   - Find minimum and maximum values
   - Identify patterns or anomalies in the data
   - Create a report showing related data from multiple tables

### Advanced Level Tasks

1. **Complex Database Operations**
   - Design and implement a database with at least three related tables
   - Create appropriate indexes
   - Implement constraints (foreign keys, unique constraints, etc.)
   - Write complex queries involving multiple joins and subqueries

2. **Application Integration**
   - Create a simple Python application that interacts with a SQLite database
   - Implement CRUD operations through the application
   - Handle potential errors and edge cases
   - Optimize database operations for performance

## Rubric for Practical Assessment

### Database Design (25%)

| Score | Description |
|-------|-------------|
| 5 | Excellent design with appropriate tables, relationships, and constraints |
| 4 | Good design with minor issues |
| 3 | Adequate design with some flaws |
| 2 | Poor design with significant issues |
| 1 | Incomplete or non-functional design |

### SQL Query Writing (25%)

| Score | Description |
|-------|-------------|
| 5 | Correct, efficient, and well-structured queries |
| 4 | Mostly correct queries with minor issues |
| 3 | Functional queries with some inefficiencies |
| 2 | Queries with significant errors |
| 1 | Non-functional or missing queries |

### Data Manipulation (25%)

| Score | Description |
|-------|-------------|
| 5 | Correctly implements all required operations |
| 4 | Implements most operations correctly |
| 3 | Implements basic operations with some errors |
| 2 | Significant errors in data manipulation |
| 1 | Unable to correctly manipulate data |

### Application/Analysis (25%)

| Score | Description |
|-------|-------------|
| 5 | Demonstrates excellent understanding and application of concepts |
| 4 | Good application with minor misconceptions |
| 3 | Basic application with some significant gaps |
| 2 | Poor application with major misconceptions |
| 1 | Unable to apply concepts effectively |

## Sample Assessment Project

### Library Management System

**Scenario**: Create a database for a small library to track books, members, and loans.

**Requirements**:

1. **Database Design**:
   - Create tables for books, members, and loans
   - Establish appropriate relationships between tables
   - Implement constraints to maintain data integrity

2. **Data Population**:
   - Add at least 10 books with details (title, author, ISBN, publication year, genre)
   - Add at least 5 members with details (name, contact information, join date)
   - Create at least 8 loan records (who borrowed what book and when)

3. **Queries to Implement**:
   - List all books by a specific author
   - Find which members currently have books on loan
   - Identify overdue books (borrowed more than 14 days ago)
   - Calculate the most popular genre based on loans
   - Find members who have never borrowed a book

4. **Advanced Tasks**:
   - Implement a system to track book availability
   - Create a view that shows comprehensive loan information
   - Write a transaction to process a book return
   - Create a Python script that allows adding new books and processing loans

**Deliverables**:
- SQL script to create and populate the database
- SQL script with all required queries
- Documentation explaining the database design
- (Optional) Python application for database interaction

## Alternative Assessment Projects

1. **School Management System**
   - Track students, teachers, courses, and grades

2. **E-commerce Database**
   - Track products, customers, orders, and inventory

3. **Movie Collection Database**
   - Track movies, actors, directors, and genres

4. **Recipe Database**
   - Track recipes, ingredients, categories, and nutritional information

5. **Personal Finance Tracker**
   - Track income, expenses, categories, and budgets
