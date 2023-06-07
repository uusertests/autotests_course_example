# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", 'r') as file:
    lines = file.read().splitlines()

# Удаляем пустые строки
lines = [line for line in lines if line.strip()]

# Преобразуем строки в целочисленные значения
prices = []
purchase = []
for line in lines:
    if line:
        prices.append(int(line))
    else:
        if purchase:
            # Сортируем покупки внутри блока
            purchase.sort(reverse=True)
            # Добавляем три самые дорогие покупки в список цен
            prices.extend(purchase[:3])
            purchase = []
    # Проверяем, что в блоке только одна покупка
    if line and not purchase:
        purchase.append(int(line))

# Если файл закончился без пустой строки, добавляем покупки из последнего блока
if purchase:
    purchase.sort(reverse=True)
    prices.extend(purchase[:3])

# Сортируем все цены по убыванию
prices.sort(reverse=True)

# Находим сумму трех самых дорогих покупок
three_most_expensive_purchases = sum(prices[:3])
print("Сумма трех самых дорогих покупок:", three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346
