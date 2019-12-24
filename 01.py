import sys
import random
from PIL import Image
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import sys


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        pass



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
