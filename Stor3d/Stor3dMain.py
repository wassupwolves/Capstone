from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import subprocess
import os

import Stor3d_ui


class Stored(QMainWindow, Stor3d_ui.Ui_MainWindow):

    filecounter = 1;

    def __init__(self):
        self.delete_previous_iterations("C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\BlendFiles")
        self.delete_previous_iterations("C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Picture")
        self.delete_previous_iterations("C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\STLFiles")

        QMainWindow.__init__(self)
        self.setupUi(self)

        validator = QDoubleValidator()
        validator.setBottom(0)

        self.boxLength.setValidator(validator)
        self.boxWidth.setValidator(validator)
        self.boxHeight.setValidator(validator)

        self.boxLength.textChanged.connect(self.check_state)
        self.boxHeight.textChanged.connect(self.check_state)
        self.boxWidth.textChanged.connect(self.check_state)

        self.renderDimensions.clicked.connect(self.submit_dimensions)
        self.generateSTLFile.clicked.connect(self.finalize_dimensions)
        self.slottedCheckBox.clicked.connect(self.toggle_sliders)

        self.lengthCellSlider.sliderReleased.connect(self.update_lengthLabel)
        self.widthCellSlider.sliderReleased.connect(self.update_widthLabel)


    def delete_previous_iterations(self, fileDirectory):
        dirPath = fileDirectory
        fileList = os.listdir(dirPath)
        for fileName in fileList:
            os.remove(dirPath + "\\" + fileName)

    def update_lengthLabel(self):
        self.gridLength.setText(str(self.lengthCellSlider.value()))

    def update_widthLabel(self):
        self.gridWidth.setText(str(self.widthCellSlider.value()))

    def toggle_sliders(self):
        if(self.slottedCheckBox.isChecked()):
            self.lengthCellSlider.setEnabled(True)
            self.widthCellSlider.setEnabled(True)
        else:
            self.lengthCellSlider.setEnabled(False)
            self.widthCellSlider.setEnabled(False)

    def write_dimensions(self):
        file = open('dimensions.txt', 'w')
        file.write('x=' + self.boxLength.text() + '\n')
        file.write('y=' + self.boxWidth.text() + '\n')
        file.write('z=' + self.boxHeight.text() + '\n')
        file.write('fileIteration=' + str(self.filecounter) + '\n')
        file.write('lengthCellCount=' + str(self.lengthCellSlider.value()) + '\n')
        file.write('widthCellCount=' + str(self.widthCellSlider.value()) + '\n')
        file.write('lid=' + str(self.lidCheckBox.isChecked()) + '\n')
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
        return 0.07
        # return ((x * 0.025) + (y * 0.025) + (z * 0.025)) / 33 3   3

    def submit_dimensions(self):
        self.write_dimensions()
        # self.write_readytoprint(False)
        self.read_dimensions()

        # Argument array to open Blender and pass certain flags for Blender to operate with
        args = ['C:\\Program Files\\Blender Foundation\\Blender\\blender.exe',
                '--background', '--python',
                'C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\BoxScript.py']
        subprocess.Popen(args)
        if self.lidCheckBox.isChecked():
            args = ['C:\\Program Files\\Blender Foundation\\Blender\\blender.exe',
                    '--background', '--python',
                    'C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Stor3d\\LidScript.py']
            subprocess.Popen(args)

        self.generateSTLFile.setEnabled(True)

        self.render_pic()

    def render_pic(self):
        QThread.sleep(2)
        pixmap = QPixmap('C:\\Users\\Jayson\\Documents\\Quarters7-9\\9Capstone\\Picture\\BoxInsert' + str(self.filecounter) + '.png')
        # finalPixmap = pixmap.scaled(512, 288, Qt.KeepAspectRatio)
        self.insert_picture.setPixmap(pixmap)

    def finalize_dimensions(self):
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

        if len(self.boxLength.text()) != 0:
            if self.boxLength.text()[0] == '.':
                self.lengthCellSlider.setMaximum(1)
            else:
                self.lengthCellSlider.setMaximum(int(self.boxLength.text().split('.')[0]))
                self.update_lengthLabel()

        if len(self.boxWidth.text()) != 0:
            if self.boxWidth.text()[0] == '.':
                self.widthCellSlider.setMaximum(1)
            else:
                self.widthCellSlider.setMaximum(int(self.boxWidth.text().split('.')[0]))
                self.update_widthLabel()

        if len(self.boxLength.text()) != 0 and len(self.boxWidth.text()) != 0:
            self.slottedCheckBox.setEnabled(True)
        else:
            self.slottedCheckBox.setEnabled(False)


app = QApplication(sys.argv)
stored = Stored()
stored.show()
app.exec_()
