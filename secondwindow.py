from PyQt5 import QtWidgets

class SecondWindow(QtWidgets.QWidget):
    def init_ui(self):
        v_layout = QtWidgets.QVBoxLayout(self)
        v_layout.addWidget(self.text)
        self.setWindowTitle('Opened Text')
        self.show()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shower = SecondWindow()
    sys.exit(app.exec_())