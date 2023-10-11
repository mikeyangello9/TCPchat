import socket


host = "192.168.56.1"
port_number = 9090

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port_number))

    exit_message = input("Enter 'exit' to close connection with server: ")

    if exit_message.lower() == "exit":
        break
    
    client_message = input("Enter message: ")
    s.send((client_message).encode('utf-8'))
    message_received = s.recv((1024))

    print(f"message from server: {message_received.decode('utf-8')}")


# send multiple messages in real-time
