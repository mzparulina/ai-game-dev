
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Fantasy RPG")


class ShopkeeperState(BaseModel):
    energy: int = 80
    inventory: int = 10
    gold: int = 0
    customers: int = 0


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/npc/decide")
def decide(state: ShopkeeperState):
    if state.energy < 40:
        decision = "Resting to recover energy"
    elif state.inventory < 3:
        decision = "Restocking inventory"
    elif state.customers == 0:
        decision = "Waiting for customers"
    else:
        decision = "Selling items to customers"


    return {
        "npc": "Shopkeeper",
        "decision": decision,
        "energy": state.energy,
        "inventory": state.inventory,
        "gold": state.gold
    }
