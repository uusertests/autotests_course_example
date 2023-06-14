# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
# Открываем файл для чтения
with open('test_file/task_3.txt', 'r') as file:
    lines = file.readlines()

# Удаляем символы новой строки из каждой строки
lines = [line.strip() for line in lines]

purchases = []  # Список для хранения покупок
current_purchase_total = 0  # Переменная для хранения суммы текущей покупки

# Обрабатываем каждую строку
for line in lines:
    if line == '':
        # Если встречаем пустую строку, значит текущая покупка закончилась
        # Добавляем сумму текущей покупки в список покупок
        if current_purchase_total > 0:
            purchases.append(current_purchase_total)
            current_purchase_total = 0  # Обнуляем сумму для следующей группы
    else:
        # Преобразуем строку с ценой в число и добавляем к текущей покупке
        current_purchase_total += float(line)

# Добавляем последнюю покупку в список покупок, если она есть
if current_purchase_total > 0:
    purchases.append(current_purchase_total)

# Сортируем список покупок по убыванию суммы
purchases.sort(reverse=True)

# Суммируем три самых дорогих покупки
three_most_expensive_purchases = sum(purchases[:3])

assert three_most_expensive_purchases == 202346
