# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PLCStBXCB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(0, 0, 800, 500))
        self.btn_Open = QPushButton(self.centralwidget)
        self.btn_Open.setObjectName(u"btn_Open")
        self.btn_Open.setGeometry(QRect(5, 510, 185, 80))
        font = QFont()
        font.setPointSize(20)
        self.btn_Open.setFont(font)
        self.btn_Save = QPushButton(self.centralwidget)
        self.btn_Save.setObjectName(u"btn_Save")
        self.btn_Save.setGeometry(QRect(205, 510, 185, 80))
        self.btn_Save.setFont(font)
        self.btn_Make = QPushButton(self.centralwidget)
        self.btn_Make.setObjectName(u"btn_Make")
        self.btn_Make.setGeometry(QRect(405, 510, 185, 80))
        self.btn_Make.setFont(font)
        self.btn_BackUp = QPushButton(self.centralwidget)
        self.btn_BackUp.setObjectName(u"btn_BackUp")
        self.btn_BackUp.setGeometry(QRect(605, 510, 185, 80))
        self.btn_BackUp.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0430", None))
        self.btn_Open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.btn_Save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btn_Make.setText(QCoreApplication.translate("MainWindow", u"Make", None))
        self.btn_BackUp.setText(QCoreApplication.translate("MainWindow", u"BackUp", None))
    # retranslateUi

