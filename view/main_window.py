# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1176, 967)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("#tab_2 QPushButton{\n"
"    margin: 5px;\n"
"    border-radius: 10px;\n"
"    height:60;\n"
"    background-color: rgb(225, 225, 225);\n"
"}\n"
"#tab_2 QPushButton:hover{\n"
"    \n"
"    background-color: rgb(218, 218, 218);\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(128, 177, 198);\n"
"    border-radius:30px\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.logo = QtWidgets.QLabel(self.frame_2)
        self.logo.setMinimumSize(QtCore.QSize(41, 41))
        self.logo.setStyleSheet("image: url(:/images/scut2.png);\n"
"")
        self.logo.setText("")
        self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.horizontalLayout_11.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.frame_2)
        self.title.setMinimumSize(QtCore.QSize(221, 21))
        self.title.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"华文行楷\";\n"
"")
        self.title.setObjectName("title")
        self.horizontalLayout_11.addWidget(self.title)
        spacerItem = QtWidgets.QSpacerItem(218, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(81, 41))
        self.frame_4.setStyleSheet("QPushBotton{\n"
"    border:none;\n"
"}\n"
"QPushBotton:hover{\n"
"    padding-bottom:5px;\n"
"}\n"
"")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_11.addWidget(self.frame_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.tabWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget.setStyleSheet("::tab{\n"
"    width: 120;\n"
"    height:50;\n"
"    background-color: rgb(128, 177, 198,100);\n"
"    border-right: 1px solid  rgb(200, 200, 200);\n"
"    font-size:20px;\n"
"}\n"
"::tab:last {\n"
"    border:none;\n"
"}\n"
"::tab:hover {\n"
"    background-color: rgb(128, 177, 198,150);\n"
"}\n"
"::tab:selected {\n"
"    background-color: rgb(128, 177, 198);\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.first_page = QtWidgets.QWidget()
        self.first_page.setObjectName("first_page")
        self.tabWidget.addTab(self.first_page, "")
        self.test = QtWidgets.QWidget()
        self.test.setObjectName("test")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.test)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_question = QtWidgets.QLabel(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_question.sizePolicy().hasHeightForWidth())
        self.label_question.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_question.setFont(font)
        self.label_question.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_question.setStyleSheet("background-color: rgba(172, 197, 224,100);\n"
"border-radius:0;")
        self.label_question.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_question.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_question.setLineWidth(0)
        self.label_question.setMidLineWidth(0)
        self.label_question.setTextFormat(QtCore.Qt.AutoText)
        self.label_question.setScaledContents(False)
        self.label_question.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_question.setWordWrap(True)
        self.label_question.setIndent(-1)
        self.label_question.setOpenExternalLinks(False)
        self.label_question.setObjectName("label_question")
        self.verticalLayout_2.addWidget(self.label_question)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(18)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.answer_1 = QtWidgets.QPushButton(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_1.sizePolicy().hasHeightForWidth())
        self.answer_1.setSizePolicy(sizePolicy)
        self.answer_1.setMinimumSize(QtCore.QSize(0, 0))
        self.answer_1.setSizeIncrement(QtCore.QSize(0, 0))
        self.answer_1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_1.setFont(font)
        self.answer_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_1.setIconSize(QtCore.QSize(20, 20))
        self.answer_1.setObjectName("answer_1")
        self.verticalLayout_3.addWidget(self.answer_1, 0, QtCore.Qt.AlignHCenter)
        self.answer_2 = QtWidgets.QPushButton(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_2.sizePolicy().hasHeightForWidth())
        self.answer_2.setSizePolicy(sizePolicy)
        self.answer_2.setMinimumSize(QtCore.QSize(0, 0))
        self.answer_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.answer_2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_2.setFont(font)
        self.answer_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_2.setIconSize(QtCore.QSize(20, 20))
        self.answer_2.setObjectName("answer_2")
        self.verticalLayout_3.addWidget(self.answer_2, 0, QtCore.Qt.AlignHCenter)
        self.answer_3 = QtWidgets.QPushButton(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_3.sizePolicy().hasHeightForWidth())
        self.answer_3.setSizePolicy(sizePolicy)
        self.answer_3.setMinimumSize(QtCore.QSize(0, 0))
        self.answer_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.answer_3.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_3.setFont(font)
        self.answer_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_3.setIconSize(QtCore.QSize(20, 20))
        self.answer_3.setObjectName("answer_3")
        self.verticalLayout_3.addWidget(self.answer_3, 0, QtCore.Qt.AlignHCenter)
        self.answer_4 = QtWidgets.QPushButton(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_4.sizePolicy().hasHeightForWidth())
        self.answer_4.setSizePolicy(sizePolicy)
        self.answer_4.setMinimumSize(QtCore.QSize(0, 0))
        self.answer_4.setSizeIncrement(QtCore.QSize(0, 0))
        self.answer_4.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_4.setFont(font)
        self.answer_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.answer_4.setIconSize(QtCore.QSize(20, 20))
        self.answer_4.setObjectName("answer_4")
        self.verticalLayout_3.addWidget(self.answer_4, 0, QtCore.Qt.AlignHCenter)
        self.button_next = QtWidgets.QPushButton(self.test)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_next.sizePolicy().hasHeightForWidth())
        self.button_next.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button_next.setFont(font)
        self.button_next.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_next.setObjectName("button_next")
        self.verticalLayout_3.addWidget(self.button_next, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.tabWidget.addTab(self.test, "")
        self.select = QtWidgets.QWidget()
        self.select.setObjectName("select")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.select)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeWidget = QtWidgets.QTreeWidget(self.select)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.setFont(font)
        self.treeWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.treeWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.treeWidget.setStyleSheet("background-color: transparent;\n"
"border: none;\n"
"\n"
"\n"
"")
        self.treeWidget.setLineWidth(1)
        self.treeWidget.setMidLineWidth(0)
        self.treeWidget.setAutoScrollMargin(16)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(0, font)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.treeWidget.headerItem().setFont(1, font)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(315)
        self.treeWidget.header().setMinimumSectionSize(37)
        self.verticalLayout_5.addWidget(self.treeWidget)
        self.tabWidget.addTab(self.select, "")
        self.mine = QtWidgets.QWidget()
        self.mine.setStyleSheet("")
        self.mine.setObjectName("mine")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.mine)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label = QtWidgets.QLabel(self.mine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 198))
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setStyleSheet("image: url(:/icons/user.png);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        self.verticalLayout_6.addWidget(self.label)
        self.label_id = QtWidgets.QLabel(self.mine)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label_id.setFont(font)
        self.label_id.setScaledContents(False)
        self.label_id.setAlignment(QtCore.Qt.AlignCenter)
        self.label_id.setObjectName("label_id")
        self.verticalLayout_6.addWidget(self.label_id)
        self.frame_5 = QtWidgets.QFrame(self.mine)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_time = QtWidgets.QLabel(self.frame_5)
        self.label_time.setGeometry(QtCore.QRect(0, -50, 803, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("")
        self.label_time.setObjectName("label_time")
        self.verticalLayout_6.addWidget(self.frame_5)
        self.button_view = QtWidgets.QPushButton(self.mine)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_view.sizePolicy().hasHeightForWidth())
        self.button_view.setSizePolicy(sizePolicy)
        self.button_view.setObjectName("button_view")
        self.verticalLayout_6.addWidget(self.button_view)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 3)
        self.verticalLayout_6.setStretch(3, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.tabWidget.addTab(self.mine, "")
        self.horizontalLayout_4.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.frame_3)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1176, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "化工实验模拟系统"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.first_page), _translate("MainWindow", "首页"))
        self.label_question.setText(_translate("MainWindow", "TextLabel"))
        self.answer_1.setText(_translate("MainWindow", "PushButton"))
        self.answer_2.setText(_translate("MainWindow", "PushButton"))
        self.answer_3.setText(_translate("MainWindow", "PushButton"))
        self.answer_4.setText(_translate("MainWindow", "PushButton"))
        self.button_next.setText(_translate("MainWindow", "下一题"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test), _translate("MainWindow", "实验安全"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "实验名称"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "学习时长"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "实验一  雷诺实验"))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "实验二  机械能转化实验"))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "实验三  流体阻力的测定"))
        self.treeWidget.topLevelItem(2).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "实验四  离心泵性能的测定"))
        self.treeWidget.topLevelItem(3).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "实验五  恒压过滤实验"))
        self.treeWidget.topLevelItem(4).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "实验六  综合传热实验"))
        self.treeWidget.topLevelItem(5).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "实验七  精馏实验"))
        self.treeWidget.topLevelItem(6).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "实验八  CO2吸收-解吸实验"))
        self.treeWidget.topLevelItem(7).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "实验九  洞道干燥实验"))
        self.treeWidget.topLevelItem(8).setText(1, _translate("MainWindow", "-"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.select), _translate("MainWindow", "实验选择"))
        self.label_id.setText(_translate("MainWindow", "显示用户账号"))
        self.label_time.setText(_translate("MainWindow", "学习总时长："))
        self.button_view.setText(_translate("MainWindow", "查看“实验安全”测验结果"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mine), _translate("MainWindow", "我的"))
import res_rc
