# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\Change_server.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Change_server(object):
    def setupUi(self, Change_server):
        Change_server.setObjectName("Change_server")
        Change_server.setWindowModality(QtCore.Qt.ApplicationModal)
        Change_server.resize(306, 175)
        Change_server.setMinimumSize(QtCore.QSize(306, 175))
        Change_server.setMaximumSize(QtCore.QSize(306, 175))
        self.pushButton_Ok = QtWidgets.QPushButton(Change_server)
        self.pushButton_Ok.setGeometry(QtCore.QRect(50, 140, 75, 23))
        self.pushButton_Ok.setObjectName("pushButton_Ok")
        self.pushButton_Cancle = QtWidgets.QPushButton(Change_server)
        self.pushButton_Cancle.setGeometry(QtCore.QRect(170, 140, 75, 23))
        self.pushButton_Cancle.setObjectName("pushButton_Cancle")
        self.label_2 = QtWidgets.QLabel(Change_server)
        self.label_2.setGeometry(QtCore.QRect(110, 20, 81, 16))
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Change_server)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 261, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ip = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_ip.setObjectName("label_ip")
        self.horizontalLayout.addWidget(self.label_ip)
        self.lineEdit_ip = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout.addWidget(self.lineEdit_ip)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Change_server)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 261, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_port = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_2.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_2.addWidget(self.lineEdit_port)

        self.retranslateUi(Change_server)
        QtCore.QMetaObject.connectSlotsByName(Change_server)

    def retranslateUi(self, Change_server):
        _translate = QtCore.QCoreApplication.translate
        Change_server.setWindowTitle(_translate("Change_server", "Change server"))
        self.pushButton_Ok.setText(_translate("Change_server", "OK"))
        self.pushButton_Cancle.setText(_translate("Change_server", "Cancle"))
        self.label_2.setText(_translate("Change_server", "Change server"))
        self.label_ip.setText(_translate("Change_server", "ip server    "))
        self.label_port.setText(_translate("Change_server", "port server"))


