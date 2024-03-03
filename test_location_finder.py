from fastapi.testclient import TestClient
from fastapi import status, HTTPException
from httpx import WSGITransport
from location_finder import app, Location, get_Location_or_404

locations = {
    "noor": Location(name="Noor", address="France"),
    "saif": Location(name="Saif", address="Italy"),
}

def fake_get_location_or_404(name: str)->Location:
    loc = locations.get(name.lower())
    if not loc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Location not found for {name}")
    return loc

# Comment out this line to stop overriding the dependency
# app.dependency_overrides[get_Location_or_404] = fake_get_location_or_404

client = TestClient(app)
# transport=WSGITransport(app=TestClient)

def test_read_location():
    response = client.get("/location/noor")
    assert response.status_code == 200
    assert response.json() == {"name": "Noor", "address": "France"}

def test_location_404():
    response = client.get("/location/john")
    assert response.status_code == status.HTTP_404_NOT_FOUND