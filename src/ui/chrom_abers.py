# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/blackgolyb/Documents/PyMage/ui/chrom_abers.ui'
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
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setMinimumSize(QtCore.QSize(150, 120))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dxSb = QtWidgets.QSpinBox(self.groupBox_2)
        self.dxSb.setObjectName("dxSb")
        self.horizontalLayout_3.addWidget(self.dxSb)
        self.dySb = QtWidgets.QSpinBox(self.groupBox_2)
        self.dySb.setObjectName("dySb")
        self.horizontalLayout_3.addWidget(self.dySb)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.chromBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.chromBtn.setObjectName("chromBtn")
        self.verticalLayout_3.addWidget(self.chromBtn)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.groupBox_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Chrom abers"))
        self.chromBtn.setText(_translate("Form", "chrom. aber."))
