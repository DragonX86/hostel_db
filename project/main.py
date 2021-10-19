import sys

from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow

from forms.faculty_window import FacultyWindow
from forms.groups_window import GroupsWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = uic.loadUiType('main.ui')[0]()
        self.ui.setupUi(self)

        self.ui.groups_button.clicked.connect(self.buttons_click_handler)
        self.ui.faculty_button.clicked.connect(self.buttons_click_handler)

        self.ui.exit_button.clicked.connect(sys.exit)

    def buttons_click_handler(self):
        sender_text = self.sender().text()

        if sender_text == 'Студенты':
            pass
        elif sender_text == 'Проживание':
            pass
        elif sender_text == 'Комнаты':
            pass
        elif sender_text == 'Секции':
            pass
        elif sender_text == 'Группы':
            self.ui.groups_window = GroupsWindow()
            self.ui.groups_window.show()
        elif sender_text == 'Корпусы':
            pass
        elif sender_text == 'Комменданты':
            pass
        elif sender_text == 'Факультеты':
            self.ui.faculty_window = FacultyWindow()
            self.ui.faculty_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())
