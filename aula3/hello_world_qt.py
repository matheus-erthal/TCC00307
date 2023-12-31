import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def window():
    app = QApplication([sys.argv])
    w = QWidget()
    b = QLabel(w)
    b.setText('Hello World!')
    b.setAlignment(Qt.AlignCenter)
    w.setGeometry(100,100,200,50)
    b.move(50,20)

    vbox = QVBoxLayout()
    vbox.addWidget(b)
    w.setLayout(vbox)
    
    w.setWindowTitle('PyQt')
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()