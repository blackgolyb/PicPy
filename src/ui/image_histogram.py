# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/blackgolyb/Documents/PyMage/ui/image_histogram.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(150, 120)
        Form.setMinimumSize(QtCore.QSize(150, 120))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.histGB = QtWidgets.QGroupBox(Form)
        self.histGB.setMinimumSize(QtCore.QSize(150, 120))
        self.histGB.setMaximumSize(QtCore.QSize(260, 120))
        self.histGB.setSizeIncrement(QtCore.QSize(0, 0))
        self.histGB.setObjectName("histGB")
        self.histogram_layout = QtWidgets.QHBoxLayout(self.histGB)
        self.histogram_layout.setContentsMargins(0, 0, 0, 0)
        self.histogram_layout.setSpacing(0)
        self.histogram_layout.setObjectName("histogram_layout")
        self.horizontalLayout.addWidget(self.histGB)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.histGB.setTitle(_translate("Form", "Histogram"))