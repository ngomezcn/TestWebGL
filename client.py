# echo-client.py
import time

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 8052  # The port used by the server

time.sleep(3)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")