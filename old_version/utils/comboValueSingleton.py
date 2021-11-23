from PyQt5.QtSql import QSqlDatabase


class ComboValueSingleton:
    __value = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(ComboValueSingleton, cls).__new__(cls)
        return cls.instance

    def set_value(self, value):
        self.__value = value

    def get_value(self):
        return self.__value
