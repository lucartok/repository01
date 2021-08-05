"""
Шифр Цезаря (сдвигом)
Функция принимает на вход набор символов (например, алфавит), текст и значение сдвига.
После этого сдвигает каждый символ на значение сдвига по набору символов. Если символа в наборе нет,
то он остаётся на своём месте без изменений.
"""


def decode_text_with_shift(character_set, input_text, shift_pos):
    result = ''
    for letter in input_text:
        is_upper = False
        not_find = True
        if letter.isupper():
            is_upper = True
            letter = letter.lower()
        for idx, symbol in enumerate(character_set):
            if symbol == letter:
                not_find = False
                if (idx + shift_pos) >= len(character_set):
                    index = (idx + shift_pos) % len(character_set)
                else:
                    index = idx + shift_pos
                if is_upper:
                    result += character_set[index].upper()
                else:
                    result += character_set[index]
        if not_find:
            result += letter
    return result


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text1 = 'Жщу а… тт… фрорзъ, э рысрт цчюлжфъ тсъ нфячяуц'
text = 'фтфт шф уд нбосихдо еч жеюдч щббмичью ицййшу ые аф уиф вапъь ф вёйо чбуе шбвецаыпм, ' \
       'з кн б учкбщ гъьгфусхдо оч ьчре цэщэп ъчтжбфй фпкыт яфтыш, хуё ъщгоуич десчч ек ' \
       'вьнчзэ лйцпуе, бею юыш ъп нныею, оч чецоч лдфдч хызэ шшцгниьо... сйртеэпт фтаучбэюк ' \
       'ъьтэёы нюо ункс чбщшщуёцтч чпце.'
result = ''
for letter in text:
    result = letter + result

text = result

for shift in range(len(alphabet)):  # перебор всех возможных сдвигов
    print(shift, ': ', decode_text_with_shift(alphabet, text, shift))
print(text)