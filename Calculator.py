from tkinter import *
from PySide2.QtWidgets import *

class Main_Menu:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(360, 720)
        self.window.move(300, 300)
        self.window.setWindowTitle("Pokemon Calculator v1.0")
        self.damage_button = QPushButton("伤害", self.window)
        self.damage_button.move(120, 100)
        # self.damage_button.clicked.connect(self.damageClicked)
        self.range_button = QPushButton("打击面", self.window)
        self.range_button.move(120, 160)

    def damageClicked(self):
        print("伤害计算模式")
        self.window.close()
        damage_cal = Damage_Calculator()
        damage_cal.start_damage()

    def close_menu(self):
        self.window.close()


class Damage_Calculator:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(360, 720)
        self.window.move(320, 320)
        self.window.setWindowTitle("Pokemon Calculator v1.0")

    def start_damage(self):
        print("伤害计算模式启动")
        self.window.show()


def start_main():
    app = QApplication(sys.argv)
    main_menu = Main_Menu()
    damage_window = Damage_Calculator()
    main_menu.damage_button.clicked.connect(main_menu.close_menu)
    main_menu.damage_button.clicked.connect(damage_window.start_damage)
    main_menu.window.show()
    app.exec_()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_main()
