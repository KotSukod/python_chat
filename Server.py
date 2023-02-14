import socket

HOST = "localhost"
PORT = 3030

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:

        print(f"Connected by{addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                conn, addr = s.accept()
            conn.sendall(data)
            print(data.decode('utf-8'))  # Выводим информацию на печать.
        conn.close()