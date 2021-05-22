# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# import time
#
#
# class TrafficLight:
#     __color: str
#
#     def __init__(self, color):
#         TrafficLight.__color = color
#         print(self.__color)
#
#     def running(self, timer):
#         self.timer = timer
#         time.sleep(self.timer)
#
#
# traffic_light = TrafficLight("Red")
# traffic_light.running(7)
# traffic_light = TrafficLight("Yellow")
# traffic_light.running(2)
# traffic_light = TrafficLight("Green")
# traffic_light.running(5)

# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т
# class Road:
#     _length: int
#     _width: int
#     depth: int
#
#     def __init__(self, length, width, depth):
#         Road._length = length
#         Road._width = width
#         Road.depth = depth
#         #print(self._length, self._width, self.depth)
#
#     def calculate():
#         total = Road._length * Road._width * Road.depth * 0.025
#         print(f'{Road._length}м*{Road._width}м*{Road.depth}см*25кг = {total}т')
#
#
# length = int(input(f'Введите длину полотна в метрах: '))
# width = int(input(f'Введите ширину полотна в метрах: '))
# depth = int(input(f'Введите толщину полотна в сантиметрах: '))
# calc = Road(length, width, depth)
# Road.calculate()

# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).
# class Worker:
#     name: str
#     surname: str
#     position: str
#     _income: list
#
#     def __init__(self, name, surname, position, income):
#         Worker.name = name
#         Worker.surname = surname
#         Worker.position = position
#         Worker._income = income
#         #print(self.name, self.surname, self.position, self._income)
#
# class Position(Worker):
#     def get_full_name():
#         print(f'Полное имя: {Worker.name} {Worker.surname}')
#
#     def get_total_income():
#         print(f'Полный доход: {Worker._income[0] + Worker._income[1]}')
#
# f_name = input(f'Введите имя: ')
# f_surname = input(f'Введите фамилию: ')
# pos = input(f'Введите должность: ')
# f_dict = []
# f_dict.append(int(input(f'Введите оклад: ')))
# f_dict.append(int(input(f'Введите премию: ')))
# worker = Worker(f_name, f_surname, pos, f_dict)
# Position.get_full_name()
# Position.get_total_income()
#
# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        Car.speed = speed
        Car.color = color
        Car.name = name
        Car.is_police = is_police

    def go():
        print(f'Машина поехала')

    def stop():
        print(f'Машина остановилась')

    def turn(direction):
        print(f'Машина поворачивает {direction}')

    def show_speed():
        print(f'Текущая скорость {Car.speed}')


class TownCar(Car):
    def show_speed():
        if Car.speed > 60:
            print(f'{TownCar}Превышение скорости')


class SportCar(Car):
    def show_def():
        print(f'Это спортивная машина')


class WorkCar(Car):
    def show_speed():
        if Car.speed > 40:
            print(f'{WorkCar}Превышение скорости')


class PoliceCar(Car):
    def show_def():
        if Car.is_police is True:
            print(f'Это полицейская машина')

car = Car(61, "Red", "Lada", True)
Car.go()
Car.stop()
Car.turn("Налево")
Car.show_speed()
TownCar.show_speed()
SportCar.show_def()
WorkCar.show_speed()
PoliceCar.show_def()
























#
#
#
# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
#
#
#
# 6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.