import pytest
from products import Product
import promotions


def test_creating_prod():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active() is True


def test_creating_prod_invalid_details():
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    p = Product("Pixel 7", price=600, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert p.is_active() is False


def test_buy_modifies_quantity():
    p = Product("iPhone 15", price=1000, quantity=10)
    total_cost = p.buy(3)
    assert p.quantity == 7
    assert total_cost == 3000


def test_buy_too_much():
    p = Product("iPad Air", price=700, quantity=5)
    with pytest.raises(Exception):
        p.buy(6)


def test_percent_discount_promo():
    """Checks if percentage discount calculates correctly"""
    p = Product("Test Laptop", price=1000, quantity=10)
    thirty_off = promotions.PercentDiscount("30% off!", percent=30)
    p.set_promotion(thirty_off)

    # 1000 * 1 * 0.7 = 700
    assert p.buy(1) == 700


def test_second_half_price_promo():
    """Checks if every second item gets 50% off"""
    p = Product("Test Phone", price=100, quantity=10)
    half_price = promotions.SecondHalfPrice("Second Half price!")
    p.set_promotion(half_price)

    # Buying 2: 100 + 50 = 150
    assert p.buy(2) == 150


def test_third_one_free_promo():
    """Checks buy 2 get 1 free logic"""
    p = Product("Test Earbuds", price=50, quantity=10)
    three_for_two = promotions.ThirdOneFree("Third One Free!")
    p.set_promotion(three_for_two)

    # Buying 3: only pay for 2 -> 50 * 2 = 100
    assert p.buy(3) == 100