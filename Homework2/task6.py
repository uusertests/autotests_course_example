# Дана строка. Напишите программу удаления символов,
# которые имеют нечетные значения индекса заданной строки

# Зададим строку
str_input = 'Hello, world!'

# Создадим новую строку, удалив символы с нечетными индексами
str_output = ''
for i in range(len(str_input)):
    if i % 2 == 0:
        str_output += str_input[i]

# Выведем результат
print('Исходная строка:', str_input)
print('Строка с удаленными символами:', str_output)
