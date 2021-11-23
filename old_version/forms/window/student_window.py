from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem

from forms.modal.student_modal import StudentsModal
from utils.operationEnum import OperationEnum
from models.studentManager import StudentManager


class StudentsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StudentsWindow, self).__init__()

        self.ui = uic.loadUiType('./designs/students_window.ui')[0]()
        self.ui.setupUi(self)

        self.ui.add_button.clicked.connect(self.buttons_click_handler)
        self.ui.edit_button.clicked.connect(self.buttons_click_handler)

        self.ui.close_button.clicked.connect(self.close)

        self.fill_table()

    def buttons_click_handler(self):
        sender_text = self.sender().text()

        if sender_text == 'Добавить запись':
            self.ui.students_modal = StudentsModal(OperationEnum.ADD)
            self.ui.students_modal.show()
        elif sender_text == 'Редактировать запись':
            self.ui.lodgers = StudentsModal(OperationEnum.EDIT)
            self.ui.lodgers.show()

    def fill_table(self):
        self.ui.students_table.setHorizontalHeaderLabels(
            [
                "Фамилия",
                "Имя",
                "Отчество",
                "Пол",
                "Дата рождения",
                "Группа"
            ]
        )
        self.ui.students_table.horizontalHeader()\
            .setSectionResizeMode(QHeaderView.Stretch)
        # self.ui.students_table.setColumnHidden(3, True)

        for student in StudentManager.all_students():
            numRows = self.ui.students_table.rowCount()
            self.ui.students_table.insertRow(numRows)

            self.ui.students_table.setItem(numRows, 0, QTableWidgetItem(student.surname))
            self.ui.students_table.setItem(numRows, 1, QTableWidgetItem(student.first_name))
            self.ui.students_table.setItem(numRows, 2, QTableWidgetItem(student.middle_name))
            self.ui.students_table.setItem(numRows, 3, QTableWidgetItem(student.gender))
            self.ui.students_table.setItem(numRows, 4, QTableWidgetItem(student.birthdate))
            self.ui.students_table.setItem(numRows, 5, QTableWidgetItem(student.group_name))
