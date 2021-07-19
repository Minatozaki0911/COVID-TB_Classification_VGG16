import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Medical Image Classification App")
window.setFixedWidth(1000)
window.move(500,500)
window.setStyleSheet("background: #292929;")

grid = QGridLayout()

def createButton(name, leftMargin, rightMargin):
    button = QPushButton(name)
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))

window.show()
sys.exit(app.exec())
