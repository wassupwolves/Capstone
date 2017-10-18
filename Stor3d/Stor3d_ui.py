# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Stor3d.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(294, 194)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.boxLength = QtWidgets.QLineEdit(self.centralwidget)
        self.boxLength.setAlignment(QtCore.Qt.AlignCenter)
        self.boxLength.setObjectName("boxLength")
        self.verticalLayout_2.addWidget(self.boxLength)
        self.boxWidth = QtWidgets.QLineEdit(self.centralwidget)
        self.boxWidth.setAlignment(QtCore.Qt.AlignCenter)
        self.boxWidth.setObjectName("boxWidth")
        self.verticalLayout_2.addWidget(self.boxWidth)
        self.boxHeight = QtWidgets.QLineEdit(self.centralwidget)
        self.boxHeight.setAlignment(QtCore.Qt.AlignCenter)
        self.boxHeight.setObjectName("boxHeight")
        self.verticalLayout_2.addWidget(self.boxHeight)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.lengthLabel.setObjectName("lengthLabel")
        self.verticalLayout.addWidget(self.lengthLabel)
        self.widthLabel = QtWidgets.QLabel(self.centralwidget)
        self.widthLabel.setObjectName("widthLabel")
        self.verticalLayout.addWidget(self.widthLabel)
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setObjectName("heightLabel")
        self.verticalLayout.addWidget(self.heightLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.submitBoxDimensions = QtWidgets.QPushButton(self.centralwidget)
        self.submitBoxDimensions.setEnabled(False)
        self.submitBoxDimensions.setObjectName("submitBoxDimensions")
        self.verticalLayout_3.addWidget(self.submitBoxDimensions)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "STOR3D"))
        self.boxLength.setPlaceholderText(_translate("MainWindow", "Length"))
        self.boxWidth.setPlaceholderText(_translate("MainWindow", "Width"))
        self.boxHeight.setPlaceholderText(_translate("MainWindow", "Height"))
        self.lengthLabel.setText(_translate("MainWindow", "Inches (L)"))
        self.widthLabel.setText(_translate("MainWindow", "Inches (W)"))
        self.heightLabel.setText(_translate("MainWindow", "Inches (H)"))
        self.submitBoxDimensions.setText(_translate("MainWindow", "Submit Box Dimensions"))

