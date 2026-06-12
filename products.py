class Product:
    def __init__(self, name, price, quantity):
        # Basic validation
        if name == "" or price < 0 or quantity < 0:
            raise Exception("Invalid details for product")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        # Auto-deactivate if stock hits zero
        if self.quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        return self.name + ", Price: " + str(self.price) + ", Quantity: " + str(self.quantity)

    def buy(self, quantity):
        if quantity > self.quantity:
            raise Exception("Not enough items in stock!")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.active = False

        return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        pass

    def buy(self, quantity):
        return self.price * quantity

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise Exception(f"Cannot buy more than {self.maximum} items of this product at once!")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"
