from src.measurement.data.repo import MeasurementRepo


def test_retrieve_by_country_returns_one_entity_successful():
    # Assign
    repo = MeasurementRepo()
    expected = 1

    # Act
    actual = len(repo.retrieve_by_country("NO"))

    # Assert
    assert actual == expected
