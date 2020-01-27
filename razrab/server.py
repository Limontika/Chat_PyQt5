import socket
import threading
import json
import pickle


def init_connection():
    while True:
        conn, addr = sock.accept()
        threading.Thread(target=receving, args=(conn, )).start()


def receving(conn):
    """
    Обработка сообщений, формирование json ответа клиенту.
    input: conn - установленное соединенние
    output: msg - сообщение
    """

    name = conn.recv(2048)
    name_chat = name.decode("utf-8")

    welcome = 'Welcome ' + name_chat
    msg = {"type": "welcome", "data": welcome}
    conn.send(json.dumps(msg).encode())
    welcome_for_all_users = "%s has joined the chat!" % name_chat
    msg = {"type": "welcome", "data": welcome_for_all_users}
    broadcast(json.dumps(msg))
    clients[conn] = name_chat
    clients_list.append(name_chat)
    msg = {"type": "client_online", "data": clients_list}
    broadcast(json.dumps(msg))
    print("отправился список пользователей:", msg)

    while True:
        try:
            while True:
                msg = conn.recv(2048)
                print(msg.decode("utf-8"))
                broadcast(name_chat + ": " + json.dumps(msg))
        except:
            conn.close()
            for i in range(len(clients_list)-1):
                if clients_list[i] == clients[conn]:
                    del clients_list[i]
                    break
            del clients[conn]
            broadcast("%s has left the chat." % name_chat)
            break


def broadcast(msg):
    for sock in clients:
        sock.send(msg.encode())

port = 9091

clients = {}
clients_list = []

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", port))

if __name__ == "__main__":
    sock.listen(5)
    print("[ Server Started ]")
    rT = threading.Thread(target=init_connection)
    rT.start()
    rT.join()
    sock.close()