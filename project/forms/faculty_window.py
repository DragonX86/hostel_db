from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from models.faculty_manager import FacultyManager
from forms.faculty_modal import FacultyModal
from utils.operationEnum import OperationEnum


class FacultyWindow(QMainWindow):
    def __init__(self):
        super(FacultyWindow, self).__init__()

        self.faculty_modal = None
        self.current_guid = None

        self.ui = uic.loadUiType('./designs/faculty_window.ui')[0]()
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
            self.ui.faculty_modal = FacultyModal(window_type, None)
        elif sender_text == 'Редактировать запись':
            window_type = OperationEnum.EDIT
            faculty = FacultyManager.get_faculty_by_id(self.current_guid)
            self.ui.faculty_modal = FacultyModal(window_type, faculty)

        self.ui.faculty_modal.com.update.connect(self.update_table_data)
        self.ui.faculty_modal.show()

    def get_current_guid(self, row):
        self.current_guid = self.ui.tableWidget.item(row, 0).text()

    def delete_record(self):
        if self.current_guid is not None:
            FacultyManager.delete_faculty_by_id(self.current_guid)
            self.update_table_data()

    def configure_tableWidget(self):
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            [
                "__GUID", "Факультет",
            ]
        )

        self.ui.tableWidget.cellClicked.connect(self.get_current_guid)
        self.update_table_data()

    def update_table_data(self):
        self.ui.tableWidget.setRowCount(0)

        for faculty in FacultyManager.get_all_faculties():
            numRows = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(numRows)

            self.ui.tableWidget.setItem(numRows, 0, QTableWidgetItem(faculty.faculty_id))
            self.ui.tableWidget.setItem(numRows, 1, QTableWidgetItem(faculty.faculty_name))
