import uuid
from datetime import datetime
from typing import List

from src.measurement.domain.entity import MeasurementEntity


class MeasurementService:
    @staticmethod
    def document_to_entity(document: dict) -> MeasurementEntity:
        id_ = str(uuid.uuid4()[:8])
        created_at = updated_at = datetime.utcnow()

        return MeasurementEntity(
            id_=id_,
            created_at=created_at,
            updated_at=updated_at,
            archived=False,
            recorded_at=document["recorded_at"],
            city=document["city"],
            country=document["country"],
            pollutant=document["pollutant"],
            value=document["value"],
        )

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
