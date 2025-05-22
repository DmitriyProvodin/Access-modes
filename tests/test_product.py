import pytest
from src.product import Product

# Проверка создания продукта и геттеров
def test_create_product():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert product.name == "Iphone 15"
    assert product.description == "512GB, Gray space"
    assert product.price == 210000.0
    assert product.quantity == 8

# Проверка сеттера цены — корректное изменение
def test_price_setter_valid():
    product = Product("Xiaomi", "Описание", 1000.0, 3)
    product.price = 2000.0
    assert product.price == 2000.0

# Проверка сеттера цены — некорректное значение (0)
def test_price_setter_zero(capfd):
    product = Product("Xiaomi", "Описание", 1000.0, 3)
    product.price = 0
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 1000.0

# Проверка сеттера цены — некорректное значение (<0)
def test_price_setter_negative(capfd):
    product = Product("Xiaomi", "Описание", 1000.0, 3)
    product.price = -100
    out, _ = capfd.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in out
    assert product.price == 1000.0

# Проверка подтверждения понижения цены (подтверждение "y")
def test_price_setter_lower_confirm(monkeypatch):
    product = Product("Xiaomi", "Описание", 1000.0, 3)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    product.price = 500.0
    assert product.price == 500.0

# Проверка отклонения понижения цены (ответ "n")
def test_price_setter_lower_decline(monkeypatch):
    product = Product("Xiaomi", "Описание", 1000.0, 3)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    product.price = 500.0
    assert product.price == 1000.0

# Проверка класса new_product без дубликатов
def test_new_product():
    data = {
        "name": "MacBook",
        "description": "Pro 14\"",
        "price": 150000,
        "quantity": 2
    }
    new = Product.new_product(data)
    assert isinstance(new, Product)
    assert new.name == "MacBook"
    assert new.price == 150000
    assert new.quantity == 2

# Проверка объединения количества и цены при совпадении имени
def test_new_product_with_duplicates():
    existing = [Product("MacBook", "Pro 14\"", 100000, 1)]
    data = {
        "name": "MacBook",
        "description": "Pro 14\"",
        "price": 150000,
        "quantity": 2
    }
    new = Product.new_product(data, existing)
    assert new.name == "MacBook"
    assert new.price == 150000
    assert new.quantity == 3
