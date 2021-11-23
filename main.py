import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow


SCREEN_SIZE = [800, 600]


class RandomCircle(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        uic.loadUi("UI.ui", self)
        self.setFixedSize(*SCREEN_SIZE)
        self.do_paint = False
        self.click = 0
        self.push.clicked.connect(self.clicked)

    def clicked(self):
        self.click = 1
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            if self.click == 1:
                self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x = randint(30, 770)
        y = randint(30, 570)
        color1 = randint(10, 255)
        color2 = randint(10, 255)
        color3 = randint(10, 255)
        qp.setBrush(QColor(color1, color2, color3))
        number = randint(5, 300)
        qp.drawEllipse(x - number // 2, y - number // 2, number, number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    fg = RandomCircle()
    fg.show()
    sys.exit(app.exec())