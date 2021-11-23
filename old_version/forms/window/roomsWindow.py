from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView

from utils.comboValueSingleton import ComboValueSingleton
from models.roomManager import RoomManager


class RoomsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(RoomsWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/window/rooms.ui')[0]()
        self.ui.setupUi(self)

        self.fill_table()

    def fill_table(self):
        combo_value = ComboValueSingleton().get_value()

        self.ui.rooms_table.setHorizontalHeaderLabels(
            [
                "Номер комнаты",
                "Общее число мест",
                "Свободных мест"
            ]
        )
        self.ui.rooms_table.horizontalHeader()\
            .setSectionResizeMode(QHeaderView.Stretch)

        for room in RoomManager.all_rooms(combo_value):
            numRows = self.ui.rooms_table.rowCount()

            self.ui.rooms_table.insertRow(numRows)
            self.ui.rooms_table.setItem(numRows, 0, QTableWidgetItem(str(room.total_number)))
            self.ui.rooms_table.setItem(numRows, 1, QTableWidgetItem(str(room.total_beds)))
            self.ui.rooms_table.setItem(numRows, 2, QTableWidgetItem(str(room.free_of_beds)))
