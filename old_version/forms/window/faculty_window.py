from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from utils.operationEnum import OperationEnum
from forms.modal.faculty_modal import FacultyModal
from models.faculty_manager import FacultyManager


class FacultyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(FacultyWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/window/faculty_window.ui')[0]()
        self.ui.setupUi(self)

        self.current_guid = None

	self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "__GUID", "Факультет",
            ]
        )

        self.ui.tableWidget.cellClicked.connect(self.get_current_guid)
        self.ui.add_button.clicked.connect(self.buttons_click_handler)
        self.ui.edit_button.clicked.connect(self.buttons_click_handler)

        self.ui.delete_button.clicked.connect(self.delete_record)

        self.ui.close_button.clicked.connect(self.close)

        self.update_table()

    def buttons_click_handler(self):
        sender_text = self.sender().text()

        window_type = None

        if sender_text == 'Добавить запись':
            window_type = OperationEnum.ADD
        elif sender_text == 'Редактировать запись':
            window_type = OperationEnum.EDIT

        self.ui.faculty_modal = FacultyModal(window_type)

        self.ui.faculty_modal.com.update.connect(self.update_table)

        self.ui.faculty_modal.show()

    def delete_record(self):
        if self.current_guid is not None:
            FacultyManager.delete_faculty_by_id(self.current_guid)
            self.update_table()

    def get_current_guid(self, row):
        self.current_guid = self.ui.tableWidget.item(row, 0).text()

    def update_table(self):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnHidden(0, True)

        for faculty in FacultyManager.all_faculties():
            numRows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(numRows)

            self.ui.tableWidget.setItem(numRows, 0, QTableWidgetItem(faculty.faculty_id))
            self.ui.tableWidget.setItem(numRows, 1, QTableWidgetItem(faculty.faculty_name))
