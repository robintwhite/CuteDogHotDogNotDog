from PyQt5 import QtWidgets
from gui import Ui_QDialog
import sys
from classifyImage import classifyImage

class ApplicationWindow(QtWidgets.QDialog, Ui_QDialog):
    def __init__(self):
        super(ApplicationWindow, self).__init__()

        self.ui = Ui_QDialog()
        self.ui.setupUi(self)

        # Initialize click ojects
        self.ui.quit_button.clicked.connect(self.quitClicked)
        self.ui.classify_button.clicked.connect(self.classify)
        self.ui.print_result.setReadOnly(True)
        self.ui.correct_num.setReadOnly(True)
        self.ui.correct_num.setText(str(0))
        self.ui.correct_button.clicked.connect(self.add_score_correct)
        self.ui.wrong_num.setReadOnly(True)
        self.ui.wrong_num.setText(str(0))
        self.ui.wrong_button.clicked.connect(self.add_score_wrong)

        # Initialize variables
        self.score_correct = 0
        self.score_wrong = 0
        self.classified = False
        self.previous_image = ""

        self.classify_model = classifyImage()

    def quitClicked(self):
        sys.exit()

    def classify(self):
        if self.ui.Image.path_to_image != "" and \
        self.ui.Image.path_to_image != self.previous_image:
            image_to_classify = self.ui.Image.path_to_image
            self.classify_model.classify(image_to_classify)
            self.ui.print_result.setText(self.classify_model.label)
            self.classified = True
            self.previous_image = self.ui.Image.path_to_image

    def add_score_correct(self):
        if self.classified:
            self.score_correct += 1
            self.ui.correct_num.setText(str(self.score_correct))
            self.classified = False


    def add_score_wrong(self):
        if self.classified:
            self.score_wrong += 1
            self.ui.wrong_num.setText(str(self.score_wrong))
            self.classified = False


def main():
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
