from typing import Optional
from PyQt5 import uic
from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import QMainWindow

from entities.group_entity import Group
from entities.group_entity import GroupManager
from entities.faculty_entity import FacultyManager
from utils.operationEnum import OperationEnum


class Communicate(QObject):
    update = pyqtSignal()


class GroupModal(QMainWindow):
    def __init__(self, window_type: OperationEnum, group: Optional[Group] = None):
        super(GroupModal, self).__init__()

        self.group = group
        self.com = Communicate()

        self.ui = uic.loadUiType('./designs/group_modal.ui')[0]()
        self.ui.setupUi(self)

        self.ui.comboBox.addItems([faculty.faculty_name for faculty in FacultyManager.get_all_faculties()])

        if window_type == OperationEnum.ADD:
            self.setWindowTitle("Добавление новой записи")
            self.ui.result_button.setText("Добавить новую запись")
            self.ui.result_button.clicked.connect(self.add_group)
        elif window_type == OperationEnum.EDIT:
            self.ui.group_name.setText(group.group_name)
            self.ui.comboBox.setCurrentText(group.faculty_name)

            self.setWindowTitle("Редактирование записи")
            self.ui.result_button.setText("Сохранить изменения")
            self.ui.result_button.clicked.connect(self.edit_group)

    def add_group(self):
        group_name = self.ui.group_name.text()

        if group_name and not group_name.isspace():
            group = Group(
                group_id=None,
                group_name=group_name,
                faculty_name=self.ui.comboBox.currentText()
            )

            GroupManager.add_new_group(group)
            self.com.update.emit()

        self.close()

    def edit_group(self):
        group_name = self.ui.group_name.text()

        if group_name and not group_name.isspace():
            if self.group is not None:
                self.group.group_name = group_name
                self.group.faculty_name = self.ui.comboBox.currentText()

                GroupManager.update_group(self.group)
                self.com.update.emit()

        self.close()
