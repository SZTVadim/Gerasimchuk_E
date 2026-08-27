from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = []

    def add_animal(self, animal: Animal):
        self.__animals.append(animal)

    def get_animals_count(self):
        return len(self.__animals)

    def get_animals_for_index(self, index):
        return self.__animals[index]


def animal_sound(animal: Animal):
    animal.make_sound()
#  Это пример полиморфизма, так как метод make_sound есть сразу и у Dog, и у Cat

dog1 = Dog("Бобик", 3)
dog2 = Dog("Шарик", 5)
cat1 = Cat("Мурка", 2)

zoo = Zoo("Городской зоопарк")
zoo.add_animal(dog1)
zoo.add_animal(dog2)
zoo.add_animal(cat1)

zoo_count = zoo.get_animals_count()
print(zoo_count)

for i in range(zoo_count):
    animal_sound(zoo.get_animals_for_index(i))

#   example_Animals = Animal()
#   Нельзя создавать объект на основе абстрактного класса
