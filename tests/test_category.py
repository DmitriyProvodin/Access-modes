from src.category import Category
from src.product import Product

def test_add_product_increases_counter():
    cat = Category("Электроника")
    start_count = Product.total_products
    product = Product("Камера", 10000, 2)
    cat.add_product(product)
    assert Product.total_products == start_count + 1

def test_products_property_output():
    cat = Category("Гаджеты")
    p1 = Product("Планшет", 20000, 4)
    p2 = Product("Часы", 15000, 3)
    cat.add_product(p1)
    cat.add_product(p2)
    result = cat.products
    assert "Планшет, 20000 руб. Остаток: 4 шт." in result
    assert "Часы, 15000 руб. Остаток: 3 шт." in result
