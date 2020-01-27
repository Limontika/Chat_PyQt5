# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(502, 382)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Chat = QtWidgets.QTextEdit(self.centralwidget)
        self.Chat.setGeometry(QtCore.QRect(130, 30, 371, 301))
        self.Chat.setObjectName("Chat")
        self.Chat.setReadOnly(True)
        self.ClientOnline = QtWidgets.QTextEdit(self.centralwidget)
        self.ClientOnline.setGeometry(QtCore.QRect(0, 30, 131, 331))
        self.ClientOnline.setObjectName("ClientOnline")
        self.InputSend = QtWidgets.QLineEdit(self.centralwidget)
        self.InputSend.setGeometry(QtCore.QRect(130, 330, 271, 31))
        self.InputSend.setObjectName("InputSend")
        self.InputSend.setFocus()
        self.Send = QtWidgets.QPushButton(self.centralwidget)
        self.Send.setGeometry(QtCore.QRect(400, 328, 111, 34))
        self.Send.setObjectName("Send")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 0, 121, 31))
        self.label.setObjectName("label")
        self.Server = QtWidgets.QLabel(self.centralwidget)
        self.Server.setGeometry(QtCore.QRect(10, 0, 111, 31))
        self.Server.setObjectName("Server")
        self.NickName = QtWidgets.QLabel(self.centralwidget)
        self.NickName.setGeometry(QtCore.QRect(400, 1, 91, 31))
        self.NickName.setObjectName("NickName")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 502, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionNew_serwer = QtWidgets.QAction(MainWindow)
        self.actionNew_serwer.setObjectName("actionNew_serwer")
        self.menuFile.addAction(self.actionNew_serwer)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LimontikaChat"))
        self.Send.setText(_translate("MainWindow", "Отправить"))
        self.label.setText(_translate("MainWindow", "Chat by Limontika"))
        self.Server.setText(_translate("MainWindow", "Server:"))
        self.NickName.setText(_translate("MainWindow", "Name: "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionNew_serwer.setText(_translate("MainWindow", "Change server"))

