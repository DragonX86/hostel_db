from PyQt5 import QtWidgets, uic
from PyQt5.QtSql import QSqlQuery
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from utils.dbConnection import DbConnection


class LodgersWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(LodgersWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/lodgers_window.ui')[0]()
        self.ui.setupUi(self)

        self.ui.tableWidget.setHorizontalHeaderLabels(["ФИО студента", "Дата заселения"])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        self.ui.close_button.clicked.connect(self.close)

        self.fill_table()

    def fill_table(self):
        DbConnection()

        query = QSqlQuery()

        if query.exec("""
            SELECT 
	            students.full_name,
                lodgers.check_in_date
            FROM lodgers 
	            INNER JOIN students 
	            ON lodgers.students_id = students.students_id"""):
            while query.next():
                numRows = self.ui.tableWidget.rowCount()

                self.ui.tableWidget.insertRow(numRows)
                self.ui.tableWidget.setItem(numRows, 0, QTableWidgetItem(str(query.value(0))))
                self.ui.tableWidget.setItem(numRows, 1, QTableWidgetItem(str(query.value(1))))

