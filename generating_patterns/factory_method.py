# Фабричный метод — это порождающий паттерн, который определяет
# интерфейс для создания объекта, но позволяет подклассам изменять
# тип создаваемого экземпляра.

# Когда использовать?

# - Класс заранее не знает, объекты каких классов ему нужно создавать
# - Класс хочет, чтобы его подклассы специфицировали создаваемые объекты
# - Вы хотите локализовать логику создания объектов

# Плюсы и минусы

# - Преимущества:

# Избавляет класс от привязки к конкретным классам продуктов
# Выделяет код производства продуктов в одно место
# Упрощает добавление новых типов продуктов
# Реализует принцип открытости/закрытости
# - Недостатки:

# Может привести к созданию большого количества подклассов
# Усложняет код из-за введения дополнительных классов
from abc import ABC, abstractmethod


class Logistics(ABC):

    @abstractmethod
    def create_transport(self):
        """Фабричный метод"""
        pass

    def plan_delivery(self):
        """Общий метод, использующий фабричный метод"""
        transport = self.create_transport()
        return f"Доставка будет выполнена: {transport.deliver()}"


class RoadLogistics(Logistics):

    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):

    def create_transport(self):
        return Ship()


class Transport(ABC):

    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):

    def deliver(self):
        return "Грузовик доставит товар по дороге"


class Ship(Transport):

    def deliver(self):
        return "Корабль доставит товар по морю"


def client_code(logistics: Logistics):
    print(logistics.plan_delivery())


# Клиентский код
road = RoadLogistics()
client_code(road)
# Вывод: Доставка будет выполнена: Грузовик доставит товар по дороге


sea = SeaLogistics()
client_code(sea)
# Вывод: Доставка будет выполнена: Корабль доставит товар по морю
