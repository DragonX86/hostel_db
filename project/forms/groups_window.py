from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QHeaderView

from entities.group_entity import GroupManager
from forms.group_modal import GroupModal
from utils.operationEnum import OperationEnum


class GroupsWindow(QMainWindow):
    def __init__(self):
        super(GroupsWindow, self).__init__()

        self.group_modal = None
        self.current_guid = None

        self.ui = uic.loadUiType('./designs/groups_window.ui')[0]()
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
            self.ui.group_modal = GroupModal(window_type)
        elif sender_text == 'Редактировать запись':
            window_type = OperationEnum.EDIT

            if self.current_guid is None:
                return None

            group = GroupManager.get_group_by_id(self.current_guid)
            self.ui.group_modal = GroupModal(window_type, group)

        self.ui.group_modal.com.update.connect(self.update_table_data)
        self.ui.group_modal.show()

    def configure_tableWidget(self):
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "__GUID", "Группа", "Факультет",
            ]
        )

        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget.cellClicked.connect(self.get_current_guid)

        self.update_table_data()

    def delete_record(self):
        if self.current_guid is not None:
            GroupManager.delete_group_by_id(self.current_guid)
            self.update_table_data()

    def get_current_guid(self, row):
        self.current_guid = self.ui.tableWidget.item(row, 0).text()

    def update_table_data(self):
        self.ui.tableWidget.setRowCount(0)

        for group in GroupManager.get_all_groups():
            groupRow = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(groupRow)

            self.ui.tableWidget.setItem(groupRow, 0, QTableWidgetItem(group.group_id))
            self.ui.tableWidget.setItem(groupRow, 1, QTableWidgetItem(group.group_name))
            self.ui.tableWidget.setItem(groupRow, 2, QTableWidgetItem(group.faculty_name))
