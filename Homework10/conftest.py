import pytest
import time


# Фикстура для всей сессии тестирования
@pytest.fixture(scope="session", autouse=True)
def session_fixture(request):
    start_time = time.time()
    print("Starting test session")

    def session_teardown():
        end_time = time.time()
        duration = end_time - start_time
        print(f"Test session finished. Duration: {duration} seconds")

    request.addfinalizer(session_teardown)


# Фикстура для конкретного теста
@pytest.fixture(scope="function")
def test_fixture(request):
    start_time = time.time()
    print("Starting test")

    def test_teardown():
        end_time = time.time()
        duration = end_time - start_time
        print(f"Test finished. Duration: {duration} seconds")

    request.addfinalizer(test_teardown)
