import pytest

from task_2 import all_division


# Тест деления на ноль
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)


# Тест деления двух положительных чисел
def test_division_positive_numbers():
    result = all_division(10, 2)
    assert result == 5


# Тест деления двух отрицательных чисел
def test_division_negative_numbers():
    result = all_division(-10, -2)
    assert result == 5


# Тест деления положительного числа на отрицательное число
@pytest.mark.smoke
def test_division_positive_by_negative():
    result = all_division(10, -2)
    assert result == -5


# Тест деления отрицательного числа на положительное число
def test_division_negative_by_positive():
    result = all_division(-10, 2)
    assert result == -5
