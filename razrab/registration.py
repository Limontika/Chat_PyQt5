# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UI\Главные формы\Registration.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(436, 263)
        Dialog.setMinimumSize(QtCore.QSize(436, 263))
        Dialog.setMaximumSize(QtCore.QSize(436, 263))
        font = QtGui.QFont()
        font.setFamily("Buxton Sketch")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 10, 111, 21))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(213, 220, 211, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonOk = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonOk.setObjectName("Ok")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancle = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButtonCancle.setObjectName("pushButtonCancle")
        self.horizontalLayout.addWidget(self.pushButtonCancle)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 401, 39))
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
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(20, 110, 401, 39))
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
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(20, 170, 401, 39))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelPasswd_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.labelPasswd_2.setObjectName("labelPasswd_2")
        self.horizontalLayout_4.addWidget(self.labelPasswd_2)
        self.inputPasswd_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_4)
        self.inputPasswd_2.setObjectName("inputPasswd_2")
        self.horizontalLayout_4.addWidget(self.inputPasswd_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Регистрация"))
        self.pushButtonOk.setText(_translate("Dialog", "Принять"))
        self.pushButtonCancle.setText(_translate("Dialog", "Отменить"))
        self.labelName.setText(_translate("Dialog", "               И мя:              "))
        self.labelPasswd.setText(_translate("Dialog", "             Пароль:          "))
        self.labelPasswd_2.setText(_translate("Dialog", "Повторите пароль:"))


