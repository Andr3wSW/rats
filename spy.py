import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    client_socket.sendall(b"Hello, this is a local test message.")
    response = client_socket.recv(1024)
    print(f"Server response: {response.decode('utf-8')}")
