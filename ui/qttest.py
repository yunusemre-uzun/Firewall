from PyQt5 import QtWidgets
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.count = 0
        self.label = QtWidgets.QLabel(self)
        self.button = QtWidgets.QPushButton(self)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("TEST")

        self.label.setText("Test 0")
        self.label.move(100, 100)

        self.button.setText("test button!!")
        self.button.clicked.connect(self.button_action)
        
    def button_action(self):
        self.count += 1
        self.label.setText("Test {}".format(self.count))
        print("clicked")

    def closeEvent(self, event):
        print("Closing...")
        event.accept()

def window():
    app = QtWidgets.QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()