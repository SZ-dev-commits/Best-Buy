import pytest
from products import Product


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