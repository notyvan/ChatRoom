from socket import *
server_port = 12000

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(("127.0.0.1", server_port))
server_socket.listen(1)
print("Server listening")

connection_socket, client_address = server_socket.accept()

print("connected")

while True: 
    message = connection_socket.recv(1024)

    if not message: 
        break

    print(f"Client: {message.decode()}")

    connection_socket.sendall(message)
connection_socket.close()
server_socket.close()