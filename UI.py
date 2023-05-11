from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 400)
        font = QtGui.QFont()
        font.setFamily("Skellyman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 500, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.back_label = QtWidgets.QLabel(self.frame)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 500, 400))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.back_label.setFont(font)
        self.back_label.setText("")
        self.back_label.setPixmap(QtGui.QPixmap("back_img.png"))
        self.back_label.setObjectName("back_label")
        self.Exit_button = QtWidgets.QPushButton(self.frame)
        self.Exit_button.setGeometry(QtCore.QRect(450, 10, 40, 40))
        font = QtGui.QFont()
        font.setFamily("Skellyman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Exit_button.setFont(font)
        self.Exit_button.setStyleSheet(
            "background-color: rgba(255, 255, 255, 0);")
        self.Exit_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("exit_img.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Exit_button.setIcon(icon)
        self.Exit_button.setIconSize(QtCore.QSize(25, 25))
        self.Exit_button.setObjectName("Exit_button")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 50, 460, 340))
        self.textEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                    "color: rgb(125,86,71);")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
