from PySide2.QtWidgets import *

class Window2(QWidget):

    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Laisser un commentaire")
        self.layout = QGridLayout()

        self.label = QLabel("""
        
        
        
        a great comment
        
        
        
        """)
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")

        self.layout.addWidget(self.label,0,0)
        self.layout.addWidget(self.button1,1,0)
        self.layout.addWidget(self.button2,1,1)

        self.setLayout(self.layout)

if __name__ == "__main__" :
    app = QApplication([])
    win = Window2()
    win.show()
    app.exec_()
