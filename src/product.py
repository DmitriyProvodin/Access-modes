class Product:
    total_products = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_products += 1

    @classmethod
    def new_product(cls, data: dict, products: list = None):
        products = products or []
        name = data.get("name")
        description = data.get("description")
        price = data.get("price")
        quantity = data.get("quantity")

        for product in products:
            if product.name == name:
                product.quantity += quantity
                if price > product.price:
                    product.price = price
                return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirm.lower() == 'y':
                self.__price = new_price
        else:
            self.__price = new_price
