import socket
import time
import threading
import sys
import mydesign
from PyQt5 import QtWidgets



class ExampleApp(QtWidgets.QMainWindow, mydesign.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.key = 8194
        self.initconnect()
        self.registration()
        self.InputSend.returnPressed.connect(self.send)
        self.Send.clicked.connect(self.send)

    def initconnect(self):

        # self.host = socket.gethostbyname(socket.gethostname())
        self.host = "173.232.224.253"
        server = (self.host, 9092)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server))

    def registration(self):

        self.alias, ok = QtWidgets.QInputDialog.getText(
            self, 'Your NAME', 'Enter your name:')

        if ok and self.alias != '':
            self.NickName.setText('Name: ' + self.alias)
            self.Server.setText('Server: ' + self.host)
            self.ClientOnline.append(self.alias)
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

                    self.Chat.append(decrypt)

                    time.sleep(0.2)
            except:
                pass

    def disconnectuser(self):
        self.s.send((self.alias).encode("utf-8"))
        self.s.close()

    def send(self):

        message = self.InputSend.text()

        # Begin
        crypt = ""
        for i in message:
            crypt += chr(ord(i) ^ self.key)
        message = crypt
        # Endmsg

        if message != "":
            self.s.send((message).encode("utf-8"))

        self.InputSend.setText("")
        self.InputSend.setFocus()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
