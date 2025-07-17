# Паттерн "Адаптер" (Adapter) позволяет объектам с несовместимыми
# интерфейсами работать вместе. Он выступает как мост между двумя
# несовместимыми интерфейсами.

# Когда использовать:

# Когда нужно использовать существующий класс,
# но его интерфейс не соответствует вашему коду
# Когда нужно использовать несколько существующих подклассов,
# но невозможно адаптировать их интерфейсы путем наследования

# Разница между подходами

# Классовый адаптер использует множественное наследование для
# адаптации одного интерфейса к другому
# Объектный адаптер использует композицию для включения адаптируемого объекта
# Преимущества паттерна:

# Отделяет и скрывает от клиента преобразование интерфейсов
# Позволяет повторно использовать существующие классы
# Реализует принцип открытости/закрытости
# # Недостатки:

# Усложняет код за счет введения дополнительных классов


# Классовый


class Target:
    """Целевой интерфейс, который ожидает клиентский код."""
    def request(self) -> str:
        return "Целевое поведение"


class Adaptee:
    """Адаптируемый класс с несовместимым интерфейсом."""
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """Адаптер делает интерфейс Adaptee совместимым с
    Target через множественное наследование."""
    def request(self) -> str:
        return f"Адаптер: (ПЕРЕВОД) {self.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """Клиентский код, который работает с объектами через Target интерфейс."""
    print(target.request())


if __name__ == "__main__":
    print("Клиент: Работаю с целевым объектом:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Клиент: У Adaptee странный интерфейс. Не понимаю:")
    print(f"Adaptee: {adaptee.specific_request()}")

    print("Клиент: Но могу работать с ним через Adapter:")
    adapter = Adapter()
    client_code(adapter)


# Объектный

class Target:
    """Целевой интерфейс."""
    def request(self) -> str:
        return "Целевое поведение"


class Adaptee:
    """Адаптируемый класс."""
    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """Адаптер использует композицию для включения Adaptee."""
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Адаптер: (ПЕРЕВОД) {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    """Клиентский код."""
    print(target.request())


if __name__ == "__main__":
    print("Клиент: Работаю с целевым объектом:")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print("Клиент: У Adaptee странный интерфейс. Не понимаю:")
    print(f"Adaptee: {adaptee.specific_request()}")

    print("Клиент: Но могу работать с ним через Adapter:")
    adapter = Adapter(adaptee)
    client_code(adapter)
