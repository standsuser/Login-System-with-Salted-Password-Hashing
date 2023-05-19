# Login-System-with-Salted-Password-Hashing

This repository contains a client-server application that allows users to securely sign up and log in to a server. The server stores user credentials using salted and hashed passwords. When a user signs up, the server generates a random salt value using the secrets library and appends it to the plain password sent by the client. The salted password is then hashed using the SHA512 function and stored on the server. When a user logs in, the server authenticates the user by comparing the sent password to the stored record.
