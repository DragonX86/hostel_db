from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

from utils.operationEnum import OperationEnum


class StudentsModal(QtWidgets.QMainWindow):
    def __init__(self, window_type: OperationEnum, ):
        super(StudentsModal, self).__init__()

        self.ui = uic.loadUiType('./designs/students_modal.ui')[0]()
        self.ui.setupUi(self)

        self.ui.gender.addItems(['Мужской', 'Женский'])

        if window_type == OperationEnum.ADD:
            self.setWindowTitle("Добавление студента")
            self.ui.result_button.setText("Добавить студента")
            self.ui.result_button.clicked.connect(self.add_student)
        elif window_type == OperationEnum.EDIT:
            self.setWindowTitle("Редактирование студента")
            self.ui.result_button.setText("Сохранить изменения")
            self.ui.result_button.clicked.connect(self.edit_student)

    def add_student(self):
        full_name = self.ui.full_name.text().strip()
        gender = self.ui.gender.currentText()
        birthdate = self.ui.birthdate.text()

        if full_name:
            DatabaseSingleton()
            query = QSqlQuery()

            query.prepare("INSERT INTO students (full_name, name, salary) VALUES (:full_name, :name, :salary)")

            query.bindValue(":full_name", full_name)
            query.bindValue(":name", "Thad Beaumont")
            query.bindValue(":salary", 65000)
            query.exec()
        else:
            msgBox = QMessageBox()
            msgBox.setText("Поле ФИО пусто. \nЗапись не будет добавлена в базу.")
            msgBox.exec()

        self.close()

    def edit_student(self):
        self.close()
