"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar,
WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости
свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed = None
    color = None
    name = None
    is_police = None

    def go(self):
        pass

    def stop(self):
        pass

    def turn(self):
        pass

    def show_speed(self):
        pass


class TownCar(Car):
    pass

    def show_speed(self):
        pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass

    def show_speed(self):
        pass


class PoliceCar(Car):
    pass
