import sys
from PyQt5.QtWidgets import (QPushButton, QWidget,
    QLineEdit, QApplication)
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            self.parent().label.setPixmap(QPixmap(m.urls()[0].toLocalFile()))


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = Button("",self)
        button.resize(100,100)
        button.setIcon(QIcon("gazo1.jpg"))
        button.setIconSize(QSize(100,100))
        button.move(0, 0)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('gazo2.png'))
        self.label.move(150,150)

        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 300)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
