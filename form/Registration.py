# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Registration.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(383, 230)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 341, 31))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.UserName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.UserName.setObjectName("UserName")
        self.horizontalLayout_2.addWidget(self.UserName)
        self.User_name = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.User_name.setObjectName("User_name")
        self.horizontalLayout_2.addWidget(self.User_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 130, 341, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.UserName_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.UserName_2.setObjectName("UserName_2")
        self.horizontalLayout_3.addWidget(self.UserName_2)
        self.User_name_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.User_name_2.setObjectName("User_name_2")
        self.horizontalLayout_3.addWidget(self.User_name_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 90, 341, 31))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.UserName_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.UserName_3.setObjectName("UserName_3")
        self.horizontalLayout_4.addWidget(self.UserName_3)
        self.User_name_3 = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.User_name_3.setObjectName("User_name_3")
        self.horizontalLayout_4.addWidget(self.User_name_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.Registration = QtWidgets.QLabel(Dialog)
        self.Registration.setGeometry(QtCore.QRect(150, 10, 71, 31))
        self.Registration.setObjectName("Registration")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(200, 190, 160, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Ok = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Ok.setObjectName("Ok")
        self.horizontalLayout.addWidget(self.Ok)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.UserName.setText(_translate("Dialog", "User name"))
        self.UserName_2.setText(_translate("Dialog", "Password"))
        self.UserName_3.setText(_translate("Dialog", "Password"))
        self.Registration.setText(_translate("Dialog", "Registration"))
        self.Ok.setText(_translate("Dialog", "Ok"))
        self.pushButton.setText(_translate("Dialog", "Cancle"))

