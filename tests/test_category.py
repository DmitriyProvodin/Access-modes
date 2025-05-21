from src.product import Product
from src.category import Category

def test_add_product_and_display():
    p = Product("Test", "Test", 100.0, 10)
    c = Category("TestCat", "Desc", [])
    c.add_product(p)
    result = c.products
    assert "Test, 100.0 руб. Остаток: 10 шт." in result
