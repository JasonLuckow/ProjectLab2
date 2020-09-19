# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMaximumSize(QtCore.QSize(1024, 600))
        font = QtGui.QFont()
        font.setKerning(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 600))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.centralwidget.setObjectName("centralwidget")
        self.littlebtn = QtWidgets.QPushButton(self.centralwidget)
        self.littlebtn.setGeometry(QtCore.QRect(760, 460, 271, 36))
        self.littlebtn.setMaximumSize(QtCore.QSize(301, 16777215))
        font = QtGui.QFont()
        font.setFamily("SantasSleighFull")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.littlebtn.setFont(font)
        self.littlebtn.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.littlebtn.setStyleSheet("background-color: rgb(9, 18, 27);\n"
"font: 20pt \"SantasSleighFull\";\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.littlebtn.setObjectName("littlebtn")
        self.jinglebtn = QtWidgets.QPushButton(self.centralwidget)
        self.jinglebtn.setGeometry(QtCore.QRect(760, 420, 271, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jinglebtn.sizePolicy().hasHeightForWidth())
        self.jinglebtn.setSizePolicy(sizePolicy)
        self.jinglebtn.setMaximumSize(QtCore.QSize(301, 16777215))
        font = QtGui.QFont()
        font.setFamily("SantasSleighFull")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jinglebtn.setFont(font)
        self.jinglebtn.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.jinglebtn.setStyleSheet("background-color: rgb(9, 18, 27);\n"
"font: 20pt \"SantasSleighFull\";\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.jinglebtn.setObjectName("jinglebtn")
        self.carolbtn = QtWidgets.QPushButton(self.centralwidget)
        self.carolbtn.setGeometry(QtCore.QRect(760, 380, 271, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carolbtn.sizePolicy().hasHeightForWidth())
        self.carolbtn.setSizePolicy(sizePolicy)
        self.carolbtn.setMaximumSize(QtCore.QSize(301, 16777215))
        font = QtGui.QFont()
        font.setFamily("SantasSleighFull")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.carolbtn.setFont(font)
        self.carolbtn.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.carolbtn.setMouseTracking(False)
        self.carolbtn.setStyleSheet("background-color: rgb(9, 18, 27);\n"
"font: 20pt \"SantasSleighFull\";\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.carolbtn.setObjectName("carolbtn")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(10, 100, 471, 57))
        font = QtGui.QFont()
        font.setFamily("SantasSleighFull")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 32pt \"SantasSleighFull\";")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(10, 180, 211, 57))
        font = QtGui.QFont()
        font.setFamily("SantasSleighFull")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label2.setFont(font)
        self.label2.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 32pt \"SantasSleighFull\";")
        self.label2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label2.setObjectName("label2")
        self.exitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.exitbtn.setGeometry(QtCore.QRect(0, 560, 91, 36))
        self.exitbtn.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.exitbtn.setStyleSheet("background-color: rgb(9, 18, 27);\n"
"font: 20pt \"SantasSleighFull\";\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.exitbtn.setObjectName("exitbtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Bell Hoppers"))
        self.littlebtn.setText(_translate("MainWindow", "Little Drummer Boy"))
        self.jinglebtn.setText(_translate("MainWindow", "Jingle Bells"))
        self.carolbtn.setText(_translate("MainWindow", "Carol of the Bells"))
        self.label1.setText(_translate("MainWindow", "Choose a christmas song to play!"))
        self.label2.setText(_translate("MainWindow", "Click a button!"))
        self.exitbtn.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
