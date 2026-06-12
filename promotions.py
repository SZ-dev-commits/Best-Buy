from abc import ABC, abstractmethod

class Promotion(ABC):
    """Base class for all promotions"""
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """Calculates price after discount"""
        pass


class PercentDiscount(Promotion):
    """Applies percentage off the total price"""
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity):
        total = product.price * quantity
        return total * (1 - self.percent / 100)


class SecondHalfPrice(Promotion):
    """Every second item gets a 50% discount"""
    def apply_promotion(self, product, quantity):
        pairs = quantity // 2
        leftovers = quantity % 2
        pair_price = product.price * 1.5
        return (pairs * pair_price) + (leftovers * product.price)


class ThirdOneFree(Promotion):
    """Buy 2 get 1 free promotion"""
    def apply_promotion(self, product, quantity):
        payable_items = quantity - (quantity // 3)
        return payable_items * product.price