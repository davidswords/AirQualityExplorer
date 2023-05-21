from unittest.mock import patch
from src.measurement.domain.service import MeasurementService
from src.measurement.domain.entity import MeasurementEntity
from datetime import datetime


@patch("src.measurement.data.repo.MeasurementRepo.upsert")
def test_upsert_calls_repo_upsert_once(mock_upsert):
    document = {
        "recorded_at": datetime.utcnow(),
        "city": "Oslo",
        "country": "NO",
        "latitude": 59.9139,
        "longitude": 10.7522,
        "pollutant": "PM2.5",
        "value": 2.5,
    }

    # Assign
    service = MeasurementService()

    # Act
    service.upsert(document)

    # Assert
    mock_upsert.assert_called_once()


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_pollutant")
def test_retrieve_by_pollutant_returns_one_entity_successful(
    mock_retrieve_by_pollutant,
):
    # Mock
    mock_retrieve_by_pollutant.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1

    # Act
    actual = len(service.retrieve_by_pollutant("PM2.5"))

    # Assert
    assert actual == expected


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_country")
def test_retrieve_by_country_returns_one_entity_successful(mock_retrieve_by_country):
    mock_retrieve_by_country.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Trondheim",
            country="NO",
            latitude=63.4468,
            longitude=10.4219,
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1
    pollutant = "PM2.5"

    # Act
    actual = len(service.retrieve_by_country(pollutant, "NO"))

    # Assert
    assert actual == expected


@patch("src.measurement.data.repo.MeasurementRepo.retrieve_by_city")
def test_retrieve_by_city_returns_one_entity_successful(mock_retrieve_by_city):
    mock_retrieve_by_city.return_value = [
        MeasurementEntity(
            id_="216bb524",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow(),
            archived=False,
            recorded_at=datetime.utcnow(),
            city="Oslo",
            country="NO",
            latitude=59.9139,
            longitude=10.7522,
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1
    pollutant = "PM2.5"

    # Act
    actual = len(service.retrieve_by_city(pollutant, "NO", "Oslo"))

    # Assert
    assert actual == expected
