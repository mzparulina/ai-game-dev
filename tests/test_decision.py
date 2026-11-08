
from ai.decision import decide_shopkeeper


def test_rest():
    result = decide_shopkeeper(20, 10, 5)
    assert result == "Resting to recover energy"


def test_restock():
    result = decide_shopkeeper(80, 1, 5)
    assert result == "Restocking inventory"


def test_idle():
    result = decide_shopkeeper(80, 10, 0)
    assert result == "Waiting for customers"


def test_sell():
    result = decide_shopkeeper(80, 10, 5)
    assert result == "Selling items to customers"
