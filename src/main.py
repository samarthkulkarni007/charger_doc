import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
def window(hello):
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
   b.setText(hello)
   w.setGeometry(0,0,1000,500)
   b.move(250,250)
   w.setWindowTitle("PyQt5")
   w.show()
   sys.exit(app.exec_())
   

window()