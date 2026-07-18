import requests
import pytest

# Константы для переиспользования
BASE_URL = "https://selenoid.autotests.cloud"
STATUS_ENDPOINT = f"{BASE_URL}/wd/hub/status"
VALID_CREDENTIALS = ("user1", "1234")
INVALID_CREDENTIALS = ("user1", "123456")


def get_status_response(auth=None):
    """Вспомогательная функция для выполнения запроса к status endpoint"""
    response = requests.get(STATUS_ENDPOINT, auth=auth)
    print(f"\nStatus code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Body: {response.text}")
    return response


def test_ready_is_true():
    """Тест проверяет, что статус ready = true при валидных кредах"""
    response = get_status_response(auth=VALID_CREDENTIALS)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    body = response.json()
    assert body.get("value", {}).get("ready") is True, "Expected ready to be True"


def test_wrong_credentials():
    """Тест проверяет, что невалидные креды возвращают 401"""
    response = get_status_response(auth=INVALID_CREDENTIALS)

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


def test_unauthorized_401():
    """Тест проверяет, что запрос без авторизации возвращает 401"""
    response = get_status_response(auth=None)

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"


# Альтернативный вариант с параметризацией (если нужно объединить тесты)
@pytest.mark.parametrize("auth,expected_status,expected_ready", [
    (VALID_CREDENTIALS, 200, True),
    (INVALID_CREDENTIALS, 401, None),
    (None, 401, None),
])
def test_status_endpoint(auth, expected_status, expected_ready):
    """Параметризованный тест для всех сценариев авторизации"""
    response = get_status_response(auth=auth)

    assert response.status_code == expected_status

    if expected_ready is not None:
        body = response.json()
        assert body.get("value", {}).get("ready") == expected_ready
