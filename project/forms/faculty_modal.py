from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, QObject
from typing import Optional

from utils.operationEnum import OperationEnum

from models.faculty_manager import FacultyManager
from models.faculty_manager import Faculty


class Communicate(QObject):
    update = pyqtSignal()


class FacultyModal(QtWidgets.QMainWindow):
    def __init__(self, window_type: OperationEnum, faculty: Optional[Faculty]):
        super(FacultyModal, self).__init__()

        self.faculty = faculty

        self.com = Communicate()

        self.ui = uic.loadUiType('./designs/faculty_modal.ui')[0]()
        self.ui.setupUi(self)

        if window_type == OperationEnum.ADD:
            self.setWindowTitle("Добавление новой записи")
            self.ui.result_button.setText("Добавить новую запись")
            self.ui.result_button.clicked.connect(self.add_faculty)
        elif window_type == OperationEnum.EDIT:
            self.ui.faculty_name.setText(faculty.faculty_name)

            self.setWindowTitle("Редактирование записи")
            self.ui.result_button.setText("Сохранить изменения")
            self.ui.result_button.clicked.connect(self.edit_faculty)

    def add_faculty(self):
        faculty_name = self.ui.faculty_name.text()

        if faculty_name and not faculty_name.isspace():
            FacultyManager.add_faculty(faculty_name)
            self.com.update.emit()

        self.close()

    def edit_faculty(self):
        faculty_name = self.ui.faculty_name.text()

        if faculty_name and not faculty_name.isspace():
            if self.faculty is not None:
                self.faculty.faculty_name = faculty_name

                FacultyManager.update_faculty(self.faculty)
                self.com.update.emit()

        self.close()
