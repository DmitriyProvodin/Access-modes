import pytest
from src.category import Category
from src.product import Product

@pytest.fixture
def sample_products():
    return [
        Product("Product A", "Description A", 1000, 5),
        Product("Product B", "Description B", 2000, 10),
    ]

@pytest.fixture
def category(sample_products):
    return Category("Test Category", "Test description", sample_products)

def test_add_product(category):
    new_product = Product("Product C", "Description C", 1500, 7)
    category.add_product(new_product)
    assert "Product C" in category.products

def test_add_invalid_product_raises_error(category):
    with pytest.raises(TypeError):
        category.add_product("Not a Product")

def test_products_property_format(category):
    output = category.products
    assert "Product A, 1000 руб. Остаток: 5 шт." in output
    assert "Product B, 2000 руб. Остаток: 10 шт." in output

def test_product_count_increments(category):
    initial_count = Category.product_count
    category.add_product(Product("Product D", "Description D", 3000, 3))
    assert Category.product_count == initial_count + 1
