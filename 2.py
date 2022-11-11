from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Простая программа')  # настройка гл. окна - заголовок
        self.setGeometry(300, 200, 350, 250)  # настройка гл. окна - отступ от левого верхнего края, ширина и высота

        self.new_text = QtWidgets.QLabel(self)   # создание текстовой надписи (пустая) для обработки в add_label

        self.main_text = QtWidgets.QLabel(self)  # создание текстовой надписи
        self.main_text.setText('Это базовая надпись')  # настройка текстовой надписи - текст
        self.main_text.move(115, 100)  # настройка текстовой надписи - отступ от левого верхнего края гл. окна
        self.main_text.adjustSize()  # настройка текстовой надписи - подстройка ширины объекта под его содержимое

        self.btn = QtWidgets.QPushButton(self)  # создание кнопки
        self.btn.move(80, 200)  # настройка кнопки - смещение в гл. окне
        self.btn.setText('Нажми на меня')  # настройка кнопки - надпись
        self.btn.setFixedWidth(200)  # настройка кнопки - фиксированная ширина
        self.btn.clicked.connect(self.add_label)   # настройка кнопки - по клику (clicked) вызывается метод add_label

    def add_label(self):
        self.new_text.setText('Вторая надпись')
        self.new_text.move(115, 70)
        self.new_text.adjustSize()

def application():
    app = QApplication(sys.argv) # создание приложения
    window = Window()       # создание главного окна, экз. класса Window дочернего от QMainWindow



    window.show()           # показать гл. окно
    sys.exit(app.exec_())   # обработка корректного закрытия гл. окна



application()