from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, QObject

from utils.operationEnum import OperationEnum

from models.faculty_manager import FacultyManager


class Communicate(QObject):
    update = pyqtSignal()


class FacultyModal(QtWidgets.QMainWindow):
    def __init__(self, window_type: OperationEnum, ):
        super(FacultyModal, self).__init__()

        self.com = Communicate()

        self.ui = uic.loadUiType('./designs/modal/faculty_modal.ui')[0]()
        self.ui.setupUi(self)

        if window_type == OperationEnum.ADD:
            self.setWindowTitle("Добавление новой записи")
            self.ui.result_button.setText("Добавить новую запись")
            self.ui.result_button.clicked.connect(self.add_faculty)
        elif window_type == OperationEnum.EDIT:
            self.setWindowTitle("Редактирование записи")
            self.ui.result_button.setText("Сохранить изменения")
            # self.ui.result_button.clicked.connect(self.edit_student)

    def add_faculty(self):
        faculty_name = self.ui.faculty_name.text()

        if faculty_name and not faculty_name.isspace():
            FacultyManager.add_faculty(faculty_name)
            self.com.update.emit()

        self.close()
