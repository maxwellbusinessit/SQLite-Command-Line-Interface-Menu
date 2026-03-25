import sqlite3
from sys import excepthook


def create_or_reference_existing_database():
    connection = sqlite3.connect("menu_project.db")
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS students (
                                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           name TEXT,
                                                           grade TEXT,
                                                           email TEXT
                   ) """)
    connection.commit()
    connection.close()
    print("Database intialized!")
    print()
    print("Welcome to SQLite Database Management Menu!")
    print()

def add_student():
    student_name = input("What is the student's name? ")
    student_grade = input("What is the student's grade? ")
    student_email = input("What is the student's email? ")

    connection = sqlite3.connect("menu_project.db")
    cursor = connection.cursor()

    sql = """INSERT INTO students(name,grade,email)
             VALUES(?,?,?)"""

    cursor.execute(sql, (student_name, student_grade, student_email))
    connection.commit()
    connection.close()
    print()
    print("Student added successfuly!")

def view_student():
    student_name = input("What is the name of the student you would like to view? ")

    connection = sqlite3.connect("menu_project.db")
    cursor = connection.cursor()

    sql = """SELECT * FROM students WHERE name = (?)"""

    cursor.execute(sql, (student_name,))
    rows = cursor.fetchall()
    connection.close()

    if len(rows) == 0:
        print("No student found with this name")
    else:
        print("\n Student Record(s):")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Grade: {row[2]}, Email: {row[3]}")

def update_student():
    student_name = input("What is the name of the student who's record you would like to update? ")
    student_newname = input("What is the new name of the student? ")
    student_newgrade = input("What is the new grade of the student? ")
    student_newemail = input("What is the new email of the student? ")

    connection = sqlite3.connect("menu_project.db")
    cursor = connection.cursor()

    sql = """UPDATE students SET name = ?, grade = ?, email = ?
             WHERE name = ?"""

    cursor.execute(sql, (student_newname, student_newgrade, student_newemail, student_name))
    connection.commit()
    connection.close()
    print("Student record successfuly updated!")

def delete_student():
    student_name = input("What is the name of the student who's record you would like to delete? ")

    connection = sqlite3.connect("menu_project.db")
    cursor = connection.cursor()

    sql = """ DELETE FROM students WHERE name = ?"""

    cursor.execute(sql, (student_name,))
    connection.commit()
    print()
    print("Record(s) successfuly deleted!")
    connection.close()


def main():
    print()
    print("1 - Add a new student record")
    print("2 - View existing student records")
    print("3 - Update an existing student's information")
    print("4 - Delete an existing student's information")
    print("5 - Exit")
    print()
    response = input("What would you like to do? ")
    return response

try:
    create_or_reference_existing_database()
    while True:
        response = main()
        if response == "5":
            print()
            print("Goodbye!")
            break
        elif response == "1":
            add_student()
        elif response == "2":
            view_student()
        elif response == "3":
            update_student()
        elif response == "4":
            delete_student()
except:
    print("An exception occured!")



