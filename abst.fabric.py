from abc import ABC, abstractmethod


# Объявляем абстрактный класс Car, представляющий интерфейс для всех автомобилей
class Car(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass


# Классы конкретных автомобилей
class ElectricCar(Car):
    def start_engine(self):
        return "Электродвигатель запущен."

    def accelerate(self):
        return "Ускорение электромобиля."


class PetrolCar(Car):
    def start_engine(self):
        return "Двигатель внутреннего сгорания запущен."

    def accelerate(self):
        return "Ускорение бензинового автомобиля."


class HybridCar(Car):
    def start_engine(self):
        return "Запуск гибридного двигателя."

    def accelerate(self):
        return "Ускорение гибридного автомобиля."


# Объявляем абстрактную фабрику CarFactory
class CarFactory(ABC):
    @abstractmethod
    def create_electric_car(self):
        pass

    @abstractmethod
    def create_petrol_car(self):
        pass

    @abstractmethod
    def create_hybrid_car(self):
        pass


# Конкретные фабрики для создания разных типов автомобилей
class ElectricCarFactory(CarFactory):
    def create_electric_car(self):
        return ElectricCar()

    def create_petrol_car(self):
        raise NotImplementedError("Петрол-автомобиль не поддерживается данной фабрикой.")

    def create_hybrid_car(self):
        raise NotImplementedError("Гибридный автомобиль не поддерживается данной фабрикой.")


class PetrolCarFactory(CarFactory):
    def create_electric_car(self):
        raise NotImplementedError("Электрический автомобиль не поддерживается данной фабрикой.")

    def create_petrol_car(self):
        return PetrolCar()

    def create_hybrid_car(self):
        raise NotImplementedError("Гибридный автомобиль не поддерживается данной фабрикой.")


class HybridCarFactory(CarFactory):
    def create_electric_car(self):
        raise NotImplementedError("Электрический автомобиль не поддерживается данной фабрикой.")

    def create_petrol_car(self):
        raise NotImplementedError("Петрол-автомобиль не поддерживается данной фабрикой.")

    def create_hybrid_car(self):
        return HybridCar()


# Используем абстрактную фабрику для создания автомобилей
def main():
    factories = {
        'electric': ElectricCarFactory(),
        'petrol': PetrolCarFactory(),
        'hybrid': HybridCarFactory()
    }

    for factory_type in ['electric', 'petrol', 'hybrid']:
        car_factory = factories[factory_type]
        
        try:
            if factory_type == 'electric':
                car = car_factory.create_electric_car()
            elif factory_type == 'petrol':
                car = car_factory.create_petrol_car()
            else:
                car = car_factory.create_hybrid_car()
            
            print(f"Тип авто: {factory_type.capitalize()} ({car.start_engine()})")
            print(car.accelerate())
        except NotImplementedError as e:
            print(e)


if __name__ == "__main__":
    main()