# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Главные формы\auth.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 213)
        Dialog.setMinimumSize(QtCore.QSize(436, 213))
        Dialog.setMaximumSize(QtCore.QSize(436, 213))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 170, 221, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonEnter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonEnter.setObjectName("Enter")
        self.horizontalLayout.addWidget(self.pushButtonEnter)
        self.pushButtonRegistration = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonRegistration.setObjectName("Registration")
        self.horizontalLayout.addWidget(self.pushButtonRegistration)
        self.Authorization = QtWidgets.QLabel(Dialog)
        self.Authorization.setGeometry(QtCore.QRect(170, 20, 101, 31))
        self.Authorization.setObjectName("Authorization")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 70, 341, 39))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelName = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelName.setObjectName("labelName")
        self.horizontalLayout_2.addWidget(self.labelName)
        self.inputName = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.inputName.setObjectName("inputName")
        self.horizontalLayout_2.addWidget(self.inputName)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 120, 341, 39))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelPasswd = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.labelPasswd.setObjectName("labelPasswd")
        self.horizontalLayout_3.addWidget(self.labelPasswd)
        self.inputPasswd = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.inputPasswd.setObjectName("inputPasswd")
        self.horizontalLayout_3.addWidget(self.inputPasswd)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Окно авторизации"))
        Dialog.setWindowIcon(QtGui.QIcon('logo-02.jpg'))
        self.pushButtonEnter.setText(_translate("Dialog", "Вход"))
        self.pushButtonRegistration.setText(_translate("Dialog", "Регистрация"))
        self.Authorization.setText(_translate("Dialog", "Авторизация"))
        self.labelName.setText(_translate("Dialog", "     Имя:    "))
        self.labelPasswd.setText(_translate("Dialog", "  Пароль:"))


