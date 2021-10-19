from dataclasses import dataclass
from typing import Optional

from PyQt5.QtSql import QSqlQuery

from utils.database import DataBaseConnection


@dataclass
class Faculty:
    faculty_id: Optional[str]
    faculty_name: str


class FacultyManager:
    @staticmethod
    def get_all_faculties():
        DataBaseConnection()
        query = QSqlQuery()

        query.prepare("""
                   SELECT
                       faculty.faculty_id,
                       faculty.faculty_name
                   FROM faculty
                   """)

        query.exec()

        while query.next():
            yield Faculty(
                faculty_id=query.value(0),
                faculty_name=query.value(1)
            )

    @staticmethod
    def get_faculty_by_id(faculty_id: str) -> Faculty:
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""SELECT
                            faculty.faculty_id,
                            faculty.faculty_name
                          FROM faculty
                          WHERE faculty_id = :faculty_id""")
        query.bindValue(":faculty_id", faculty_id)

        query.exec()

        while query.next():
            return Faculty(
                faculty_id=query.value(0),
                faculty_name=query.value(1)
            )

    @staticmethod
    def add_new_faculty(faculty_name: str):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("INSERT INTO faculty ('faculty_name') VALUES (:faculty_name)")
        query.bindValue(":faculty_name", faculty_name)

        query.exec()

    @staticmethod
    def update_faculty(faculty: Faculty):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""UPDATE faculty
                         SET faculty_name = :faculty_name
                         WHERE faculty_id = :faculty_id""")

        query.bindValue(":faculty_id", faculty.faculty_id)
        query.bindValue(":faculty_name", faculty.faculty_name)

        query.exec()

    @staticmethod
    def delete_faculty_by_id(faculty_id: str):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("DELETE FROM faculty WHERE faculty_id = :faculty_id")

        query.bindValue(":faculty_id", faculty_id)

        query.exec()
