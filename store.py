class Store:
    """Represents the store holding products"""
    def __init__(self, products=None):
        if products is None:
            products = []
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(p.quantity for p in self.products)

    def get_all_products(self):
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        total_price = 0.0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

    def __contains__(self, product):
        """Allows checking if a product exists using 'in'"""
        return product in self.products

    def __add__(self, other):
        """Allows combining two stores using '+'"""
        if not isinstance(other, Store):
            return NotImplemented
        return Store(self.products + other.products)