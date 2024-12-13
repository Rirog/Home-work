"""13 DZ"""
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Модели данных
class Person(BaseModel):
    """Создание базовой модели данных"""
    name: str
    age: int


class Student(Person):
    """Класс Student, наследуемый от класса Person"""
    grades: list[int] = []


class GraduateStudent(Person):
    """Класс Student, наследуемый от Person"""
    thesis_topic: str


# Хранилище данных
students = {}


# Эндпоинт для добавления нового студента
@app.post("/students/")
def create_student(student: Union[Student, GraduateStudent]):
    """Создает нового студента"""
    student_id_counter = 1
    student_id = student_id_counter
    student_id_counter += 1

    if isinstance(student, GraduateStudent):
        students[student_id] = {
            "name": student.name,
            "age": student.age,
            "grades": [],
            "thesis_topic": student.thesis_topic,
        }
    else:
        students[student_id] = {
            "name": student.name,
            "age": student.age,
            "grades": student.grades,
            "thesis_topic": None,
        }

    return {"id": student_id, "message": "Student added successfully"}


# Эндпоинт для добавления оценки студенту
@app.put("/students/{student_id}/grades/")
def add_grade(student_id: int, grade: int):
    """Добавляет оценку студенту"""
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id]["grades"].append(grade)
    return {"message": "Grade added successfully"}


# Эндпоинт для получения списка студентов, отсортированных по средней оценке
@app.get("/students/")
def get_students_sorted_by_average_grade():
    """Возращает список студентов, отсортированных по средней оценке"""
    sorted_students = sorted(
        students.values(),
        key=lambda x:
        sum(x["grades"]) / len(x["grades"]) if x["grades"] else 0,
        reverse=True,
    )

    return [
        {
            "name": student["name"],
            "age": student["age"],
            "average_grade":
            sum(student["grades"]) / len(student["grades"])
            if student["grades"] else 0,
            "thesis_topic": student["thesis_topic"],
        }
        for student in sorted_students
    ]


@app.get("/students/{student_id}")
def get_student(student_id: int):
    """Возвращение информации о студенте"""
    student = students[student_id]
    return {
        "name": student["name"],
        "age": student["age"],
        "grades": student["grades"],
        "thesis_topic": student["thesis_topic"],
    }

