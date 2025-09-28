# SQL Interview Questions

This document contains common SQL interview questions and answers to help students prepare for technical interviews. The questions are organized by difficulty level and topic.

## Basic SQL Questions

### 1. What is SQL?
**Answer**: SQL (Structured Query Language) is a standard programming language specifically designed for managing and manipulating relational databases. It's used to query, insert, update, and modify data in a relational database management system (RDBMS).

### 2. What are the different types of SQL commands?
**Answer**: SQL commands are grouped into four main categories:
- **DDL (Data Definition Language)**: Commands like CREATE, ALTER, DROP, TRUNCATE
- **DML (Data Manipulation Language)**: Commands like SELECT, INSERT, UPDATE, DELETE
- **DCL (Data Control Language)**: Commands like GRANT, REVOKE
- **TCL (Transaction Control Language)**: Commands like COMMIT, ROLLBACK, SAVEPOINT

### 3. What is a primary key?
**Answer**: A primary key is a column or combination of columns that uniquely identifies each row in a table. It cannot contain NULL values and must be unique across the table.

### 4. What is a foreign key?
**Answer**: A foreign key is a column or combination of columns in one table that refers to the primary key in another table. It establishes a relationship between two tables.

### 5. What is the difference between DELETE and TRUNCATE commands?
**Answer**: 
- DELETE is a DML command that removes specific rows based on a condition. It can be rolled back.
- TRUNCATE is a DDL command that removes all rows from a table. It's faster than DELETE but cannot be rolled back (in most databases).

### 6. Explain the difference between CHAR and VARCHAR data types.
**Answer**:
- CHAR is a fixed-length character data type. If you store a string smaller than the declared size, it will be padded with spaces.
- VARCHAR is a variable-length character data type. It only uses as much space as needed for the stored string, plus a small overhead.

### 7. What is the purpose of the GROUP BY clause?
**Answer**: The GROUP BY clause groups rows that have the same values into summary rows. It's typically used with aggregate functions (like COUNT, MAX, MIN, SUM, AVG) to group the result-set by one or more columns.

## Intermediate SQL Questions

### 8. Explain the different types of JOINs in SQL.
**Answer**:
- **INNER JOIN**: Returns records that have matching values in both tables
- **LEFT JOIN**: Returns all records from the left table and matched records from the right table
- **RIGHT JOIN**: Returns all records from the right table and matched records from the left table
- **FULL JOIN**: Returns all records when there is a match in either left or right table
- **CROSS JOIN**: Returns the Cartesian product of both tables (all possible combinations)

### 9. What is normalization and what are the normal forms?
**Answer**: Normalization is the process of organizing data to reduce redundancy and improve data integrity. The main normal forms are:
- **1NF**: Eliminate repeating groups, create separate tables for each set of related data
- **2NF**: Meet 1NF requirements and remove partial dependencies
- **3NF**: Meet 2NF requirements and remove transitive dependencies
- **BCNF**: A stronger version of 3NF
- **4NF**: Deal with multi-valued dependencies
- **5NF**: Deal with join dependencies

### 10. What is an index and how does it work?
**Answer**: An index is a database structure that improves the speed of data retrieval operations. It works similar to an index in a book, allowing the database engine to find data without scanning the entire table. While indexes speed up data retrieval, they slow down data insertion, deletion, and updates because the index must also be updated.

### 11. What is a view in SQL?
**Answer**: A view is a virtual table based on the result-set of a SQL statement. It contains rows and columns, just like a real table, but doesn't store the data physically. Views can simplify complex queries, provide an additional security layer, and present data in a more user-friendly way.

### 12. Explain the HAVING clause and how it differs from WHERE.
**Answer**: 
- The WHERE clause filters individual rows before grouping.
- The HAVING clause filters groups after the GROUP BY clause is applied.
- HAVING is typically used with aggregate functions, while WHERE is used with individual rows.

### 13. What are subqueries and when would you use them?
**Answer**: A subquery is a query nested inside another query. You would use subqueries when:
- You need to perform operations based on the results of another query
- You want to filter results based on aggregate values
- You need to compare values across different tables
- You want to create more readable queries by breaking down complex logic

## Advanced SQL Questions

### 14. Explain the concept of a transaction and ACID properties.
**Answer**: A transaction is a sequence of operations performed as a single logical unit of work. ACID properties ensure reliable processing of transactions:
- **Atomicity**: All operations in a transaction succeed or all are rolled back
- **Consistency**: A transaction brings the database from one valid state to another
- **Isolation**: Concurrent transactions don't interfere with each other
- **Durability**: Once a transaction is committed, it remains so even in case of system failure

### 15. What are common table expressions (CTEs) and how are they useful?
**Answer**: Common Table Expressions (CTEs) are temporary result sets that can be referenced within a SELECT, INSERT, UPDATE, or DELETE statement. They're useful for:
- Breaking down complex queries into simpler, more readable parts
- Creating recursive queries
- Using the same subquery multiple times in a single statement
- Improving query organization and maintainability

