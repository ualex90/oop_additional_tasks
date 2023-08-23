"""
Напишите класс Person, представляющий человека, имеющий следующие методы:

- __init__(self, name, age): конструктор, принимающий имя человека и его возраст;
- get_name(self): метод, который возвращает имя человека;
- get_age(self): метод, который возвращает возраст человека.

Напишите класс Employee2, наследующийся от класса Person, представляющий сотрудника, имеющий следующие методы:

- __init__(self, name, age, salary): конструктор, принимающий имя сотрудника, его возраст и зарплату;
- get_salary(self): метод, который возвращает зарплату сотрудника.

Напишите класс Manager2, наследующийся от класса Employee2, представляющий менеджера, имеющий следующие методы:

- __init__(self, name, age, salary, bonus): конструктор, принимающий имя менеджера, его возраст, зарплату и бонус;
- get_bonus(self): метод, который возвращает бонус менеджера.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Employee2(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def get_salary(self):
        return self.salary


class Manager2(Employee2):
    def __init__(self, name, age, salary, bonus):
        super().__init__(name, age, salary)
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus


person = Person("John", 30)
print(person.get_name())  # John
print(person.get_age())  # 30

employee = Employee2("Jane", 25, 5000)
print(employee.get_name())  # Jane
print(employee.get_age())  # 25
print(employee.get_salary())  # 5000

manager = Manager2("Bob", 40, 10000, 5000)
print(manager.get_name())  # Bob
print(manager.get_age())  # 40
print(manager.get_salary())  # 10000
print(manager.get_bonus())  # 5000
