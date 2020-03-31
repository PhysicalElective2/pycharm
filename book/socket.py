import socket
host='127.0.0.1'
port = 8080
web=socket.socket()
web.bind((host,port))
web.listen(5)
print("等待连接")
while True:
    conn,addr=web.accept()
    data=conn.recv(1024)
    print(data)
    conn.sendall(b'HTTP/1.1 200 OK\r\n\r\n\Hello')
    conn.close()