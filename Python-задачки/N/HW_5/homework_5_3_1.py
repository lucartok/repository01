"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую
построчно данные. При этом английские числительные должны заменяться на
русские. Новый блок строк должен записываться в новый текстовый файл.

"""

my_file = open('HW_5_3_1.txt', encoding='utf-8')
new_file = open('HW_5_3_1_1.txt', 'w', encoding='utf-8')
numbers = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for i in my_file:
    i = i.split(' ', 1)
    string = numbers[i[0]] + '  ' + i[1]
    print(string.replace('\n', ''), file=new_file)

my_file.close()
new_file.close()
