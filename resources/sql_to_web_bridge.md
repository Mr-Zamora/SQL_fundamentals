# Bridging SQL to Web Applications

This guide serves as a bridge between your SQL knowledge and web application development with Flask. It will help you understand how the SQL skills you've learned apply in the context of web applications.

## 1. Understanding Databases in Web Applications

### The Web Application Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│             │     │             │     │             │
│   Browser   │◄───►│  Web Server │◄───►│  Database   │
│   (Client)  │     │   (Flask)   │     │  (SQLite)   │
│             │     │             │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
    Request            Process            Store/Retrieve
    Response           Render             Data
```

In a web application:
1. The **client** (browser) sends requests to the server
2. The **server** (Flask) processes these requests
3. The server often needs to store or retrieve data from a **database** (SQLite)
4. The server sends a response back to the client

### Key Differences from Terminal SQL Usage

1. **Connections are temporary**: In web apps, database connections are opened when needed and closed afterward
2. **Multiple users**: Web apps handle many users simultaneously accessing the database
3. **Security concerns**: User input must be sanitized to prevent SQL injection attacks
4. **Performance matters**: Inefficient queries can slow down your entire application

## 2. Setting Up Flask with SQLite

### Basic Flask Setup

First, install Flask:
```bash
pip install flask
```

Create a basic Flask application structure:
```
my_flask_app/
├── app.py              # Main application file
├── schema.sql          # SQL schema definitions
├── static/             # Static files (CSS, JS)
├── templates/          # HTML templates
│   └── index.html
└── instance/           # Instance-specific data
    └── school.db       # SQLite database
```

### Creating the Database Connection

In your `app.py`:

```python
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # Required for flash messages

def get_db_connection():
    """Create a connection to the database."""
    conn = sqlite3.connect('instance/school.db')
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    return conn

def init_db():
    """Initialize the database with schema."""
    conn = get_db_connection()
    with open('schema.sql') as f:
        conn.executescript(f.read())
    conn.close()

@app.route('/')
def index():
    """Home page - show list of students."""
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)
```

### Database Schema

In `schema.sql`:

```sql
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS courses;
DROP TABLE IF EXISTS enrollments;

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade INTEGER,
    email TEXT UNIQUE
);

CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    teacher TEXT,
    room TEXT
);

CREATE TABLE enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    enrollment_date TEXT,
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (id)
);
```

### Basic Template

In `templates/index.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Student Database</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
        tr:nth-child(even) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <h1>Students</h1>
    
    {% if students %}
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Age</th>
            <th>Grade</th>
            <th>Email</th>
            <th>Actions</th>
        </tr>
        {% for student in students %}
        <tr>
            <td>{{ student['id'] }}</td>
            <td>{{ student['name'] }}</td>
            <td>{{ student['age'] }}</td>
            <td>{{ student['grade'] }}</td>
            <td>{{ student['email'] }}</td>
            <td>
                <a href="{{ url_for('view_student', id=student['id']) }}">View</a>
                <a href="{{ url_for('edit_student', id=student['id']) }}">Edit</a>
            </td>
        </tr>
        {% endfor %}
    </table>
    {% else %}
    <p>No students found.</p>
    {% endif %}
    
    <p><a href="{{ url_for('add_student') }}">Add New Student</a></p>
</body>
</html>
```

## 3. Implementing CRUD Operations

### Create: Adding New Records

```python
@app.route('/add', methods=('GET', 'POST'))
def add_student():
    """Add a new student to the database."""
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        
        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            # IMPORTANT: Use parameterized queries to prevent SQL injection
            conn.execute('INSERT INTO students (name, age, grade, email) VALUES (?, ?, ?, ?)',
                         (name, age, grade, email))
            conn.commit()
            conn.close()
            flash('Student added successfully!')
            return redirect(url_for('index'))
            
    return render_template('add_student.html')
```

### Read: Retrieving Records

```python
@app.route('/student/<int:id>')
def view_student(id):
    """View a single student's details."""
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    
    # Get the courses this student is enrolled in
    enrollments = conn.execute('''
        SELECT courses.name, courses.teacher, enrollments.enrollment_date
        FROM enrollments
        JOIN courses ON enrollments.course_id = courses.id
        WHERE enrollments.student_id = ?
    ''', (id,)).fetchall()
    
    conn.close()
    
    if student is None:
        flash('Student not found!')
        return redirect(url_for('index'))
        
    return render_template('student_detail.html', student=student, enrollments=enrollments)
