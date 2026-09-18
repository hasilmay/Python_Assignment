import socket
def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 65432))

        message = "Hello from Client!"
        client_socket.sendall(message.encode('utf-8'))

        client_socket.close()

    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Is server.py running first?")
    except Exception as e:
        print("Socket error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    start_client()
