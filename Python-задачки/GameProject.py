import random

words_bank = (
    'автострада', 'бензин', 'инопланетянин', 'самолет',
    'библиотека', 'шайба', 'олимпиада', 'весна',
    'шахматы',
)

secret_word = random.choice(words_bank)
# print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))
# gamer_word[2] = 'г'
# print(gamer_word)
# print(dir(gamer_word))

print('Угадайте слово!')

errors_cnt = 0
while True:
    letter = input('введите ОДНУ русскую букву: ').lower()
    if len(letter) != 1:  # ord()
        continue

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            # print(idx, symbol)
            if symbol == letter:
                gamer_word[idx] = letter
        if gamer_word.count('*') == 0:
            print('вы выиграли!')
            print(f'было загадано слово: {secret_word}')
            break
    else:
        # errors_cnt++
        # errors_cnt = errors_cnt + 1
        errors_cnt += 1
        print('ошибок допущено:', errors_cnt)
        if errors_cnt == 8:
            print('вы проиграли ;(')
            break
    print(''.join(gamer_word))
