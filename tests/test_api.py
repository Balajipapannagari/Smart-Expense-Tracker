import os
import sys
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import storage
from src.main import app


@pytest.fixture(autouse=True)
def clean_data_file(tmp_path, monkeypatch):
    # Point storage at a fresh temp file for every test so tests don't clash
    test_file = tmp_path / "expenses.json"
    monkeypatch.setattr(storage, "DATA_FILE", test_file)
    yield


client = TestClient(app)


def test_add_expense():
    response = client.post("/expenses", json={
        "title": "Groceries",
        "amount": 45.50,
        "category": "Food",
        "date": "2026-07-01"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Groceries"
    assert "id" in data


def test_list_expenses_empty():
    response = client.get("/expenses")
    assert response.status_code == 200
    assert response.json() == []


def test_list_and_filter_by_category():
    client.post("/expenses", json={"title": "Bus ticket", "amount": 2.5, "category": "Transport", "date": "2026-07-02"})
    client.post("/expenses", json={"title": "Coffee", "amount": 3.0, "category": "Food", "date": "2026-07-02"})

    response = client.get("/expenses?category=Food")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "Food"


def test_total_overall_and_by_category():
    client.post("/expenses", json={"title": "Rent", "amount": 500, "category": "Housing", "date": "2026-07-01"})
    client.post("/expenses", json={"title": "Pizza", "amount": 20, "category": "Food", "date": "2026-07-02"})

    response = client.get("/expenses/total")
    assert response.status_code == 200
    data = response.json()
    assert data["overall_total"] == 520
    assert data["by_category"]["Housing"] == 500
    assert data["by_category"]["Food"] == 20


def test_total_for_specific_category():
    client.post("/expenses", json={"title": "Rent", "amount": 500, "category": "Housing", "date": "2026-07-01"})

    response = client.get("/expenses/total?category=Housing")
    assert response.status_code == 200
    assert response.json() == {"category": "Housing", "total": 500}


def test_delete_expense():
    add_response = client.post("/expenses", json={"title": "Movie", "amount": 12, "category": "Entertainment", "date": "2026-07-03"})
    expense_id = add_response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 204

    list_response = client.get("/expenses")
    assert list_response.json() == []


def test_delete_nonexistent_expense():
    response = client.delete("/expenses/does-not-exist")
    assert response.status_code == 404


def test_invalid_amount_rejected():
    response = client.post("/expenses", json={"title": "Bad", "amount": -5, "category": "Food", "date": "2026-07-01"})
    assert response.status_code == 422
