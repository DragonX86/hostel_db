import sys
from utils import indicators

from PyQt5 import QtWidgets, QtGui, QtCore, uic
from PyQt5.QtGui import QColor, QPen, QBrush

from forms.window.buildingWindow import BuildingWindow
from forms.window.commandantsWindow import CommandantsWindow
from forms.window.lodgersWindow import LodgersWindow
from forms.window.roomsWindow import RoomsWindow
from forms.window.sectionWindow import SectionWindow
from forms.window.student_window import StudentsWindow
from forms.window.faculty_window import FacultyWindow

from utils.comboValueSingleton import ComboValueSingleton

sections = [
    "Секция 110", "Секция 210", "Секция 120", "Секция 220", "Секция 130", "Секция 230", "Секция 140",
    "Секция 240", "Секция 150", "Секция 250", "Секция 160", "Секция 260", "Секция 170", "Секция 270",
    "Секция 180", "Секция 280", "Секция 190", "Секция 290"
]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = uic.loadUiType('main.ui')[0]()
        self.ui.setupUi(self)

        self.ui.section_combobox.addItems(sections)
        self.ui.section_combobox.lineEdit().setAlignment(QtCore.Qt.AlignCenter)
        self.ui.section_combobox.currentTextChanged.connect(self.on_combobox_changed)

        self.ui.students_button.clicked.connect(self.buttons_click_handler)
        self.ui.lodgers_button.clicked.connect(self.buttons_click_handler)
        self.ui.rooms_button.clicked.connect(self.buttons_click_handler)
        self.ui.section_button.clicked.connect(self.buttons_click_handler)
        self.ui.commandants_button.clicked.connect(self.buttons_click_handler)
        self.ui.building_button.clicked.connect(self.buttons_click_handler)
        self.ui.faculty_button.clicked.connect(self.buttons_click_handler)

        self.ui.exit_button.clicked.connect(sys.exit)

        self.scene = QtWidgets.QGraphicsScene()
        self.scene.addPixmap(QtGui.QPixmap("./section.png"))
        self.ui.section_view.setScene(self.scene)

        self.draw_room_indicators()
        self.draw_labels()

    def buttons_click_handler(self):
        sender_text = self.sender().text()

        if sender_text == 'Студенты':
            self.ui.students = StudentsWindow()
            self.ui.students.show()
        elif sender_text == 'Проживание':
            self.ui.lodgers = LodgersWindow()
            self.ui.lodgers.show()
        elif sender_text == 'Комнаты':
            combo_value = self.ui.section_combobox.currentText()
            ComboValueSingleton().set_value(combo_value.split()[1])

            self.ui.rooms = RoomsWindow()
            self.ui.rooms.show()
        elif sender_text == 'Секции':
            self.ui.section = SectionWindow()
            self.ui.section.show()
        elif sender_text == 'Корпусы':
            self.ui.building = BuildingWindow()
            self.ui.building.show()
        elif sender_text == 'Комменданты':
            self.ui.commandants = CommandantsWindow()
            self.ui.commandants.show()
        elif sender_text == 'Факультеты':
            self.ui.faculty = FacultyWindow()
            self.ui.faculty.show()

    def on_combobox_changed(self):
        self.scene.clear()
        self.scene.addPixmap(QtGui.QPixmap("./section.png"))
        self.draw_room_indicators()
        self.draw_labels()

    def draw_labels(self):
        combo_value = int(self.ui.section_combobox.currentText().split()[1])
        value = round(combo_value / 10)

        rooms = [
            (196, 17, f"Комната {value}1"), (330, 17, f"Комната {value}2"), (465, 17, f"Комната {value}3"), (595, 17, f"Комната {value}4"),
            (196, 399, f"Комната {value}5"), (330, 399, f"Комната {value}6"), (465, 399, f"Комната {value}7"), (595, 399, f"Комната {value}8")
        ]

        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)

        for x, y, room in rooms:
            text = self.scene.addText(room)
            text.setFont(font)
            text.setPos(x, y)

    def draw_room_indicators(self):
        combo_value = int(self.ui.section_combobox.currentText().split()[1])
        value = round(combo_value / 10) * 10

        for x, y, color in indicators.get_indicators(value):
            self.scene.addRect(x, y, 35, 35, pen=QPen(QColor("black")), brush=QBrush(QColor(color)))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()

    sys.exit(app.exec())
