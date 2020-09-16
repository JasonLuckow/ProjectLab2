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
        MainWindow.resize(855, 606)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.carolbtn = QtWidgets.QPushButton(self.centralwidget)
        self.carolbtn.setGeometry(QtCore.QRect(250, 280, 101, 51))
        self.carolbtn.setObjectName("carolbtn")
        self.jinglebtn = QtWidgets.QPushButton(self.centralwidget)
        self.jinglebtn.setGeometry(QtCore.QRect(360, 280, 101, 51))
        self.jinglebtn.setObjectName("jinglebtn")
        self.littlebtn = QtWidgets.QPushButton(self.centralwidget)
        self.littlebtn.setGeometry(QtCore.QRect(470, 280, 101, 51))
        self.littlebtn.setObjectName("littlebtn")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(280, 90, 261, 141))
        self.label1.setAutoFillBackground(True)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 855, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bell Hoppers"))

        self.carolbtn.setText(_translate("MainWindow", "Carol of the Bells"))
        self.carolbtn.clicked.connect(self.carolclicked)

        self.jinglebtn.setText(_translate("MainWindow", "Jingle Bells"))
        self.jinglebtn.clicked.connect(self.jingleclicked)

        self.littlebtn.setText(_translate("MainWindow", "Little Drummer Boy"))
        self.littlebtn.clicked.connect(self.littleclicked)

        self.label1.setText(_translate("MainWindow", "Choose a christmas song to play!"))

    def carolclicked(self):
        print("Carol button was clicked")

    def jingleclicked(self):
        print("Jingle button was clicked")

    def littleclicked(self):
        print("Little button was clicked")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
