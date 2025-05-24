from product import Product
from category import Category
from category_iterator import CategoryIterator

def test_product_str():
    product = Product("Ноутбук", "Мощный ноутбук", 80000, 5)
    assert str(product) == "Ноутбук, 80000 руб. Остаток: 5 шт."

def test_product_add():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 150, 3)
    assert p1 + p2 == 100 * 2 + 150 * 3

def test_category_str():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 150, 3)
    category = Category("Электроника", "Гаджеты", [p1, p2])
    assert str(category) == "Электроника, количество продуктов: 5 шт."

def test_category_iterator():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 150, 3)
    category = Category("Электроника", "Гаджеты", [p1, p2])
    iterator = CategoryIterator(category)
    items = [product for product in iterator]
    assert items == [p1, p2]
