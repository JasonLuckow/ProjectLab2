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
        MainWindow.resize(965, 548)
        MainWindow.setAcceptDrops(False)
        MainWindow.setToolTip("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.jinglebtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jinglebtn.sizePolicy().hasHeightForWidth())
        self.jinglebtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.jinglebtn.setFont(font)
        self.jinglebtn.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.jinglebtn.setObjectName("jinglebtn")
        self.gridLayout.addWidget(self.jinglebtn, 3, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label1.setFont(font)
        self.label1.setAutoFillBackground(False)
        self.label1.setStyleSheet("color: rgb(255, 255, 255);")
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 0, 1, 3)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label2.setFont(font)
        self.label2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 1, 1, 1)
        self.littlebtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.littlebtn.setFont(font)
        self.littlebtn.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.littlebtn.setObjectName("littlebtn")
        self.gridLayout.addWidget(self.littlebtn, 3, 2, 1, 1)
        self.carolbtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carolbtn.sizePolicy().hasHeightForWidth())
        self.carolbtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setKerning(True)
        self.carolbtn.setFont(font)
        self.carolbtn.setStyleSheet("background-color: rgb(0, 85, 0);\n"
"border: 0.5px green;\n"
"color: rgb(255, 255, 255);")
        self.carolbtn.setObjectName("carolbtn")
        self.gridLayout.addWidget(self.carolbtn, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Bell Hoppers"))
        self.jinglebtn.setText(_translate("MainWindow", "Jingle Bells"))
        self.label1.setText(_translate("MainWindow", "Choose a christmas song to play!"))
        self.label2.setText(_translate("MainWindow", "Click button!"))
        self.littlebtn.setText(_translate("MainWindow", "Little Drummer Boy"))
        self.carolbtn.setText(_translate("MainWindow", "Carol of the Bells"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
