# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildForm2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChildForm2(object):
    def setupUi(self, ChildForm2):
        ChildForm2.setObjectName("ChildForm2")
        ChildForm2.resize(618, 494)
        self.textEdit = QtWidgets.QTextEdit(ChildForm2)
        self.textEdit.setGeometry(QtCore.QRect(110, 70, 421, 371))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildForm2)
        QtCore.QMetaObject.connectSlotsByName(ChildForm2)

    def retranslateUi(self, ChildForm2):
        _translate = QtCore.QCoreApplication.translate
        ChildForm2.setWindowTitle(_translate("ChildForm2", "Form"))
        self.textEdit.setHtml(_translate("ChildForm2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">我是子窗口的内容</p></body></html>"))