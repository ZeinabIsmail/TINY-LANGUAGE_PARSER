import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form")
        Form1.resize(783, 535)
        self.title = 'Parser Tree'
        self.left = 100
        self.top = 100
        self.width = 640
        self.height = 480
        Form1.setWindowTitle(self.title)
        Form1.setGeometry(self.left, self.top, self.width, self.height)
        self.label = QtWidgets.QLabel(Form1)
        pixmap = QPixmap('SyntaxTree.png')
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.width(), pixmap.height())
        Form1.resize(pixmap.width(), pixmap.height())
        Form1.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QMainWindow()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())