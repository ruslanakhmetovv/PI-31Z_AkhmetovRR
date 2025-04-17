
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

class Transmission:
    def __init__(self, gearbox_type):
        self.gearbox_type = gearbox_type

class Body:
    def __init__(self, body_style):
        self.body_style = body_style

class Wheel:
    def __init__(self, wheel_size):
        self.wheel_size = wheel_size

class Car:
    def __init__(self):
        self.engine = None
        self.transmission = None
        self.body = None
        self.wheels = []

    def set_engine(self, engine):
        self.engine = engine

    def set_transmission(self, transmission):
        self.transmission = transmission

    def set_body(self, body):
        self.body = body

    def add_wheel(self, wheel):
        self.wheels.append(wheel)

    def display_specs(self):
        print(f"Engine Horsepower: {self.engine.horsepower}")
        print(f"Transmission Type: {self.transmission.gearbox_type}")
        print(f"Body Style: {self.body.body_style}")
        print(f"Wheel Size: {[wheel.wheel_size for wheel in self.wheels]}")

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def build_engine(self, horsepower):
        self.car.set_engine(Engine(horsepower))

    def build_transmission(self, gearbox_type):
        self.car.set_transmission(Transmission(gearbox_type))

    def build_body(self, body_style):
        self.car.set_body(Body(body_style))

    def build_wheels(self, wheel_size):
        for _ in range(4):
            self.car.add_wheel(Wheel(wheel_size))

    def get_result(self):
        return self.car


class CarDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_sedan(self):
        self.builder.build_engine(180)
        self.builder.build_transmission("Automatic")
        self.builder.build_body("Sedan")
        self.builder.build_wheels(17)

    def construct_suv(self):
        self.builder.build_engine(250)
        self.builder.build_transmission("Manual")
        self.builder.build_body("SUV")
        self.builder.build_wheels(19)

    def construct_sports_car(self):
        self.builder.build_engine(350)
        self.builder.build_transmission("Sequential")
        self.builder.build_body("Sports Car")
        self.builder.build_wheels(20)

# Пример клиента, использующего директор и строитель
builder = CarBuilder()
director = CarDirector(builder)

# Строительство седана
director.construct_sedan()
sedan = builder.get_result()
sedan.display_specs()

# Строительство внедорожника (SUV)
director.construct_suv()
suv = builder.get_result()
suv.display_specs()

# Строительство спортивного автомобиля
director.construct_sports_car()
sports_car = builder.get_result()
sports_car.display_specs()