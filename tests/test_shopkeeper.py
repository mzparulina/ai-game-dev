
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_shopkeeper_rest():
    response = client.post(
        "/npc/decide",
        json={"energy": 20, "inventory": 10, "gold": 0}
    )
    assert response.status_code == 200
    assert response.json()["decision"] == (
        "Resting to recover energy"
    )


def test_shopkeeper_restock():
    response = client.post(
        "/npc/decide",
        json={"energy": 80, "inventory": 2, "gold": 0}
    )
    assert response.json()["decision"] == (
        "Restocking inventory"
    )


def test_shopkeeper_sell():
    response = client.post(
        "/npc/decide",
        json={"energy": 80, "inventory": 10, "gold": 0}
    )
    assert response.json()["decision"] == (
        "Selling items to customers"
    )
