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
            python_marks REAL DEFAULT 0,
            database_marks REAL DEFAULT 0,
            math_marks REAL DEFAULT 0,
            english_marks REAL DEFAULT 0,
            computer_marks REAL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_table()
    print("Database created successfully!")
