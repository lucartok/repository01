"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
string_count = 0
words_count = 0
all_words_count = 0

with open('HW_5_2.txt', 'r', encoding='utf-8') as f:
    for line in f:

        # считаем количество строк
        string_count += 1

        # считаем количество слов
        line.strip()  # удаляем лишние пробелы
        words_count += line.count(' ') + 1

        # считаем общее количество слов
        all_words_count += words_count

        # выводим строку и рядом с ней кол-во слов
        print(words_count, line.replace('\n', ''))
        words_count = 0

print('-' * 50)
print(f'Количество строк: {string_count}')
print(f'Количество слов: {all_words_count}')
