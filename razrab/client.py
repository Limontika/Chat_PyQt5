import socket
import time
import threading
import json
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

        self.host = socket.gethostbyname(socket.gethostname())
        # print(self.host)
        # self.host = "185.139.69.158"
        server = (self.host, 9091)

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((server))

    def registration(self):

        self.alias, ok = QtWidgets.QInputDialog.getText(
            self, 'Your NAME', 'Enter your name:')

        if ok and self.alias != '':
            self.NickName.setText('Name: ' + self.alias)
            self.Server.setText('Server: ' + self.host)
            self.connectuser()
            rT = threading.Thread(target=self.chat)
            rT.start()

    def connectuser(self):
        self.s.send((self.alias).encode())

    def chat(self):
        while True:
            message = self.s.recv(2048)
            message = message.decode().split("\n")
            print("1:->", message)
            # print("Список потоков", threading.enumerate()[0])
            # tmp = msg.decode()
            # print("2:->", json.loads(tmp))
            for msg in message:
                if msg:
                    tmp = json.loads(msg)
                    print("3:->", tmp.get("type"))
                    if tmp.get("type") == "welcome":
                        self.Chat.append(tmp.get("data"))
                    if tmp.get("type") == "client_online":
                        for item in tmp.get("data"):
                            self.ClientOnline.clear()
                            self.ClientOnline.append(item)
            # try:
            #     while True:
            #         msg = self.s.recv(2048)
            #         print("1:->",msg.decode())
            #         tmp = msg.decode()
            #         print("2:->", json.loads(tmp))
            #         tmp = json.loads(tmp)
            #         print("3:->", tmp.get("type"))
            #         if tmp.get("type") == "welcome":
            #             self.Chat.append(tmp.get("data"))
            #         if tmp.get("type") == "client_online":
            #             self.ClientOnline.append(msg.decode())
            #
            #         # decrypt = ""
            #         # k = False
            #         #
            #         # for i in msg.decode():
            #         #     if i == ":":
            #         #         k = True
            #         #         decrypt += i
            #         #     elif k == False or i == " ":
            #         #         decrypt += i
            #         #     else:
            #         #         decrypt += chr(ord(i) ^ self.key)
            #
            #
            #
            #         time.sleep(0.2)
            # except:
            #     pass

    def disconnectuser(self):
        self.s.send((self.alias).encode())
        self.s.close()

    def send(self):

        message = self.InputSend.text()

        # Старт шифрования
        # crypt = ""
        # for i in message:
        #     crypt += chr(ord(i) ^ self.key)
        # message = crypt
        # Конец

        if message != "":
            self.s.send((message).encode())

        self.InputSend.setText("")
        self.InputSend.setFocus()

    def closeEvent(self):
        self.disconnectuser()

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
