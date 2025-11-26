# Паттерн Компоновщик (Composite) позволяет сгруппировать объекты в
# древовидные структуры и работать с ними как с единым объектом.

# Ключевые преимущества паттерна Компоновщик:
# - Единообразие - клиенты работают с простыми и составными объектами одинаково
# - Простота - легко добавлять новые виды компонентов
# - Гибкость - можно строить сложные древовидные структуры
# - Рекурсивность - легко выполнять операции над всей структурой

# Когда использовать:
# - Когда нужно представить иерархию "часть-целое"
# - Когда клиенты должны единообразно трактовать простые и составные объекты
# - При работе с древовидными структурами (файловые системы, UI компоненты,
# организационные структуры)


from abc import ABC, abstractmethod
from typing import List


class FileSystemComponent(ABC):

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> str:
        pass


class File(FileSystemComponent):

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self, indent: int = 0) -> str:
        return " " * indent + f"{self.name} ({self.size} bytes)"


class Directory(FileSystemComponent):

    def __init__(self, name: str):
        self.name = name
        self._children: List[FileSystemComponent] = []

    def add(self, component: FileSystemComponent) -> None:
        self._children.append(component)

    def remove(self, component: FileSystemComponent) -> None:
        self._children.remove(component)

    def get_size(self) -> int:
        total_size = 0
        for child in self._children:
            total_size += child.get_size()
        return total_size

    def display(self, indent: int = 0) -> str:
        result = [" " * indent + f"{self.name} ({self.get_size()} bytes)"]
        for child in self._children:
            result.append(child.display(indent + 1))
        return "\n".join(result)


if __name__ == "__main__":
    file1 = File("document.txt", 1500)
    file2 = File("image.jpg", 2500)
    file3 = File("data.csv", 800)
    file4 = File("readme.md", 300)

    root = Directory("Root")
    documents = Directory("Documents")
    images = Directory("Images")

    documents.add(file1)
    documents.add(file3)
    documents.add(file4)

    images.add(file2)

    root.add(documents)
    root.add(images)

    print("File System Structure:")
    print(root.display())

    print(f"\nTotal size: {root.get_size()} bytes")
