"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
"""


class Storage:
    pass


class Appliance:
    gen_param_1 = None
    gen_param_2 = None
    gen_param_3 = None
    gen_param_4 = None
    gen_param_5 = None


class Printer(Appliance):
    prn_param_1 = None
    prn_param_2 = None
    prn_param_3 = None


class Scanner(Appliance):
    scan_param_1 = None
    scan_param_2 = None
    scan_param_3 = None


class Xerox(Appliance):
    xrx_param_1 = None
    xrx_param_2 = None
    xrx_param_3 = None
