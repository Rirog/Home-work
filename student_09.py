"""DZ09 student"""
from abc import ABC, abstractmethod


class Person(ABC):
    """ Создание абстрактного класса Person"""
    total_man = 0

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.total_man += 1

    @abstractmethod
    def display_info(self):
        pass


class Student(Person):
    """Реализация класса Student наследуещего абсрактынй класс Person"""
    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        self.grades = []

    def add_grade(self, grade):
        """Доюовление оценки студенту"""
        self.grades.append(grade)
        return f"Оценка успешно добавлена студенту {self.name}"

    @staticmethod
    def average_grade(grades):
        """Нахождение средней оценкки"""
        return sum(grades) / len(grades) if grades else 0

    def display_info(self):
        print(
            f"\nName: {self.name}"
            f"\nAge: {self.age}"
            f"\nAverage_grade: {self.average_grade(self.grades): .2f}"
            )

    def __str__(self):
        return (
            f"\nName: {self.name}, "
            f"Age: {self.age}, "
            f"Average_grade: {self.average_grade(self.grades): .2f}"
            )

    def __add__(self, grade):
        self.add_grade(grade)
        return self

    def __mul__(self, coefficient):
        return self.average_grade(self.grades) * coefficient


class GraduateStudent(Student):
    """Реализация класса GraduateStudent"""
    def __init__(self, name: str, age: int, topic: str):
        super().__init__(name, age)
        self.topic = topic

    def set_thesis_topic(self, thesis_topic):
        """Добовление дипломной работы"""
        self.topic = thesis_topic

    def display_info(self):
        super().display_info()
        print(f"Topic: {self.topic}")

    def __str__(self):
        super().__str__()
        return f", Topic: {self.topic}"

    @staticmethod
    def total_students():
        """Вывод общего количества студентов"""
        print(f"\nОбщее количество студентов: {Person.total_man}")


students = []


def add_student():
    """Добовление студента"""
    name = input("Введите имя студента: ")
    age = int(input("Введите возраст студента: "))
    is_graduate = input("Это выпускник? (да/нет): ").strip().lower()
    if is_graduate == "да":
        thesis = input("Введите тему дипломной работы: ")
        student = GraduateStudent(name, age, thesis)
    elif is_graduate == "нет":
        student = Student(name, age)
    else:
        print("Неверно введённый ответ")
        return
    students.append(student)
    print("Студент добавлен!\n")


def add_grade():
    """Добовление оценки студенту"""
    name = input("Введите имя студента: ")
    for student in students:
        if student.name == name:
            grade = float(input("Введите оценку: "))
            grade = student + grade
            print("Оценка добавлена!\n")
            return
    print("Студент не найден!\n")


def set_thesis():
    """Добавление дипломной работы"""
    name = input("Введите имя выпускника: ")
    for student in students:
        if isinstance(student, GraduateStudent) and student.name == name:
            thesis = input("Введите новую тему дипломной работы: ")
            student.set_thesis_topic(thesis)
            print("Тема дипломной работы обновлена!\n")
            return
    print("Выпускник не найден!\n")


def display_students():
    """Вывод студента"""
    for student in students:
        student.display_info()
    print()


def sort_students():
    """Сортировака студентов по средней  оценке"""
    sorted_students = sorted(students,
                             key=Student.average_grade,
                             reverse=True)
    for student in sorted_students:
        student.display_info()
    print()


def total_students():
    """Общее количесвто студентов"""
    GraduateStudent.total_students()


def show_string_representation():
    """Вывод строковое предстовление студента"""
    name = input("Введите имя студента: ")
    for student in students:
        if student.name == name:
            print(str(student) + "\n")
            return
    print("Студент не найден!\n")


MENU = {
    "1": add_student,
    "2": add_grade,
    "3": set_thesis,
    "4": display_students,
    "5": sort_students,
    "6": total_students,
    "7": show_string_representation,
    "0": exit
}


def menu():
    """Реализация меню"""
    while True:
        print("\nМеню:"
              "\n1. Добавить студента"
              "\n2. Добавить оценку студенту"
              "\n3. Добавить тему дипломной работы выпускнику"
              "\n4. Показать информацию о студентах"
              "\n5. Сортировать студентов по средней оценке"
              "\n6. Показать общее количество студентов"
              "\n7. Показать строковое представление студента"
              "\n0. Выйти")

        choice = input("Выберите действие: ")

        if MENU[choice]:
            MENU[choice]()
        else:
            print("Неверный ввод! Попробуйте снова.\n")


if __name__ == "__main__":
    menu()
