import socket

#ya_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
add = ("localhost", 3030)

#ya_socket1.connect("localhost", 3030)
j = 1
while (j == 1):
    message1 = input("Введите сообщение: ")
    if (message1 == 'exit'):
        j = 0
    else:
        ya_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ya_socket1.connect(('localhost', 3030))
        ya_socket1.sendall(message1.encode('utf-8'))
        dara = ya_socket1.recv(1024)
        ya_socket1.close()
