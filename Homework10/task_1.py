# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код
def generate_random_name():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        word1 = ''.join(random.choice(letters) for _ in range(random.randint(1, 15)))
        word2 = ''.join(random.choice(letters) for _ in range(random.randint(1, 15)))
        yield f"{word1} {word2}"
