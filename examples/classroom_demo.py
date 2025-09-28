"""
SQL Classroom Demonstration Tool

This interactive script helps teachers demonstrate SQL concepts to students.
It provides a menu-based interface to run SQL examples from the tutorial.
"""

import sqlite3
import os
import time
import sys

class SQLDemo:
    def __init__(self):
        self.db_path = 'school.db'
        self.conn = None
        self.cursor = None
        
    def setup_database(self):
        """Create a fresh database with sample data"""
        # Delete the database if it already exists
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
            
        # Connect to the database
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
        # Enable foreign key support
        self.cursor.execute("PRAGMA foreign_keys = ON")
        
        print("\n=== Creating database structure ===")
        
        # Create tables
        self.cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            grade INTEGER,
            email TEXT UNIQUE
        )
        ''')
        print("✓ Created students table")
        
        self.cursor.execute('''
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            teacher TEXT,
            room TEXT,
            max_students INTEGER
        )
        ''')
        print("✓ Created courses table")
        
        self.cursor.execute('''
        CREATE TABLE enrollments (
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            course_id INTEGER,
            enrollment_date TEXT,
            grade TEXT,
            FOREIGN KEY (student_id) REFERENCES students (id),
            FOREIGN KEY (course_id) REFERENCES courses (id)
        )
        ''')
        print("✓ Created enrollments table")
        
        print("\n=== Inserting sample data ===")
        
        # Insert students
        self.cursor.execute('''
        INSERT INTO students (name, age, grade, email)
        VALUES 
            ('John Smith', 17, 12, 'john.smith@school.edu'),
            ('Sarah Johnson', 18, 12, 'sarah.j@school.edu'),
            ('Michael Wong', 17, 12, 'michael.w@school.edu'),
            ('Emma Brown', 16, 11, 'emma.b@school.edu'),
            ('David Lee', 16, 11, 'david.lee@school.edu'),
            ('Lisa Chen', 17, 11, 'lisa.c@school.edu'),
            ('James Wilson', 18, 12, 'james.w@school.edu'),
            ('Olivia Martinez', 16, 11, 'olivia.m@school.edu')
        ''')
        print("✓ Added 8 students")
        
        # Insert courses
        self.cursor.execute('''
        INSERT INTO courses (name, teacher, room, max_students)
        VALUES 
            ('Mathematics', 'Mr. Anderson', 'Room 101', 30),
            ('English Literature', 'Ms. Davis', 'Room 203', 25),
            ('Computer Science', 'Mrs. Wilson', 'Lab 3', 20),
            ('Physics', 'Dr. Brown', 'Lab 1', 24),
            ('History', 'Mr. Thompson', 'Room 105', 30)
        ''')
        print("✓ Added 5 courses")
        
        # Insert enrollments
        self.cursor.execute('''
        INSERT INTO enrollments (student_id, course_id, enrollment_date, grade)
        VALUES 
            (1, 1, '2023-09-01', 'A'),
            (1, 3, '2023-09-01', 'A-'),
            (2, 1, '2023-09-01', 'B+'),
            (2, 2, '2023-09-01', 'A'),
            (3, 1, '2023-09-01', 'B'),
            (3, 3, '2023-09-01', 'A'),
            (3, 4, '2023-09-01', 'B+'),
            (4, 2, '2023-09-01', 'A-'),
            (4, 5, '2023-09-01', 'B'),
            (5, 4, '2023-09-01', 'A'),
            (5, 5, '2023-09-01', 'B+'),
            (6, 1, '2023-09-01', 'A-'),
            (6, 2, '2023-09-01', 'B'),
            (7, 3, '2023-09-01', 'A'),
            (7, 4, '2023-09-01', 'A-'),
            (8, 2, '2023-09-01', 'B+'),
            (8, 5, '2023-09-01', 'A')
        ''')
        print("✓ Added 17 enrollments")
        
        self.conn.commit()
        print("\n✓ Database setup complete!")
    
    def connect(self):
        """Connect to the existing database"""
        if not os.path.exists(self.db_path):
            print(f"Database '{self.db_path}' does not exist. Creating it...")
            self.setup_database()
            return
            
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON")
    
    def close(self):
        """Close the database connection"""
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
    
    def execute_query(self, query, params=(), fetch=True, commit=False):
        """Execute a SQL query and return the results"""
        try:
            self.cursor.execute(query, params)
            
            if commit:
                self.conn.commit()
                
            if fetch:
                return self.cursor.fetchall()
            return None
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return None
    
    def display_results(self, results, headers=None):
        """Display query results in a formatted table"""
        if not results:
            print("No results found.")
            return
            
        # Get column names if not provided
        if not headers and self.cursor.description:
            headers = [column[0] for column in self.cursor.description]
        
        # Calculate column widths
        if headers:
            col_widths = [len(str(header)) for header in headers]
            for row in results:
                for i, cell in enumerate(row):
                    if i < len(col_widths):
                        col_widths[i] = max(col_widths[i], len(str(cell)))
        else:
            col_widths = [len(str(cell)) for cell in results[0]]
            
        # Print headers
        if headers:
            header_row = " | ".join(str(header).ljust(col_widths[i]) for i, header in enumerate(headers))
            print(header_row)
            print("-" * len(header_row))
        
        # Print data rows
        for row in results:
            row_str = " | ".join(str(cell).ljust(col_widths[i]) if i < len(col_widths) else str(cell) 
                                for i, cell in enumerate(row))
            print(row_str)
        
        print(f"\n{len(results)} rows returned.")
    
    def run_demo_query(self, title, query, params=(), commit=False):
        """Run a demo query with title and explanation"""
        print(f"\n=== {title} ===")
        print(f"SQL: {query}")
        
        results = self.execute_query(query, params, commit=commit)
        if results is not None:
            self.display_results(results)
            
        input("\nPress Enter to continue...")
    
    def show_table_info(self, table_name):
        """Show information about a table"""
        print(f"\n=== Table: {table_name} ===")
        
        # Get table schema
        schema = self.execute_query(f"SELECT sql FROM sqlite_master WHERE name = ?", (table_name,))
        if schema:
            print(f"Schema: {schema[0][0]}")
        
        # Get column info
        columns = self.execute_query(f"PRAGMA table_info({table_name})")
        if columns:
            print("\nColumns:")
            for col in columns:
                print(f"  {col[1]} ({col[2]}){' PRIMARY KEY' if col[5] else ''}{' NOT NULL' if col[3] else ''}")
        
        # Get row count
        count = self.execute_query(f"SELECT COUNT(*) FROM {table_name}")
        if count:
            print(f"\nRow count: {count[0][0]}")
        
        # Show sample data
        sample = self.execute_query(f"SELECT * FROM {table_name} LIMIT 5")
        if sample:
            print("\nSample data:")
            self.display_results(sample)
        
        input("\nPress Enter to continue...")
    
    def run_custom_query(self):
        """Allow the user to enter and run a custom SQL query"""
        print("\n=== Custom SQL Query ===")
        print("Enter your SQL query (type 'exit' to return to menu):")
        
        while True:
            query = input("\nSQL> ")
            
            if query.lower() == 'exit':
                break
                
            if not query.strip():
                continue
                
            try:
                commit_needed = any(keyword in query.upper() for keyword in ['INSERT', 'UPDATE', 'DELETE', 'DROP', 'CREATE', 'ALTER'])
                results = self.execute_query(query, fetch=not commit_needed, commit=commit_needed)
                
                if results is not None:
                    self.display_results(results)
                elif commit_needed:
                    print("Query executed successfully.")
            except Exception as e:
                print(f"Error: {e}")
    
    def show_menu(self):
        """Display the main menu"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n==== SQL Classroom Demo Tool ====\n")
        print("1. Setup/Reset Database")
        print("2. Show Table Information")
        print("3. Basic SELECT Demos")
        print("4. Filtering Demos")
        print("5. Ordering and Limiting Demos")
        print("6. Updating and Deleting Demos")
        print("7. Join Demos")
        print("8. Aggregate Function Demos")
        print("9. Run Custom SQL Query")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-9): ")
        return choice
    
    def show_table_menu(self):
        """Display the table selection menu"""
        print("\n=== Select a Table ===")
        print("1. students")
        print("2. courses")
        print("3. enrollments")
        print("4. Back to main menu")
        
        choice = input("\nEnter your choice (1-4): ")
        return choice
    
    def run_basic_select_demos(self):
        """Run basic SELECT statement demos"""
        demos = [
            ("Select all students", "SELECT * FROM students"),
            ("Select specific columns", "SELECT name, grade FROM students"),
            ("Select with condition", "SELECT * FROM students WHERE grade = 12"),
            ("Select with multiple conditions", "SELECT * FROM students WHERE grade = 12 AND age >= 18"),
        ]
        
        for title, query in demos:
            self.run_demo_query(title, query)
    
    def run_filtering_demos(self):
        """Run filtering demos"""
        demos = [
            ("Filter with equality", "SELECT * FROM students WHERE grade = 12"),
            ("Filter with comparison", "SELECT * FROM students WHERE age > 16"),
            ("Filter with LIKE", "SELECT * FROM students WHERE name LIKE 'J%'"),
            ("Filter with IN", "SELECT * FROM students WHERE grade IN (11, 12)"),
            ("Filter with AND", "SELECT * FROM students WHERE grade = 12 AND age >= 18"),
            ("Filter with OR", "SELECT * FROM students WHERE grade = 11 OR name LIKE 'J%'"),
            ("Filter with NULL", "SELECT * FROM students WHERE email IS NULL"),
        ]
        
        for title, query in demos:
            self.run_demo_query(title, query)
    
    def run_ordering_limiting_demos(self):
        """Run ordering and limiting demos"""
        demos = [
            ("Order by name (ascending)", "SELECT * FROM students ORDER BY name"),
            ("Order by age (descending)", "SELECT * FROM students ORDER BY age DESC"),
            ("Order by multiple columns", "SELECT * FROM students ORDER BY grade DESC, name ASC"),
            ("Limit results", "SELECT * FROM students LIMIT 3"),
            ("Limit with offset", "SELECT * FROM students LIMIT 3 OFFSET 2"),
        ]
        
        for title, query in demos:
            self.run_demo_query(title, query)
    
    def run_update_delete_demos(self):
        """Run update and delete demos"""
        # First, make a backup of the database
        self.conn.close()
        if os.path.exists(self.db_path):
            backup_path = f"{self.db_path}.bak"
            if os.path.exists(backup_path):
                os.remove(backup_path)
            import shutil
            shutil.copy2(self.db_path, backup_path)
        
        # Reconnect
        self.connect()
        
        demos = [
            ("Before update", "SELECT * FROM students WHERE id = 5"),
            ("Update a record", "UPDATE students SET age = 17 WHERE id = 5", None, True),
            ("After update", "SELECT * FROM students WHERE id = 5"),
            
            ("Before delete", "SELECT * FROM enrollments WHERE student_id = 8"),
            ("Delete records", "DELETE FROM enrollments WHERE student_id = 8", None, True),
            ("After delete", "SELECT * FROM enrollments WHERE student_id = 8"),
        ]
        
        for demo in demos:
            if len(demo) == 2:
                title, query = demo
                self.run_demo_query(title, query)
            else:
                title, query, params, commit = demo
                self.run_demo_query(title, query, params, commit)
        
        # Restore from backup
        self.conn.close()
        backup_path = f"{self.db_path}.bak"
        if os.path.exists(backup_path):
            os.remove(self.db_path)
            import shutil
            shutil.copy2(backup_path, self.db_path)
            os.remove(backup_path)
        
        # Reconnect
        self.connect()
        print("\nDatabase restored to original state.")
    
    def run_join_demos(self):
        """Run join demos"""
        demos = [
            ("Inner join example", """
                SELECT students.name, courses.name as course_name
                FROM students
                INNER JOIN enrollments ON students.id = enrollments.student_id
                INNER JOIN courses ON enrollments.course_id = courses.id
                ORDER BY students.name, courses.name
                LIMIT 10
            """),
            
            ("Left join example", """
                SELECT students.name, courses.name as course_name
                FROM students
                LEFT JOIN enrollments ON students.id = enrollments.student_id
                LEFT JOIN courses ON enrollments.course_id = courses.id
                ORDER BY students.name, courses.name
                LIMIT 10
            """),
            
            ("Find students in a specific course", """
                SELECT students.name
                FROM students
                JOIN enrollments ON students.id = enrollments.student_id
                JOIN courses ON enrollments.course_id = courses.id
                WHERE courses.name = 'Mathematics'
                ORDER BY students.name
            """),
            
            ("Find courses with no students", """
                SELECT courses.name
                FROM courses
                LEFT JOIN enrollments ON courses.id = enrollments.course_id
                WHERE enrollments.id IS NULL
            """),
        ]
        
        for title, query in demos:
            self.run_demo_query(title, query)
    
    def run_aggregate_demos(self):
        """Run aggregate function demos"""
        demos = [
            ("Count all students", "SELECT COUNT(*) FROM students"),
            
            ("Count students by grade", """
                SELECT grade, COUNT(*) as student_count
                FROM students
                GROUP BY grade
                ORDER BY grade
            """),
            
            ("Average age by grade", """
                SELECT grade, AVG(age) as average_age
                FROM students
                GROUP BY grade
                ORDER BY grade
            """),
            
            ("Course enrollment counts", """
                SELECT courses.name, COUNT(enrollments.id) as enrollment_count
                FROM courses
                LEFT JOIN enrollments ON courses.id = enrollments.course_id
                GROUP BY courses.id
                ORDER BY enrollment_count DESC
            """),
            
            ("Students with most courses", """
                SELECT students.name, COUNT(enrollments.id) as course_count
                FROM students
                LEFT JOIN enrollments ON students.id = enrollments.student_id
                GROUP BY students.id
                ORDER BY course_count DESC
            """),
        ]
        
        for title, query in demos:
            self.run_demo_query(title, query)
    
    def run(self):
        """Run the main application loop"""
        self.connect()
        
        while True:
            choice = self.show_menu()
            
            if choice == '0':
                break
            elif choice == '1':
                self.setup_database()
            elif choice == '2':
                table_choice = self.show_table_menu()
                if table_choice == '1':
                    self.show_table_info('students')
                elif table_choice == '2':
                    self.show_table_info('courses')
                elif table_choice == '3':
                    self.show_table_info('enrollments')
            elif choice == '3':
                self.run_basic_select_demos()
            elif choice == '4':
                self.run_filtering_demos()
            elif choice == '5':
                self.run_ordering_limiting_demos()
            elif choice == '6':
                self.run_update_delete_demos()
            elif choice == '7':
                self.run_join_demos()
            elif choice == '8':
                self.run_aggregate_demos()
            elif choice == '9':
                self.run_custom_query()
        
        self.close()

if __name__ == "__main__":
    demo = SQLDemo()
    demo.run()