### 16. How would you optimize a slow SQL query?
**Answer**: To optimize a slow SQL query:
1. Add appropriate indexes to columns used in WHERE, JOIN, and ORDER BY clauses
2. Avoid using functions on indexed columns in WHERE clauses
3. Be specific in SELECT statements (avoid SELECT *)
4. Use JOINs instead of subqueries where possible
5. Limit the result set size with TOP, LIMIT, or FETCH
6. Consider denormalizing data for read-heavy operations
7. Use EXPLAIN or execution plans to analyze query performance
8. Rewrite complex queries to use more efficient logic

### 17. What is a deadlock and how can it be prevented?
**Answer**: A deadlock occurs when two or more transactions are waiting for each other to release locks, resulting in a standstill. Prevention methods include:
1. Access objects in the same order in all transactions
2. Keep transactions short and in a single batch
3. Use appropriate isolation levels
4. Add deadlock detection to applications
5. Use timeouts for transactions
6. Minimize lock contention by designing efficient queries

### 18. Explain window functions and their use cases.
**Answer**: Window functions perform calculations across a set of table rows related to the current row. They're useful for:
- Calculating running totals or moving averages
- Ranking results (ROW_NUMBER, RANK, DENSE_RANK)
- Accessing values from previous or following rows
- Performing aggregate calculations without collapsing rows
- Partitioning data for analysis within groups

### 19. What is the difference between correlated and non-correlated subqueries?
**Answer**:
- **Non-correlated subquery**: Runs independently of the outer query and is executed once
- **Correlated subquery**: References columns from the outer query and is executed once for each row processed by the outer query

### 20. How would you handle hierarchical or tree-structured data in SQL?
**Answer**: There are several approaches:
1. **Adjacency List Model**: Store parent-child relationships with foreign keys
2. **Nested Set Model**: Use left and right values to represent tree positions
3. **Path Enumeration**: Store the path from root to each node
4. **Closure Table**: Store all relationships between nodes
5. **Recursive CTEs**: Use recursive queries to traverse the hierarchy (available in modern SQL)

## SQL Problem Solving

### Problem 1: Find duplicate records
**Question**: How would you find duplicate records in a table?

**Answer**:
```sql
SELECT column_name, COUNT(column_name) as count
FROM table_name
GROUP BY column_name
HAVING COUNT(column_name) > 1;
```

### Problem 2: Second highest salary
**Question**: Write a query to find the second highest salary from an employees table.

**Answer**:
```sql
-- Using subquery
SELECT MAX(salary) 
FROM employees 
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Using ORDER BY and LIMIT
SELECT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;
```

### Problem 3: Department with highest average salary
**Question**: Write a query to find the department with the highest average salary.

**Answer**:
```sql
SELECT d.department_name, AVG(e.salary) as avg_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
ORDER BY avg_salary DESC
LIMIT 1;
```

### Problem 4: Update multiple rows conditionally
**Question**: How would you update salaries for all employees in a specific department by increasing them by 10%?

**Answer**:
```sql
UPDATE employees
SET salary = salary * 1.1
WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'IT');
```

### Problem 5: Pivot table query
**Question**: How would you create a pivot table showing the count of employees by department and job title?

**Answer**:
```sql
-- Using CASE statements (works in most databases)
SELECT 
    department_name,
    SUM(CASE WHEN job_title = 'Manager' THEN 1 ELSE 0 END) as managers,
    SUM(CASE WHEN job_title = 'Developer' THEN 1 ELSE 0 END) as developers,
    SUM(CASE WHEN job_title = 'Analyst' THEN 1 ELSE 0 END) as analysts
FROM employees e
JOIN departments d ON e.department_id = d.department_id
GROUP BY department_name;
```

## Database-Specific Questions

### SQLite-Specific Questions

1. **What are the main advantages of SQLite?**
   **Answer**: SQLite is serverless, requires zero configuration, is self-contained, and stores the entire database in a single cross-platform file. It's lightweight, reliable, and doesn't require installation or setup.

2. **What are the limitations of SQLite compared to other database systems?**
   **Answer**: SQLite has limited concurrency for write operations, lacks user management, has limited ALTER TABLE functionality, and doesn't enforce all constraints by default (like foreign keys). It's not suitable for high-volume websites or applications requiring multiple simultaneous write operations.

3. **How do you enable foreign key constraints in SQLite?**
   **Answer**: Foreign key constraints are disabled by default in SQLite. To enable them:
   ```sql
   PRAGMA foreign_keys = ON;
   ```
   This needs to be executed for each database connection.

## Tips for SQL Interviews

1. **Practice writing queries without an IDE**: Be comfortable writing SQL without auto-completion or syntax highlighting.

2. **Understand execution order**: Know the logical order of SQL operations (FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT).

3. **Be ready to explain your approach**: Interviewers often care more about your thought process than the exact syntax.

4. **Consider performance**: Think about how your queries would perform with large datasets.

5. **Ask clarifying questions**: Make sure you understand the problem before diving into a solution.

6. **Know your basics well**: Most SQL interviews focus heavily on JOINs, subqueries, and aggregate functions.

7. **Practice with real data**: Use sample databases like Northwind, Sakila, or AdventureWorks to practice realistic scenarios.
