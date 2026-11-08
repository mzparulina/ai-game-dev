
def decide_shopkeeper(
    energy: int,
    inventory: int,
    customers: int
) -> str:
    """Choose an action based on the shopkeeper's state."""

    if energy < 40:
        return "Resting to recover energy"

    elif inventory < 3:
        return "Restocking inventory"

    elif customers == 0:
        return "Waiting for customers"

    else:
        return "Selling items to customers"
