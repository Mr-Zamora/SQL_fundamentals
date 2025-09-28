# Visual SQL Guide

## SQL Command Categories

```
SQL Commands
│
├── Data Definition Language (DDL)
│   ├── CREATE - Create database objects (tables, indexes, etc.)
│   ├── ALTER - Modify database objects
│   ├── DROP - Delete database objects
│   └── TRUNCATE - Remove all records from a table
│
├── Data Manipulation Language (DML)
│   ├── SELECT - Retrieve data from tables
│   ├── INSERT - Add new records
│   ├── UPDATE - Modify existing records
│   └── DELETE - Remove records
│
├── Data Control Language (DCL)
│   ├── GRANT - Give privileges to users
│   └── REVOKE - Take away privileges
│
└── Transaction Control
    ├── BEGIN TRANSACTION - Start a transaction
    ├── COMMIT - Save changes
    └── ROLLBACK - Undo changes
```

## Database Structure Hierarchy

```
Database
│
├── Tables
│   │
│   ├── Columns (Fields)
│   │   │
│   │   ├── Data Types
│   │   │   ├── INTEGER
│   │   │   ├── TEXT
│   │   │   ├── REAL
│   │   │   ├── BLOB
│   │   │   └── NULL
│   │   │
│   │   └── Constraints
│   │       ├── PRIMARY KEY
│   │       ├── FOREIGN KEY
│   │       ├── UNIQUE
│   │       ├── NOT NULL
│   │       ├── CHECK
│   │       └── DEFAULT
│   │
│   └── Rows (Records)
│
├── Indexes
│
└── Views
```

## SELECT Statement Structure

```
SELECT column1, column2, ...
FROM table_name
[JOIN table_name ON condition]
[WHERE condition]
[GROUP BY column]
[HAVING condition]
[ORDER BY column ASC|DESC]
[LIMIT number [OFFSET number]]
```

## Table Relationships

```
┌───────────┐     ┌────────────────┐     ┌───────────┐
│ Students  │     │  Enrollments   │     │  Courses  │
├───────────┤     ├────────────────┤     ├───────────┤
│ id (PK)   │◄────┤ student_id (FK)│     │ id (PK)   │
│ name      │     │ course_id (FK) ├────►│ name      │
│ age       │     │ enrollment_date│     │ teacher   │
│ grade     │     │ grade          │     │ room      │
└───────────┘     └────────────────┘     └───────────┘
```

## Common SQL Query Patterns

### Basic CRUD Operations

**Create (INSERT)**
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Read (SELECT)**
```sql
SELECT * FROM table_name WHERE condition;
```

**Update (UPDATE)**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

**Delete (DELETE)**
```sql
DELETE FROM table_name WHERE condition;
```

### JOIN Types Visualization

```
Table A       Table B
┌───┬───┐    ┌───┬───┐
│ 1 │ A │    │ 1 │ X │
│ 2 │ B │    │ 3 │ Y │
│ 3 │ C │    │ 5 │ Z │
└───┴───┘    └───┴───┘

INNER JOIN:
┌───┬───┬───┐
│ 1 │ A │ X │
│ 3 │ C │ Y │
└───┴───┴───┘

LEFT JOIN:
┌───┬───┬───┐
│ 1 │ A │ X │
│ 2 │ B │   │
│ 3 │ C │ Y │
└───┴───┴───┘

RIGHT JOIN:
┌───┬───┬───┐
│ 1 │ A │ X │
│ 3 │ C │ Y │
│   │   │ Z │
└───┴───┴───┘

FULL OUTER JOIN:
┌───┬───┬───┐
│ 1 │ A │ X │
│ 2 │ B │   │
│ 3 │ C │ Y │
│   │   │ Z │
└───┴───┴───┘
```

## SQL Query Execution Order

```
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → DISTINCT → ORDER BY → LIMIT
```

1. **FROM/JOIN**: First, the database determines which tables to query and how they're joined
2. **WHERE**: Filters rows based on conditions
3. **GROUP BY**: Groups rows with the same values
4. **HAVING**: Filters groups based on conditions
5. **SELECT**: Determines which columns to include in the result
6. **DISTINCT**: Removes duplicate rows
7. **ORDER BY**: Sorts the result
8. **LIMIT/OFFSET**: Limits the number of rows returned

## Common SQL Functions

### Aggregate Functions
- **COUNT()** - Counts rows
- **SUM()** - Adds values
- **AVG()** - Calculates average
- **MIN()** - Finds minimum value
- **MAX()** - Finds maximum value

### String Functions
- **UPPER()** - Converts to uppercase
- **LOWER()** - Converts to lowercase
- **LENGTH()** - Returns string length
- **SUBSTR()** - Extracts substring

### Date Functions
- **DATE()** - Converts to date
- **TIME()** - Converts to time
- **DATETIME()** - Converts to datetime
- **strftime()** - Formats date/time

## Database Normalization

### First Normal Form (1NF)
- Each table cell should contain a single value
- Each record needs to be unique

### Second Normal Form (2NF)
- Must be in 1NF
- All non-key attributes depend on the entire primary key

### Third Normal Form (3NF)
- Must be in 2NF
- No transitive dependencies (non-key columns shouldn't depend on other non-key columns)

## SQLite vs Other Database Systems

| Feature | SQLite | MySQL | PostgreSQL |
|---------|--------|-------|------------|
| Server | No (file-based) | Yes | Yes |
| Configuration | Minimal | Moderate | Complex |
| Concurrency | Limited | Good | Excellent |
| Data Types | Dynamic | Strict | Strict & Extensible |
| Best For | Learning, Small apps, Embedded | Web apps, Medium-sized apps | Large apps, Complex data |
