"""
Напишите класс MyList, представляющий собой список, имеющий следующие методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __repr__(self): магический метод, возвращающий строковое представление списка,
которое можно использовать для создания нового объекта класса MyList;
- __str__(self): магический метод, возвращающий строковое представление списка;
- __len__(self): магический метод, возвращающий длину списка;
- __add__(self, other): магический метод, который позволяет складывать списки и возвращать новый список.
"""
import copy


class MyList:
    def __init__(self, data: list) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.data})'

    def __str__(self) -> str:
        return f'{self.data}'

    def __len__(self) -> int:
        return len(self.data)

    def __add__(self, other: 'MyList') -> 'MyList':
        new = copy.deepcopy(self.data)
        new.extend(other.data)
        return MyList(new)


my_list1 = MyList([1, 2, 3])
print(repr(my_list1))  # MyList([1, 2, 3])
print(str(my_list1))  # [1, 2, 3]
print(len(my_list1))  # 3

my_list2 = MyList([4, 5, 6])
my_list3 = my_list1 + my_list2
print(my_list3)  # [1, 2, 3, 4, 5, 6]
