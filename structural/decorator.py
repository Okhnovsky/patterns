# Когда использовать:
# - Когда нужно добавлять обязанности объектам динамически
# - Когда нельзя использовать наследование


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
