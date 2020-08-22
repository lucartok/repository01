"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
на склад и передачу в определенное подразделение компании. Для хранения данных о наименовании
и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую
структуру, например словарь.
"""


class Storage:
    stored_items = []

    def delivery_to(self, apl):

        new_item = {'type_of_appliance': apl.type_of_appliance,
                    'department': apl.department,
                    'condition': apl.condition,
                    'model': apl.model,
                    'serial_number': apl.serial_number,
                    'color': apl.color
                    }
        self.stored_items.append(new_item)

    def delivery_from(self):
        pass


class Appliance:

    def __init__(self, type_of_appliance, department, condition):
        self.type_of_appliance = type_of_appliance
        self.department = department
        self.condition = condition


class Printer(Appliance):
    def __init__(self, model, serial_number, color, type_of_appliance, department, condition):
        self.model = model
        self.serial_number = serial_number
        self.color = color
        super().__init__(type_of_appliance, department, condition)


class Scanner(Appliance):

    def __init__(self, model, serial_number, color, type_of_appliance, department, condition):
        self.model = model
        self.serial_number = serial_number
        self.color = color
        super().__init__(type_of_appliance, department, condition)


printer1 = Printer('Canon A1232', 'A343Ke3234', 'white', 'printer', 'accounting', 'new')
scanner1 = Scanner('Xerox P12', 'n23ndkdasdf', 'black', 'scanner', 'writers', 'used')

sklad1 = Storage
sklad1.delivery_to(self=sklad1, apl=printer1)
sklad1.delivery_to(self=sklad1, apl=scanner1)

print(sklad1.stored_items)
