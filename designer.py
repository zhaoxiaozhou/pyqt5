# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo1.1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(506, 398)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_label = QtWidgets.QLabel(Form)
        self.edit_label.setObjectName("edit_label")
        self.gridLayout.addWidget(self.edit_label, 0, 0, 1, 1)
        self.brower_label = QtWidgets.QLabel(Form)
        self.brower_label.setObjectName("brower_label")
        self.gridLayout.addWidget(self.brower_label, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.edit_label.setText(_translate("Form", "QTextLabel"))
        self.brower_label.setText(_translate("Form", "QTextBrowser"))
