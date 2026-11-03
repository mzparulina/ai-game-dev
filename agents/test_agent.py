
class ShopkeeperAgent:
    def __init__(self):
        self.energy = 80
        self.inventory = 10
        self.gold = 0

    def decide(self):
        if self.energy < 30:
            return "Resting to recover energy"

        if self.inventory < 3:
            return "Restocking inventory"

        return "Selling items to customers"


agent = ShopkeeperAgent()

print("=== AI SHOPKEEPER ===")
print("Energy:", agent.energy)
print("Inventory:", agent.inventory)
print("Decision:", agent.decide())

agent.energy = 20
print("Decision when tired:", agent.decide())
