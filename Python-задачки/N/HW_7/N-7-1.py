"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором
@classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:

    # def __init__(self, text):
    #     self.text = text  # не знаю, нафига тогда это надо.

    @classmethod
    def from_string(cls, day_month_year):
        try:
            day, month, year = map(int, day_month_year.split('.'))
        except ValueError:
            print('Дружочек, это не дата!')
        else:
            print(day, month, year)

    @staticmethod
    def is_date_valid(day_month_year):
        try:
            day, month, year = map(int, day_month_year.split('.'))
        except ValueError:
            print('Дружочек, это не дата!')
        else:
            if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2020:
                print('Верная дата')
            else:
                print('Неверная дата')


text = input('Введите дату: ')
Date.from_string(text)
Date.is_date_valid(text)
