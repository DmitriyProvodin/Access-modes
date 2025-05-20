from src.product import Product

class Category:
    def __init__(self, name: str):
        self.name = name
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Product.total_products += 1

    @property
    def products(self) -> str:
        return "".join([
            f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
            for p in self.__products
        ])
