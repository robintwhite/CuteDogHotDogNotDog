# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Button(QtWidgets.QLabel):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
        self.path_to_image = ""

    def dragEnterEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        m = e.mimeData()
        if m.hasUrls():
            self.setPixmap(QtGui.QPixmap(m.urls()[0].toLocalFile()))
            self.path_to_image = str(m.urls()[0].toLocalFile())
            #str(m.urls()[0].toLocalFile().toLocal8Bit().data())

class Ui_QDialog(object):
    def setupUi(self, QDialog):
        QDialog.setObjectName("QDialog")
        QDialog.resize(483, 372)
        QDialog.setMinimumSize(QtCore.QSize(483, 372))
        QDialog.setMaximumSize(QtCore.QSize(483, 372))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Lib/hotdog.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        QDialog.setWindowIcon(icon)
        QDialog.setAutoFillBackground(False)
        QDialog.setStyleSheet("background-color: rgb(255, 255, 0);")
        QDialog.setSizeGripEnabled(False)
        self.classify_button = QtWidgets.QPushButton(QDialog)
        self.classify_button.setGeometry(QtCore.QRect(148, 310, 75, 30))
        self.classify_button.setStyleSheet("font: 87 10pt \"Arial Black\";\n"
"background-color: rgb(170, 170, 170);")
        self.classify_button.setObjectName("classify_button")
        self.Image = Button("", QDialog)
        self.Image.setGeometry(QtCore.QRect(45, 15, 270, 235))
        self.Image.setAcceptDrops(True)
        self.Image.setAutoFillBackground(False)
        self.Image.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"font: 75 10pt \"Calibri\";")
        self.Image.setText("Drop image here!")
        self.Image.setAlignment(QtCore.Qt.AlignCenter)
        self.Image.setScaledContents(True)
        self.Image.setObjectName("Image")
        self.quit_button = QtWidgets.QPushButton(QDialog)
        self.quit_button.setGeometry(QtCore.QRect(390, 340, 75, 23))
        self.quit_button.setStyleSheet("background-color: rgb(216, 216, 216);")
        self.quit_button.setObjectName("quit_button")
        self.print_result = QtWidgets.QLineEdit(QDialog)
        self.print_result.setGeometry(QtCore.QRect(130, 260, 113, 20))
        self.print_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgba(255, 255, 255, 0);")
        self.print_result.setObjectName("print_result")
        self.label_result = QtWidgets.QLabel(QDialog)
        self.label_result.setGeometry(QtCore.QRect(70, 260, 47, 20))
        self.label_result.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_result.setObjectName("label_result")
        self.correct_button = QtWidgets.QPushButton(QDialog)
        self.correct_button.setGeometry(QtCore.QRect(48, 310, 81, 31))
        self.correct_button.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 255, 0);\n"
"alternate-background-color: rgb(170, 0, 255);")
        self.correct_button.setObjectName("correct_button")
        self.wrong_button = QtWidgets.QPushButton(QDialog)
        self.wrong_button.setGeometry(QtCore.QRect(238, 310, 75, 31))
        self.wrong_button.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 0, 0);")
        self.wrong_button.setObjectName("wrong_button")
        self.correct_num = QtWidgets.QLineEdit(QDialog)
        self.correct_num.setGeometry(QtCore.QRect(330, 40, 61, 20))
        self.correct_num.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(85, 255, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.correct_num.setObjectName("correct_num")
        self.label_score = QtWidgets.QLabel(QDialog)
        self.label_score.setGeometry(QtCore.QRect(380, 10, 47, 20))
        self.label_score.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_score.setObjectName("label_score")
        self.label_correct_num = QtWidgets.QLabel(QDialog)
        self.label_correct_num.setGeometry(QtCore.QRect(400, 40, 71, 20))
        self.label_correct_num.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_correct_num.setObjectName("label_correct_num")
        self.label_wrong_num = QtWidgets.QLabel(QDialog)
        self.label_wrong_num.setGeometry(QtCore.QRect(400, 70, 71, 20))
        self.label_wrong_num.setStyleSheet("font: 87 10pt \"Arial Black\";")
        self.label_wrong_num.setObjectName("label_wrong_num")
        self.wrong_num = QtWidgets.QLineEdit(QDialog)
        self.wrong_num.setGeometry(QtCore.QRect(330, 70, 61, 20))
        self.wrong_num.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"background-color: rgb(255, 65, 65);\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.wrong_num.setObjectName("wrong_num")
        self.logo = QtWidgets.QLabel(QDialog)
        self.logo.setGeometry(QtCore.QRect(344, 131, 121, 141))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("Lib/logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")

        self.retranslateUi(QDialog)
        QtCore.QMetaObject.connectSlotsByName(QDialog)

    def retranslateUi(self, QDialog):
        _translate = QtCore.QCoreApplication.translate
        QDialog.setWindowTitle(_translate("QDialog", "DogHotDogNotDog"))
        self.classify_button.setText(_translate("QDialog", "Classify!"))
        self.quit_button.setText(_translate("QDialog", "Quit"))
        self.label_result.setText(_translate("QDialog", "Result"))
        self.correct_button.setText(_translate("QDialog", "Correct!"))
        self.wrong_button.setText(_translate("QDialog", "Wrong!"))
        self.label_score.setText(_translate("QDialog", "Score"))
        self.label_correct_num.setText(_translate("QDialog", "Correct"))
        self.label_wrong_num.setText(_translate("QDialog", "Incorrect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QDialog = QtWidgets.QDialog()
    ui = Ui_QDialog()
    ui.setupUi(QDialog)
    QDialog.show()
    sys.exit(app.exec_())
