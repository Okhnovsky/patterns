# Паттерн Прототип позволяет создавать новые объекты путем
# копирования существующих (прототипов), вместо создания через
# конструктор. Это полезно, когда создание объекта ресурсоемко
# (например, требует сложных вычислений или работы с БД),
# а нужно много похожих объектов.

# Плюсы:

# Уменьшает дублирование кода при создании объектов.
# Позволяет гибко настраивать копии.
# Ускоряет создание сложных объектов.

# Минусы:

# Глубокое копирование может быть медленным для сложных объектов.
# Иногда проще использовать фабрики или конструкторы.


import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register(self, name, obj):
        self._objects[name] = obj

    def unregister(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects[name])
        obj.__dict__.update(attrs)  # Обновляем атрибуты, если нужно
        return obj


# Пример использования
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def __str__(self):
        return f"{self.model} ({self.color})"


# Создаем прототип
prototype = Prototype()

# Регистрируем объект-прототип
car_prototype = Car("Tesla Model S", "Red")
prototype.register("Tesla", car_prototype)

# Клонируем объект
cloned_car = prototype.clone("Tesla", color="Blue")  # Меняем цвет
print(cloned_car)  # Tesla Model S (Blue)
