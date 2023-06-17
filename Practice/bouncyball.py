class BouncyBall:

    def __init__(self, price, size, brand):
        self._price = price
        self._size = size
        self._brand = brand

    @property
    def price(self):
        return self._price

    @property
    def size(self):
        return self._size

    @property
    def brand(self):
        return self._brand

    @price.setter
    def price(self, new_price):
        self._price = new_price

    @size.setter
    def size(self, new_size):
        self._size = new_size

    @brand.setter
    def brand(self, new_brand):
        self._brand = new_brand