```

### Update: Modifying Records

```python
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_student(id):
    """Edit a student's information."""
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    
    if student is None:
        flash('Student not found!')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        email = request.form['email']
        
        if not name:
            flash('Name is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE students SET name = ?, age = ?, grade = ?, email = ? WHERE id = ?',
                         (name, age, grade, email, id))
            conn.commit()
            conn.close()
            flash('Student updated successfully!')
            return redirect(url_for('index'))
            
    return render_template('edit_student.html', student=student)
```

### Delete: Removing Records

```python
@app.route('/delete/<int:id>', methods=('POST',))
def delete_student(id):
    """Delete a student."""
    conn = get_db_connection()
    
    # First delete related enrollments (maintain referential integrity)
    conn.execute('DELETE FROM enrollments WHERE student_id = ?', (id,))
    
    # Then delete the student
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    
    flash('Student deleted successfully!')
    return redirect(url_for('index'))
```

## 4. Best Practices for Databases in Web Applications

### Connection Management

**Bad Practice:**
```python
# Creating a new connection for every function
def get_students():
    conn = sqlite3.connect('school.db')
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return students

def get_courses():
    conn = sqlite3.connect('school.db')
    courses = conn.execute('SELECT * FROM courses').fetchall()
    conn.close()
    return courses
```

**Good Practice:**
```python
# Using a connection context manager
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('instance/school.db')
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
```

### Preventing SQL Injection

**Vulnerable Code:**
```python
# NEVER DO THIS!
@app.route('/search')
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    students = conn.execute(f"SELECT * FROM students WHERE name LIKE '%{query}%'").fetchall()
    conn.close()
    return render_template('search_results.html', students=students)
```

**Secure Code:**
```python
@app.route('/search')
def search():
    query = request.args.get('q')
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students WHERE name LIKE ?", (f'%{query}%',)).fetchall()
    conn.close()
    return render_template('search_results.html', students=students)
```

### Using Transactions

```python
@app.route('/enroll', methods=['POST'])
def enroll_student():
    student_id = request.form['student_id']
    course_ids = request.form.getlist('course_ids')
    
    conn = get_db_connection()
    try:
        # Start a transaction
        conn.execute('BEGIN')
        
        # Check if student exists
        student = conn.execute('SELECT id FROM students WHERE id = ?', (student_id,)).fetchone()
        if not student:
            raise ValueError("Student not found")
            
        # Process enrollments
        for course_id in course_ids:
            # Check if course exists
            course = conn.execute('SELECT id FROM courses WHERE id = ?', (course_id,)).fetchone()
            if not course:
                raise ValueError(f"Course {course_id} not found")
                
            # Check if already enrolled
            existing = conn.execute(
                'SELECT id FROM enrollments WHERE student_id = ? AND course_id = ?', 
                (student_id, course_id)
            ).fetchone()
            
            if not existing:
                conn.execute(
                    'INSERT INTO enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)',
                    (student_id, course_id, datetime.now().strftime('%Y-%m-%d'))
                )
        
        # Commit the transaction
        conn.commit()
        flash('Enrollment successful!')
        
    except Exception as e:
        # Roll back in case of error
        conn.rollback()
        flash(f'Error: {str(e)}')
        
    finally:
        conn.close()
        
    return redirect(url_for('view_student', id=student_id))
```

### Pagination for Large Datasets

```python
@app.route('/students')
def list_students():
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Number of items per page
    
    conn = get_db_connection()
    
    # Get total count
    total = conn.execute('SELECT COUNT(*) FROM students').fetchone()[0]
    
    # Get paginated results
    offset = (page - 1) * per_page
    students = conn.execute(
        'SELECT * FROM students LIMIT ? OFFSET ?', 
        (per_page, offset)
    ).fetchall()
    
    conn.close()
    
    # Calculate total pages
    total_pages = (total + per_page - 1) // per_page
    
    return render_template(
        'student_list.html',
        students=students,
        page=page,
        total_pages=total_pages
    )
