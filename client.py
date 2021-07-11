#client.py
import socket
serverip = '192.168.1.30'
port = 7500

while True:
	data = input('Send Message: ')
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ', data_server)
	server.close()


def SendtoWaiting(data):
	serverip = '192.168.1.30'
	port = 7500
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))
	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ', data_server)
	server.close()

