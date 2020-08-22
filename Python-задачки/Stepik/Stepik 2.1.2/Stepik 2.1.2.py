import sys
sys.stdin = open("Input_data_1.txt", "r")

n = int(input())  # число классов исключений
# Построим структуру классов исключений
my_structure = []
my_structure.clear()
my_request = []
for i in range(n):
    my_request.clear()
    # считываем запрос и разбираем его
    my_text = input()
    if my_text.find(' ') > 0:
        my_request = my_text.split()
        # избавляемся от двоеточия
        if my_request.count(':'):
            my_request.remove(':')
    else:
        # вносим в структуру или игнорируем
        if not (my_text in my_structure):
            temp_dict = {'name_of_class_err': my_text, "class_err_parent's": []}
            my_structure.append(temp_dict)
            continue

    # заполняем структуру my_structure
    if len(my_request):
        if not (my_request[0] in my_structure):
            temp = {'name_of_class_err': my_request[0]}
            del my_request[0]
            temp["class_err_parent's"] = my_request[:]
            my_structure.append(temp)
# ===============================================================================================


def working_row(class_name):
    # Эта функция находит строку в нашей базе данных, соответствующую имени класса
    # и выводит её номер
    for row, name in enumerate(my_structure):
        if name['name_of_class_err'] == class_name:
            return row


def get_result_of_finding(row, class_par):
    if row is None:
        return False
    # Эта рекурсивная функция ищет прямого предка, а если не находит,
    # то ищет дальнего предка
    if class_par in my_structure[row]["class_err_parent's"]:
        return True
    elif len(my_structure[row]["class_err_parent's"]) > 0:
        i_find = False
        for next_par in my_structure[row]["class_err_parent's"]:
            if get_result_of_finding(working_row(next_par), class_par):
                i_find = True
                break
        if i_find:
            return True
        else:
            return False
    elif len(my_structure[row]["class_err_parent's"]) == 0:
        return False


m = int(input())  # количество обрабатываемых исключений Антоном
# Создадим список, в который будем записывать поступающие по порядку названия исключений
err_list_order = []
my_answers = []  # результирующий список, который выводим
for i in range(m):
    # считываем название ошибки
    current_err_name = input()

    # Надо проверить, является ли новая ошибка потомком предыдущих (введёных Антоном) и если да,
    # то внести её в my_answers.
    err_has_parent = False

    # Проверяем
    # если эта ошибка уже была, вносим её в результирующий список и идём дальше.
    if current_err_name in err_list_order:
        my_answers.append(current_err_name)
        continue
    # проверяем, если ли в списке ошибок предки новой ошибки
    for is_it_parent in err_list_order:
        err_has_parent = get_result_of_finding(working_row(current_err_name), is_it_parent)
        if err_has_parent:
            my_answers.append(current_err_name)
            break
    if not err_has_parent:
        err_list_order.append(current_err_name)

# ===============================================================================================
for i in my_answers:
    print(i)
