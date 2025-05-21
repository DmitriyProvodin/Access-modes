class Product:
    count = 0

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.count += 1

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirm = input("Вы уверены, что хотите понизить цену? (y/n): ")
            if confirm.lower() != 'y':
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, data: dict, existing_products: list | None = None):
        if existing_products is None:
            return cls(data["name"], data["description"], data["price"], data["quantity"])

        for product in existing_products:
            if product.name == data["name"]:
                product.quantity += data["quantity"]
                if data["price"] > product.price:
                    product.price = data["price"]
                return product

        return cls(data["name"], data["description"], data["price"], data["quantity"])
