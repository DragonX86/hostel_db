from dataclasses import dataclass
from typing import Optional

from PyQt5.QtSql import QSqlQuery

from utils.database import DataBaseConnection


@dataclass
class Group:
    group_id: Optional[str]
    group_name: str
    faculty_name: str


class GroupManager:
    @staticmethod
    def get_all_groups():
        DataBaseConnection()
        query = QSqlQuery()

        query.prepare("""
                SELECT 
                    groups.groups_id,
                    groups.groups_name,
                    faculty.faculty_name
                FROM groups
                    JOIN faculty 
                    ON groups.faculty_id = faculty.faculty_id
                """)

        query.exec()

        while query.next():
            yield Group(
                group_id=query.value(0),
                group_name=query.value(1),
                faculty_name=query.value(2)
            )

    @staticmethod
    def get_group_by_id(group_id: str) -> Group:
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""
               SELECT
                   groups.groups_id,
                   groups.groups_name,
                   faculty.faculty_name
               FROM groups
                   JOIN faculty
                   ON groups.faculty_id = faculty.faculty_id
               WHERE groups_id = :groups_id
           """)

        query.bindValue(":groups_id", group_id)

        query.exec()

        while query.next():
            return Group(
                group_id=query.value(0),
                group_name=query.value(1),
                faculty_name=query.value(2)
            )

    @staticmethod
    def add_new_group(group: Group):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""
                INSERT INTO groups (groups_name, faculty_id)
                VALUES (:groups_name, 
                    (SELECT faculty_id FROM faculty WHERE faculty_name = :faculty_name)
                )
                """)

        query.bindValue(":groups_name", group.group_name)
        query.bindValue(":faculty_name", group.faculty_name)

        query.exec()

    @staticmethod
    def update_group(group: Group):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("""
                UPDATE groups
                SET 
                    groups_name = :groups_name,
                    faculty_id = (SELECT faculty_id FROM faculty WHERE faculty_name = :faculty_name)
                WHERE groups_id = :groups_id
            """)

        query.bindValue(":groups_id", group.group_id)
        query.bindValue(":groups_name", group.group_name)
        query.bindValue(":faculty_name", group.faculty_name)

        query.exec()

    @staticmethod
    def delete_group_by_id(group_id: str):
        DataBaseConnection()

        query = QSqlQuery()

        query.prepare("DELETE FROM groups WHERE groups_id = :groups_id")

        query.bindValue(":groups_id", group_id)

        query.exec()
