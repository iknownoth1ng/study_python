from gevent import spawn,joinall,monkey;monkey.patch_all()
from socket import *


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
        spawn(talk,conn)
    server.close()    


if __name__ == "__main__":
    g=spawn(server,'127.0.0.1', 8080)
    g.join()
