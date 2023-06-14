# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3

import pytest


@pytest.fixture
def id_check(request):
    return request.node.get_closest_marker("id_check").args


@pytest.mark.id_check(1, 2, 3)
def test(id_check):
    print(id_check)
