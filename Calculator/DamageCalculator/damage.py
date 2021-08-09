from PySide2.QtWidgets import *


class Damage_Calculator:
    def __init__(self):
        self.window = QWidget()
        self.window.resize(360, 720)
        self.window.move(320, 320)
        self.window.setWindowTitle("Pokemon 伤害计算器")
        self.layout = QVBoxLayout()
        self.input_box = QPlainTextEdit(self.window)
        self.input_box.setPlaceholderText("请输入：")
        self.layout.addWidget(self.input_box)
        self.return_button = QPushButton("返回", self.window)
        self.layout.addWidget(self.return_button)
        self.return_button.clicked.connect(self.close_damage)

    def start_damage(self):
        print("伤害计算模式启动")
        self.window.show()

    def close_damage(self):
        print("伤害计算模式关闭")
        self.window.close()