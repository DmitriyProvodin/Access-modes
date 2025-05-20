class Product:
    total_products = 0

    def __init__(self, name: str, price: float, quantity: int, description: str = ""):
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.description = description
        Product.total_products += 1

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            answer = input("Вы действительно хотите понизить цену? (y/n): ")
            if answer.lower() == "y":
                self.__price = new_price
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, data: dict, existing_products: list = None) -> "Product":
        name = data.get("name")
        price = data.get("price")
        quantity = data.get("quantity")
        description = data.get("description", "")

        if existing_products:
            for product in existing_products:
                if product.name == name:
                    product.quantity += quantity
                    if price > product.price:
                        product.price = price
                    return product

        return cls(name, price, quantity, description)
