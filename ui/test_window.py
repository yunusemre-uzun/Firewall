# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_window3.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(716, 269)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.notification_label = QtWidgets.QLabel(self.centralwidget)
        self.notification_label.setGeometry(QtCore.QRect(270, 40, 179, 61))
        self.notification_label.setAlignment(QtCore.Qt.AlignCenter)
        self.notification_label.setObjectName("notification_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 140, 679, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(70)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.allowButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.allowButton.setObjectName("allowButton")
        self.horizontalLayout.addWidget(self.allowButton)
        self.denyButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.denyButton.setObjectName("denyButton")
        self.horizontalLayout.addWidget(self.denyButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.notification_label.setText(_translate("MainWindow", "TextLabel"))
        self.allowButton.setText(_translate("MainWindow", "Allow"))
        self.denyButton.setText(_translate("MainWindow", "Deny"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
