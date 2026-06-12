class Product:
    """Represents a standard store product with properties and magic methods"""

    def __init__(self, name, price, quantity):
        if name == "":
            raise Exception("Product name cannot be empty")
        self._name = name
        self.price = price  # Uses setter validation
        self.quantity = quantity  # Uses setter validation
        self._active = True
        self._promotion = None

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("Price cannot be negative")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise Exception("Quantity cannot be negative")
        self._quantity = value
        if self._quantity == 0:
            self._active = False

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, value):
        self._promotion = value

    def is_active(self):
        return self._active

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")

        if self.promotion:
            cost = self.promotion.apply_promotion(self, quantity)
        else:
            cost = self.price * quantity

        self.quantity -= quantity
        return cost

    def __str__(self):
        """Replaces show() to allow direct printing"""
        res = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            res += f", Promotion: {self.promotion.name}"
        return res

    def __gt__(self, other):
        """Allows > comparison based on price"""
        return self.price > other.price

    def __lt__(self, other):
        """Allows < comparison based on price"""
        return self.price < other.price


class NonStockedProduct(Product):
    """Digital item with no stock tracking"""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    @Product.quantity.setter
    def quantity(self, value):
        """Keeps quantity at 0 for non-stocked products"""
        self._quantity = 0

    def buy(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __str__(self):
        res = f"{self.name}, Price: {self.price}, Quantity: Unlimited"
        if self.promotion:
            res += f", Promotion: {self.promotion.name}"
        return res


class LimitedProduct(Product):
    """Product with a maximum purchase limit"""

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception("Order quantity exceeds maximum limit!")
        return super().buy(quantity)

    def __str__(self):
        res = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
        if self.promotion:
            res += f", Promotion: {self.promotion.name}"
        return res