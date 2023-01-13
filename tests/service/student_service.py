from tests.domain.student import Student


def find_student_by_id(id: int) -> Student:
    # query database
    return Student(1, "Tom")


def save_student(student: Student) -> None:
    pass


def change_name(student_id: int, name: str) -> None:
    if student := find_student_by_id(student_id):
        student.name = name
        save_student(student)
