import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets, QtCore
import UI
from PyQt5.QtCore import QPoint, QCoreApplication
import json
import os


class UI(QtWidgets.QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # Это нужно для инициализации нашего дизайна
        self.setupUi(self)

        # убираем рамку windows
        self.setWindowFlags(QtCore.Qt.WindowStaysOnBottomHint |
                            QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)

        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.setWindowOpacity(0.5)

        self.Exit_button.clicked.connect(QCoreApplication.instance().quit)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


def main():
    # Новый экземпляр QApplication
    app = QtWidgets.QApplication(sys.argv)
    window = UI()  # Создаём объект класса ExampleApp

    window.show()  # Показываем окно
    # Запускаем цикл обработки событий клавиатуры
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':
    main()
