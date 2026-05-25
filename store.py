class Store:
    def __init__(self, product_list):
        self.products = product_list

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def get_total_quantity(self):
        total = 0
        for p in self.products:
            total += p.get_quantity()
        return total

    def get_all_products(self):
        # Only return products that are still active
        active_list = []
        for p in self.products:
            if p.is_active():
                active_list.append(p)
        return active_list

    def order(self, shopping_list):
        total_bill = 0
        for item in shopping_list:
            prod = item[0]
            amount = item[1]
            total_bill += prod.buy(amount)
        return total_bill
