"""
Напишите класс Timer, который будет вычислять время выполнения блока кода. Класс должен иметь следующие методы:

- __enter__(self): магический метод, который запускает таймер;
- __exit__(self, exc_type, exc_val, exc_tb): магический метод, который останавливает таймер
и выводит время выполнения блока кода.
"""
from time import perf_counter, sleep


class Timer:
    def __init__(self) -> None:
        self.start = None
        self.__elapsed_time = None

    @property
    def elapsed_time(self) -> float:
        return self.__elapsed_time

    def __enter__(self) -> 'Timer':
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.__elapsed_time = perf_counter() - self.start


with Timer() as timer:
    sleep(0.5)
print("Execution time:", timer.elapsed_time)
