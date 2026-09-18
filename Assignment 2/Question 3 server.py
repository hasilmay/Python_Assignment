import socket

def start_server():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 65432))
        server_socket.listen(1)
        print("Server is listening on port 65432...")

        conn, addr = server_socket.accept()
        print(f"Connected by: {addr}")

        data = conn.rec(1024)
        if data:
            print(f"Received message: {data.decode('utf-8')}")

        conn.close()
        server_socket.close()
    except socket.error as e:
        print(f"Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    start_server()