from typing import Optional
from dataclasses import dataclass

from PyQt5.QtSql import QSqlQuery

from utils.database import DataBaseConnection


@dataclass
class Building:
    building_id: Optional[str]
    building_address: str


class BuildingManager:
    @staticmethod
    def get_all_buildings():
        DataBaseConnection()
        query = QSqlQuery()

        query.prepare("""
            SELECT
                building.building_id,
                building.building_address
            FROM building
        """)

        query.exec()

        while query.next():
            yield Building(
                building_id=query.value(0),
                building_address=query.value(1)
            )

    @staticmethod
    def get_building_by_id(building_id: str) -> Building:
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""
            SELECT
                building.building_id,
                building.building_address
            FROM building
            WHERE building_id = :building_id
        """)

        query.bindValue(":building_id", building_id)

        query.exec()

        while query.next():
            return Building(
                building_id=query.value(0),
                building_address=query.value(1)
            )

    @staticmethod
    def add_new_building(building_address: str):
        DataBaseConnection()
        query = QSqlQuery()

        query.prepare("INSERT INTO building (building_address) VALUES (:building_address)")
        query.bindValue(":building_address", building_address)

        query.exec()

    @staticmethod
    def update_building(building: Building):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""
                UPDATE building
                SET 
                    building_address = :building_address
                WHERE building_id = :building_id
            """)

        query.bindValue(":building_id", building.building_id)
        query.bindValue(":building_address", building.building_address)

        query.exec()

    @staticmethod
    def delete_building_by_id(building_id: str):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("DELETE FROM building WHERE building_id = :building_id")
        query.bindValue(":building_id", building_id)

        query.exec()
