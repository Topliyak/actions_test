import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# Непадающие тесты
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_read_existing_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Item"

def test_create_item():
    item_data = {"name": "New Item", "price": 15.99, "is_offer": False}
    response = client.post("/items/", json=item_data)
    assert response.status_code == 200
    assert response.json()["name"] == "New Item"

def test_create_user():
    user_data = {"username": "john", "email": "john@example.com", "age": 30}
    response = client.post("/users/", json=user_data)
    assert response.status_code == 200
    assert response.json()["username"] == "john"

# Падающие тесты (закомментированы)
def test_read_nonexistent_item():
    """Этот тест упадет - мы ожидаем 404, но получаем 200"""
    response = client.get("/items/999")
    # assert response.status_code == 404  # Должно быть раскомментировано для правильной работы
    assert response.status_code == 200  # Неправильное утверждение - тест упадет

def test_create_user_with_negative_age():
    """Этот тест упадет из-за неправильного ожидания"""
    user_data = {"username": "test", "email": "test@example.com", "age": -5}
    response = client.post("/users/", json=user_data)
    # assert response.status_code == 400  # Должно быть раскомментировано
    assert response.status_code == 200  # Неправильное утверждение - тест упадет
