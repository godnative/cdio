
import threading
import mysqlconnect
import socket
import signal
import sys




def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    data = sock.recv(1024)
    d = (data.decode('utf-8')).encode('ascii')
    if len(d) == 22 :

        fengsu = int(d[0:4])
        yuliang = int(d[4:8])
        qiya = int(d[8:14])
        wendu = int(d[14:18])
        shidu = int(d[18:20])
        fengxiang = int(d[20:22])
        print(fengsu)
        mysqlconnect.indexsql(wendu, shidu,yuliang,fengsu,qiya,fengxiang)
    sock.close()

def quit(signum, frame):
    print("exit")
    sys.exit()

if __name__ == '__main__':
    try:
        signal.signal(signal.SIGINT, quit)
        signal.signal(signal.SIGTERM, quit)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('0.0.0.0', 6001))
        s.listen(5)
        print('Waiting for connection...')
        while True:
            # 接受一个新连接:
            sock, addr = s.accept()
            # 创建新线程来处理TCP连接:
            t1 = threading.Thread(target=tcplink, args=(sock, addr))
            t1.setDaemon(True)
            t1.start()
    except Exception as c:
        print(c)

