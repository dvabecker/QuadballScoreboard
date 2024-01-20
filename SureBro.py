from PyQt5.QtWidgets import QDialog
import os
from sureBro_ui import Ui_sureBro


class SureBro(QDialog):
    def __init__(self, main_window):
        super().__init__()
        self.ui = Ui_sureBro()
        self.ui.setupUi(self)
        self.main = main_window

    def yes(self):
        self.accept()
        self.main.close()

    def no(self):
        self.accept()
