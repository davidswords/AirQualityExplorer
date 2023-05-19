import json

import pytest
from src import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_retrieve_measurement_country_returns_200_successful(client):
    # Assign
    expected = 200

    # Act
    actual = client.get("/measurement/NO").status_code

    # Assert
    assert actual == expected


def test_retrieve_measurement_country_returns_measurements_successful(client):
    # Assign
    expected = 4

    # Act
    actual = len(json.loads(client.get("/measurement/NO").data))

    # Assert
    assert actual == expected
