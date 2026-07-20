import os
import pytest
import requests

# Конфигурация
API_URL = "https://book-club.qa.guru/api/v1/auth/token/"
USERNAME = os.getenv("TEST_USERNAME", "test2007262048")
PASSWORD = os.getenv("TEST_PASSWORD", "test2007262048")
TOKEN_PREFIX = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"


# Вспомогательные функции
def perform_auth_request(payload, headers=None):
    """Выполняет запрос аутентификации и возвращает ответ"""
    headers = headers or {}
    return requests.post(API_URL, json=payload, headers=headers)


def print_response_details(response):
    """Выводит детали ответа для отладки"""
    print(f"\nStatus code: {response.status_code}")
    print(f"Headers: {response.headers}")
    print(f"Body: {response.text}")


def validate_token_structure(token):
    """Проверяет структуру JWT токена"""
    assert token.startswith(TOKEN_PREFIX), "Token should start with expected prefix"
    parts = token.split(".")
    assert len(parts) == 3, "Token should have 3 parts"
    return parts


def create_auth_payload(username, password):
    """Создает payload для запроса аутентификации"""
    return {"username": username, "password": password}


# Тесты
@pytest.mark.smoke
def test_successful_auth():
    """Тест успешной аутентификации с валидными учетными данными"""
    payload = create_auth_payload(USERNAME, PASSWORD)
    response = perform_auth_request(payload)

    print_response_details(response)

    # Проверка статуса
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Проверка структуры ответа
    body = response.json()
    assert "access" in body, "Response should contain access token"
    assert "refresh" in body, "Response should contain refresh token"

    access_token = body["access"]
    refresh_token = body["refresh"]

    # Валидация токенов
    validate_token_structure(access_token)
    validate_token_structure(refresh_token)

    # Дополнительные проверки
    assert access_token != refresh_token, "Access and refresh tokens should be different"
    assert len(access_token) > 0, "Access token should not be empty"
    assert len(refresh_token) > 0, "Refresh token should not be empty"


@pytest.mark.negative
def test_wrong_credentials_auth():
    """Тест аутентификации с неверными учетными данными"""
    payload = create_auth_payload(USERNAME, "wrong_password")
    response = perform_auth_request(payload)

    print_response_details(response)

    # Проверка статуса
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"

    # Проверка сообщения об ошибке
    body = response.json()
    assert "detail" in body, "Response should contain error detail"
    assert body["detail"] == "Invalid username or password.", "Unexpected error message"


@pytest.mark.negative
def test_wrong_content_type_auth():
    """Тест аутентификации с неправильным Content-Type заголовком"""
    payload = create_auth_payload(USERNAME, PASSWORD)
    headers = {"content-type": "image/png"}

    response = perform_auth_request(payload, headers)

    print_response_details(response)

    # Проверка статуса
    assert response.status_code == 415, f"Expected 415, got {response.status_code}"

    # Проверка сообщения об ошибке
    body = response.json()
    assert "detail" in body, "Response should contain error detail"
    assert "Unsupported media type" in body["detail"], "Unexpected error message"


# Дополнительный тест для проверки пустых данных
@pytest.mark.negative
def test_empty_credentials_auth():
    """Тест аутентификации с пустыми учетными данными"""
    payload = create_auth_payload("", "")
    response = perform_auth_request(payload)

    print_response_details(response)

    # Проверка на валидацию на стороне сервера
    assert response.status_code in [400, 401, 422], \
        f"Expected error status code, got {response.status_code}"


# Фикстура для повторного использования в других тестах
@pytest.fixture
def auth_token():
    """Возвращает валидный токен для использования в других тестах"""
    payload = create_auth_payload(USERNAME, PASSWORD)
    response = perform_auth_request(payload)
    assert response.status_code == 200
    return response.json()["access"]


# Параметризованный тест для различных сценариев
@pytest.mark.parametrize("username,password,expected_status", [
    (USERNAME, PASSWORD, 200),
    (USERNAME, "wrong", 401),
    ("wrong_user", PASSWORD, 401),
    ("", PASSWORD, 401),
    (USERNAME, "", 401),
])
def test_auth_various_scenarios(username, password, expected_status):
    """Тест аутентификации с различными комбинациями учетных данных"""
    payload = create_auth_payload(username, password)
    response = perform_auth_request(payload)

    assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code} for credentials: {username}/{password}"
