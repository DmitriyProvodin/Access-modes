import pytest
from src.product import Product

def test_product_init():
    p = Product("Мышь", 500, 10)
    assert p.name == "Мышь"
    assert p.price == 500
    assert p.quantity == 10

def test_price_setter_positive():
    p = Product("Клавиатура", 1000, 5)
    p.price = 1200
    assert p.price == 1200

def test_price_setter_zero_or_negative(capsys):
    p = Product("Монитор", 15000, 2)
    p.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert p.price == 15000

def test_price_lower_confirm_yes(monkeypatch):
    p = Product("Принтер", 8000, 1)
    monkeypatch.setattr("builtins.input", lambda _: "y")
    p.price = 6000
    assert p.price == 6000

def test_price_lower_confirm_no(monkeypatch, capsys):
    p = Product("Сканер", 5000, 1)
    monkeypatch.setattr("builtins.input", lambda _: "n")
    p.price = 4000
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert p.price == 5000

def test_new_product_creation():
    data = {"name": "Микрофон", "price": 3000, "quantity": 3, "description": "Студийный"}
    p = Product.new_product(data)
    assert isinstance(p, Product)
    assert p.name == "Микрофон"
    assert p.price == 3000
    assert p.quantity == 3

def test_new_product_merging():
    existing = [Product("Камера", 10000, 2)]
    data = {"name": "Камера", "price": 12000, "quantity": 3}
    updated = Product.new_product(data, existing)
    assert updated.quantity == 5
    assert updated.price == 12000
