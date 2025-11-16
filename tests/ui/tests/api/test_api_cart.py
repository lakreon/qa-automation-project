import requests
import pytest

BASE_URL = "https://www.demoblaze.com"

def test_add_to_cart_api():
    # Пример API-запроса (Demoblaze имеет публичные эндпоинты)
    response = requests.get(f"{BASE_URL}/data/product.json")
    data = response.json()
    
    assert response.status_code == 200
    assert len(data) > 0  # Проверяем, что товары загружены
    assert "title" in data[0]  # Первый товар имеет название
