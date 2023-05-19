import pytest
from src import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint_returns_200(client):
    # Assign
    expected = 200

    # Act
    actual = client.get("/health").status_code

    # Assert
    assert actual == expected


def test_health_endpoint_returns_healthy(client):
    # Assign
    expected = b"healthy!"

    # Act
    actual = client.get("/health").data

    # Assert
    assert actual == expected
