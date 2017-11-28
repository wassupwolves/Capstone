# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Stor3d2.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 440)
        MainWindow.setMinimumSize(QtCore.QSize(560, 440))
        MainWindow.setMaximumSize(QtCore.QSize(560, 440))
        MainWindow.setStyleSheet("QGroupBox{\n"
"    border: 1px solid transparent;\n"
"    border-radius: 4px;\n"
"    border-color: #1C517D;\n"
"}\n"
"\n"
"QPushButton{\n"
"    font-size: 12px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 4px;\n"
"    color: #eee;\n"
"    background-color: #428BCA;\n"
"    border-color: #1C517D;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #eee;\n"
"    background-color: #1C517D;\n"
"    border-color: #428BCA;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    color: #000;\n"
"    background-color: #eee;\n"
"    border-color: #1C517D;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    border: 1px solid #1C517D;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #bbb;\n"
"    background: white;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1, stop: 0 #428BCA, stop: 1 #84AED3);\n"
"    background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, stop: 0 #84AED3, stop: 1 #428BCA);\n"
"    border: 1px solid #1C517D;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #fff;\n"
"    border: 1px solid #1C517D;\n"
"    height: 10px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
"    border: 1px solid #1C517D;\n"
"    width: 13px;\n"
"    margin-top: -2px;\n"
"    margin-bottom: -2px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #fff, stop:1 #ddd);\n"
"    border: 1px solid #1C517D;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"    background: #bbb;\n"
"    border-color: #1C517D;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"    background: #eee;\n"
"    border-color: #1C517D;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"    background: #eee;\n"
"    border: 1px solid #1C517D;\n"
"    border-radius: 4px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainBox = QtWidgets.QGroupBox(self.centralwidget)
        self.mainBox.setGeometry(QtCore.QRect(10, 10, 540, 400))
        self.mainBox.setMinimumSize(QtCore.QSize(540, 400))
        self.mainBox.setMaximumSize(QtCore.QSize(540, 400))
        self.mainBox.setStyleSheet("QGroupBox{\n"
"    background-color: #428BCA ;\n"
"}\n"
"")
        self.mainBox.setObjectName("mainBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.mainBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.mainBox)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"    color: #eee;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupbox = QtWidgets.QGroupBox(self.mainBox)
        self.groupbox.setStyleSheet("background-color: #eee;")
        self.groupbox.setObjectName("groupbox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupbox)
        self.gridLayout.setObjectName("gridLayout")
        self.boxLength = QtWidgets.QLineEdit(self.groupbox)
        self.boxLength.setAlignment(QtCore.Qt.AlignCenter)
        self.boxLength.setObjectName("boxLength")
        self.gridLayout.addWidget(self.boxLength, 0, 0, 1, 1)
        self.boxWidth = QtWidgets.QLineEdit(self.groupbox)
        self.boxWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.boxWidth.setObjectName("boxWidth")
        self.gridLayout.addWidget(self.boxWidth, 1, 0, 1, 1)
        self.widthLabel = QtWidgets.QLabel(self.groupbox)
        self.widthLabel.setMaximumSize(QtCore.QSize(16777215, 25))
        self.widthLabel.setObjectName("widthLabel")
        self.gridLayout.addWidget(self.widthLabel, 1, 1, 1, 1)
        self.boxHeight = QtWidgets.QLineEdit(self.groupbox)
        self.boxHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.boxHeight.setObjectName("boxHeight")
        self.gridLayout.addWidget(self.boxHeight, 2, 0, 1, 1)
        self.heightLabel = QtWidgets.QLabel(self.groupbox)
        self.heightLabel.setObjectName("heightLabel")
        self.gridLayout.addWidget(self.heightLabel, 2, 1, 1, 1)
        self.lengthLabel = QtWidgets.QLabel(self.groupbox)
        self.lengthLabel.setObjectName("lengthLabel")
        self.gridLayout.addWidget(self.lengthLabel, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupbox)
        self.groupbox1 = QtWidgets.QGroupBox(self.mainBox)
        self.groupbox1.setStyleSheet("background-color: #eee;")
        self.groupbox1.setObjectName("groupbox1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupbox1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slottedCheckBox = QtWidgets.QCheckBox(self.groupbox1)
        self.slottedCheckBox.setEnabled(False)
        self.slottedCheckBox.setObjectName("slottedCheckBox")
        self.horizontalLayout.addWidget(self.slottedCheckBox)
        self.gridLength = QtWidgets.QLabel(self.groupbox1)
        self.gridLength.setEnabled(False)
        self.gridLength.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridLength.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLength.setObjectName("gridLength")
        self.horizontalLayout.addWidget(self.gridLength)
        self.gridX = QtWidgets.QLabel(self.groupbox1)
        self.gridX.setEnabled(False)
        self.gridX.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.gridX.setAlignment(QtCore.Qt.AlignCenter)
        self.gridX.setObjectName("gridX")
        self.horizontalLayout.addWidget(self.gridX)
        self.gridWidth = QtWidgets.QLabel(self.groupbox1)
        self.gridWidth.setEnabled(False)
        self.gridWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.gridWidth.setObjectName("gridWidth")
        self.horizontalLayout.addWidget(self.gridWidth)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.lengthCellSlider = QtWidgets.QSlider(self.groupbox1)
        self.lengthCellSlider.setEnabled(False)
        self.lengthCellSlider.setMinimum(1)
        self.lengthCellSlider.setMaximum(10)
        self.lengthCellSlider.setProperty("value", 1)
        self.lengthCellSlider.setOrientation(QtCore.Qt.Horizontal)
        self.lengthCellSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.lengthCellSlider.setTickInterval(1)
        self.lengthCellSlider.setObjectName("lengthCellSlider")
        self.verticalLayout.addWidget(self.lengthCellSlider)
        self.widthCellSlider = QtWidgets.QSlider(self.groupbox1)
        self.widthCellSlider.setEnabled(False)
        self.widthCellSlider.setMinimum(1)
        self.widthCellSlider.setMaximum(10)
        self.widthCellSlider.setOrientation(QtCore.Qt.Horizontal)
        self.widthCellSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.widthCellSlider.setTickInterval(1)
        self.widthCellSlider.setObjectName("widthCellSlider")
        self.verticalLayout.addWidget(self.widthCellSlider)
        self.lidCheckBox = QtWidgets.QCheckBox(self.groupbox1)
        self.lidCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lidCheckBox.setObjectName("lidCheckBox")
        self.verticalLayout.addWidget(self.lidCheckBox)
        self.verticalLayout_3.addWidget(self.groupbox1)
        self.groupbox2 = QtWidgets.QGroupBox(self.mainBox)
        self.groupbox2.setStyleSheet("QGroupBox{\n"
"    background-color: #eee;\n"
"}\n"
"")
        self.groupbox2.setObjectName("groupbox2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupbox2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.renderDimensions = QtWidgets.QPushButton(self.groupbox2)
        self.renderDimensions.setEnabled(False)
        self.renderDimensions.setObjectName("renderDimensions")
        self.verticalLayout_2.addWidget(self.renderDimensions)
        self.generateSTLFile = QtWidgets.QPushButton(self.groupbox2)
        self.generateSTLFile.setEnabled(False)
        self.generateSTLFile.setObjectName("generateSTLFile")
        self.verticalLayout_2.addWidget(self.generateSTLFile)
        self.verticalLayout_3.addWidget(self.groupbox2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.insert_picture = QtWidgets.QLabel(self.mainBox)
        self.insert_picture.setMinimumSize(QtCore.QSize(375, 375))
        self.insert_picture.setStyleSheet("QLabel{\n"
"    color: #eee;\n"
"}")
        self.insert_picture.setAlignment(QtCore.Qt.AlignCenter)
        self.insert_picture.setObjectName("insert_picture")
        self.horizontalLayout_2.addWidget(self.insert_picture)
        self.boxHeight.raise_()
        self.boxWidth.raise_()
        self.heightLabel.raise_()
        self.boxLength.raise_()
        self.widthLabel.raise_()
        self.lengthLabel.raise_()
        self.lengthLabel.raise_()
        self.gridX.raise_()
        self.slottedCheckBox.raise_()
        self.gridWidth.raise_()
        self.gridLength.raise_()
        self.lidCheckBox.raise_()
        self.lengthCellSlider.raise_()
        self.widthCellSlider.raise_()
        self.slottedCheckBox.raise_()
        self.generateSTLFile.raise_()
        self.renderDimensions.raise_()
        self.label.raise_()
        self.insert_picture.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stor3D"))
        self.label.setText(_translate("MainWindow", "Objects with dimensions bigger than \"23\" in any category may render darker than usual"))
        self.boxLength.setPlaceholderText(_translate("MainWindow", "Length"))
        self.boxWidth.setPlaceholderText(_translate("MainWindow", "Width"))
        self.widthLabel.setText(_translate("MainWindow", "Inches"))
        self.boxHeight.setPlaceholderText(_translate("MainWindow", "Height"))
        self.heightLabel.setText(_translate("MainWindow", "Inches"))
        self.lengthLabel.setText(_translate("MainWindow", "Inches"))
        self.slottedCheckBox.setText(_translate("MainWindow", "Cells?"))
        self.gridLength.setText(_translate("MainWindow", "1"))
        self.gridX.setText(_translate("MainWindow", "x"))
        self.gridWidth.setText(_translate("MainWindow", "1"))
        self.lidCheckBox.setText(_translate("MainWindow", "Lid?"))
        self.renderDimensions.setText(_translate("MainWindow", "Render Dimensions"))
        self.generateSTLFile.setText(_translate("MainWindow", "Generate 3D File"))
        self.insert_picture.setText(_translate("MainWindow", "Click \"Render Dimensions\" Button to Display Box Here..."))

