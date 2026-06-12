import pytest
import promotions
from products import Product, NonStockedProduct, LimitedProduct


def test_creating_prod():
    """Checks if creating a regular product sets everything correctly"""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active() is True


def test_creating_prod_invalid_details():
    """Verifies that invalid details throw an exception"""
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_prod_becomes_inactive():
    """Checks if reaching 0 stock deactivates the item"""
    p = Product("Pixel 7", price=600, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert p.is_active() is False


def test_buy_modifies_quantity():
    """Checks if buying returns the correct cost and lowers stock"""
    p = Product("iPhone 15", price=1000, quantity=10)
    total_cost = p.buy(3)
    assert p.quantity == 7
    assert total_cost == 3000


def test_buy_too_much():
    """Verifies buying over available stock throws an exception"""
    p = Product("iPad Air", price=700, quantity=5)
    with pytest.raises(Exception):
        p.buy(6)


def test_limited_product_exceeds_maximum():
    """Checks limited product order rules"""
    p = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
    with pytest.raises(Exception):
        p.buy(2)


def test_percent_discount_promo():
    """Checks percentage discount calculation"""
    p = Product("Test Laptop", price=1000, quantity=10)
    thirty_off = promotions.PercentDiscount("30% off!", percent=30)
    p.promotion = thirty_off
    assert p.buy(1) == 700


def test_second_half_price_promo():
    """Checks second item half price calculation"""
    p = Product("Test Phone", price=100, quantity=10)
    half_price = promotions.SecondHalfPrice("Second Half price!")
    p.promotion = half_price
    assert p.buy(2) == 150


def test_third_one_free_promo():
    """Checks buy 2 get 1 free calculation"""
    p = Product("Test Earbuds", price=50, quantity=10)
    three_for_two = promotions.ThirdOneFree("Third One Free!")
    p.promotion = three_for_two
    assert p.buy(3) == 100