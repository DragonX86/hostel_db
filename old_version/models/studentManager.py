from dataclasses import dataclass

from PyQt5.QtSql import QSqlQuery

from utils.dbConnection import DbConnection


@dataclass
class Student:
    surname: str
    first_name: str
    middle_name: str
    gender: str
    birthdate: str
    group_name: str


class StudentManager:
    @staticmethod
    def all_students():
        DbConnection()
        query = QSqlQuery()

        query.prepare("""
        SELECT
            student.student_id,
            student.surname,
            student.first_name,
            student.middle_name,
            student.gender,
            student.birthdate,
            groups.groups_name
        FROM student
            JOIN groups
            ON student.groups_id = groups.groups_id
        """)

        query.exec()

        while query.next():
            yield Student(
                surname=query.value(0),
                first_name=query.value(1),
                middle_name=query.value(2),
                gender=query.value(3),
                birthdate=query.value(4),
                group_name=query.value(5)
            )
