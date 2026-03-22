class Cat:

    # конструктор
    # self - чтоб обращаться к собственным атрибутам и методам
    def __init__(self, name, year, color):
        self.name = name
        self.year = year
        self.color = color

    def walk(self):
        print(f'Cat "{self.name}" is walking')


new_cat = Cat("Bars", 2021, 'black')
print(new_cat.name)
print(new_cat.year)
print(new_cat.color)

red_cat = Cat("Red Cat", 2022, 'red')
print(red_cat.name)
print(red_cat.year)
print(red_cat.color)
red_cat.walk()


# классметод обращается к атрибутам самого класса, а не к атрибутам экземпляра класса (self можно не передавать)
class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    # статический метод - метод, который не имеет доступа ни к атрибутам класса, ни к атрибутам экземпляра
    @staticmethod
    def norm2(x, y):
        return x * x + y * y


a = Vector()
print(a.validate(5))
print(a.norm2(2, 3))


class Token:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def is_valid(value: str):
       return value.isalnum() and value.isascii()

    @classmethod
    def from_bytes(cls, data: bytes):
        return cls(data.decode('utf-8'))

raw = 'QWER123'

print(Token.is_valid(raw))

t1 = Token.from_bytes(b'world')
t2 = Token.from_bytes(b'QWER123')

print(t1.value)
print(t2.value)