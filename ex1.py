from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QVBoxLayout
#from PySide2.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.label = QLabel("Ceci est un QLabel")
        self.QPushButton = QPushButton("Ceci est un QPushButton")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.QPushButton)

        self.setLayout(self.layout)

if __name__ == "__main__" :
    app = QApplication([])
    win = Window()
    win.show()
    app.exec_()
