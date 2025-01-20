"""13 DZ"""
from typing import Union, Dict

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()



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


students = {}


@app.post("/students/")
async def create_student(student: Union[Student, GraduateStudent]):
    """Создает нового студента"""
    student_id = len(students) + 1
    students[student_id] = student

    return {"id": student_id, "message": "Student added successfully"}



@app.put("/students/{student_id}/grades/")
async def add_grade(student_id: int, grade: int):
    """Добавляет оценку студенту"""
    if student_id not in students:
        return {"error": "Student not found"}
    students[student_id].grades.append(grade)
    return {"message": "Grade added successfully"}



@app.get("/students/")
async def get_students_sorted_by_average_grade():
    """Возращает список студентов, отсортированных по средней оценке"""
    student: Union[Student, GraduateStudent]
    sorted_students = sorted(
        students.values(),
       key=lambda student: (
            sum(student.grades) / len(student.grades) if isinstance(student, Student) and student.grades else 0
        ),
        reverse=True,
    )

    return [ student.dict()
        for student in sorted_students]



@app.get("/students/{student_id}")
async def get_student(student_id: int):
    """Возвращение информации о студенте"""
    student: Union[Student, GraduateStudent] = students[student_id]
    return student.model_dump()