```

## 5. Mini-Project: Student Management System

Let's build a simple student management system that demonstrates all these concepts.

### Project Structure

```
student_system/
├── app.py              # Main application file
├── schema.sql          # Database schema
├── init_db.py          # Script to initialize the database
├── static/
│   └── style.css       # CSS styles
└── templates/
    ├── base.html       # Base template
    ├── index.html      # Home page
    ├── students/
    │   ├── list.html   # List all students
    │   ├── view.html   # View student details
    │   ├── add.html    # Add new student
    │   └── edit.html   # Edit student
    └── courses/
        ├── list.html   # List all courses
        ├── view.html   # View course details
        └── add.html    # Add new course
```

### Implementation Steps

1. **Set up the Flask application**
   - Create the project structure
   - Install Flask
   - Create the basic app.py file

2. **Create the database schema**
   - Define tables for students, courses, and enrollments
   - Create indexes for frequently queried columns

3. **Implement student management**
   - List all students
   - View student details
   - Add new students
   - Edit existing students
   - Delete students

4. **Implement course management**
   - List all courses
   - View course details with enrolled students
   - Add new courses

5. **Implement enrollment management**
   - Enroll students in courses
   - View a student's course load
   - Remove students from courses

## 6. From SQL to ORM (Optional Advanced Topic)

While direct SQL is great for learning, many web applications use Object-Relational Mappers (ORMs) like SQLAlchemy to interact with databases.

### Example with SQLAlchemy

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///school.db'
db = SQLAlchemy(app)

# Define models
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    grade = db.Column(db.Integer)
    email = db.Column(db.String(100), unique=True)
    
    enrollments = db.relationship('Enrollment', backref='student', lazy=True)
    
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(100))
    room = db.Column(db.String(50))
    
    enrollments = db.relationship('Enrollment', backref='course', lazy=True)
    
class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.String(10))

# Create the database
with app.app_context():
    db.create_all()
```

### Using the ORM for CRUD Operations

```python
# Create
@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    age = request.form['age']
    grade = request.form['grade']
    email = request.form['email']
    
    new_student = Student(name=name, age=age, grade=grade, email=email)
    db.session.add(new_student)
    db.session.commit()
    
    return redirect(url_for('index'))

# Read
@app.route('/student/<int:id>')
def view_student(id):
    student = Student.query.get_or_404(id)
    return render_template('student_detail.html', student=student)

# Update
@app.route('/edit/<int:id>', methods=['POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.name = request.form['name']
    student.age = request.form['age']
    student.grade = request.form['grade']
    student.email = request.form['email']
    
    db.session.commit()
    return redirect(url_for('index'))

# Delete
@app.route('/delete/<int:id>', methods=['POST'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('index'))
```

## 7. Exercises

1. **Basic Flask Integration**
   - Create a Flask application that displays all students in a table
   - Add a page to display all courses

2. **Form Handling**
   - Create a form to add new students
   - Implement form validation

3. **Complete CRUD**
   - Implement edit and delete functionality for students
   - Add the ability to enroll students in courses

4. **Advanced Features**
   - Add search functionality to find students by name
   - Implement pagination for the student list
   - Create a dashboard showing statistics (students per grade, courses per teacher)

5. **Full Application**
   - Build a complete student management system
   - Include authentication so only authorized users can make changes
   - Add reporting features (e.g., class rosters, grade reports)

## 8. Resources for Further Learning

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLite with Flask Tutorial](https://flask.palletsprojects.com/en/2.0.x/tutorial/database/)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Web Application Security Fundamentals](https://owasp.org/www-project-top-ten/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Conclusion

You've now seen how the SQL skills you've learned can be applied in the context of web applications. The fundamental concepts remain the same, but the way you interact with the database changes to accommodate the web environment. As you continue to develop web applications, you'll find that a solid understanding of SQL is invaluable for creating efficient, secure, and scalable systems.

Remember that the connection between your web application and your database is a critical component of your system's architecture. Taking the time to design it well and follow best practices will pay dividends as your application grows in complexity and usage.
