# Интерпретатор — это поведенческий паттерн проектирования,
# который определяет грамматику для языка и интерпретирует
# предложения этого языка. По сути, он создает небольшой
# "язык внутри языка"

# Когда использовать?
#     Когда есть простая грамматика языка
#     Когда производительность не критична
#     Когда нужно легко изменять и расширять грамматику
#     Для DSL (Domain-Specific Language) - предметно-ориентированных языков

# Плюсы:
#     Упрощает изменение и расширение грамматики
#     Легко реализуется для простых грамматик
#     Отделяет грамматику от логики выполнения

# Минусы:
#     Сложен для сложных грамматик
#     Медленный (каждый элемент требует своего объекта)
#     Подходит только для простых языков
#     Сложно поддерживать при росте грамматики


from abc import ABC, abstractmethod


class Expr(ABC):
    """Абстрактный базовый класс."""

    @abstractmethod
    def check(self, data):
        pass


class AgeGreater(Expr):
    """Проверка возраста."""

    def __init__(self, age: int):
        self.age = age
    
    def check(self, data: dict):
        return data['age'] > self.age


class NameContains(Expr):
    """Проверка имени."""

    def __init__(self, text: str):
        self.text = text
    
    def check(self, data: dict):
        return self.text in data["name"]


class And(Expr):
    """Условие."""

    def __init__(self, left: Expr, right: Expr):
        self.left = left
        self.right = right
    
    def check(self, person: dict):
        return self.left.check(person) and self.right.check(person)


def main():
    person = {"name": "Иван", "age": 25}
    filter1 = And(AgeGreater(20), NameContains("Ив"))
    print(filter1.check(person))


if __name__ == "__main__":
    main()
