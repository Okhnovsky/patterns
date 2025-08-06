# Паттерн "Мост" разделяет абстракцию и реализацию так, чтобы
# они могли изменяться независимо. Он полезен, когда нужно избежать
# постоянного наследования и жесткой привязки абстракции к конкретной
#       реализации.

# Когда использовать?

# Когда нужно разделить монолитный класс, который содержит несколько
#       реализаций одной функциональности.
# Когда нужно расширять классы в двух независимых плоскостях
#       (абстракция и реализация).
# Когда реализацию нужно изменять во время выполнения программы.


# Преимущества паттерна "Мост"

# ✅ Разделение абстракции и реализации – можно изменять их независимо.
# ✅ Уменьшение сложности кода – вместо множества подклассов используется
#   композиция.
# ✅ Гибкость – реализацию можно менять динамически во время выполнения.


# Реализация разных устройств и пультов управления
from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):
    def turn_on(self):
        return "Телевизор включен"

    def turn_off(self):
        return "Телевизор выключен"


class Radio(Device):
    def turn_on(self):
        return "Радио включено"

    def turn_off(self):
        return "Радио выключено"


class RemoteControl:
    def __init__(self, device: Device):
        self._device = device

    def toggle_power(self):
        print(self._device.turn_on() if not
              self._is_on else self._device.turn_off())
        self._is_on = not self._is_on


# Использование
tv = TV()
remote = RemoteControl(tv)
remote.toggle_power()  # Телевизор включен
remote.toggle_power()  # Телевизор выключен


radio = Radio()
remote = RemoteControl(radio)
remote.toggle_power()  # Радио включено
