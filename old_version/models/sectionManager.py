from dataclasses import dataclass

from PyQt5.QtSql import QSqlQuery

from utils.dbConnection import DbConnection


@dataclass
class Section:
    section_number: int
    free_rooms: int
    building_address: str


class SectionManager:
    @staticmethod
    def all_section():
        DbConnection()
        query = QSqlQuery()

        query.prepare("""
        SELECT
            section.section_number,
            section.free_rooms,
            building.building_address
        FROM section
            JOIN building
            ON section.building_id = building.building_id        
        """)

        query.exec()

        while query.next():
            yield Section(
                section_number=query.value(0),
                free_rooms=query.value(1),
                building_address=query.value(2)
            )
