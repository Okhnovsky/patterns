# Абстрактная фабрика — это порождающий паттерн, который позволяет
# создавать семейства связанных объектов, не привязываясь к конкретным классам.

# Когда использовать?

# - Нужно создавать группы взаимосвязанных объектов.
# - Система не должна зависеть от способа создания объектов.
# - Требуется поддержка разных вариантов объектов
# (например, для разных ОС или тем оформления).

# Плюсы:

# Изоляция конкретных классов от клиента.
# Гибкость в добавлении новых семейств объектов.
# Соответствие принципу открытости/закрытости (OCP).

# Минусы:

# Усложнение кода из-за множества классов.
# Требует предварительного проектирования.


from abc import ABC, abstractmethod


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass


class LightFactory(GUIFactory):

    def create_button(self):
        return LightButton()

    def create_checkbox(self):
        return LightCheckbox()


class DarkFactory(GUIFactory):

    def create_button(self):
        return DarkButton()

    def create_checkbox(self):
        return DarkCheckbox()


class Button(ABC):

    @abstractmethod
    def render(self):
        pass


class Checkbox(ABC):

    @abstractmethod
    def render(self):
        pass


class LightButton(Button):

    def render(self):
        return "Светлая кнопка"


class LightCheckbox(Checkbox):

    def render(self):
        return "Светлый чекбокс"


class DarkButton(Button):

    def render(self):
        return "Тёмная кнопка"


class DarkCheckbox(Checkbox):

    def render(self):
        return "Тёмный чекбокс"


def create_ui(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.render())
    print(checkbox.render())


# Клиентский код
light_factory = LightFactory()
create_ui(light_factory)
# Вывод:
# Светлая кнопка
# Светлый чекбокс


dark_factory = DarkFactory()
create_ui(dark_factory)
# Вывод:
# Тёмная кнопка
# Тёмный чекбокс
