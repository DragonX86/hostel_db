from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem

from models.buildingManager import BuildingManager


class BuildingWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(BuildingWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/window/building.ui')[0]()
        self.ui.setupUi(self)

        self.fill_table()

    def fill_table(self):
        self.ui.tableWidget.setHorizontalHeaderLabels(["Адресс корпусов"])

        for building in BuildingManager.all_building():
            numRows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(numRows)

            value = QTableWidgetItem(building.building_address)

            self.ui.tableWidget.setItem(numRows, 0, value)
