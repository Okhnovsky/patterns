# Цепочка обязанностей — это поведенческий паттерн проектирования,
# который позволяет передавать запросы последовательно по цепочке
# обработчиков. Каждый обработчик решает, может ли он обработать
# запрос, и либо обрабатывает его, либо передаёт следующему в цепочке.

# Когда использовать:
# - Когда есть несколько объектов, которые могут обработать запрос,
# и заранее неизвестно, какой именно
# - Когда нужно динамически назначать обработчики во время выполнения
# - Когда необходимо отделить отправителя запроса от получателей
# - В системах обработки событий, middleware, логгерах

# Плюсы:
# Уменьшает связанность (отправитель не знает получателя)
# Гибкость (можно изменять цепочку на лету)
# Принцип единой ответственности (каждый обработчик решает свою задачу)
# Управление порядком обработки

# Минусы:
# Нет гарантии обработки запроса
# Сложнее отлаживать
# Производительность может страдать при длинных цепочках
# Риск создания циклических зависимостей


from abc import ABC, abstractmethod
from typing import Optional, Any


class Handler(ABC):
    """
    Абстрактный обработчик.
    """

    def __init__(self):
        self._next_handler: Optional[Handler] = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: Any) -> Optional[str]:
        pass

    def _handle_next(self, request: Any) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandlerA(Handler):
    """
    Конкретный обработчик А.
    """

    def handle(self, request: Any) -> Optional[str]:
        if request == "A":
            return "Handler A обработал запрос А."
        else:
            print("Handler A передает запрос дальше")
            return self._handle_next(request)


class ConcreteHandlerB(Handler):
    """
    Конкретный обработчик B.
    """

    def handle(self, request: Any) -> Optional[str]:
        if request == "B":
            return "Handler B обработал запрос B."
        else:
            print("Handler B передает запрос дальше")
            return self._handle_next(request)


class ConctreteHandlerC(Handler):
    """
    Конкретный обработчик C.
    """

    def handle(self, request: Any) -> Optional[str]:
        if request == "C":
            return "Handler C обработал запрос C."
        else:
            print("Handler C передает запрос дальше")
            return self._handle_next(request)


def client_code(handler: Handler, requests: list) -> None:
    for request in requests:
        result = handler.handle(request)

        if result:
            print(result)
        else:
            print("Запрос не был обработан")


if __name__ == "__main__":
    handler_a = ConcreteHandlerA()
    handler_b = ConcreteHandlerB()
    handler_c = ConctreteHandlerC()

    handler_a.set_next(handler_b).set_next(handler_c)

    requests = ["A", "B", "C", "A", "D"]

    client_code(handler_a, requests)
