from typing import Optional
from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from entities.building_entity import Building, BuildingManager
from utils.operationEnum import OperationEnum


class Communicate(QObject):
    update = pyqtSignal()


class BuildingModal(QMainWindow):
    def __init__(self, window_type: OperationEnum, building: Optional[Building] = None):
        super(BuildingModal, self).__init__()

        self.building = building
        self.com = Communicate()

        self.ui = uic.loadUiType('./designs/building_modal.ui')[0]()
        self.ui.setupUi(self)

        if window_type == OperationEnum.ADD:
            self.setWindowTitle("Добавление новой записи")
            self.ui.result_button.setText("Добавить новую запись")
            self.ui.result_button.clicked.connect(self.add_group)
        elif window_type == OperationEnum.EDIT:
            self.ui.building_address.setText(building.building_address)

            self.setWindowTitle("Редактирование записи")
            self.ui.result_button.setText("Сохранить изменения")
            self.ui.result_button.clicked.connect(self.edit_group)

    def add_group(self):
        building_address = self.ui.building_address.text()

        if building_address and not building_address.isspace():
            BuildingManager.add_new_building(building_address)
            self.com.update.emit()

        self.close()

    def edit_group(self):
        building_address = self.ui.building_address.text()

        if building_address and not building_address.isspace():
            if self.building is not None:
                self.building.building_address = building_address

                BuildingManager.update_building(self.building)
                self.com.update.emit()

        self.close()
