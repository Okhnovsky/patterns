# Паттерн Хранитель (Memento) - это поведенческий паттерн проектирования,
# который позволяет сохранять и восстанавливать предыдущее состояние объекта,
# не раскрывая подробностей его реализации.

# Плюсы:
#     Сохраняет инкапсуляцию - внутреннее состояние объекта не раскрывается
#     Упрощает структуру Создателя - ему не нужно заботиться о хранении истории состояний
#     Позволяет легко реализовать отмену операций (undo/redo)
#     Не нарушает границ инкапсуляции самого хранителя

# Минусы:
#     Требует дополнительной памяти при частом сохранении состояний
#     Может усложнить код, если нужно сохранять сложные состояния
#     Опекуну нужно управлять жизненным циклом хранителей
#     Дополнительные затраты на сериализацию/копирование данных

from dataclasses import dataclass
from typing import List
from copy import deepcopy
import time


@dataclass
class TextEditorMemento:
    content: str
    cursor_position: int
    timestamp: float

    def get_snapshot_info(self) -> str:
        """Возвращает информацию о снимке."""
        return f"Снимок от {time.ctime(self.timestamp)}: '{self.content[:20]}...'"


class TextEditor:
    def __init__(self):
        self._content = ""
        self._cursor_position = 0

    def write(self, text: str) -> None:
        """Добавляет текст в редактор."""
        self._content += text
        self._cursor_position = len(self._content)
        print(f"Записано: '{text}'")

    def delete_last_char(self) -> None:
        """Удаляет последний символ."""
        if self._content:
            self._content = self._content[:-1]
            self._cursor_position = len(self._content)
            print("Удален последний символ")

    def set_cursor(self, position: int) -> None:
        """Устанавливает позицию курсора."""
        if 0 <= position <= len(self._content):
            self._cursor_position = position
            print(f"Курсор установлен на позицию {position}")

    def save(self) -> TextEditorMemento:
        """Создает снимок текущего состояния."""
        return TextEditorMemento(
            content=deepcopy(self._content),
            cursor_position=self._cursor_position,
            timestamp=time.time()
        )

    def restore(self, memento: TextEditorMemento) -> None:
        """Восстанавливает состояние из снимка."""
        self._content = memento.content
        self._cursor_position = memento.cursor_position
        print(f"Восстановлено состояние от {time.ctime(memento.timestamp)}")

    def __str__(self) -> str:
        """Отображает текущее состояние редактора."""
        display = self._content[:self._cursor_position] + "|" + self._content[self._cursor_position:]
        return f"Редактор: '{display}'"


class EditorHistory:
    def __init__(self, editor: TextEditor):
        self._editor = editor
        self._history: List[TextEditorMemento] = []
        self._current_index = -1

    def save_state(self) -> None:
        """Сохраняет текущее состояние в историю."""
        if self._current_index < len(self._history) - 1:
            self._history = self._history[:self._current_index + 1]

        self._history.append(self._editor.save())
        self._current_index += 1
        print(f"Состояние сохранено. Всего сохранений: {len(self._history)}")

    def undo(self) -> bool:
        """Отменяет последнее действие"""
        if self._current_index > 0:
            self._current_index -= 1
            self._editor.restore(self._history[self._current_index])
            return True
        print("Невозможно отменить - достигнуто начало истории")
        return False

    def redo(self) -> bool:
        """Повторяет отмененное действие."""
        if self._current_index < len(self._history) - 1:
            self._current_index += 1
            self._editor.restore(self._history[self._current_index])
            return True
        print("Невозможно повторить - достигнут конец истории")
        return False

    def show_history(self) -> None:
        """Показывает историю сохранений."""
        print("\n=== История состояний ===")
        for i, memento in enumerate(self._history):
            prefix = "-> " if i == self._current_index else "   "
            print(f"{prefix}{i}: {memento.get_snapshot_info()}")


def main():
    editor = TextEditor()
    history = EditorHistory(editor)
    
    print("=== Демонстрация паттерна Хранитель ===\n")

    history.save_state()

    editor.write("Привет")
    print(editor)
    history.save_state()

    editor.write(", мир!")
    print(editor)
    history.save_state()

    editor.delete_last_char()
    editor.delete_last_char()
    print(editor)
    history.save_state()

    history.show_history()

    print("\n=== Демонстрация отмены действий ===")

    history.undo()
    print(editor)

    history.undo()
    print(editor)

    history.redo()
    print(editor)

    print("\n=== Новое действие после отмены ===")
    editor.write(" Python!")
    print(editor)
    history.save_state()
    history.show_history()


if __name__ == "__main__":
    main()
