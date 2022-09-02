# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 110, 160, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.chapter_selectors = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.chapter_selectors.setContentsMargins(0, 0, 0, 0)
        self.chapter_selectors.setObjectName("chapter_selectors")
        self.chapter_one = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_one.setObjectName("chapter_one")
        self.chapter_selectors.addWidget(self.chapter_one)
        self.chapter_two = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_two.setObjectName("chapter_two")
        self.chapter_selectors.addWidget(self.chapter_two)
        self.chapter_three = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_three.setObjectName("chapter_three")
        self.chapter_selectors.addWidget(self.chapter_three)
        self.chapter_four = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_four.setObjectName("chapter_four")
        self.chapter_selectors.addWidget(self.chapter_four)
        self.chapter_five = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_five.setObjectName("chapter_five")
        self.chapter_selectors.addWidget(self.chapter_five)
        self.chapter_six = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_six.setObjectName("chapter_six")
        self.chapter_selectors.addWidget(self.chapter_six)
        self.chapter_seven = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_seven.setObjectName("chapter_seven")
        self.chapter_selectors.addWidget(self.chapter_seven)
        self.chapter_eight = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_eight.setObjectName("chapter_eight")
        self.chapter_selectors.addWidget(self.chapter_eight)
        self.chapter_nine = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.chapter_nine.setObjectName("chapter_nine")
        self.chapter_selectors.addWidget(self.chapter_nine)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(210, 40, 581, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.experiment_principle = QtWidgets.QWidget()
        self.experiment_principle.setObjectName("experiment_principle")
        self.principle_ppt = QtWidgets.QTextBrowser(self.experiment_principle)
        self.principle_ppt.setGeometry(QtCore.QRect(60, 90, 311, 251))
        self.principle_ppt.setObjectName("principle_ppt")
        self.tabWidget.addTab(self.experiment_principle, "")
        self.experiment_steps = QtWidgets.QWidget()
        self.experiment_steps.setObjectName("experiment_steps")
        self.steps_ppt = QtWidgets.QTextBrowser(self.experiment_steps)
        self.steps_ppt.setGeometry(QtCore.QRect(90, 140, 291, 221))
        self.steps_ppt.setObjectName("steps_ppt")
        self.tabWidget.addTab(self.experiment_steps, "")
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.tabWidget.addTab(self.test, "")
        self.data_processing = QtWidgets.QWidget()
        self.data_processing.setObjectName("data_processing")
        self.tabWidget.addTab(self.data_processing, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.chapter_one.setText(_translate("mainWindow", "第一章"))
        self.chapter_two.setText(_translate("mainWindow", "第二章"))
        self.chapter_three.setText(_translate("mainWindow", "第三章"))
        self.chapter_four.setText(_translate("mainWindow", "第四章"))
        self.chapter_five.setText(_translate("mainWindow", "第五章"))
        self.chapter_six.setText(_translate("mainWindow", "第六章"))
        self.chapter_seven.setText(_translate("mainWindow", "第七章"))
        self.chapter_eight.setText(_translate("mainWindow", "第八章"))
        self.chapter_nine.setText(_translate("mainWindow", "第九章"))
        self.principle_ppt.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示实验原理的ppt</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.experiment_principle), _translate("mainWindow", "实验原理"))
        self.steps_ppt.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">显示实验步骤的ppt</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.experiment_steps), _translate("mainWindow", "实验步骤"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test), _translate("mainWindow", "测试"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_processing), _translate("mainWindow", "数据处理"))