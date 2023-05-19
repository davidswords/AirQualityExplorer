from datetime import datetime


class MeasurementEntity:
    def __init__(
        self,
        id_: str,
        created_at: datetime,
        updated_at: datetime,
        archived: bool,
        recorded_at: datetime,
        city: str,
        country: str,
        pollutant: str,
        value: float,
    ):
        self.id_ = id_
        self.created_at = created_at
        self.updated_at = updated_at
        self.archived = archived
        self.recorded_at = recorded_at
        self.city = city
        self.country = country
        self.pollutant = pollutant
        self.value = value

    def __str__(self):
        return (
            f"{self.id_}\n"
            f"{self.created_at}\n"
            f"{self.updated_at}\n"
            f"{self.archived}\n"
            f"{self.recorded_at}\n"
            f"{self.city}\n"
            f"{self.country}\n"
            f"{self.pollutant}\n"
            f"{self.value}\n"
        )
