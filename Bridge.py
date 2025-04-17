from abc import ABC, abstractmethod

# Интерфейс для устройства (общий протокол взаимодействия)
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def set_state(self, state):
        pass

# Абстрактный класс устройства ТВ
class TV(Device):
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1

    def turn_on(self):
        print(f'{self.brand} телевизор включен.')

    def turn_off(self):
        print(f'{self.brand} телевизор выключен.')

    def set_state(self, channel):
        self.channel = channel
        print(f'{self.brand} переключил канал на {channel}.')

# Абстрактный класс устройства Лампочка
class Light(Device):
    def __init__(self, brand):
        self.brand = brand
        self.brightness = 50

    def turn_on(self):
        print(f'{self.brand} лампочка включена.')

    def turn_off(self):
        print(f'{self.brand} лампочка выключена.')

    def set_state(self, brightness):
        self.brightness = brightness
        print(f'{self.brand} уровень яркости установлен на {brightness}%.')

# Производители устройств (конкретные реализации)
class SonyTV(TV):
    def __init__(self):
        super().__init__('Sony')

class SamsungTV(TV):
    def __init__(self):
        super().__init__('Samsung')

class PhilipsLight(Light):
    def __init__(self):
        super().__init__('Philips')

class IKEALight(Light):
    def __init__(self):
        super().__init__('IKEA')

# Удалённый контроллер (использует интерфейс Device)
class RemoteControl:
    def __init__(self, device):
        self.device = device

    def power_toggle(self):
        if isinstance(self.device, TV):
            if self.device.channel > 0:
                self.device.turn_off()
            else:
                self.device.turn_on()
        else:
            if self.device.brightness > 0:
                self.device.turn_off()
            else:
                self.device.turn_on()

    def change_state(self, state):
        self.device.set_state(state)

# Клиентский код
if __name__ == '__main__':
    samsung_tv = SamsungTV()
    remote_control_tv = RemoteControl(samsung_tv)
    remote_control_tv.power_toggle()  # Включаем телевизор
    remote_control_tv.change_state(5)  # Переключаем канал на 5-й
    remote_control_tv.power_toggle()  # Выключаем телевизор

    philips_light = PhilipsLight()
    remote_control_light = RemoteControl(philips_light)
    remote_control_light.power_toggle()  # Включаем лампочку
    remote_control_light.change_state(80)  # Регулируем яркость до 80%
    remote_control_light.power_toggle()  # Выключаем лампочку