from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import subprocess

import Stor3d_ui


class Stored(QMainWindow, Stor3d_ui.Ui_MainWindow):

    filecounter = 1;

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

        self.renderDimensions.clicked.connect(self.submit_dimensions)
        self.generateSTLFile.clicked.connect(self.generate_stlfile)

    def write_dimensions(self):
        file = open('dimensions.txt', 'w')
        file.write('x=' + self.boxLength.text() + '\n')
        file.write('y=' + self.boxWidth.text() + '\n')
        file.write('z=' + self.boxHeight.text() + '\n')
        file.write('fileIteration=' + str(self.filecounter) + '\n')
        file.close()

    def write_readytoprint(self, print_status):
        file = open('readytoprint.txt', 'w')
        file.write(str(print_status))
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
        print(dimensions[3])
        thickness = self.calculate_thickness(float(dimensions[0]), float(dimensions[1]), float(dimensions[2]))
        print(thickness)

    def calculate_thickness(self, x, y, z):
        return ((x * 0.05) + (y * 0.05) + (z * 0.05)) / 3

    def submit_dimensions(self):
        self.write_dimensions()
        self.write_readytoprint(False)
        # self.read_dimensions()

        args = ['C:\\Program Files\\Blender Foundation\\Blender\\blender.exe',
                '--background', '--python',
                'C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\BoxScript.py']
        subprocess.Popen(args)
        self.generateSTLFile.setEnabled(True)

        self.render_pic()

    def render_pic(self):
        QThread.sleep(1)
        pixmap = QPixmap('C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\insert.png')
        finalPixmap = pixmap.scaled(512, 288, Qt.KeepAspectRatio)
        self.insert_picture.setPixmap(finalPixmap)

    def generate_stlfile(self):
        self.write_readytoprint(True)

        args = ['C:\\Program Files\\Blender Foundation\\Blender\\blender.exe',
                '--background', '--python',
                'C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\BoxScript.py']
        subprocess.Popen(args)

        self.filecounter += 1

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
            self.renderDimensions.setEnabled(True)
        else:
            self.renderDimensions.setEnabled(False)


app = QApplication(sys.argv)
stored = Stored()
stored.show()
app.exec_()
