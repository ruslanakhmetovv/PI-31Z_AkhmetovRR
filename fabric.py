from abc import ABC, abstractmethod

# Базовый абстрактный класс Animal
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

# Классы конкретных животных
class Lion(Animal):
    def make_sound(self):
        return "Рычание!"

class Monkey(Animal):
    def make_sound(self):
        return "Визг!"

class Elephant(Animal):
    def make_sound(self):
        return "Трубление!"

# Абстрактная фабрика AnimalFactory
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self) -> Animal:
        pass

# Конкретные фабрики для каждого животного
class LionFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Lion()

class MonkeyFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Monkey()

class ElephantFactory(AnimalFactory):
    def create_animal(self) -> Animal:
        return Elephant()

# Используем фабрики для создания экземпляров и вызова методов
if __name__ == "__main__":
    lion_factory = LionFactory()
    monkey_factory = MonkeyFactory()
    elephant_factory = ElephantFactory()
    
    # Создаем животных через фабрики
    lion = lion_factory.create_animal()
    print(lion.make_sound())  # Выведет: Рычание!

    monkey = monkey_factory.create_animal()
    print(monkey.make_sound())  # Выведет: Визг!

    elephant = elephant_factory.create_animal()
    print(elephant.make_sound())  # Выведет: Трубление!