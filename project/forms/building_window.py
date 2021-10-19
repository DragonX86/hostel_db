from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from entities.building_entity import BuildingManager
from forms.building_modal import BuildingModal
from utils.operationEnum import OperationEnum


class BuildingWindow(QMainWindow):
    def __init__(self):
        super(BuildingWindow, self).__init__()

        self.building_modal = None
        self.current_guid = None

        self.ui = uic.loadUiType('./designs/building_window.ui')[0]()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.buttons_click_handler)
        self.ui.edit_button.clicked.connect(self.buttons_click_handler)
        self.ui.delete_button.clicked.connect(self.delete_record)

        self.ui.close_button.clicked.connect(self.close)

        self.configure_tableWidget()

    def buttons_click_handler(self):
        sender_text = self.sender().text()

        if sender_text == 'Добавить запись':
            window_type = OperationEnum.ADD
            self.ui.building_modal = BuildingModal(window_type)
        elif sender_text == 'Редактировать запись':
            window_type = OperationEnum.EDIT

            if self.current_guid is None:
                return None

            building = BuildingManager.get_building_by_id(self.current_guid)
            self.ui.building_modal = BuildingModal(window_type, building)

        self.ui.building_modal.com.update.connect(self.update_table_data)
        self.ui.building_modal.show()

    def configure_tableWidget(self):
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "__GUID", "Адресс корпуса",
            ]
        )

        self.ui.tableWidget.cellClicked.connect(self.get_current_guid)
        self.update_table_data()

    def delete_record(self):
        if self.current_guid is not None:
            BuildingManager.delete_building_by_id(self.current_guid)
            self.update_table_data()

    def get_current_guid(self, row):
        self.current_guid = self.ui.tableWidget.item(row, 0).text()

    def update_table_data(self):
        self.ui.tableWidget.setRowCount(0)

        for building in BuildingManager.get_all_buildings():
            buildingRow = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(buildingRow)

            self.ui.tableWidget.setItem(buildingRow, 0, QTableWidgetItem(building.building_id))
            self.ui.tableWidget.setItem(buildingRow, 1, QTableWidgetItem(building.building_address))
