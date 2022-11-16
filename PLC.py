from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 100)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        # self.textEdit.setGeometry(QtCore.QRect(0, 0, 800, 500))
        # self.textEdit.setObjectName("textEdit")
        self.btn_OpenFile = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenFile.setGeometry(QtCore.QRect(5, 10, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_OpenFile.setFont(font)
        self.btn_OpenFile.setObjectName("btn_OpenFile")
        self.btn_OpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_OpenFolder.setGeometry(QtCore.QRect(205, 10, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_OpenFolder.setFont(font)
        self.btn_OpenFolder.setObjectName("btn_OpenFolder")
        self.btn_Make_File = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Make_File.setGeometry(QtCore.QRect(405, 10, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Make_File.setFont(font)
        self.btn_Make_File.setObjectName("btn_Make_File")
        self.btn_Make_Folder = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Make_Folder.setGeometry(QtCore.QRect(605, 10, 185, 80))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_Make_Folder.setFont(font)
        self.btn_Make_Folder.setObjectName("btn_Make_Folder")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_function()
        self.file_name = ''
        self.folder_name = ''
        self.file_content = None

    def btn_function(self):
        self.btn_OpenFile.clicked.connect(lambda: self.open_file_function())
        self.btn_OpenFolder.clicked.connect(lambda: self.open_folder_function())
        self.btn_Make_File.clicked.connect(lambda: self.make_file_function())
        self.btn_Make_Folder.clicked.connect(lambda: self.make_folder_function())

    def open_file_function(self, path = None):  # диалог открытия файла
        self.file_name = QtWidgets.QFileDialog.getOpenFileName()[0] if path is None else path
        try:
            content = open(self.file_name, 'r')
            with content:
                self.file_content = content.read()
                # self.textEdit.setText(self.file_content)
            content.close()
        except:
            pass

    # def save_function(self):  # диалог сохраниения файла
    #     save_name_file = QtWidgets.QFileDialog.getSaveFileName()[0]
    #     try:
    #         file_content = open(save_name_file, 'w')
    #         text = self.textEdit.toPlainText()
    #         file_content.write(text)
    #         file_content.close()
    #     except:
    #         pass

    def open_folder_function(self):
        self.folder_name = QtWidgets.QFileDialog.getExistingDirectory()


    def make_file_function(self, path = None):
        path = self.file_name if path is None else path
        self.backup_function(path)
        try:
            open_file_content = open(path, 'w')
            text = self.file_content
            new_text = text.replace('fill=\"rgb(239,228,176)\" stroke-width=\"1.25\" stroke=\"rgb(0,0,0)\"',
                                    'fill=\"rgba(0,0,0,0)\" stroke-width=\"1.25\" stroke=\"rgba(0,0,0,0)\"')
            open_file_content.write(new_text)
            open_file_content.close()
        except:
            pass

    def make_folder_function(self):
        dir_list = list(filter(lambda x: x.endswith("svg"), os.listdir(self.folder_name)))
        for path_file in dir_list:
                # check_svg = i.split(".")[1]
                # if i.endswith("svg"):
            self.make_file_function(self.folder_name + "/" + path_file)
                    # full_path = self.folder_name + "\\" + i
                    # with open(full_path, "r", encoding="utf-8") as f:
                    #     old_data = f.read()
                    #     new_data = old_data.replace(
                    #         'fill=\"rgb(239,228,176)\" stroke-width=\"1.25\" stroke=\"rgb(0,0,0)\"',
                    #         'fill=\"rgba(0,0,0,0)\" stroke-width=\"1.25\" stroke=\"rgba(0,0,0,0)\"')

                    # with open(full_path, "w", encoding="utf-8") as f:
                    #     f.write(new_data)


    def backup_function(self, path = None):  # резервное копирование файла в .old
        path = self.file_name if path is None else path
        try:
            self.create_old_dir(path)
            open_file_content = open(self.file_path_former(path), 'w')
            self.open_file_function(path)
            open_file_content.write(self.file_content)
            open_file_content.close()
        except:
            pass

    def create_old_dir(self, path: str):
        d = path[0:path.rfind(f'/'):] + '/old/'
        if not os.path.exists(d):
            os.mkdir(d)

    def file_path_former(self, path: str):
        left = path[0:path.rfind(f'/'):]
        right = '/old' + path[path.rfind(f'/')::]
        return left + right

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Программа"))
        self.btn_OpenFile.setText(_translate("MainWindow", "OpenFile"))
        self.btn_OpenFolder.setText(_translate("MainWindow", "OpenFolder"))
        self.btn_Make_File.setText(_translate("MainWindow", "MakeFile"))
        self.btn_Make_Folder.setText(_translate("MainWindow", "MakeFolder"))


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
