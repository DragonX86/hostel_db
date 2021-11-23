from dataclasses import dataclass

from PyQt5.QtSql import QSqlQuery

from utils.dbConnection import DbConnection


@dataclass
class Commandant:
    surname: str
    first_name: str
    middle_name: str
    building_address: str


class CommandantManager:
    @staticmethod
    def all_commandant():
        DbConnection()
        query = QSqlQuery()

        query.prepare("""
        SELECT
            commandant.surname,
            commandant.first_name,
            commandant.middle_name,
            building.building_address
        FROM commandant
            JOIN building
            ON commandant.building_id = building.building_id
        """)

        query.exec()

        while query.next():
            yield Commandant(
                surname=query.value(0),
                first_name=query.value(1),
                middle_name=query.value(2),
                building_address=query.value(3)
            )
