class Temperature:

    def __init__(self, value):
        self._c = value # _ - protected значение

    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature cannot be negative')
        self._c = value
        return self._c

c = Temperature(10)
print(c._c)
print(c.celsius(100))

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    def print_data(self):
        print(f"Пользователь с именем {self.__name} и возрастом {self.__age}")

tom = Person("Tom", 22)
tom.print_data()
tom.__age = 10
print(tom.__age)
# print(tom.__name) -- нельзя обратиться к private-полю