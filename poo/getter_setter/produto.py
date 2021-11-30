class Product:
    def __init__(self, product: str, price: float) -> None:
        self.product = product
        self.price = price

    def discount(self, percent: float) -> float:
        self.price = self.price - (self.price * (percent / 100))
        return self.price

    # getter: product
    @property
    def product(self) -> str:
        return self._product

    # setter: product
    @product.setter
    def product(self, name: str):
        # product: str
        if isinstance(name, str):
            # product: capitalize
            self._product = name.capitalize()

    # getter: price
    @property
    def price(self) -> float:
        return self._price

    # setter: price
    @price.setter
    def price(self, value: float):
        # verifica a entrada de dados
        if isinstance(value, float):
            self._price = value
        # se o valor for um inteiro faz o casting pra float
        elif isinstance(value, int):
            self._price = float(value)


if __name__ == '__main__':
    dell = Product('INTEL CORE I5: DELL', 5000)
    print(dell.price, dell.product)

    acer = Product('INTEL CORE I5: ACER', 5001.0)
    print(acer.price, acer.product)
