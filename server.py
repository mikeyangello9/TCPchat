import socket

host = "192.168.56.1"
port_number = 9090
 
s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # FA: addressing family, SA: communication protocol
s.bind((host, port_number))

client_list = []


## the above socket is to establish a connection
s.listen(5) # connection limit


## accept connections 
while True:

     
    try:
        communication_socket, address = s.accept()  ## the communication socket is to communicate with the client
        print(f"connected to {address}")
        client_list.append(address)
        print (client_list)
        message = communication_socket.recv((1024))  ## anticipate the clients message 

     
        print(f"message from client is: {message.decode('utf-8')}")


    except (socket.error, ConnectionResetError) as err:
        print(f"{address} disconnected! {err}")

    finally:
        server_reply = input("Enter a reply: ")
        communication_socket.send(server_reply.encode('utf-8'))
        print(f"connection with {address} has been closed!")
        communication_socket.close()
    if not message:
        break
    


        #end while based on key press or something,can already be done on the client side

    



#connect to multiple clients at a time 
## maybe reply in real-time











