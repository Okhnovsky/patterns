# Observer - это поведенческий паттерн проектирования,
# который создает механизм подписки, позволяющий одним 
# объектам следить и реагировать на события, происходящие 
# в других объектах.

# Плюсы:
# Слабая связанность - субъект не знает деталей наблюдателей
# Поддержка принципа open/closed - можно добавлять новых наблюдателей без изменения кода субъекта
# Гибкость - возможность динамически добавлять/удалять наблюдателей
# Broadcast communication - один субъект может оповещать множество наблюдателей

# Минусы:
# Непредсказуемый порядок уведомлений - наблюдатели получают уведомления в случайном порядке
# Утечки памяти - если не отписывать наблюдателей
# Сложность отладки - трудно отследить цепочку вызовов
# Медленная работа при большом количестве наблюдателей
# Проблема "проклятия бензопилы" - сложно понять, кто и зачем подписался


from abc import ABC, abstractmethod
from typing import List


class Observer(ABC):

    @abstractmethod
    def update(self, message: str) -> None:
        pass


class Subject(ABC):

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, message: str) -> None:
        pass


class NewsAgency(Subject):

    def __init__(self):
        self._observers: List[Observer] = []
        self._latest_news = ""
    
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        print(f"Новый подписчик добавлен")
    
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"Подписчик отписался")
    
    def notify(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)

    def publish_news(self, news: str) -> None:
        self._latest_news = news
        print(f"\nНОВОСТЬ: {news}")
        self.notify(news)


class TVChannel(Observer):

    def __init__(self, name: str):
        self._name = name

    def update(self, message: str) -> None:
        print(f"[{self._name} TV] Срочно в эфир: {message}")


class RadioStation(Observer):

    def __init__(self, name: str):
        self._name = name
    
    def update(self, message: str) -> None:
        print(f"[Радио {self._name}] Передаем новость: {message}")


class PhoneApp(Observer):

    def __init__(self, user: str):
        self._user = user
    
    def update(self, message: str) -> None:
        print(f"[Приложение {self._user}] PUSH-уведомление: {message}")


if __name__ == "__main__":
    news_agency = NewsAgency()

    tv1 = TVChannel("Первый")
    tv2 = TVChannel("Россия 24")
    radio = RadioStation("Вести FM")
    phone = PhoneApp("Анна")

    news_agency.attach(tv1)
    news_agency.attach(tv2)
    news_agency.attach(radio)
    news_agency.attach(phone)

    news_agency.publish_news("Запущен новый спутник!")

    news_agency.detach(tv2)

    news_agency.publish_news("Открыт новый вид животных!")
