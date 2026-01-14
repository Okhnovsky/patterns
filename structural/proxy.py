# Заместитель - структурный паттерн, который предоставляет объект-заменитель,
# контролирующий доступ к другому объекту.

# Плюсы ✅
# Контроль доступа к реальному объекту
# Ленивая инициализация тяжелых объектов
# Кэширование результатов
# Добавление дополнительной логики без изменения реального объекта
# Упрощение клиентского кода

# Минусы ❌
# Усложнение кода за счет дополнительных классов
# Задержки из-за дополнительной обработки
# Может скрывать проблемы реального объекта
# Накладные расходы на переадресацию вызовов

from abc import ABC, abstractmethod


class Subject(ABC):

    @abstractmethod
    def request(self):
        pass


class RealSubject(Subject):

    def request(self):
        return "Реальный объект. Обработка запроса."


class Proxy(Subject):

    def __init__(self, real_subject: RealSubject = None):
        self._real_subject = real_subject
        self._access_count = 0

    def request(self):
        if self._check_access():
            result = self._real_subject.request()
            self._log_access()
            return f"Прокси: {result}"
        return "Доступ запрещен"

    def _check_access(self):
        print("Проверка прав доступа")
        return True

    def _log_access(self):
        self._access_count += 1
        print(f"Всего запросов: {self._access_count}")


if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy()

    print(proxy.request())
