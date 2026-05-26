import socket
import threading

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(b"Acknowledged")
            except socket.error:
                break
    print(f"[DISCONNECTED] {addr} disconnected.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 65432))
    server.listen()
    print("[LISTENING] Server is waiting for connections...")
    
    while True:
        conn, addr = server.accept()
        # Create a new thread dedicated to handling the specific client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
