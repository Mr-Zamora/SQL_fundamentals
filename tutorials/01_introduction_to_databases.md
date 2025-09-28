# 1. Introduction to Databases

## What is a Database?

A database is an organized collection of structured information or data, typically stored electronically in a computer system. Databases are designed to efficiently store, retrieve, and manage data.

Think of a database like a digital filing cabinet where information is stored in an organized way that makes it easy to find and use.

## Why We Use Databases

We use databases instead of simple files (like text files or spreadsheets) for several important reasons:

1. **Data Integrity**: Databases enforce rules to ensure data is accurate and consistent
2. **Efficient Storage**: They minimize data duplication and optimize storage
3. **Fast Retrieval**: Databases can quickly find and return specific information
4. **Concurrent Access**: Multiple users can access and modify data simultaneously
5. **Security**: Databases provide ways to control who can see or change different data
6. **Scalability**: They can handle growing amounts of data without performance issues
7. **Data Relationships**: Databases can represent connections between different pieces of information

## Database Structure: Tables, Rows, and Columns

Most databases you'll work with (including SQLite) are **relational databases**, which organize data into tables.

### Tables

- A table is like a spreadsheet with rows and columns
- Each table stores information about a specific type of entity (e.g., students, courses, teachers)
- Tables have a name that identifies them (e.g., "students")

### Columns (Fields)

- Columns represent attributes or properties of the entity
- Each column has a name and a data type that restricts what can be stored
- Example: In a "students" table, columns might include "name", "age", "grade", etc.

### Rows (Records)

- Each row contains data about one specific instance of the entity
- A row is a complete set of data for one item
- Example: One row in the "students" table would contain all information about a single student

## Visual Example

Here's how a simple "students" table might look:

| id | name           | age | grade |
|----|----------------|-----|-------|
| 1  | John Smith     | 17  | 12    |
| 2  | Sarah Johnson  | 18  | 12    |
| 3  | Michael Wong  | 17  | 12    |

In this example:
- The table name is "students"
- There are 4 columns: id, name, age, and grade
- There are 3 rows, each representing a different student
- The "id" column uniquely identifies each student

## Key Terms

- **Database**: The overall container for all your data
- **Table**: A collection of related data organized in rows and columns
- **Column/Field**: A single attribute of the data (e.g., name, age)
- **Row/Record**: A complete set of fields for one item
- **Cell**: The intersection of a row and column, containing a single piece of data
- **Primary Key**: A column (or columns) that uniquely identifies each row

In the next section, we'll learn how to set up SQLite and create our first database.
