"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""
from math import lcm, gcd


class Fraction:
    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.numerator}, {self.denominator})'

    def __str__(self) -> str:
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other: 'Fraction') -> str:
        lcm_ = lcm(self.denominator, other.denominator)
        numerator = (self.numerator * (lcm_ // self.denominator)) + (other.numerator * (lcm_ // other.denominator))
        gcd_ = gcd(numerator, lcm_)
        return f'{numerator // gcd_}/{lcm_ // gcd_}'


fraction1 = Fraction(1, 2)
print(repr(fraction1))  # Fraction(1, 2)
print(str(fraction1))  # 1/2

fraction2 = Fraction(3, 4)
fraction3 = fraction1 + fraction2
print(fraction3)  # 5/4
