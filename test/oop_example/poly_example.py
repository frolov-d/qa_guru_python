class Alive:
    def __init__(self, year):
        self.year = year

    def alive(self):
        print(f'It is alive ({self.year})')


class Animal:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def speak():
        print('speak')


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        s = f"{self.name.strip()} makes Woof"
        print(s)


class Cat(Animal, Alive):

    def __init__(self, name, year, color=None):
        super().__init__(name)
        Alive.__init__(self, year)
        self.color = color

    def walk(self):
        print(f'Cat "{self.name}" walk ... ')

    def speak(self):
        s = f"{self.name.strip()} makes Meow"
        print(s)


animal = Animal('Animal')
animal.speak()

dog = Dog('Bob')
dog.speak()
print(dog.name)

cat = Cat('Черныщ', 2012, 'black')
print(cat.name)
cat.walk()
cat.speak()
cat.alive()
