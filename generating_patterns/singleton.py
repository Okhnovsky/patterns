# Singleton (Одиночка) - это порождающий паттерн проектирования, 
# который гарантирует, что у класса есть только один экземпляр, 
# и предоставляет глобальную точку доступа к этому экземпляру.

# Когда использовать Singleton

# Когда в программе должен быть единственный экземпляр класса, доступный всем клиентам
# Когда нужно более строгое управление глобальными переменными
# Для кэширования, логгирования, подключения к БД и других ресурсоемких операций

# Ограничения

# Нарушает принцип единственной ответственности (SRP)
# Усложняет тестирование из-за глобального состояния
# Может создавать проблемы в многопоточных приложениях


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


# Пример использования
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # Выведет: True


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class Database:
    def __init__(self):
        print("Инициализация базы данных")


# Пример использования
db1 = Database()
db2 = Database()

print(db1 is db2)  # Выведет: True


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):
    def __init__(self):
        print("Инициализация логгера")


# Пример использования
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # Выведет: True
