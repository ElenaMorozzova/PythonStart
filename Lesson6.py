# Task1 Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод
# running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать
# переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого
# состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый)
# — на ваше усмотрение. Переключение между режимами должно осуществляться только в
# указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр
# и вызвав описанный метод.Задачу можно усложнить, реализовав проверку порядка режимов, и
# при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def __init__(self, color):
        self.__color = color

    def running(self):
        i = 0
        color_list = ['красный', 'желтый', 'зеленый']
        while i < 3:
            for col in color_list:
                print(f'Сейчас светофор {TrafficLight.__color}')
                if i == 0:
                    sleep(7)
                    TrafficLight.__color = color_list[i + 1]
                elif i == 1:
                    sleep(2)
                    TrafficLight.__color = color_list[i + 1]
                elif i == 2:
                    sleep(10)
                    print(f'Светофор закончил работу')
                i += 1


TrafficLight = TrafficLight('красный')
TrafficLight.running()

# Task2 Реализовать класс Road ( дорога), в котором определить атрибуты: length ( длина), width
# (ширина). Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого
# для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса
# асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см
# толщины полотна. Проверить работу метода. # Например: 20м*5000м*25кг*5см = 12500 т


class Road:
    __weight_of_sm = 25
    __height_in_sm = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_tonns(self):
        return (self.__length * self.__width * self.__weight_of_sm * self.__height_in_sm) / 1000


road_1 = Road(float(input('Длина дороги:')), float(input('Ширина дороги:')))
print(f'Масса асфальта для дороги (тонн):{road_1.mass_tonns()}')
print(f'Массу на кв. м. полотна тоже изменить нельзя она равна:{road_1._Road__weight_of_sm}')

# Task3 Реализовать базовый класс Worker (работник), в котором определить атрибуты: name,
# surname, position ( должность), income ( доход). Последний атрибут должен быть
# защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus}. Создать класс Position ( должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника ( get_full_name) и
# дохода с учетом премии ( get_total_income) . Проверить работу примера на реальных данных
# (создать экземпляры класса Position , передать данные, проверить значения атрибутов,
# вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + " " + self.surname
        return f'Полное имя сотрудника: {full_name}'

    def get_total_income(self):
        total_salary = self._income.get("wage") + self._income.get("bonus")
        return f'Доход с учетом премиии: {total_salary}'


a = Position('Николай', 'Николаев', 'Экономист', 50000, 10000)
print(a.get_full_name())
print(a.get_total_income())

# Task4 Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed,
# color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод
# show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60
# (TownCar ) и 40 (WorkCar ) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False, direction=None):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if self.is_police is True:
            return f"{self.color} полицейский {self.name} поехал со скоростью {self.speed} км/ч"
        else:
            return f"{self.color} {self.name} поехал со скоростью {self.speed} км/ч"

    def stop(self):
        if self.is_police is True:
            return f"{self.color} полицейский {self.name} остановился"
        else:
            return f"{self.color} {self.name} остановился"

    def turn(self, direction):
        self.direction = direction
        if direction in ['налево', 'направо', 'назад', 'right', 'left', 'back']:
            return f"{self.color} {self.name} повернул {self.direction}"
        else:
            return f"Укажите правильное направление"

    def show_speed(self):
        return f"Текущая скорость автомобиля {self.speed} км/ч"


class TownCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if float(self.speed) > 60:
            return f"Превышение скорости на {float(self.speed) - 60} км/ч!"
        else:
            return f"Скорость в пределах допустимого - {self.speed} км/ч"


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        if float(self.speed) > 40:
            return f"Превышение скорости на {float(self.speed) - 40} км/ч!"
        else:
            return f"Скорость в пределах допустимого - {self.speed} км/ч"


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True, direction=None):
        super().__init__(speed, color, name, is_police, direction)


TownCar_1 = TownCar('70', 'Красный', 'BMW')
print(TownCar_1.go())
print(TownCar_1.stop())
print(TownCar_1.turn('направо'))
print(TownCar_1.show_speed())

WorkCar_1 = WorkCar('70', 'Синий', 'Smart')
print(WorkCar_1.go())
print(WorkCar_1.stop())
print(WorkCar_1.turn('направо'))
print(WorkCar_1.show_speed())

SportCar_1 = SportCar('120', 'Белый', 'Lamborghini')
print(SportCar_1.go())
print(SportCar_1.stop())
print(SportCar_1.turn('кккккккк'))
print(SportCar_1.show_speed())

PoliceCar_1 = PoliceCar('100', 'Черный', 'Hyundai')
print(PoliceCar_1.go())
print(PoliceCar_1.stop())
print(PoliceCar_1.turn('налево'))
print(PoliceCar_1.show_speed())

# Task5 Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title
# (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать
# три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
# реализовать переопределение метода draw. Для каждого из классов метод должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки.'


class Pen(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        return f'Пишет {self.title}.'


class Pencil(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        return f'Рисует {self.title}.'


class Handle(Stationery):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def draw(self):
        return f'Красит {self.title}.'


Stationery_0 = Stationery('Any')
print(Stationery_0.draw())
Pen_1 = Pen('синяя ручка')
print(Pen_1.draw())
Pencil_1 = Pencil('красный карандаш')
print(Pencil_1.draw())
Handle_1 = Handle('зеленый маркер')
print(Handle_1.draw())
