# Фасад — структурный паттерн, который предоставляет простой интерфейс к
# сложной системе классов, библиотеке или фреймворку.
# Скрывает сложность системы за единым упрощенным API

# ИДЕАЛЬНЫЕ СЛУЧАИ ИСПОЛЬЗОВАНИЯ:
# - Работа со сложными библиотеками/фреймворками
# - Интеграция legacy-кода
# - Упрощение сложных workflow
# - Предоставление удобного API для внешних потребителей

# НЕ ИСПОЛЬЗОВАТЬ Фасад когда:
# - Нужен полный контроль над подсистемой
# - Подсистема и так простая
# - Часто нужно расширять функциональность


# Сложные подсистемы
class EngineSystem:
    def check_oil_pressure(self):
        print("Проверка давления масла... OK")
        return True

    def check_coolant_temperature(self):
        print("Проверка температуры охлаждающей жидкости... OK")
        return True

    def start_ignition(self):
        print("Запуск зажигания...")
        return "Игнишн запущен"


class FuelSystem:
    def check_fuel_pressure(self):
        print("Проверка давления топлива... OK")
        return True

    def activate_pump(self):
        print("Активация топливного насоса...")
        return "Насос активен"

    def inject_fuel(self):
        print("Впрыск топлива...")
        return "Топливо впрыснуто"


class ElectricalSystem:
    def check_battery(self):
        print("Проверка аккумулятора... OK")
        return True

    def power_on_ecu(self):
        print("Питание на блок управления...")
        return "ECU включен"

    def initialize_sensors(self):
        print("Инициализация датчиков...")
        return "Датчики готовы"


# ФАСАД - упрощенный интерфейс
class CarFacade:
    def __init__(self):
        self.engine = EngineSystem()
        self.fuel = FuelSystem()
        self.electrical = ElectricalSystem()

    def start_car(self):
        """Простой метод для запуска автомобиля"""
        print("=" * 40)
        print("ЗАПУСК АВТОМОБИЛЯ")
        print("=" * 40)

        results = []

        # Последовательность запуска скрыта от клиента
        results.append(self.electrical.check_battery())
        results.append(self.electrical.power_on_ecu())
        results.append(self.electrical.initialize_sensors())

        results.append(self.engine.check_oil_pressure())
        results.append(self.engine.check_coolant_temperature())

        results.append(self.fuel.check_fuel_pressure())
        results.append(self.fuel.activate_pump())

        results.append(self.engine.start_ignition())
        results.append(self.fuel.inject_fuel())

        print("=" * 40)
        print("АВТОМОБИЛЬ ЗАПУЩЕН!")
        print("=" * 40)

        return all(results)

    def stop_car(self):
        """Простой метод для остановки автомобиля"""
        print("\nОстановка автомобиля...")
        # Сложная логика остановки скрыта
        return "Автомобиль остановлен"


# Клиентский код
def main():
    # БЕЗ фасада (сложно, нужно знать все детали)
    print("БЕЗ ФАСАДА:")
    engine = EngineSystem()
    fuel = FuelSystem()
    electrical = ElectricalSystem()

    electrical.check_battery()
    electrical.power_on_ecu()
    electrical.initialize_sensors()
    engine.check_oil_pressure()
    # ... и еще 5-6 вызовов
    print("\n")

    # С фасадом (просто)
    print("С ФАСАДОМ:")
    car = CarFacade()
    car.start_car()  # Один простой вызов!


if __name__ == "__main__":
    main()
