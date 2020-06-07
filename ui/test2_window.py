from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys

def draw():
    '''
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    #ui.set_notification_text("Spotify", "127.0.0.1", "8080")
    app.exec_()'''
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()
    layout.addWidget(QPushButton('Top'))
    layout.addWidget(QPushButton('Bottom'))
    window.setLayout(layout)
    window.show()
    app.exec_()

#draw()