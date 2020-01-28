import socket
import time
import threading
import json
import sys
import mydesign
import change_server
from PyQt5 import QtWidgets, QtCore


class ChangeForm(QtWidgets.QMainWindow, change_server.Ui_Change_server):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton_Cancle.clicked.connect(self.close)
        self.pushButton_Ok.clicked.connect(self.change_server)

    def change_server(self):
        ExampleApp.host = self.lineEdit_ip.text()
        ExampleApp.port = self.lineEdit_port.text()
        self.close()

class ExampleApp(QtWidgets.QMainWindow, mydesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.key = 8194
        self.action_Connect.triggered.connect(self.initconnect)
        self.action_ChangeServer.triggered.connect(self.changeServer)
        self.InputSend.returnPressed.connect(self.send)
        self.Send.clicked.connect(self.send)

    def initconnect(self):
        global s
        # self.host = socket.gethostbyname(socket.gethostname())
        self.port = 9092
        self.host = "your_addr"
        server = (self.host, self.port)

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server))

        self.registration()

    def registration(self):

        self.alias, ok = QtWidgets.QInputDialog.getText(
            self, 'Your NAME', 'Enter your name:')

        if ok and self.alias != '':
            self.NickName.setText('Name: ' + self.alias)
            self.Server.setText('Server: ' + self.host)
            self.connectuser()
            # создадим поток
            self.thread = QtCore.QThread()
            # создадим объект для выполнения кода в другом потоке
            self.browser_chat = BrowserChat()
            # перенесём объект в другой поток
            self.browser_chat.moveToThread(self.thread)
            # после чего подключим все сигналы и слоты
            self.browser_chat.new_message.connect(self.chat)
            # подключим сигнал старта потока к методу run у объекта, который должен выполнять код в другом потоке
            self.thread.started.connect(self.browser_chat.run)
            # запустим поток
            self.thread.start()

    def connectuser(self):
        s.send((self.alias).encode())

    @QtCore.pyqtSlot(object)
    def chat(self, object):
        for msg in object:
            if msg:
                tmp = json.loads(msg)
                print("3:->", tmp.get("type"))
                if tmp.get("type") == "welcome":
                    self.Chat.append(tmp.get("data"))
                if tmp.get("type") == "client_online":
                    self.ClientOnline.clear()
                    for item in tmp.get("data"):
                        self.ClientOnline.append(item)
                if tmp.get("type") == "message":
                    self.Chat.append(tmp.get("data"))
                if tmp.get("type") == "client_disconect":
                    self.Chat.append(tmp.get("data"))

                    # decrypt = ""
                    # k = False
                    #
                    # for i in msg.decode():
                    #     if i == ":":
                    #         k = True
                    #         decrypt += i
                    #     elif k == False or i == " ":
                    #         decrypt += i
                    #     else:
                    #         decrypt += chr(ord(i) ^ self.key)

    def disconnectuser(self):
        s.send((self.alias).encode())
        s.close()

    def send(self):

        message = self.InputSend.text()

        # Старт шифрования
        # crypt = ""
        # for i in message:
        #     crypt += chr(ord(i) ^ self.key)
        # message = crypt
        # Конец

        if message != "":
            s.send((message).encode())

        self.InputSend.setText("")
        self.InputSend.setFocus()

    def closeEvent(self):
        self.disconnectuser()

    def changeServer(self):
        print("gg")
        self.window = ChangeForm()
        print(self.window.show())



class BrowserChat(QtCore.QObject):
    running = False
    new_message = QtCore.pyqtSignal(object)

    # метод, который будет выполнять алгоритм в другом потоке
    def run(self):
        while True:
            try:
                while True:
                    message = s.recv(2048)
                    message = message.decode().split("\n")
                    print("1:->", message)
                    self.new_message.emit(message)
                    QtCore.QThread.msleep(1000)
            except:
                pass


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec_())  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
