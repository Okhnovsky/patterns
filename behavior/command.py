# Паттерн "Команда" — это поведенческий паттерн проектирования, 
# который инкапсулирует запрос как объект, позволяя параметризовать 
# клиентов с различными запросами, организовывать запросы в очередь 
# или логировать их, а также поддерживать отмену операций.

# Плюсы (+):

#     ✅ Убирает прямую зависимость между объектами, вызывающими операции,
#  и объектами, которые их выполняют

#     ✅ Позволяет реализовать отмену/повтор операций

#     ✅ Позволяет собирать сложные команды из простых

#     ✅ Упрощает добавление новых команд без изменения существующего кода

#     ✅ Позволяет реализовать отложенный запуск операций

# Минусы (-):

#     ❌ Усложняет код из-за введения множества дополнительных классов

#     ❌ Может привести к созданию большого количества классов команд


from abc import ABC, abstractmethod
from typing import List
from datetime import datetime


class Command(ABC):
    """Абстрактный класс команды."""

    @abstractmethod
    def execute(self) -> None:
        """Выполнить команду."""
        pass

    @abstractmethod
    def undo(self) -> None:
        """Отменить команду."""
        pass


class Light:
    """Светильник."""

    def __init__(self, location: str):
        self.location = location
        self.is_on = False

    def turn_on(self) -> None:
        self.is_on = True
        print(f"Свет в {self.location} включен") 
    
    def turn_off(self) -> None:
        self.is_on = False
        print(f"Свет в {self.location} выключен")


class Thermostat:
    """Термостат."""

    def __init__(self, location: str):
        self.location = location
        self.temperature = 22
    
    def set_temperature(self, temp: float) -> None:
        self.temperature = temp
        print(f"Температура в {self.location} установлена на {temp}°C")


class LightOnCommand(Command):
    """Команда включения света."""

    def __init__(self, light: Light):
        self.light = light
        self.previous_state = None
    
    def execute(self) -> None:
        self.previous_state = self.light.is_on
        self.light.turn_on()
    
    def undo(self) -> None:
        if self.previous_state is False:
            self.light.turn_off()
        elif self.previous_state is True:
            self.light.turn_on()


class LightOffCommand(Command):
    """Команда выключения света."""

    def __init__(self, light: Light):
        self.light = light
        self.previous_state = None
    
    def execute(self) -> None:
        self.previous_state = self.light.is_on
        self.light.turn_off()
    
    def undo(self) -> None:
        if self.previous_state is True:
            self.light.turn_on()
        elif self.previous_state is False:
            self.light.turn_off()


class MacroCommand(Command):
    """Макрокоманда - набор нескольких команд."""

    def __init__(self, commands: List[Command]):
        self.commands = commands
        self.executed_commands = []
    
    def execute(self) -> None:
        self.executed_commands = []
        for command in self.commands:
            command.execute()
            self.executed_commands.append(command)
    
    def undo(self) -> None:
        for command in reversed(self.executed_commands):
            command.undo()


class SetTemperatureCommand(Command):
    """Команда установки температуры."""

    def __init__(self, thermostat: Thermostat, temperature: float):
        self.thermostat = thermostat
        self.temperature = temperature
        self.previous_temperature = None
    
    def execute(self) -> None:
        self.previous_temperature = self.thermostat.temperature
        self.thermostat.set_temperature(self.temperature)
    
    def undo(self) -> None:
        if self.previous_temperature is not None:
            self.thermostat.set_temperature(self.previous_temperature)


class RemoteControl:
    """Пульт управления умным домом."""

    def __init__(self):
        self.on_commands = {}
        self.off_commands = {}
        self.history = []
        self.undo_stack = []
    
    def set_command(self, slot: int, on_command: Command,
                    off_command: Command) -> None:
        """Устанавливает команды для слота."""
        self.on_commands[slot] = on_command
        self.off_commands[slot] = off_command
    
    def press_on_button(self, slot: int) -> None:
        """Нажать кнопку включения."""
        if slot in self.on_commands:
            command = self.on_commands[slot]
            command.execute()
            self.history.append((datetime.now(), "ON", slot, command))
            self.undo_stack.append(command)
    
    def press_off_button(self, slot: int) -> None:
        """Нажать кнопку выключения."""
        if slot in self.off_commands:
            command = self.off_commands[slot]
            command.execute()
            self.history.append((datetime.now(), "OFF", slot, command))
            self.undo_stack.append(command)
    
    def press_undo(self) -> None:
        """Отменить последнюю операцию."""
        if self.undo_stack:
            command = self.undo_stack.pop()
            command.undo()
            print("Отмена последней операции")
    
    def show_history(self) -> None:
        """Показать историю комманд."""
        print("История комманд")
        for time, action, slot, command in self.history:
            print(f"{time.strftime('%H:%M:%S')} - "
                  f"{action} слот {slot} ({command.__class__.__name__})")


def main():
    living_room_light = Light("гостиной")
    bedroom_light = Light("спальне")
    thermostat = Thermostat("гостиной")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    bedroom_light_on = LightOnCommand(bedroom_light)
    bedroom_light_off = LightOffCommand(bedroom_light)
    set_warm_temp = SetTemperatureCommand(thermostat, 25)
    set_cool_temp = SetTemperatureCommand(thermostat, 20)

    cinema_mode = MacroCommand([
        living_room_light_off,
        bedroom_light_off,
        set_warm_temp,
    ])

    morning_mode = MacroCommand([
        living_room_light_on,
        set_cool_temp,
    ])

    remote = RemoteControl()
    remote.set_command(0, living_room_light_on, living_room_light_off)
    remote.set_command(1, bedroom_light_on, bedroom_light_off)
    remote.set_command(2, set_warm_temp, set_cool_temp)
    remote.set_command(3, cinema_mode, morning_mode)

    remote.press_on_button(0)
    remote.press_on_button(1)
    remote.press_on_button(2)
    remote.press_on_button(3)

    remote.press_undo()
    remote.press_undo()

    remote.press_on_button(3)

    remote.show_history()


if __name__ == "__main__":
    main()
