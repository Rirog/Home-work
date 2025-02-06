"""13 DZ"""
from typing import Union, Optional, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()


class Person(BaseModel):
    """Создание базовой модели данных"""
    name: str
    age: int


class Student(Person):
    """Класс Student, наследуемый от класса Person"""
    grades: Optional[List[int]] = []


class GraduateStudent(Student):
    """Класс GraduateStudent, наследуемый от Person"""
    thesis_topic: Optional[str] = None


class CreateStudent(BaseModel):
    """Создания метода для валидации ответов """
    id: int
    messege: str

students = {}

def avarage_grare(student: Union[Student, GraduateStudent]):
    """Функция для сортировки студентов по средней оценке"""
    return sum(student.grades) / len(student.grades) if student.grades else 0


@app.post("/students/", response_model=CreateStudent)
async def create_student(student: Union[Student, GraduateStudent]):
    """Создает нового студента"""
    student_id = len(students) + 1
    students[student_id] = student
    return CreateStudent(id=student_id, message='Student added successfully')


@app.put("/students/{student_id}/grades/")
async def add_grade(student_id: int, grade: int):
    """Добавляет оценку студенту"""
    if student_id not in students:
        return {"error": "Student not found"}
    if isinstance(students[student_id], GraduateStudent):
        raise HTTPException(status_code=400,
                            detail="error: A graduate cannot be given a grade")
    students[student_id].grades.append(grade)
    return {"message": "Grade added successfully"}


@app.get("/students/")
async def get_students_sorted_by_average_grade():
    """Возращает список студентов, отсортированных по средней оценке"""
    sorted_students = sorted(students.values(),
                             key=avarage_grare,
                             reverse=True)

    return [student.dict()
            for student in sorted_students]
