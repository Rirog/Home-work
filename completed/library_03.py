"""Создание библиотеки"""
class Book:
    """Класс для представления физической книги в библиотеке."""
    def __init__(self, title, author, year, pages):
        """Инициализация атрибутов книги."""
        self.__title = title
        self.__author = author
        self.__year = year
        self.__pages = pages
        self.__availability = True

    @property
    def title(self):
        """Возвращает название книги."""
        return self.__title

    @title.setter
    def title(self, new_title):
        """Устанавливает название книги."""
        self.__title = new_title

    @property
    def author(self):
        """Возвращает автора книги."""
        return self.__author

    @author.setter
    def author(self, new_author):
        """Устанавливает автора книги."""
        self.__author = new_author

    @property
    def year(self):
        """Возвращает год издания книги."""
        return self.__year

    @year.setter
    def year(self, new_year):
        """Устанавливает год издания книги."""
        self.__year = new_year

    @property
    def pages(self):
        """Возвращает количество страниц в книге."""
        return self.__pages

    @pages.setter
    def pages(self, new_pages):
        """Устанавливает количество страниц в книге."""
        self.__pages = new_pages

    @property
    def availability(self):
        """Возвращает доступность книги."""
        return self.__availability

    @availability.setter
    def availability(self, new_availability):
        self.__availability = new_availability


    def display_info(self):
        """Выводит информацию о книге."""
        status = 'доступна' if  self.__availability else 'недоступна'
        print(f"\nНазвание: {self.__title}\
            \nАвтор: {self.__author}\
            \nГод издания: {self.__year}\
            \nСтраниц: {self.__pages}\
            \nСтатус: {status}")

    def borrow_book(self):
        """Снижает количество доступных книг при взятии книги."""
        if self.__availability:
            self.__availability = False
            print(f"Книга '{self.__title}' взята.")
        else:
            print(f"Книга '{self.__title}' недоступна для взятия.")

    def return_book(self):
        """Увеличивает количество доступных книг при возврате книги."""
        if not self.__availability:
            self.__availability = True
            print(f"\nКнига '{self.__title}' возвращена в библиотеку.")
        else:
            print(f"\nКнига '{self.__title}' уже в библиотеке")

library = []

def add_book():
    """Добавляет книгу в библиотеку."""
    title = input("Введите название книги: ")
    author = input("Введите автора книги: ")

    while True:
        try:
            year = int(input("Введите год издания книги(не больше текущего года): "))
            if year <= 2024:
                break
        except ValueError:
            print("Пожалуйста, введите корректный год (число).")

    while True:
        try:
            pages = int(input("Введите количество страниц: "))
            if pages > 0:
                break
        except ValueError:
            print("Пожалуйста, введите корректное количество страниц (число).")

    library.append(Book(title, author, year, pages))
    print(f"\nКнига '{title}' добавлена в библиотеку.")

def take_book():
    """Позволяет взять книгу из библиотеки."""
    title = input("Введите название книги, которую хотите взять: ")
    for book in library:
        book.borrow_book()
        return
    print(f"Книга '{title}' не найдена или недоступна для взятия.")

def return_b():
    """Позволяет вернуть книгу в библиотеку."""
    title = input("Введите название книги, которую хотите вернуть: ")
    for book in library:
        if book.title == title:
            book.return_book()
            return
        else:
            print(f"Книга '{title}' не найдена среди взятых.")

def show_book_info():
    """Показывает информацию о книге по названию."""
    title = input("Введите название книги: ")
    for book in library:
        if book.title == title:
            book.display_info()
            return
    print(f"\nКнига '{title}' не найдена.")

def show_all_books():
    """Показывает список всех книг в библиотеке."""
    if library:
        for book in library:
            print(f"\nКнига: {book.title}, "
                f"Автор: {book.author}, "
                f"Год: {book.year}, "
                f"Страниц: {book.pages}, "
                f"Статус: {'доступна' if  book.availability else 'недоступна'}")
    else:
        print("\nВ библиотеке нет книг.")

def main():
    """Основная функция программы, содержащая цикл для ввода команд."""
    while True:
        print("\nМеню:\
        \n1 - Добавить книгу\
        \n2 - Взять книгу\
        \n3 - Вернуть книгу\
        \n4 - Показать информацию о книге\
        \n5 - Показать список всех книг\
        \n0 - Выйти")

        command = input("\nВведите опцию: ").strip()

        if command == "1":
            add_book()
        elif command == "2":
            take_book()
        elif command == "3":
            return_b()
        elif command == "4":
            show_book_info()
        elif command == "5":
            show_all_books()
        elif command == "0":
            print("Выход...")
            break
        else:
            print("Неверная команда, попробуйте снова.")

if __name__ == "__main__":
    main()
