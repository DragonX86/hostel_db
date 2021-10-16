from PyQt5.QtSql import QSqlDatabase


class DataBaseConnection:
    __sdb = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataBaseConnection, cls).__new__(cls)
            __sdb = QSqlDatabase.addDatabase('QSQLITE')
            __sdb.setDatabaseName("./main.db")
            __sdb.open()
        return cls.instance
