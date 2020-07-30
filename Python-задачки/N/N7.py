def int_func(word1):
    return word1.capitalize()


# print(int_func(input("Введите слово: ")))

"""
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных
пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной
строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
"""
# text = input('Введите предложение:\n')
#
# list_of_words = text.split(' ')
# text = ''
# for one_word in list_of_words:
#     text += int_func(one_word)
#     text += ' '
#
# print('Результат:\n' + text)

"""
или
"""


# text = input('Введите предложение:\n')
#
# list_of_words = text.split(' ')
# text = []
# for one_word in list_of_words:
#     text.append(int_func(one_word))
#
# sec = ' '
# print('Результат:\n' + sec.join(text))
