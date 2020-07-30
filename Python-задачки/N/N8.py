"""
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""
total_sum = 0
try:
    while True:
        for el in map(int, input().split()):
            current_sum = 0
            current_sum += el
            total_sum = total_sum + current_sum
        print(f'Сумма: {total_sum}')
except ValueError:
    print(f'Итого: {total_sum}')

# text_string = '23 2 12 12 32 34 12 33 2 1 2 33'
# text_list = map(int, text_string.split())
# print(sum(text_list))
