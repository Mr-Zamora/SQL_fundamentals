# 11. Database Design Basics

Good database design is crucial for creating efficient, maintainable, and scalable applications. In this section, we'll cover the fundamental concepts of database design.

## What is a Primary Key?

A primary key is a column (or combination of columns) that uniquely identifies each row in a table. Primary keys:

- Must be unique (no two rows can have the same primary key value)
- Cannot be NULL
- Should rarely or never change
- Should be simple and efficient

### Creating a Table with a Primary Key

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
);
```

In SQLite, `INTEGER PRIMARY KEY` automatically becomes an auto-incrementing column.

### Composite Primary Keys

Sometimes a single column isn't enough to uniquely identify a row. In these cases, you can use multiple columns as a composite primary key:

```sql
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    grade TEXT,
    PRIMARY KEY (student_id, course_id)
);
```

This means a student cannot be enrolled in the same course twice.

## Foreign Keys

Foreign keys establish relationships between tables by referencing the primary key of another table:

```sql
CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

This creates a relationship where:
- Each enrollment must reference a valid student
- Each enrollment must reference a valid course

### Enabling Foreign Key Support in SQLite

SQLite has foreign key support, but it's disabled by default. To enable it:

```sql
PRAGMA foreign_keys = ON;
```

You need to run this each time you connect to the database.

## Naming Conventions

Consistent naming makes your database easier to understand and maintain:

### Table Names

- Use plural nouns (students, courses, enrollments)
- Use lowercase with underscores for multi-word names (course_materials)
- Be descriptive but concise

### Column Names

- Use singular nouns (name, age, enrollment_date)
- Use lowercase with underscores for multi-word names (first_name)
- Use id for primary keys
- Use table_name_id for foreign keys (student_id, course_id)

## Normalization Basics

Normalization is the process of organizing data to reduce redundancy and improve data integrity.

### First Normal Form (1NF)

- Each table cell should contain a single value
- Each record needs to be unique

Bad design:
```
| student_id | name      | courses                |
|------------|-----------|------------------------|
| 1          | John      | Math, Science, English |
```

Better design (1NF):
```
| student_id | name | course  |
|------------|------|---------|
| 1          | John | Math    |
| 1          | John | Science |
| 1          | John | English |
```

### Second Normal Form (2NF)

- Must be in 1NF
- All non-key attributes depend on the entire primary key

### Third Normal Form (3NF)

- Must be in 2NF
- No transitive dependencies (non-key columns shouldn't depend on other non-key columns)

## One Table vs. Multiple Tables

### When to Use a Single Table

Use a single table when:
- The data is simple and self-contained
- There are no repeating groups of data
- The data doesn't need to be shared with other entities

Example: A simple todo list might just need one table.

### When to Use Multiple Tables

Use multiple tables when:
- Data would be duplicated across rows
- Different types of entities are involved
- You need to represent one-to-many or many-to-many relationships

Example: Our school database uses multiple tables because:
- A student can enroll in multiple courses
- A course can have multiple students
- We don't want to repeat student information for each course they take

## Common Database Relationships

### One-to-One

One record in table A relates to exactly one record in table B.

Example: A student and their student_details:
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE student_details (
    student_id INTEGER PRIMARY KEY,
    address TEXT,
    phone TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id)
);
```

### One-to-Many

One record in table A relates to multiple records in table B.

Example: A teacher and their courses:
```sql
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
```

### Many-to-Many

Multiple records in table A relate to multiple records in table B. This requires a junction table.

Example: Students and courses (as we've seen with enrollments):
```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

## Practice Exercise: Design a School Database

Design a database for a school with the following requirements:
1. Track students, teachers, courses, and departments
2. Students can enroll in multiple courses
3. Each course has one teacher
4. Each teacher belongs to one department
5. Track student grades for each course
6. Store contact information for students and teachers

## Next Steps

Now that you understand the basics of database design, in the next section we'll explore some advanced topics and next steps for your SQL journey.
