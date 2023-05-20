from unittest.mock import patch
from src.measurement.domain.service import MeasurementService
from src.measurement.domain.entity import MeasurementEntity
from datetime import datetime


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
            pollutant="PM2.5",
            value=2.5,
        )
    ]

    # Assign
    service = MeasurementService()
    expected = 1

    # Act
    actual = len(service.retrieve_by_country("NO"))

    # Assert
    assert actual == expected
