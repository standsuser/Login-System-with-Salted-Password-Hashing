import socket

SERVER_IP = '192.158.1.38'
SERVER_PORT = 5678

def send_msg(s, message_type, username, password):
    message = f"{message_type},{username},{password}"
    s.send(message.encode())
    data = s.recv(1024)
    print(data.decode())
    
with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    username = input('Enter username\n')
    password = input('Enter password\n')
    message_type = input('Please enter a number for one of the following: 1.sign up  2.log in\n')
    s.connect((SERVER_IP, SERVER_PORT))
    send_msg(s, message_type, username, password)

input()


# At the client side:
# 1. Ask the user for his/her username and password.
# 2. Ask the user whether he/she is trying to sign up or login
# 3. Send a message to the server that contains the following:
# {Message_Type, Username, Password}

