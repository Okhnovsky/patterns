# Приспособленец - структурный паттерн, который позволяет вместить
# большее количество объектов в отведённую оперативную
# память за счёт разделения общего состояния между объектами.

# Когда применять:
# Когда в приложении используется большое количество объектов
# Когда нехватка оперативной памяти существенно сказывается на
# производительности
# Когда большую часть состояния объектов можно вынести наружу
# Когда приложение не зависит от идентичности объектов

# Плюсы ✅
# Экономия памяти - основной плюс
# Ускорение работы при создании объектов
# Снижение нагрузки на сборщик мусора
# Централизованное управление общим состоянием

# Минусы ❌
# Усложнение кода за счет разделения состояния
# Накладные расходы на поиск/создание приспособленцев
# Не применим, если объекты должны быть уникальными
# Потокобезопасность требует дополнительных мер


class Character:
    """Приспособленец для символов."""

    def __init__(self, char, font, size, color):
        self.char = char
        self.font = font
        self.size = size
        self.color = color

    def display(self, position):
        return (f"'{self.char}' ({self.font}, {self.size}px, "
                f"{self.color}) at {position}")


class CharacterFactory:

    _characters = {}

    @classmethod
    def get_character(cls, char, font="Arial", size=12, color="black"):
        key = (char, font, size, color)
        if key not in cls._characters:
            cls._characters[key] = Character(char, font, size, color)
        return cls._characters[key]


class TextEditor:

    def __init__(self):
        self.characters = []
        self.positions = []

    def add_char(self, char, position, font="Arial", size=12, color="black"):
        char_obj = CharacterFactory.get_character(char, font, size, color)
        self.characters.append(char_obj)
        self.positions.append(position)

    def display(self):
        for char, pos in zip(self.characters, self.positions):
            print(char.display(pos))


editor = TextEditor()
text = "Hello World"
for i, char in enumerate(text):
    editor.add_char(char, position=i)

print("Создано символов:", len(editor.characters))
print("Уникальных объектов Character:", len(CharacterFactory._characters))
