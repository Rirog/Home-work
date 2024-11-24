"""Упрпавление заказами"""
class Order:
    """Класс для представления обычного заказа."""
    def __init__(self, order_number, dishes=None, status="Создан"):
        self.order_number = order_number
        self.dishes = dishes if dishes else []
        self.status = status

    def add_dishes(self, new_dishes):
        """Добавляет блюда в заказ."""
        self.dishes.extend(new_dishes)
        print(f"Блюда добавлены в заказ №{self.order_number}: {', '.join(new_dishes)}.")

    def update_status(self, new_status):
        """Обновляет статус заказа."""
        self.status = new_status
        print(f"Статус заказа №{self.order_number} обновлен на: {self.status}.")

    def get_info(self):
        """Возвращает информацию о заказе."""
        return (f"\nЗаказ №{self.order_number}\n"
                f"Тип: Обычный\n"
                f"Блюда: {', '.join(self.dishes) if self.dishes else 'Нет'}\n"
                f"Статус: {self.status}")

class DeliveryOrder(Order):
    """Класс для представления заказа с доставкой."""
    def __init__(self, order_number, address, delivery_time, dishes=None, status="Создан"):
        super().__init__(order_number, dishes, status)
        self.address = address
        self.delivery_time = delivery_time

    def update_delivery_status(self, new_status):
        """Обновляет статус доставки."""
        self.status = new_status
        print(f"Статус доставки для заказа №{self.order_number} обновлен на: {self.status}.")

    def get_info(self):
        """Возвращает информацию о заказе на доставку."""
        return (f"\nЗаказ №{self.order_number}\n"
                f"Тип: Доставка\n"
                f"Адрес: {self.address}\n"
                f"Время доставки: {self.delivery_time}\n"
                f"Блюда: {', '.join(self.dishes) if self.dishes else 'Нет'}\n"
                f"Статус: {self.status}")

# Глобальные переменные
orders = []
# Функции для взаимодействия через терминал
def create_order():
    """Создает новый заказ (обычный или доставку)."""
    order_counter = 1
    print("Выберите тип заказа: 1 - Обычный, 2 - Доставка")
    choice = input("Ваш выбор: ")

    if choice == "1":
        orders.append(Order(order_counter))
        print(f"Обычный заказ №{order_counter} создан.")
    elif choice == "2":
        address = input("Введите адрес доставки: ")
        delivery_time = input("Введите время доставки: ")
        orders.append(DeliveryOrder(order_counter, address, delivery_time))
        print(f"Заказ на доставку №{order_counter} создан.")
    else:
        print("Неверный выбор.")
        return

    order_counter += 1

def add_dishes_to_order():
    """Добавляет блюда в заказ."""
    order_number = int(input("Введите номер заказа: "))
    for order in orders:
        if order.order_number == order_number:
            dishes = input("Введите блюда через запятую: ")
            dish_list = [dish.strip() for dish in dishes.split(",")]
            order.add_dishes(dish_list)  # Используем метод из класса
            return
    print("Заказ не найден.")

def show_order_info():
    """Отображает информацию о заказе."""
    order_number = int(input("Введите номер заказа: "))
    for order in orders:
        if order.order_number == order_number:
            print(order.get_info())  # Используем метод из класса
            return
    print("Заказ не найден.")


def update_order_status():
    """Изменяет статус заказа."""
    order_number = int(input("Введите номер заказа: "))
    new_status = input("Введите новый статус: ")
    for order in orders:
        if order.order_number == order_number:
            if isinstance(order, DeliveryOrder):
                order.update_delivery_status(new_status)  # Метод доставки
            else:
                order.update_status(new_status)  # Метод обычного заказа
            return
    print("Заказ не найден.")


def show_all_orders():
    """Показывает все заказы."""
    if not orders:
        print("Заказов нет.")
        return
    for order in orders:
        print(order.get_info())


def delete_order():
    """Удаляет завершенный заказ."""
    order_number = int(input("Введите номер заказа: "))
    for order in orders.copy():
        if order.order_number == order_number:
            orders.remove(order)
            print(f"Заказ №{order_number} удален.")
            return
    print("Заказ не найден.")


# Основное меню
def main():
    """меню"""
    while True:
        print("\nМеню:"
        "\n1. Создать заказ"
        "\n2. Добавить блюда в заказ"
        "\n3. Показать информацию о заказе"
        "\n4. Изменить статус заказа"
        "\n5. Показать все заказы"
        "\n6. Удалить заказ"
        "\n0. Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            create_order()
        elif choice == "2":
            add_dishes_to_order()
        elif choice == "3":
            show_order_info()
        elif choice == "4":
            update_order_status()
        elif choice == "5":
            show_all_orders()
        elif choice == "6":
            delete_order()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
