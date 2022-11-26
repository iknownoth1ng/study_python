from socket import *
from threading import Thread

def talk(conn):
    while True:
        try:
            if data := conn.recv(1024): #* 海象运算符 在表达式中进行变量赋值
                conn.send(data.upper())
            else:
                break
        except ConnectionResetError:
            break
    conn.close()


def server(ip,port):
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind((ip,port))

    server.listen(5)
    while True:
        conn,add=server.accept()
        t=Thread(target=talk,args=(conn,))
        t.start()

    server.close()    


if __name__ == "__main__":
    server('127.0.0.1', 8080)
