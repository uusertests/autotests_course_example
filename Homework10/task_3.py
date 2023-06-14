# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize(
    'a, b, expected_result',
    [
        (10, 2, 5),         # Набор данных 1
        (-10, -2, 5),       # Набор данных 2
        pytest.param(10, -2, -5, marks=pytest.mark.smoke),       # Набор данных 3 (смок)
        pytest.param(10, 0, 0, marks=pytest.mark.skip)   # Набор данных 4 (с пропуском)
    ]
)
@pytest.mark.smoke
def test_division(a, b, expected_result):
    result = all_division(a, b)
    assert result == expected_result
    