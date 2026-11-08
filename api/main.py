
from fastapi import FastAPI
from pydantic import BaseModel
from ai.decision import decide_shopkeeper


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
    decision = decide_shopkeeper(
    energy=state.energy,
    inventory=state.inventory,
    customers=state.customers
)



    return {"decision": decision}
