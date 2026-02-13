# Паттерн Iterator в Python — это поведенческий паттерн,
# который позволяет последовательно обходить элементы 
# составного объекта (коллекции), не раскрывая его 
# внутреннее представление.


# Плюсы:
    # Единый интерфейс для обхода разных коллекций
    # Инкапсуляция логики обхода
    # Возможность множества одновременных обходов
    # Упрощает классы коллекций

# Минусы:
    # Не всегда эффективен для простых коллекций
    # Создает дополнительный объект (итератор)
    # Может быть избыточным


class BookCollection:
    """Коллекция книг."""

    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        self._books.append(book)
    
    def __iter__(self):
        return BookIterator(self._books)


class BookIterator:
    """Итератор для коллекции книг."""

    def __init__(self, books):
        self._books = books
        self._index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index < len(self._books):
            book = self._books[self._index]
            self._index += 1
            return book
        raise StopIteration


def main():
    library = BookCollection()
    library.add_book("Война и мир")
    library.add_book("Преступление и наказание")
    library.add_book("Мастер и Маргарита")

    for book in library:
        print(book)


if __name__ == "__main__":
    main()
