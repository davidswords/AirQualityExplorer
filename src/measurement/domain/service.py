import uuid
from datetime import datetime
from typing import List

from src.measurement.data.repo import MeasurementRepo
from src.measurement.domain.entity import MeasurementEntity


class MeasurementService:
    def __init__(self, repo: MeasurementRepo = None):
        self.repo = repo or MeasurementRepo()

    @staticmethod
    def document_to_entity(document: dict) -> MeasurementEntity:
        id_ = str(uuid.uuid4())[:8]
        created_at = updated_at = datetime.utcnow()

        return MeasurementEntity(
            id_=id_,
            created_at=created_at,
            updated_at=updated_at,
            archived=False,
            recorded_at=document["recorded_at"],
            city=document["city"],
            country=document["country"],
            latitude=document["latitude"],
            longitude=document["longitude"],
            pollutant=document["pollutant"],
            value=document["value"],
        )

    def upsert(self, document: dict) -> None:
        entity = self.document_to_entity(document=document)
        self.repo.upsert(entity=entity)

    def retrieve_by_pollutant(self, pollutant: str) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_pollutant(pollutant=pollutant)

    def retrieve_by_country(
        self, pollutant: str, country: str
    ) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_country(pollutant=pollutant, country=country)

    def retrieve_by_city(
        self, pollutant: str, country: str, city: str
    ) -> List[MeasurementEntity]:
        return self.repo.retrieve_by_city(
            pollutant=pollutant, country=country, city=city
        )
