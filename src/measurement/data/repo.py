from datetime import datetime
from typing import List

from src.measurement.domain.entity import MeasurementEntity


class MeasurementRepo:
    @staticmethod
    def retrieve_by_country(country: str) -> List[MeasurementEntity]:
        return [
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
            ),
        ]
