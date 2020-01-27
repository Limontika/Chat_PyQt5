import socket
import threading
import pickle


def init_connection():
    while True:
        conn, addr = sock.accept()
        threading.Thread(target=receving, args=(conn, )).start()


def receving(conn):

    name = conn.recv(2048)
    name_chat = name.decode("utf-8")

    welcome = 'Welcome ' + name_chat
    conn.send(bytes(welcome, "utf8"))
    msg = "%s has joined the chat!" % name_chat
    broadcast(bytes(msg, "utf8"))
    clients[conn] = name_chat
    clients_list.append(name_chat)
    print(clients_list)

    while True:
        try:
            while True:
                msg = conn.recv(2048)
                print(msg.decode("utf-8"))
                broadcast(msg, name_chat + ": ")
        except:
            conn.close()
            for i in range(len(clients_list)-1):
                if clients_list[i] == clients[conn]:
                    del clients_list[i]
                    break
            del clients[conn]
            broadcast(bytes("%s has left the chat." % name_chat, "utf8"))
            break


def broadcast(msg, prefix=""):
    for sock in clients:
        sock.send(bytes(prefix, "utf8") + msg)

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
