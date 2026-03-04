# Паттерн Посредник (Mediator) — это поведенческий паттерн проектирования,
# который позволяет уменьшить связанность множества взаимодействующих
# классов между собой, заставляя их общаться не напрямую друг с другом,
# а через объект-посредник.

# Когда использовать?
#     - Когда вам трудно изменять классы из-за большого количества
# хаотичных связей с другими классами.
#     - Когда вы хотите повторно использовать компонент, но ему
# слишком сложно без «подклейки» дополнительных классов.
#     - Когда логика взаимодействия сложная и ее лучше централизовать
# в одном месте (чтобы не дублировать код в нескольких компонентах).

# Плюсы и минусы

# Плюсы:
#     Убирает зависимости между компонентами (слабая связность).
#     Упрощает взаимодействие (все управляется в одном месте).
#     Облегчает повторное использование отдельных компонентов.

# Минусы:

#     Посредник может превратиться в объект,
# который знает слишком много и делает слишком много.


from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def notify(self, sender: object, event: str, data: any = None):
        pass


class ChatMediator(Mediator):

    def __init__(self):
        self._users = []
    
    def add_user(self, user):
        self._users.append(user)
    
    def notify(self, sender, event, data):
        if event == "message":
            for user in self._users:
                if user != sender:
                    user.recieve(data)
    

class User:

    def __init__(self, name, mediator: Mediator):
        self.name = name
        self._mediator = mediator
    
    def send(self, message):
        print(f"{self.name} отправляет {message}")
        self._mediator.notify(self, "message", message)
    
    def recieve(self, message):
        print(f"{self.name} получил {message}")


def main():
    mediator = ChatMediator()

    alice = User("Alice", mediator)
    bob = User("Bob", mediator)
    charlie = User("Charlie", mediator)

    mediator.add_user(alice)
    mediator.add_user(bob)
    mediator.add_user(charlie)

    alice.send("Всем привет!")


if __name__ == "__main__":
    main()
