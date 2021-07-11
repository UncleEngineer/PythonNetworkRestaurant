#server.py
import socket

my_ip = '192.168.1.30'
port = 7000

while True:
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	server.bind((my_ip,port))
	server.listen(1)
	print('Waiting for client...')

	client, addr = server.accept()
	print('Connected from: ',str(addr))
	data = client.recv(1024).decode('utf-8')
	print('Message from client: ',data)
	client.send('We received your Message.'.encode('utf-8'))
	client.close()