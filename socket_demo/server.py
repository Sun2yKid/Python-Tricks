import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()    # 5 as usual
    conn, addr = s.accept()
    with conn:
        print('Connected by: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print('Received: ', data)
            # print('conn.send', conn.send(data))    # Returns the number of bytes sent.
            print('conn.sendall', conn.sendall(data))    # None is returned on success.
