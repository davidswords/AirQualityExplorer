from src.measurement.domain.service import MeasurementService


def test_retrieve_by_country_returns_one_entity_successful():
    # Assign
    service = MeasurementService()
    expected = 1

    # Act
    actual = len(service.retrieve_by_country('NO'))

    # Assert
    assert actual == expected
