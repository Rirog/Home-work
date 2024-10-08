class Book:
    """Класс для представления физической книги в библиотеке."""

    available_books = 0  

    def __init__(self, title, author, year, pages):
        """Инициализация атрибутов книги."""
        self.title = title  
        self.author = author  
        self.year = year  
        self.pages = pages  
        Book.available_books += 1 

    @staticmethod
    def total_books():
        """Выводит общее количество доступных книг."""
        print(f"\nВсего доступных книг: {Book.available_books}")

    def display_info(self):
        """Выводит информацию о книге."""
        print(f"\nНазвание: {self.title}\
            \nАвтор: {self.author}\
            \nГод издания: {self.year}\
            \nСтраниц: {self.pages}")

    def borrow_book(self):
        """Снижает количество доступных книг при взятии книги."""
        if Book.available_books > 0:
            Book.available_books -= 1  
            print(f"Книга '{self.title}' взята.")
        else:
            print(f"Книга '{self.title}' недоступна для взятия.")

    def return_book(self):
        """Увеличивает количество доступных книг при возврате книги."""
        Book.available_books += 1  
        print(f"\nКнига '{self.title}' возвращена в библиотеку.")

    def __str__(self):
        """Возвращает строковое представление книги."""
        return (f'\nКнига: {self.title}, '
                f'Автор: {self.author}, '
                f'Год: {self.year}, '
                f'Страниц: {self.pages}').strip()


class DigitalBook(Book):
    """Класс для представления цифровой книги в библиотеке, наследуемый от Book."""

    def __init__(self, title, author, year, pages, file_format):
        """Инициализация атрибутов цифровой книги."""
        super().init(title, author, year, pages)  
        self.file_format = file_format  

    def display_info(self):
        """Выводит информацию о цифровой книге, включая формат файла."""
        super().display_info() 
        print(f"\nФормат файла: {self.file_format}")

    def download_book(self):
        """Выводит сообщение о доступности цифровой книги для скачивания."""
        print(f"\nКнига '{self.title}' доступна для скачивания в формате {self.file_format}.")

    def __str__(self):
        """Возвращает строковое представление цифровой книги."""
        return (f'\nЭлектронная книга: {self.title}, '
                f'Автор: {self.author}, '
                f'Год: {self.year}, '
                f'Страниц: {self.pages}, '
                f'Формат: {self.file_format}').strip()


library = [] 


def add_book():
    """Добавляет книгу (физическую или цифровую) в библиотеку."""
    book_type = input("Введите тип книги (физическая(ф) или цифровая(ц)): ").strip().lower()
    if book_type == "ф" or book_type == 'ц':
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = int(input("Введите год издания книги: "))
        pages = int(input("Введите количество страниц: "))

        if book_type == "ф":
            book = Book(title, author, year, pages)
            library.append(book) 
            print(f"\nФизическая книга '{title}' добавлена в библиотеку.")
        elif book_type == "ц":
            file_format = input("Введите формат файла (PDF, EPUB и т.д.): ")
            dbook = DigitalBook(title, author, year, pages, file_format)
            library.append(dbook)  
            print(f"\nЦифровая книга '{title}' добавлена в библиотеку.")
    else:
        print("Неверный тип книги!")

def take_book():
    """Позволяет взять физическую книгу из библиотеки."""
    title = input("Введите название книги, которую хотите взять: ")
    for book in library:
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.borrow_book()  
            return
    print(f"Книга '{title}' не найдена или недоступна для взятия.")


def return_book():
    """Позволяет вернуть физическую книгу в библиотеку."""
    title = input("Введите название книги, которую хотите вернуть: ")
    for book in library:
        if isinstance(book, Book) and not isinstance(book, DigitalBook) and book.title == title:
            book.return_book()  
            return
    print(f"Книга '{title}' не найдена среди взятых.")


def download_book():
    """Позволяет скачать цифровую книгу."""
    title = input("Введите название книги, которую хотите скачать: ")
    for book in library:
        if isinstance(book, DigitalBook) and book.title == title:
            book.download_book()  
            return
    print(f"\nЦифровая книга '{title}' не найдена.")


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
            print(book) 
    else:
        print("\nВ библиотеке нет книг.")


def show_book_str():
    """Показывает строковое представление книги по названию."""
    title = input("Введите название книги: ")
    for book in library:
        if book.title == title:
            print(str(book))  
            return
    print(f"\nКнига '{title}' не найдена.")


def main():
    """Основная функция программы, содержащая цикл для ввода команд."""
    while True:
        print("\nДоступные команды:\
        \n1 - Добавить книгу\
        \n2 - Взять физическую книгу\
        \n3 - Вернуть физическую книгу\
        \n4 - Скачать цифровую книгу\
        \n5 - Показать информацию о книге\
        \n6 - Показать список всех книг\
        \n7 - Показать общее количество книг\
        \n8 - Показать строковое представление книги\
        \n0 - Выйти")

        command = input("\nВведите команду: ").strip()

        if command == "1":
            add_book()
        elif command == "2":
            take_book()
        elif command == "3":
            return_book()
        elif command == "4":
            download_book()
        elif command == "5":
            show_book_info()
        elif command == "6":
            show_all_books()
        elif command == "7":
            Book.total_books()  
        elif command == "8":
            show_book_str()
        elif command == "0":
            print("Выход...")
            break  
        else:
            print("Неверная команда, попробуйте снова.")

if __name__ == "__main__":
    main()