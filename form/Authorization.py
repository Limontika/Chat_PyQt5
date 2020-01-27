# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Authorization.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Authorization_2(object):
    def setupUi(self, Authorization_2):
        Authorization_2.setObjectName("Authorization_2")
        Authorization_2.resize(371, 204)
        self.centralwidget = QtWidgets.QWidget(Authorization_2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 160, 271, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Enter.setObjectName("Enter")
        self.horizontalLayout.addWidget(self.Enter)
        self.Registration = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Registration.setObjectName("Registration")
        self.horizontalLayout.addWidget(self.Registration)
        self.Anonym = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Anonym.setObjectName("Anonym")
        self.horizontalLayout.addWidget(self.Anonym)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 341, 31))
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
        self.Authorization = QtWidgets.QLabel(self.centralwidget)
        self.Authorization.setGeometry(QtCore.QRect(150, 20, 71, 31))
        self.Authorization.setObjectName("Authorization")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 341, 31))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Password = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Password.setObjectName("Password")
        self.horizontalLayout_3.addWidget(self.Password)
        self.listWidget_2 = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        Authorization_2.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authorization_2)
        QtCore.QMetaObject.connectSlotsByName(Authorization_2)

    def retranslateUi(self, Authorization_2):
        _translate = QtCore.QCoreApplication.translate
        Authorization_2.setWindowTitle(_translate("Authorization_2", "MainWindow"))
        self.Enter.setText(_translate("Authorization_2", "Enter"))
        self.Registration.setText(_translate("Authorization_2", "Registration"))
        self.Anonym.setText(_translate("Authorization_2", "Anonym"))
        self.UserName.setText(_translate("Authorization_2", "User name"))
        self.Authorization.setText(_translate("Authorization_2", "Authorization"))
        self.Password.setText(_translate("Authorization_2", "Password"))

