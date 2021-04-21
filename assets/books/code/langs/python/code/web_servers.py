# Create a Mini Server

import socket 	# The socket class supports listening for incoming connections.
host = ''
port = 3535
my_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_server.bind((host, port))
my_server.listen(1)

# Now you can accept incoming connections like this:
addr = my_server.accept()
print('Connected ... ', addr)
data = conn.recv(1024)
conn.close()


## Tornado
'''
https://www.tornadoweb.org/en/stable/
Tornado is a Python web framework and asynchronous networking library, originally developed at FriendFeed. By using non-blocking network I/O, Tornado can scale to tens of thousands of open connections, making it ideal for long polling, WebSockets, and other applications that require a long-lived connection to each user.
'''