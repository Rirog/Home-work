"""DZ05 CAFE"""


class Order:
    """Класс для представления обычного заказа."""
    def __init__(self, order_number, type_order, list_dishes=None, status="Создан"):
        self.order_number = order_number
        self.type_order = type_order
        self.list_dishes = list_dishes if list_dishes else []
        self.status = status


    def add_dishes(self, new_dishes):
        """Добавляет блюда в заказ."""
        self.list_dishes.extend(new_dishes)
        print(f"\nБлюда добавлены в заказ №{self.order_number}:"
              f"{', '.join(new_dishes)}.")


    def update_status(self, new_status):
        """Обновляет статус заказа."""
        self.status = new_status
        print(f"\nСтатус заказа №{self.order_number}"
              f"обновлен на: {self.status}.")


    def display_info(self):
        """Метод для вывода информации о обычносм заказе"""
        print(f"\nНомер заказа: {self.order_number};"
              f"\nТип: {self.type_order};"
              f"\nСписок блюд: {self.list_dishes};"
              f"\nСтатус: {self.status};")


class DeliveryOrder(Order):
    """Наследование класса Order для доставки"""
    def __init__(self, order_number, type_order,address , time, list_dishes=None, status="Создан"):
        super().__init__(order_number, type_order, list_dishes, status)
        self.address = address
        self.time = time


    def update_delivery_status(self, new_status):
        """Обновляет статус доставки."""
        self.status = new_status
        print(f"Статус доставки для заказа №{self.order_number}"
              f"обновлен на: {self.status}.")


    def display_info(self):
        super().display_info()
        print(f"Адрес: {self.address};"
                f"\nВремя: {self.time};")


orders = []


def create_order():
    """Создает новый заказ (обычный или доставку)."""
    order_counter = len(orders) + 1
    print("\nВыберите тип заказа: 1 - Обычный, 2 - Доставка")
    choice = input("Ваш выбор: ")

    if choice == "1":
        orders.append(Order(order_counter,  "Обычный"))
        print(f"Обычный заказ №{order_counter} создан.")
    elif choice == "2":
        address = input("Введите адрес доставки: ")
        time = input("Введите время доставки: ")
        orders.append(DeliveryOrder(order_counter, "Доставка", address, time))
        print(f"Заказ на доставку №{order_counter} создан.")
    else:
        print("Неверный выбор.")
        return


def add_dishes_to_order():
    """Добавляет блюда в заказ."""
    order_number = int(input("Введите номер заказа: "))
    for order in orders:
        if order.order_number == order_number:
            dishes = input("Введите блюда через запятую: ")
            dish_list = [dish.strip() for dish in dishes.split(",")]
            order.add_dishes(dish_list)
            return
    print("Заказ не найден.")


def show_order_info():
    """Отображает информацию о заказе."""
    order_number = int(input("Введите номер заказа: "))
    for order in orders:
        if order.order_number == order_number:
            order.display_info()
            return
        print("Заказ не найден.")


def update_order_status():
    """Изменяет статус заказа."""
    order_number = int(input("Введите номер заказа: "))
    new_status = input("Введите новый статус: ")
    for order in orders:
        if order.order_number == order_number:
            if isinstance(order, DeliveryOrder):
                order.update_delivery_status(new_status)
            else:
                order.update_status(new_status)
            return
    print("Заказ не найден.")
orders.clear()

def show_all_orders():
    """Показывает все заказы."""
    if not orders:
        print("Заказов нет.")
        return
    for order in orders:
        order.display_info()


def main():
    """меню"""
    while True:
        print("\nМеню:"
              "\n1. Создать заказ"
              "\n2. Добавить блюда в заказ"
              "\n3. Показать информацию о заказе"
              "\n4. Изменить статус заказа"
              "\n5. Показать все заказы"
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
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
