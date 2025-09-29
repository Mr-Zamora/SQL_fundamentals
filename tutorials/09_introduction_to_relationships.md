# 9. Introduction to Database Relationships

Now that you've mastered working with single tables, it's time to explore one of the most powerful aspects of relational databases: relationships between tables.

## Why Use Multiple Tables?

So far, we've stored all our data in single, independent tables. However, in real-world applications, data is often interconnected. For example:

- A student can enroll in multiple courses
- A teacher can teach multiple classes
- A product can belong to multiple categories

Using a single table for this kind of data would lead to:
- **Data redundancy**: The same information repeated in multiple rows
- **Update anomalies**: Changing data in one place but not others
- **Insert anomalies**: Unable to add certain data without adding other data
- **Delete anomalies**: Unintentionally losing data when deleting records

## Types of Relationships

There are three main types of relationships between tables:

### 1. One-to-One (1:1)

In a one-to-one relationship, each record in Table A is related to exactly one record in Table B, and vice versa.

**Example**: A student and their student ID card

```
Students Table:
id | name | age | grade
------------------------
1  | John | 17  | 12
2  | Sarah| 18  | 12

ID_Cards Table:
card_id | student_id | issue_date  | expiry_date
------------------------------------------------
101     | 1          | 2023-01-15  | 2024-01-15
102     | 2          | 2023-01-20  | 2024-01-20
```

One-to-one relationships are relatively rare and often used for:
- Splitting a large table into two for performance
- Separating frequently accessed data from rarely accessed data
- Storing optional information that doesn't apply to all records

### 2. One-to-Many (1:N)

In a one-to-many relationship, each record in Table A can be related to multiple records in Table B, but each record in Table B is related to only one record in Table A.

**Example**: A teacher and their courses

```
Teachers Table:
id | name        | subject
---------------------------
1  | Mr. Anderson| Mathematics
2  | Ms. Davis   | English

Courses Table:
id | name                | teacher_id | room
-------------------------------------------
1  | Algebra             | 1          | 101
2  | Calculus            | 1          | 102
3  | English Literature  | 2          | 203
4  | Creative Writing    | 2          | 204
```

One-to-many is the most common type of relationship in databases.

### 3. Many-to-Many (N:M)

In a many-to-many relationship, each record in Table A can be related to multiple records in Table B, and each record in Table B can be related to multiple records in Table A.

**Example**: Students and courses (a student can take multiple courses, and a course can have multiple students)

This requires a third table called a "junction table" or "bridge table":

```
Students Table:
id | name  | age | grade
-----------------------
1  | John  | 17  | 12
2  | Sarah | 18  | 12
3  | Mike  | 17  | 12

Courses Table:
id | name                | room
----------------------------
1  | Mathematics         | 101
2  | English Literature  | 203
3  | Computer Science    | Lab 3

Enrollments Table (Junction Table):
student_id | course_id | enrollment_date
---------------------------------------
1          | 1         | 2023-09-01
1          | 3         | 2023-09-01
2          | 1         | 2023-09-01
2          | 2         | 2023-09-01
3          | 2         | 2023-09-01
3          | 3         | 2023-09-01
```

## Primary and Foreign Keys

To establish relationships between tables, we use keys:

### Primary Key

A primary key is a column (or combination of columns) that uniquely identifies each row in a table. Primary keys:
- Must be unique
- Cannot be NULL
- Should rarely or never change
- Should be simple and efficient

Example: `id` in the Students table

### Foreign Key

A foreign key is a column in one table that refers to the primary key in another table. Foreign keys:
- Create a link between two tables
- Enforce referential integrity (ensuring related records exist)
- Can be NULL (if the relationship is optional)
- Can refer to the same table (self-referencing)

Example: `teacher_id` in the Courses table refers to `id` in the Teachers table

## Database Normalization

Normalization is the process of organizing data to reduce redundancy and improve data integrity. There are several "normal forms," but the first three are most common:

### First Normal Form (1NF)
- Each table cell should contain a single value
- Each record needs to be unique

### Second Normal Form (2NF)
- Must be in 1NF
- All non-key attributes depend on the entire primary key

### Third Normal Form (3NF)
- Must be in 2NF
- No transitive dependencies (non-key columns shouldn't depend on other non-key columns)

## Benefits of Proper Database Design

Using relationships between tables provides several advantages:
- **Reduced redundancy**: Data is stored in only one place
- **Data integrity**: Changes are made in one place and automatically reflected everywhere
- **Flexibility**: The database structure can evolve more easily
- **Efficiency**: Queries can be more efficient with properly indexed relationships

## Practice Exercise: Planning a Database

Design a database for a library with the following requirements:
1. Track books, authors, and members
2. A book can have multiple authors
3. A member can check out multiple books
4. Track when books are checked out and returned

Draw a diagram showing the tables and their relationships.

## Next Steps

Now that you understand the theory behind database relationships, in the next section we'll learn how to create tables with relationships using foreign keys.
