import socket
import hashlib
import secrets
import json

SERVER_IP = '192.158.1.38'
SERVER_PORT = 5678
USERS_FILENAME = 'users.json'

try:
    with open(USERS_FILENAME, 'r') as f: #read users data from file
        users = json.load(f)
except FileNotFoundError:
    users = {}  #if file does not exist

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((SERVER_IP, SERVER_PORT))
    print('Server is listening')
    s.listen(1)
    conn,addr = s.accept()
    print(f'Connection accepted from :{addr}')
    with conn:
        while True:
            data = conn.recv(1024)
            #print(f"Received data: {data}")
            message_type, username, password = data.decode().split(',')
            #print(message_type, username, password)
            if message_type == '1':
                salt = secrets.token_hex(16)
                salted_pass = password + salt
                hashed_pass = hashlib.sha512(salted_pass.encode()).hexdigest()
                users[username] = {'salt': salt, 'hashed_pass': hashed_pass}
                conn.send(b'You have signed up!')
                
                with open(USERS_FILENAME, 'w') as f:  #save updated users to file

                    json.dump(users, f)
                    
                    
            elif message_type == '2':
                if username in users:
                    salt = users[username]['salt']
                    salted_pass = password + salt
                    hashed_pass = hashlib.sha512(salted_pass.encode()).hexdigest()
                    if hashed_pass == users[username]['hashed_pass']:
                        conn.send(b'You have logged in!')
                    else:
                        conn.send(b'Incorrect password')
                else:
                    conn.send(b'Username not found')
            else:
                break
            break
            
            

# • At the server side when a user tries to sign up:
# 1. Generate the salt for this user using token hex function from secrets library
# in python.
# 2. Append the calculated salt to the plain password sent from the client
# 3. Hash the salted password and store the hash along side with the user name of
# the client and the used salt
# 4. You have to perform hashing using SHA512 function that is implemented
# inside hashlib library in python.



# • At the server side when a user tries to log in:
# 1. Retrieve the salt for this client using the username
# 2. Add the salt to the sent password and then hash the salted password using
# SHA512
# 3. Compare the hash to the stored record for this client and send back to him/her
# whether he/she is authenticated or not.