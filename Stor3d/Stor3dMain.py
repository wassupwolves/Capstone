from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import subprocess

import Stor3d_ui


class Stored(QMainWindow, Stor3d_ui.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        validator = QDoubleValidator()

        self.boxLength.setValidator(validator)
        self.boxWidth.setValidator(validator)
        self.boxHeight.setValidator(validator)

        self.boxLength.textChanged.connect(self.check_state)
        self.boxHeight.textChanged.connect(self.check_state)
        self.boxWidth.textChanged.connect(self.check_state)

        self.submitBoxDimensions.clicked.connect(self.submit_dimensions)

    def write_dimensions(self):
        file = open('dimensions.txt', 'w')
        file.write('x=' + self.boxLength.text() + '\n')
        file.write('y=' + self.boxWidth.text() + '\n')
        file.write('z=' + self.boxHeight.text() + '\n')
        file.close()

    def read_dimensions(self):
        dimensions = []
        file = open('dimensions.txt', 'r')
        for line in file:
            dimensions += line.strip().split('=')[1:]
        print(dimensions)
        print(dimensions[0])
        print(dimensions[1])
        print(dimensions[2])
        thickness = self.calculate_thickness(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))
        print(thickness)

    def calculate_thickness(self, x, y, z):
        return ((x * 0.05) + (y * 0.05) + (z * 0.05)) / 3

    def submit_dimensions(self):
        self.write_dimensions()
        self.read_dimensions()

        args = ['C:\\Program Files\\Blender Foundation\\Blender\\blender.exe',
                '--python',
                'C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\BoxScript.py']
        # print(self.dimensions)
        subprocess.Popen(args)

    def check_state(self):
        sender = self.sender()
        validator = sender.validator()
        state = validator.validate(sender.text(), 0)[0]
        if state == QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        sender.setStyleSheet('QLineEdit { background-color: %s }' % color)

        validator = self.boxLength.validator()
        lengthState = validator.validate(self.boxLength.text(), 0)[0]

        validator = self.boxWidth.validator()
        widthState = validator.validate(self.boxWidth.text(), 0)[0]

        validator = self.boxHeight.validator()
        heightState = validator.validate(self.boxHeight.text(), 0)[0]

        if lengthState == QValidator.Acceptable and widthState == QValidator.Acceptable and heightState == QValidator.Acceptable:
            self.submitBoxDimensions.setEnabled(True)
        else:
            self.submitBoxDimensions.setEnabled(False)


app = QApplication(sys.argv)
stored = Stored()
stored.show()
app.exec_()
