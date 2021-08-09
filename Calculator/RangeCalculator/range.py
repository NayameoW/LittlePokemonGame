from PySide2.QtWidgets import *

class Range_Calculator:
    def __init__(self):
        self.window = QMainWindow()
        self.window.resize(360, 720)
        self.window.move(320, 320)
        self.window.setWindowTitle("Pokemon 打击面计算器")

    def start_range(self):
        print("打击面模式启动")
        self.window.show()
