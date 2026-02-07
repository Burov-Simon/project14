class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        return (self.price * self.quantity) + (other.price * other.quantity)

    @classmethod
    def new_product(cls, prodict):
        return cls(
            prodict["name"],
            prodict["description"],
            prodict["price"],
            prodict["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        q_prod = 0
        for product in self.__products:
            q_prod += product.quantity
        return f'{self.name}, количество продуктов: {q_prod} шт.'


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        return [
            f"{p.name}: {p.price} руб. Остаток: {p.quantity} шт."
            for p in self.__products
        ]
