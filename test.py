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
        MainWindow.resize(762, 545)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 2, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setAutoFillBackground(True)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 1, 0, 1, 3)
        self.jinglebtn = QtWidgets.QPushButton(self.centralwidget)
        self.jinglebtn.setObjectName("jinglebtn")
        self.gridLayout.addWidget(self.jinglebtn, 6, 1, 1, 1)
        self.littlebtn = QtWidgets.QPushButton(self.centralwidget)
        self.littlebtn.setObjectName("littlebtn")
        self.gridLayout.addWidget(self.littlebtn, 6, 2, 1, 1)
        self.carolbtn = QtWidgets.QPushButton(self.centralwidget)
        self.carolbtn.setObjectName("carolbtn")
        self.gridLayout.addWidget(self.carolbtn, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 762, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "The Bell Hoppers"))
        self.label2.setText(_translate("MainWindow", "Click a button!"))
        self.label1.setText(_translate("MainWindow", "Choose a christmas song to play!"))
        self.jinglebtn.setText(_translate("MainWindow", "Jingle Bells"))
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
