import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QPushButton, QLineEdit
from PyQt5 import uic

class Dialog_window(QDialog):
    def __init__(self):
        super(Dialog_window, self).__init__()

        uic.loadUi("inputUI.ui", self)

        self.input_browse_button.clicked.connect(self.Input_Browse_Clicked)
        self.output_browse_button.clicked.connect(self.Output_Browse_Clicked)
        self.OK_button.accepted.connect(self.OK_Accepted)
        self.OK_button.rejected.connect(self.OK_Rejected)

    def Input_Browse_Clicked(self):
        print("Input directory here")
        self.input_path = QFileDialog.getExistingDirectory(self, "Open Folder", os.path.expanduser("~"),
                QFileDialog.ShowDirsOnly)
        self.input_dir_path.setText(self.input_path)

    def Output_Browse_Clicked(self):
        print("Output directory here")
        self.output_path = QFileDialog.getExistingDirectory(self, "Open Folder", os.path.expanduser("~"),
                QFileDialog.ShowDirsOnly)
        self.output_dir_path.setText(self.output_path)

    def OK_Accepted(self):
        scale_value = self.scale_value.text()
        print(scale_value)
        if int(scale_value) in range(0,100):
            print("scale value valid")
            os.system("python ImageResize.py -i {} -o {} -s {}".format(self.input_path, self.output_path, scale_value))
        else:
            print("use default scale")
            os.system("python ImageResize.py -i {} -o {}".format(self.input_path, self.output_path))

    def OK_Rejected(self):
        self.close()

if __name__=="__main__":
    app = QApplication(sys.argv)
    Dialog = Dialog_window()
    Dialog.show()
    sys.exit(app.exec_())
