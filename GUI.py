import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QTextEdit, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5 import uic

from resizeUI import Dialog_window

class Main_Window(QMainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()

        uic.loadUi('GUI.ui', self)

        self.setWindowTitle("COVID-19 Diagnosis")
        self.setFixedSize(600,400)

        self.resize_button.clicked.connect(self.Resize_Button_Clicked)
        self.train_button.clicked.connect(self.Train_Button_Clicked)
        self.start_button.clicked.connect(self.Start_Button_Clicked)
        
    def Resize_Button_Clicked(self):
        Dialog = QDialog()
        
        print("start button clicked")

    def Train_Button_Clicked(self):
        print("start button clicked")
    
    def Start_Button_Clicked(self):
        print("start button clicked")


if __name__=="__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    Window = Main_Window()
    Window.show()
    sys.exit(app.exec_())
