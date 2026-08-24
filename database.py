import sqlite3


DATABASE_NAME = "students.db"


def connect_database():
    return sqlite3.connect(DATABASE_NAME)


def create_table():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            course TEXT NOT NULL,
            python_marks REAL NOT NULL,
            database_marks REAL NOT NULL,
            math_marks REAL NOT NULL,
            english_marks REAL NOT NULL,
            computer_marks REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_student(
    name,
    age,
    course,
    python_marks,
    database_marks,
    math_marks,
    english_marks,
    computer_marks
):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students (
            name,
            age,
            course,
            python_marks,
            database_marks,
            math_marks,
            english_marks,
            computer_marks
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        name,
        age,
        course,
        python_marks,
        database_marks,
        math_marks,
        english_marks,
        computer_marks
    ))

    connection.commit()
    connection.close()


def get_all_students():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        ORDER BY id
    """)

    students = cursor.fetchall()

    connection.close()

    return students


def search_student(keyword):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM students
        WHERE name LIKE ? OR id = ?
    """, (f"%{keyword}%", keyword))

    students = cursor.fetchall()

    connection.close()

    return students


def update_student(
    student_id,
    name,
    age,
    course,
    python_marks,
    database_marks,
    math_marks,
    english_marks,
    computer_marks
):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET
            name = ?,
            age = ?,
            course = ?,
            python_marks = ?,
            database_marks = ?,
            math_marks = ?,
            english_marks = ?,
            computer_marks = ?
        WHERE id = ?
    """, (
        name,
        age,
        course,
        python_marks,
        database_marks,
        math_marks,
        english_marks,
        computer_marks,
        student_id
    ))

    connection.commit()

    updated = cursor.rowcount

    connection.close()

    return updated


def delete_student(student_id):
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM students
        WHERE id = ?
    """, (student_id,))

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    return deleted


if __name__ == "__main__":
    create_table()
    print("Database created successfully!")
