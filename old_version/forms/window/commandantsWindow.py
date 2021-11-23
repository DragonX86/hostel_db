from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from models.commandantManager import CommandantManager


class CommandantsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CommandantsWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/window/commandants.ui')[0]()
        self.ui.setupUi(self)

        self.fill_table()

    def fill_table(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "Фамилия",
                "Имя",
                "Отчество",
                "Адресс корпуса"
            ]
        )

        self.ui.tableWidget.horizontalHeader()\
            .setSectionResizeMode(QHeaderView.Stretch)

        for commandant in CommandantManager.all_commandant():
            numRows = self.ui.tableWidget.rowCount()

            self.ui.tableWidget.insertRow(numRows)

            self.ui.tableWidget.setItem(numRows, 0, QTableWidgetItem(commandant.surname))
            self.ui.tableWidget.setItem(numRows, 1, QTableWidgetItem(commandant.first_name))
            self.ui.tableWidget.setItem(numRows, 2, QTableWidgetItem(commandant.middle_name))
            self.ui.tableWidget.setItem(numRows, 3, QTableWidgetItem(commandant.building_address))
