# 12. Using SQL with Python: ORMs vs. Raw SQL

Now that you've learned how to work with SQL directly, let's explore how to integrate SQL with Python applications. There are two main approaches: using raw SQL queries or using an Object-Relational Mapper (ORM).

## Approaches to Database Access in Python

When working with databases in Python, you have two primary options:

1. **Raw SQL**: Writing SQL queries directly and using a database driver
2. **ORM (Object-Relational Mapping)**: Using Python objects that map to database tables

Let's explore both approaches using our school database as an example.

## Raw SQL with Python

Using raw SQL gives you direct control over your queries and can be implemented with Python's built-in `sqlite3` module:

```python
import sqlite3

# Connect to the database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Execute a query with parameters (safe from SQL injection)
def get_students_by_grade(grade):
    cursor.execute("SELECT * FROM students WHERE grade = ?", (grade,))
    return cursor.fetchall()

# Create a new student
def create_student(name, age, grade):
    cursor.execute(
        "INSERT INTO students (name, age, grade) VALUES (?, ?, ?)",
        (name, age, grade)
    )
    conn.commit()
    return cursor.lastrowid

# Update a student's grade
def update_student_grade(student_id, new_grade):
    cursor.execute(
        "UPDATE students SET grade = ? WHERE id = ?",
        (new_grade, student_id)
    )
    conn.commit()

# Delete a student
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()

# Example usage
students_in_grade_12 = get_students_by_grade(12)
for student in students_in_grade_12:
    print(student)

# Always close the connection when done
conn.close()
```

### Advantages of Raw SQL

1. **Full Control**: You have complete control over the SQL being executed
2. **Performance**: Direct SQL can be optimized for specific database engines
3. **Transparency**: It's clear exactly what SQL is being executed
4. **Database-Specific Features**: You can use features specific to your database

### Disadvantages of Raw SQL

1. **Boilerplate Code**: You need to write more code for basic operations
2. **SQL Injection Risk**: You must carefully parameterize queries
3. **Database Coupling**: Your code is more tightly coupled to a specific database
4. **Manual Object Mapping**: You need to manually convert between SQL rows and Python objects

## Object-Relational Mapping (ORM)

ORMs provide a higher-level abstraction, allowing you to work with database tables as Python classes and rows as objects. Let's see how our school database might look using SQLAlchemy, a popular Python ORM:

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Create the engine and base class
engine = create_engine('sqlite:///school.db')
Base = declarative_base()

# Define models (Python classes that map to database tables)
class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    grade = Column(Integer)
    
    # Define relationship to enrollments
    enrollments = relationship("Enrollment", back_populates="student")
    
    def __repr__(self):
        return f"<Student(name='{self.name}', age={self.age}, grade={self.grade})>"

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    
    # Define relationships
    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    
    def __repr__(self):
        return f"<Course(name='{self.name}')>"

class Teacher(Base):
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    subject = Column(String)
    email = Column(String)
    
    # Define relationship to courses
    courses = relationship("Course", back_populates="teacher")
    
    def __repr__(self):
        return f"<Teacher(name='{self.name}', subject='{self.subject}')>"

class Enrollment(Base):
    __tablename__ = 'enrollments'
    
    student_id = Column(Integer, ForeignKey('students.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'), primary_key=True)
    enrollment_date = Column(String)
    
    # Define relationships
    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    
    def __repr__(self):
        return f"<Enrollment(student_id={self.student_id}, course_id={self.course_id})>"

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Query examples
def get_students_by_grade(grade):
    return session.query(Student).filter(Student.grade == grade).all()

# Create a new student
def create_student(name, age, grade):
    student = Student(name=name, age=age, grade=grade)
    session.add(student)
    session.commit()
    return student.id

# Update a student's grade
def update_student_grade(student_id, new_grade):
    student = session.query(Student).get(student_id)
    if student:
        student.grade = new_grade
        session.commit()

# Delete a student
def delete_student(student_id):
    student = session.query(Student).get(student_id)
    if student:
        session.delete(student)
        session.commit()

# Example usage
students_in_grade_12 = get_students_by_grade(12)
for student in students_in_grade_12:
    print(student)

# Complex query example: Find all students enrolled in a specific course
def students_in_course(course_name):
    return session.query(Student).\
        join(Enrollment).\
        join(Course).\
        filter(Course.name == course_name).\
        all()

math_students = students_in_course("Mathematics")
for student in math_students:
    print(student)
```

### Advantages of ORMs

1. **Productivity**: Less code for common operations
2. **Object-Oriented**: Work with Python objects instead of SQL rows
3. **Database Independence**: Easier to switch between different database systems
4. **Safety**: Reduced risk of SQL injection
5. **Validation**: Many ORMs include data validation features
6. **Relationships**: Easier to work with related tables

### Disadvantages of ORMs

1. **Performance Overhead**: Slight performance cost compared to optimized raw SQL
2. **Learning Curve**: Need to learn the ORM's API
3. **Complex Queries**: Some complex queries can be harder to express
4. **Black Box**: Less visibility into the actual SQL being generated

## When to Use Each Approach

### Consider Raw SQL When:

- You need maximum performance for complex queries
- You're working with database-specific features
- You're writing analytical queries or reports
- You need complete control over indexing or query optimization

### Consider ORM When:

- You want to increase developer productivity
- Your application needs to work with multiple database systems
- You're building a typical CRUD (Create, Read, Update, Delete) application
- You have complex object relationships to manage

## Hybrid Approach

Many applications use a hybrid approach:

```python
# Using SQLAlchemy ORM for most operations
students = session.query(Student).filter(Student.grade == 12).all()

# But dropping to raw SQL for complex analytics
from sqlalchemy import text
result = session.execute(text("""
    SELECT 
        courses.name, 
        COUNT(enrollments.student_id) as student_count,
        AVG(students.age) as avg_age
    FROM courses
    JOIN enrollments ON courses.id = enrollments.course_id
    JOIN students ON enrollments.student_id = students.id
    GROUP BY courses.name
    HAVING COUNT(enrollments.student_id) > 5
    ORDER BY student_count DESC
"""))

for row in result:
    print(f"Course: {row.name}, Students: {row.student_count}, Avg Age: {row.avg_age}")
```

This gives you the best of both worlds: the productivity of an ORM for routine operations and the power of raw SQL for complex queries.

## Practice Exercise: Working with the School Database in Python

1. Install SQLAlchemy: `pip install sqlalchemy`
2. Create Python classes for the students, teachers, and courses tables
3. Write functions to:
   - List all students in a specific grade
   - Add a new course
   - Enroll a student in a course
   - Find all courses taught by a specific teacher
4. Try implementing the same functionality using both raw SQL and an ORM

## Next Steps

Now that you know how to integrate SQL with Python applications, in the next section we'll explore advanced SQL topics and additional resources for continuing your SQL journey.
