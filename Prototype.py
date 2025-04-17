import copy

# Класс-заказ (будет использоваться как контейнер для изменений)
class Order:
    def __init__(self, prototype):
        self.order_number = prototype.order_number
        self.products = list(prototype.products)  # Глубокая копия списка продуктов
        self.total_price = prototype.total_price

    def __repr__(self):
        return f"Order Number: {self.order_number}\nProducts: {self.products}\nTotal Price: ${self.total_price:.2f}"

# Прототип заказа
class OrderPrototype:
    def __init__(self):
        self.order_number = None
        self.products = []  # Список товаров
        self.total_price = 0.0  # Общая сумма заказа

    def clone(self):
        # Возвращаем глубокую копию прототипа
        return copy.deepcopy(self)

# Демонстрационный пример использования
if __name__ == "__main__":
    # Создаем прототип заказа
    prototype_order = OrderPrototype()
    prototype_order.order_number = 1001
    prototype_order.products = ["Product A", "Product B", "Product C"]
    prototype_order.total_price = 150.00

    # Создаем первый заказ на основе прототипа
    order1 = Order(prototype_order.clone())
    order1.order_number = 1002  # Меняем номер заказа
    order1.total_price = 200.00  # Меняем цену

    # Создаем второй заказ на основе прототипа
    order2 = Order(prototype_order.clone())
    order2.order_number = 1003  # Меняем номер заказа
    order2.products.append("Product D")  # Добавляем новый продукт

    # Выводим информацию о заказах
    print("Order 1:\n", order1)
    print("\nOrder 2:\n", order2)