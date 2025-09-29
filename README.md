# SQL Tutorial for Year 12 Software Engineering

This tutorial is designed to teach the fundamentals of SQL (Structured Query Language) to Year 12 software engineering students. It follows a hands-on approach with practical examples using SQLite.

## Prerequisites

- Basic understanding of programming concepts
- Python installed (optional, for Python integration)
- SQLite installed (instructions provided)

## Tutorial Structure

### Part 1: Single Table Operations

1. **Introduction to Databases**
   - What is a database?
   - Why we use databases
   - Tables, rows, columns explained

2. **Getting Started with SQLite**
   - Installing and accessing SQLite
   - Creating a new database
   - Opening the SQLite shell

3. **Creating Tables**
   - CREATE TABLE syntax
   - Choosing appropriate data types
   - Planning table structure
   - Column constraints (PRIMARY KEY, NOT NULL, etc.)

4. **Inserting Data**
   - INSERT INTO syntax
   - Adding one row at a time
   - Batch insert example
   - Working with DEFAULT values

5. **Reading Data (SELECT)**
   - SELECT * FROM table
   - Selecting specific columns
   - Using expressions and aliases
   - Aggregate functions (COUNT, AVG, etc.)

6. **Filtering Data**
   - Using =, <, >, !=
   - Text filters with LIKE
   - Combining filters with AND, OR
   - NULL values and IN operator

7. **Ordering and Limiting Results**
   - ORDER BY ascending/descending
   - Sorting by multiple columns
   - LIMIT clause for pagination
   - Practical use cases

8. **Updating and Deleting Records**
   - UPDATE ... SET ... WHERE ...
   - DELETE FROM ... WHERE ...
   - Safe practices with transactions
   - Avoiding accidental data loss

### Part 2: Relational Database Concepts

9. **Introduction to Database Relationships**
   - Types of relationships (one-to-one, one-to-many, many-to-many)
   - Primary and foreign keys
   - Database normalization basics

10. **Creating Related Tables**
    - Designing tables with relationships
    - Implementing foreign keys
    - Ensuring referential integrity
    - Self-referencing tables

11. **Working with Multiple Tables**
    - JOIN operations (INNER, LEFT, CROSS)
    - Querying across related tables
    - Aggregating joined data
    - Common JOIN problems

### Part 3: Advanced Topics and Applications

12. **Using SQL with Python: ORMs vs. Raw SQL**
    - Raw SQL approach with sqlite3
    - Object-Relational Mapping with SQLAlchemy
    - Comparing advantages and disadvantages
    - Hybrid approaches for real-world applications

13. **Advanced SQL Topics and Next Steps**
    - Integrating with web frameworks
    - Exporting/importing data (CSV/JSON)
    - Alternative database systems
    - Resources for further learning

## How to Use This Tutorial

Each section has its own file with explanations and examples. Follow along by running the SQL commands in your SQLite shell or through Python.

## Getting Help

If you encounter any issues or have questions, refer to the SQLite documentation or ask for assistance.

Happy learning!
