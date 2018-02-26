import socket

serversocket = socket.socket(
	socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind((socket.gethostname(), 80))
print socket.SOCK_STREAM
serversocket.listen(5)
serversocket.close()
