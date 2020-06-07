# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.testButton = QtWidgets.QPushButton(self.centralwidget)
        self.testButton.setEnabled(True)
        self.testButton.setGeometry(QtCore.QRect(300, 440, 201, 61))
        self.testButton.setObjectName("testButton")
        self.testLabel = QtWidgets.QLabel(self.centralwidget)
        self.testLabel.setGeometry(QtCore.QRect(350, 140, 121, 21))
        self.testLabel.setObjectName("testLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionTest1 = QtWidgets.QAction(MainWindow)
        self.actionTest1.setObjectName("actionTest1")
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionTest1)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.testButton.setText(_translate("MainWindow", "PushButton"))
        self.testLabel.setText(_translate("MainWindow", "Testing the label"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionTest1.setText(_translate("MainWindow", "Test1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
