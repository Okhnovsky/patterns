# Паттерн Декоратор (Decorator) позволяет динамически добавлять объектам
# новую функциональность, оборачивая их в объекты-обёртки.

# Ключевые преимущества паттерна Декоратор:
# - Гибкость - можно динамически добавлять/удалять обязанности объектам
# - Соответствие OCP - расширяем функциональность без изменения существующего
#  кода
# - Одна ответственность - каждый декоратор отвечает за одну конкретную функцию
# - Композиционная мощность - можно комбинировать декораторы в любой
# последовательности
# - Инверсия зависимостей - работаем с абстракциями, а не конкретными
# реализациями

# Когда использовать:
# - Когда нужно добавлять обязанности объектам динамически и прозрачно
# - Когда расширение функциональности с помощью наследования нецелесообразно
# - Когда нужно добавлять cross-cutting concerns (логирование, кэширование,
# валидацию)
# - При работе с компонентами, где требуется гибкая конфигурация поведения
# - Когда важно сохранить интерфейс базового объекта неизменным


class Coffee:

    def cost(self) -> int:
        return 100

    def description(self) -> str:
        return "Простой кофе"


class CoffeeDecorator(Coffee):

    def __init__(self, coffee: Coffee):
        self._coffee = coffee


class MilkDecorator(CoffeeDecorator):

    def cost(self) -> int:
        return self._coffee.cost() + 30

    def description(self) -> str:
        return self._coffee.description() + ", молоко"


class SugarDecorator(CoffeeDecorator):

    def cost(self) -> int:
        return self._coffee.cost() + 10

    def description(self) -> str:
        return self._coffee.description() + ", сахар"


class WhipDecorator(CoffeeDecorator):

    def cost(self) -> int:
        return self._coffee.cost() + 50

    def description(self) -> str:
        return self._coffee.description() + ", взбитые сливки"


coffee = Coffee()
print(f"{coffee.description()}: ${coffee.cost()}")

coffee = MilkDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

coffee = SugarDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")

coffee = WhipDecorator(coffee)
print(f"{coffee.description()}: ${coffee.cost()}")
