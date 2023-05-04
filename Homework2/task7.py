# Дано 2 строки из неповторяющихся символов: первая строка длиной 3 символа,
# вторая точно содержит символы первой строки в любом порядке.
# Напишите программу, не используя циклы и условия, которая находит срез минимальной длины
# во второй строке, который будет содержать все символы первой строки. Например,
# first_string = ‘wtf’ и second_string = ‘brick quz
# jmpy veldt whangs fox’, срез минимальной длины: ‘t whangs f’

# Зададим строки
first_string = 'wtf'
second_string = 'brick quz jmpy veldt whangs fox'

# Найдем срез минимальной длины, содержащий все символы из первой строки
result = second_string[min(second_string.index(char) for char in first_string):
                       max(second_string.index(char) for char in first_string) + 1]

# Выведем результат на экран
print('Первая строка:', first_string)
print('Вторая строка:', second_string)
print('Срез минимальной длины, содержащий все символы первой строки:', result)
