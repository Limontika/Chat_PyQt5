import socket
import time
import threading
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QApplication,
                             QGridLayout, QLabel, QTextEdit, QInputDialog,
                             QAction, qApp, QMainWindow)
from PyQt5.QtGui import QIcon


class Chats(QWidget):

    def __init__(self):
        super().__init__()

        self.key = 8194
        self.initUI()
        self.initconnect()
        self.registration()
        # self.msg = msg

    def initUI(self):

        chat = QLabel('Chat')

        self.chatEdit = QTextEdit(self)
        self.chatEdit.setReadOnly(True)

        self.sendEdit = QLineEdit(self)
        self.sendEdit.setPlaceholderText("Сообщение")
        self.sendEdit.returnPressed.connect(self.send)
        self.sendEdit.setFocus()

        self.nameEdit = QLabel(self)

        self.btnSend = QPushButton('Отправить')
        self.btnSend.clicked.connect(self.send)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(chat, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        grid.addWidget(self.chatEdit, 2, 0, 3, 0)

        grid.addWidget(self.sendEdit, 5, 0)
        grid.addWidget(self.btnSend, 5, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('CHAT')
        self.show()

    def initconnect(self):

        # host = socket.gethostbyname(socket.gethostname())
        host = "173.232.224.253"
        server = (host, 9091)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server))

    def registration(self):

        self.alias, ok = QInputDialog.getText(
            self, 'Your NAME', 'Enter your name:')

        if ok and self.alias != '':
            self.nameEdit.setText('Name: ' + self.alias)
            self.nameEdit.adjustSize()
            self.connectuser()
            rT = threading.Thread(target=self.chat)
            rT.start()

    def connectuser(self):
        self.s.send((self.alias).encode("utf-8"))

    def chat(self):
        while True:
            try:
                while True:
                    msg = self.s.recv(2048)
                    decrypt = ""
                    k = False

                    for i in msg.decode("utf-8"):
                        if i == ":":
                            k = True
                            decrypt += i
                        elif k == False or i == " ":
                            decrypt += i
                        else:
                            decrypt += chr(ord(i) ^ self.key)

                    # print(decrypt)
                    self.chatEdit.append(decrypt)

                    time.sleep(0.2)
            except:
                pass

    def disconnectuser(self):
        self.s.send((self.alias).encode("utf-8"))
        self.s.close()

    def send(self):

        message = self.sendEdit.text()

        # Begin
        crypt = ""
        for i in message:
            crypt += chr(ord(i) ^ self.key)
        message = crypt
        # Endmsg

        if message != "":
            self.s.send((message).encode("utf-8"))

        self.sendEdit.setText("")
        self.sendEdit.setFocus()
            


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Chats()
    sys.exit(app.exec_())
