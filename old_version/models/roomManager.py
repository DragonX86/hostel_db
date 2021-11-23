from dataclasses import dataclass

from PyQt5.QtSql import QSqlQuery

from utils.dbConnection import DbConnection


@dataclass
class Room:
    room_number: int
    section_number: int
    total_number: int
    total_beds: int
    free_of_beds: int


class RoomManager:
    @staticmethod
    def all_rooms(section_number: int):
        DbConnection()
        query = QSqlQuery()

        query.prepare("""
            SELECT 
                room.room_number,
                section.section_number, 
                room.total_beds, 
                room.free_of_beds 
            FROM room
                JOIN section 
                ON room.section_id = section.section_id  
            WHERE section.section_number = :section_number
            ORDER BY room.room_number
        """)

        query.bindValue(":section_number", section_number)
        query.exec()

        while query.next():
            yield Room(
                room_number=query.value(0),
                section_number=query.value(1),
                total_number=query.value(0) + query.value(1),
                total_beds=query.value(2),
                free_of_beds=query.value(3)
            )
