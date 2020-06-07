from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()

        self.myCloseAction = None

        self.resize(710, 587)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 200, 681, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.notification_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.notification_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notification_label.setObjectName("notification_label")
        self.gridLayout.addWidget(self.notification_label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(70)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.allowButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.allowButton.setObjectName("allowButton")
        self.horizontalLayout.addWidget(self.allowButton)
        self.denyButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.denyButton.setObjectName("denyButton")
        self.horizontalLayout.addWidget(self.denyButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 710, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.notification_label.setText("Test label")
        self.allowButton.setText("Allow")
        self.denyButton.setText("Deny")

    def set_notification_text(self, app_name, ip, port):
        new_str = "{} wants to connect to {} on port {}.".format(app_name, ip, port)
        self.notification_label.setText(new_str)

    def closeWindow(self):
        self.close()

    def closeEvent(self, event):
        if self.myCloseAction is not None:
            self.myCloseAction()
        print("Closing...")
        event.accept()
    
    def setCloseAction(self, action):
        self.myCloseAction = action

    def setAllowAction(self, action):
        self.allowButton.clicked.connect(action)

    def setDenyAction(self, action):
        self.denyButton.clicked.connect(action)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    ui.set_notification_text("Spotify", "127.0.0.1", "8080")
    sys.exit(app.exec_())