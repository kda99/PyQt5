from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Tibetan Machine Uni")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(175, 175, 175);")
        self.label.setObjectName("label")
        self.label.setMargin(20)
        self.btn_zero = QtWidgets.QPushButton(self.centralwidget)
        self.btn_zero.setGeometry(QtCore.QRect(0, 400, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_zero.setFont(font)
        self.btn_zero.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_zero.setObjectName("btn_zero")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(100, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(200, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_9.setObjectName("btn_9")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(300, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_div = QtWidgets.QPushButton(self.centralwidget)
        self.btn_div.setGeometry(QtCore.QRect(300, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.btn_div.setFont(font)
        self.btn_div.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_div.setObjectName("btn_div")
        self.btn_sub = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sub.setGeometry(QtCore.QRect(300, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.btn_sub.setFont(font)
        self.btn_sub.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_sub.setObjectName("btn_sub")
        self.btn_mult = QtWidgets.QPushButton(self.centralwidget)
        self.btn_mult.setGeometry(QtCore.QRect(300, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.btn_mult.setFont(font)
        self.btn_mult.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_mult.setObjectName("btn_mult")
        self.btn_equal = QtWidgets.QPushButton(self.centralwidget)
        self.btn_equal.setGeometry(QtCore.QRect(150, 400, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(45)
        self.btn_equal.setFont(font)
        self.btn_equal.setStyleSheet("background-color: rgb(222, 255, 243);")
        self.btn_equal.setObjectName("btn_equal")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_function()  # добавляет обработчики кнопок
        self.flag_equal = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "         0"))
        self.btn_zero.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_mult.setText(_translate("MainWindow", "*"))
        self.btn_equal.setText(_translate("MainWindow", "="))

    def add_function(self):
        self.btn_zero.clicked.connect(lambda: self.write_number(
            self.btn_zero.text()))  # по нажатию кнопки вызывается обработчик write_number, которому передается текст на нажимаемой кнопке
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_sub.clicked.connect(lambda: self.write_number(self.btn_sub.text()))
        self.btn_mult.clicked.connect(lambda: self.write_number(self.btn_mult.text()))
        self.btn_div.clicked.connect(lambda: self.write_number(self.btn_div.text()))
        self.btn_equal.clicked.connect(self.results)

    def write_number(self, item):  # добавление текста в виджет вывода информации по обработчику кнопок
        if self.label.text() == "         0" or self.flag_equal:
            self.label.setText(item)
            self.flag_equal = False
        else:
            self.label.setText(self.label.text() + item)

    def results(self):  # вычисление результата выражения
        if not self.flag_equal:
            res = eval(self.label.text())
            self.label.setText('Результат: ' + str(res))
            self.flag_equal = True
        else:
            error = QMessageBox()  # создание всплывающего окна
            error.setWindowTitle('Ошибка')  # текст заголовка всплывающего окна
            error.setText('Сейчас это действие выполнить нельзя')  # текст всплывающего окна
            error.setIcon(QMessageBox.Warning)  # иконка всплывающего окна
            error.setStandardButtons(
                QMessageBox.Reset | QMessageBox.Ok | QMessageBox.Cancel)  # установка кнопок всплывающего окна
            error.setDefaultButton(QMessageBox.Ok)  # установка кнопки всплывающего окна, которая будет подсвечиваться
            error.setInformativeText('Два раза действие не выполнить')  # доп. текст под error.setText
            error.setDetailedText('Детали причины вызова окна')  # доп. кнопка
            error.buttonClicked.connect(self.popup_action)  # вызов обработчика при нажатии любой кнопки вспл. окна

            error.exec_()

    def popup_action(self, btn):  # обработка кнопок всплывающего окна
        if btn.text() == 'Ok':
            print('Print Ok')
        elif btn.text() == 'Reset':
            self.label.setText('')
            self.flag_equal = False


import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
