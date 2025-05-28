# Строитель — это порождающий паттерн, который позволяет
# создавать сложные объекты пошагово, отделяя конструирование
# объекта от его представления.

# Когда использовать?

# - Объект имеет много параметров
# (некоторые обязательные, некоторые опциональные).
# - Нужно создавать разные представления одного объекта.
# - Хочется избежать "телескопического конструктора" (множества перегрузок).

# Плюсы и минусы

# - Плюсы:

# Позволяет создавать объекты пошагово.
# Изолирует сложную логику сборки.
# Поддерживает разные варианты одного объекта.

# - Минусы:

# Усложняет код из-за дополнительных классов.
# Избыточен для простых объектов.
from abc import ABC, abstractmethod


class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return (f"Computer: CPU={self.cpu}, "
                f"RAM={self.ram}, Storage={self.storage}, "
                f"GPU={self.gpu}")


class ComputerBuilder(ABC):

    def __init__(self):
        self.computer = Computer()

    @abstractmethod
    def set_cpu(self, cpu: str):
        pass

    @abstractmethod
    def set_ram(self, ram: str):
        pass

    @abstractmethod
    def set_storage(self, storage: str):
        pass

    @abstractmethod
    def set_gpu(self, gpu: str):
        pass

    def get_computer(self) -> Computer:
        return self.computer


class GamingComputerBuilder(ComputerBuilder):

    def set_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self  # Возвращаем self для чейнинга

    def set_ram(self, ram: str):
        self.computer.ram = ram
        return self

    def set_storage(self, storage: str):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu: str):
        self.computer.gpu = gpu
        return self


builder = GamingComputerBuilder()
computer = (
    builder
    .set_cpu("AMD Ryzen 7")
    .set_ram("32GB")
    .set_storage("1TB SSD")
    .set_gpu("RTX 3080")
    .get_computer()
)
print(computer)
