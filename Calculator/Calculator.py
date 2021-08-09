import sys

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from DamageCalculator import damage
from RangeCalculator import range


class Main_Menu:
    def __init__(self):
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.resize(360, 720)
        self.window.move(300, 300)
        self.window.setWindowTitle("Pokemon Calculator v1.0")
        self.damage_button = QPushButton("伤害")
        self.layout.addWidget(self.damage_button)
        self.range_button = QPushButton("打击面")
        self.layout.addWidget(self.range_button)
        self.window.setLayout(self.layout)

    def start_menu(self):
        print("主程序启动")
        self.window.show()

    def close_menu(self):
        print("欢迎您再来")
        self.window.close()


def start_main():
    app = QApplication()
    app.setWindowIcon(QIcon("../icon/pokemonBall.jpeg"))
    main_menu = Main_Menu()
    damage_window = damage.Damage_Calculator()
    range_window = range.Range_Calculator()

    main_menu.damage_button.clicked.connect(main_menu.close_menu)
    main_menu.damage_button.clicked.connect(damage_window.start_damage)
    main_menu.range_button.clicked.connect(main_menu.close_menu)
    main_menu.range_button.clicked.connect(range_window.start_range)
    damage_window.return_button.clicked.connect(main_menu.start_menu)

    main_menu.start_menu()
    app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_main()
