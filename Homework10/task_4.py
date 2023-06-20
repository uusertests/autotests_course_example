# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


class TestExample:
    def test_one(self, test_fixture):
        # Тест 1
        assert 1 + 1 == 2

    def test_two(self, test_fixture):
        # Тест 2
        assert 2 * 2 == 4

    def test_three(self, test_fixture):
        # Тест 3
        assert 3 - 1 == 2
