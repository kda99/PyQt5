from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 800, 500))
        self.textEdit.setObjectName("textEdit")
        self.btn_Open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Open.setGeometry(QtCore.QRect(5, 510, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Open.setFont(font)
        self.btn_Open.setObjectName("btn_Open")
        self.btn_Save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Save.setGeometry(QtCore.QRect(205, 510, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Save.setFont(font)
        self.btn_Save.setObjectName("btn_Save")
        self.btn_Make = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Make.setGeometry(QtCore.QRect(405, 510, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Make.setFont(font)
        self.btn_Make.setObjectName("btn_Make")
        self.btn_BackUp = QtWidgets.QPushButton(self.centralwidget)
        self.btn_BackUp.setGeometry(QtCore.QRect(605, 510, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_BackUp.setFont(font)
        self.btn_BackUp.setObjectName("btn_BackUp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_function()
        self.file_name = ''


    #
    def btn_function(self):
        self.btn_Open.clicked.connect(lambda: self.open_function())
        self.btn_Save.clicked.connect(lambda: self.save_function())
        self.btn_Make.clicked.connect(lambda: self.make_function())
        self.btn_BackUp.clicked.connect(lambda: self.backup_function())

    def open_function(self):  # диалог открытия файла
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()[0]
        try:
            file_content = open(self.file_name, 'r')
            with file_content:
                line = file_content.read()
                self.textEdit.setText(line)
            file_content.close()
        except:
            pass

    def save_function(self):  # диалог сохраниения файла
        save_name_file = QtWidgets.QFileDialog.getSaveFileName()[0]
        try:
            file_content = open(save_name_file, 'w')
            text = self.textEdit.toPlainText()
            file_content.write(text)
            file_content.close()
        except:
            pass

    def backup_function(self):  # резервное копирование файла в .old
        try:
            # file_content = open(str(self.file_name) + '/old/.old', 'w')
            self.create_old_dir(self.file_name)
            file_content = open(self.file_path_former(self.file_name), 'w')
            text = self.textEdit.toPlainText()
            file_content.write(text)
            file_content.close()
        except:
            pass

    def create_old_dir(self, path: str):
        d = path[0:path.rfind(f'/'):] + '/old/'
        if not os.path.exists(d):
            os.mkdir(d)

    def file_path_former(self, path: str):
        left = path[0:path.rfind(f'/'):]
        right = '/old' + path[path.rfind(f'/')::] + '.old'
        print(left + right)
        return left + right

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа"))
        self.btn_Open.setText(_translate("MainWindow", "Open"))
        self.btn_Save.setText(_translate("MainWindow", "Save"))
        self.btn_Make.setText(_translate("MainWindow", "Make"))
        self.btn_BackUp.setText(_translate("MainWindow", "BackUp"))


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
