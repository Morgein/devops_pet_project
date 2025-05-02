import pytest
from app.main import app  # Импортируем Flask-приложение

@pytest.fixture
def client():
    """Создаем тестовый клиент Flask"""
    with app.test_client() as client:
        yield client

def test_hello(client):
    """Тестирование маршрута '/'"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello from your DevOps pet project!'

