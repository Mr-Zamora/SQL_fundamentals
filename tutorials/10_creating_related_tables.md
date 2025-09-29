# 10. Creating Related Tables

Now that you understand the concept of relationships between tables, let's learn how to implement them in SQLite using foreign keys.

## Enabling Foreign Key Support in SQLite

SQLite has foreign key support, but it's disabled by default. To enable it:

```sql
PRAGMA foreign_keys = ON;
```

You need to run this each time you connect to the database. In Python:

```python
import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON;")
```

## Creating Tables with Foreign Keys

### One-to-Many Relationship Example

Let's create two tables with a one-to-many relationship: teachers and courses (one teacher can teach multiple courses).

```sql
-- First, create the "parent" table (the "one" side)
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    subject TEXT NOT NULL,
    email TEXT UNIQUE
);

-- Then, create the "child" table with a foreign key (the "many" side)
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    room TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
);
```

The `FOREIGN KEY` constraint specifies that the `teacher_id` column in the courses table references the `id` column in the teachers table.

### Many-to-Many Relationship Example

For a many-to-many relationship, we need a junction table. Let's create tables for students, courses, and enrollments:

```sql
-- First table
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
);

-- Second table (we already created courses above)
-- CREATE TABLE courses (...)

-- Junction table for the many-to-many relationship
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    grade TEXT,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

Notice that the junction table:
- Has foreign keys to both related tables
- Often has a composite primary key (combination of both foreign keys)
- Can contain additional information about the relationship (enrollment date, grade)

### One-to-One Relationship Example

For a one-to-one relationship, we can use a unique constraint on the foreign key:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER
);

CREATE TABLE student_details (
    student_id INTEGER PRIMARY KEY,
    address TEXT,
    phone TEXT,
    parent_name TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id)
);
```

By making `student_id` the primary key in the `student_details` table, we ensure that each student can have at most one record in this table.

## Foreign Key Actions

You can specify what happens when a referenced record is deleted or updated:

```sql
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
```

The available actions are:
- `CASCADE`: Automatically delete or update the referencing rows
- `SET NULL`: Set the referencing columns to NULL
- `SET DEFAULT`: Set the referencing columns to their default values
- `RESTRICT`: Prevent the deletion or update if there are referencing rows
- `NO ACTION`: Similar to RESTRICT, but checked after other constraints

## Self-Referencing Tables

A table can reference itself, which is useful for hierarchical data:

```sql
CREATE TABLE employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    title TEXT,
    manager_id INTEGER,
    FOREIGN KEY (manager_id) REFERENCES employees (id)
);
```

This allows each employee to have a manager who is also an employee.

## Checking Referential Integrity

When you try to insert data that violates a foreign key constraint, SQLite will prevent it:

```sql
-- This will fail if there's no teacher with id = 999
INSERT INTO courses (name, teacher_id) VALUES ('Physics', 999);
```

The error message will be something like:
```
FOREIGN KEY constraint failed
```

## Viewing Table Relationships

To see the structure of your tables including foreign keys:

```sql
.schema table_name
```

## Practice Exercise: Creating Related Tables

1. Create a `publishers` table with columns for id, name, and location
2. Create a `books` table with columns for id, title, year, and publisher_id (foreign key to publishers)
3. Create an `authors` table with columns for id, name, and birth_year
4. Create a `book_authors` junction table to represent the many-to-many relationship between books and authors

## Next Steps

Now that you've created tables with relationships, in the next section we'll learn how to work with data across multiple related tables using JOINs.
