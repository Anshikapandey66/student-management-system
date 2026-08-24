from database import create_table, add_student


def add_student_menu():
    print("\n========== ADD STUDENT ==========")

    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    print("\nEnter marks:")

    python_marks = float(input("Python: "))
    database_marks = float(input("Database: "))
    math_marks = float(input("Math: "))
    english_marks = float(input("English: "))
    computer_marks = float(input("Computer: "))

    add_student(
        name,
        age,
        course,
        python_marks,
        database_marks,
        math_marks,
        english_marks,
        computer_marks
    )

    print("\nStudent added successfully! ✅")


def main():
    create_table()

    print("=" * 40)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 40)

    add_student_menu()


if __name__ == "__main__":
    main()
