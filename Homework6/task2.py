# Нелокальные изменения
# Имеется функция global_function с локальной переменной msg = 1
# Ваша задача дополнить логику функции global_function следующим образом:
# global_function должна содержать в себе функцию local_function
# local_function должна изменить значение переменной msg на значение 2

def global_function():
    msg = 1  # Локальная переменная msg

    def local_function():
        nonlocal msg  # Используем ключевое слово nonlocal для указания на внешнюю переменную msg
        msg = 2  # Изменяем значение переменной msg на 2

    local_function()  # Вызываем внутреннюю функцию для изменения переменной msg
    return msg  # Возвращаем измененное значение переменной msg


assert global_function() == 2, 'Значение переменной msg должно быть равно 2'
print('Все ок')
