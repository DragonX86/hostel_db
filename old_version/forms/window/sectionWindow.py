from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from models.sectionManager import SectionManager


class SectionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SectionWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/window/section.ui')[0]()
        self.ui.setupUi(self)

        self.fill_table()

    def fill_table(self):
        self.ui.section_table.setHorizontalHeaderLabels(
            [
                "Номер секции",
                "Число комнат на секцию",
                "Адресс корпуса"
            ]
        )
        self.ui.section_table.horizontalHeader()\
            .setSectionResizeMode(QHeaderView.Stretch)

        for section in SectionManager.all_section():
            section_number = QTableWidgetItem(str(section.section_number))
            free_rooms = QTableWidgetItem(str(section.free_rooms))
            building_address = QTableWidgetItem(section.building_address)

            numRows = self.ui.section_table.rowCount()
            self.ui.section_table.insertRow(numRows)
            self.ui.section_table.setItem(numRows, 0, section_number)
            self.ui.section_table.setItem(numRows, 1, free_rooms)
            self.ui.section_table.setItem(numRows, 2, building_address)
