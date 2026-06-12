class Product:
    """Represents a standard store product"""

    def __init__(self, name, price, quantity):
        if name == "" or price < 0 or quantity < 0:
            raise Exception("Invalid details for product")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Step 3 property

    def get_promotion(self):
        """Gets current promotion"""
        return self.promotion

    def set_promotion(self, promotion):
        """Sets new promotion"""
        self.promotion = promotion

    def remove_promotion(self):
        """Removes promotion"""
        self.promotion = None

    def is_active(self):
        return self.active

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")

        # Use promo price if active
        if self.promotion:
            cost = self.promotion.apply_promotion(self, quantity)
        else:
            cost = self.price * quantity

        self.quantity -= quantity
        if self.quantity == 0:
            self.active = False
        return cost

    def show(self):
        res = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"
        if self.promotion:
            res += f", Promotion: {self.promotion.name}"
        return res


class NonStockedProduct(Product):
    """Digital item with no stock tracking"""

    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def buy(self, quantity):
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self):
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
            raise Exception("Not enough items in stock!")
        return super().buy(quantity)

    def show(self):
        res = f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
        if self.promotion:
            res += f", Promotion: {self.promotion.name}"
        return res