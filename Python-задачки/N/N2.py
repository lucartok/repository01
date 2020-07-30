"""
2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
"""
n = int(input('Сколько всего элементов в списке? '))

my_list = []
for i in range(n):
    my_list.append(input('Следующий элемент: '))

print('Исходные данные:\n', my_list)

last_element = len(my_list) - 2 if len(my_list) % 2 == 1 else len(my_list) - 1
for i in range(0, last_element, 2):
    temp = my_list[i + 1]
    my_list[i + 1] = my_list[i]
    my_list[i] = temp

print('Результат: \n', my_list)
