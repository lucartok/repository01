"""
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Или эквивалентно записи:

class Class1(Class2, Class3 ... ClassK):
    pass
Класс A является прямым предком класса B, если B отнаследован от A:


class B(A):
    pass


Класс A является предком класса C, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Например:
class B(A):
    pass

class C(B):
    pass

# A -- предок С


Вам необходимо отвечать на запросы, является ли один класс предком другого класса

Важное примечание:
Создавать классы не требуется.
Мы просим вас промоделировать этот процесс, и понять существует ли путь от одного класса до другого.
Формат входных данных
В первой строке входных данных содержится целое число n - число классов.

В следующих n строках содержится описание наследования классов. В i-й строке указано от каких классов
наследуется i-й класс. Обратите внимание, что класс может ни от кого не наследоваться. Гарантируется,
что класс не наследуется сам от себя (прямо или косвенно), что класс не наследуется явно от одного
класса более одного раза.

В следующей строке содержится число q - количество запросов.

В следующих q строках содержится описание запросов в формате <имя класса 1> <имя класса 2>.
Имя класса – строка, состоящая из символов латинского алфавита, длины не более 50.

Формат выходных данных
Для каждого запроса выведите в отдельной строке слово "Yes", если класс 1 является предком класса 2,
и "No", если не является.

Sample Input:

4
A
B : A
C : A
D : B C
4
A B
B D
C D
D A
Sample Output:

Yes
Yes
Yes
No
"""
"""
my_structure = [
     {'name_of_class': 'A', 'class_parent's': []},
     {'name_of_class': 'B', 'class_parent's': ['A']},
     {'name_of_class': 'C', 'class_parent's': ['A']},
     {'name_of_class': 'D', 'class_parent's': ['B', 'C']}
    ...
]
"""
import sys
sys.stdin = open("input2.txt", "r")

n = int(input())  # число классов
# Построим структуру классов
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
            temp_dict = {'name_of_class': my_text, "class_parent's": []}
            my_structure.append(temp_dict)
            continue

    # заполняем структуру my_structure
    if len(my_request):
        if not (my_request[0] in my_structure):
            temp = {'name_of_class': my_request[0]}
            del my_request[0]
            temp["class_parent's"] = my_request[:]
            my_structure.append(temp)

# ===============================================================================================
def working_row(class_name):
    # Эта функция находит строку в нашей базе данных, соответствующую имени класса
    # и выводит её номер
    for row in range(len(my_structure)):
        if my_structure[row]['name_of_class'] == class_name:
            return row


def get_result_of_finding(row, class_par):
    if row is None:
        return 'No'
    # Эта рекурсивная функция ищет прямого предка, а если не находит,
    # то ищет дальнего предка
    if class_par in my_structure[row]["class_parent's"]:
        return 'Yes'
    elif len(my_structure[row]["class_parent's"]) > 0:
        i_find = False
        for next_par in my_structure[row]["class_parent's"]:
            if get_result_of_finding(working_row(next_par), class_par) == 'Yes':
                i_find = True
                break
        if i_find:
            return 'Yes'
        else:
            return 'No'
    elif len(my_structure[row]["class_parent's"]) == 0:
        return 'No'


q = int(input())  # количество запросов
my_answers = []
for i in range(q):
    my_request.clear()
    # считываем запрос и разбираем его
    my_request = input().split()

    # ищем
    if my_request[0] == my_request[1] and working_row(my_request[0]):
        my_answers.append('Yes')
    else:
        my_answers.append(get_result_of_finding(working_row(my_request[1]), my_request[0]))
    # ===============================================================================================
    for i in my_request:
        print(i)
# ===============================================================================================
# with open('output2.2.txt', 'w', encoding='utf-8') as f:
#     for answer in my_answers:
#         f.write(answer + '\n')
