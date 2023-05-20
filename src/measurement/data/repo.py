from typing import List

from src.measurement.domain.entity import MeasurementEntity
from src.measurement.data.dao import MeasurementDAO


class MeasurementRepo:
    @staticmethod
    def _to_entity(dao: MeasurementDAO) -> MeasurementEntity:
        return MeasurementEntity(
            id_=dao.id_,
            created_at=dao.created_at,
            updated_at=dao.updated_at,
            archived=dao.archived,
            recorded_at=dao.recorded_at,
            city=dao.city,
            country=dao.country,
            pollutant=dao.pollutant,
            value=dao.value,
        )

    def retrieve_by_country(self, country: str) -> List[MeasurementEntity]:
        daos = MeasurementDAO.query.filter(
            MeasurementDAO.country == country and
            MeasurementDAO.archived is False
        ).all()

        return [self._to_entity(dao) for dao in daos]
