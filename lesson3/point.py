"""
Напишите класс Point, представляющий собой точку на плоскости, имеющий следующие методы:

- __init__(self, x, y): конструктор, принимающий координаты точки;
- __repr__(self): магический метод, возвращающий строковое представление точки, которое можно
  использовать для создания нового объекта класса Point;
- __str__(self): магический метод, возвращающий строковое представление точки;
- __add__(self, other): магический метод, который позволяет складывать точки и возвращать новую точку.
"""


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def __add__(self, other: 'Point') -> 'Point':
        return self.__class__((self.x + other.x), (self.y + other.y))


point1 = Point(1, 2)
print(repr(point1))  # Point(1, 2)
print(str(point1))  # (1, 2)

point2 = Point(3, 4)
point3 = point1 + point2
print(point3)  # (4, 6)
