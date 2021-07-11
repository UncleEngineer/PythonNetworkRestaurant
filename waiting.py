#waiting.py

##############NETWORK CONFIG###############
import csv
import os
allfile = os.listdir()

def Save(data):
	with open('config_waiting.csv','w',newline='') as file:
		#fw = 'file writer'
		fw = csv.writer(file)
		fw.writerows(data)
		print('Save Done!')


def Read():
	if 'config_waiting.csv' not in allfile:
		allip = [['waiting','192.168.0.100',8000]]
		Save(allip)
	with open('config_waiting.csv',newline='') as file:
		#fr = 'file reader'
		fr = csv.reader(file)
		data = list(fr)

	return data

readip = Read()
ip_waiting = readip[0]

waitingip = ip_waiting[1]
waitingport = int(ip_waiting[2])

print('IP/PORT: ',waitingip,waitingport)
##############NETWORK CONFIG###############

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import threading

GUI = Tk()
GUI.geometry('900x700')
GUI.title('Waiting : โปรแกรมรออาหาร')

FONT = ('Angsana New',15)


def SettingIP(event=None):
	GUI2 = Toplevel()
	GUI2.geometry('500x300')
	GUI2.title('กรุณาตั้งค่า ip ก่อนใช้งาน')

	readip = Read()
	ip_waiting = readip[0]


	########################
	L3 = ttk.Label(GUI2,text='Waiting IP').pack(pady=10)
	v_waitingip = StringVar()
	v_waitingip.set(ip_waiting[1])
	E3 = ttk.Entry(GUI2,textvariable=v_waitingip,font=FONT)
	E3.pack(pady=10)

	L4 = ttk.Label(GUI2,text='Waiting Port').pack(pady=10)
	v_waitingport = StringVar()
	v_waitingport.set(int(ip_waiting[2]))
	E4 = ttk.Entry(GUI2,textvariable=v_waitingport,font=FONT)
	E4.pack(pady=10)
	########################
	def SaveSetting():
		saveip = [['waiting',v_waitingip.get(),v_waitingport.get()]]
		Save(saveip)
		messagebox.showinfo('บันทึก ip ใหม่','บันทึก ip ใหม่แล้ว!')
		GUI2.withdraw()

	B1 = ttk.Button(GUI2,text='Save',command=SaveSetting)
	B1.pack(ipady=10,ipadx=20)

	GUI2.mainloop()

GUI.bind('<F10>',SettingIP)


F1 = Frame(GUI)
F2 = Frame(GUI)

F1.place(x=20,y=20)
F2.place(x=20,y=300)


L11 = ttk.Label(F1,text='รายการคิวที่กำลังทำอาหาร',font=FONT,foreground='red').pack()
v_waiting = StringVar()
v_waiting.set('---------ยังไม่มีรายการ----------')

Waiting = ttk.Label(F1,textvariable=v_waiting, font=('Angsana New',40,'bold'))
Waiting.configure(foreground='red')
Waiting.pack(pady=20)


L21 = ttk.Label(F2,text='รายการคิวที่เสร็จแล้ว',font=FONT,foreground='green').pack()
v_finish = StringVar()
v_finish.set('---------ยังไม่มีรายการ----------')

finish = ttk.Label(F2,textvariable=v_finish, font=('Angsana New',40,'bold'))
finish.configure(foreground='green')
finish.pack(pady=20)




##################SERVER###################
global waiting_list
global finish_list
waiting_list = []
finish_list = []


def RunServer():
	
	my_ip = waitingip # '192.168.1.30'
	port = waitingport # 7500

	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((my_ip,port))
		server.listen(1)
		print('Waiting for client...')

		client, addr = server.accept()
		print('Connected from: ',str(addr))
		data = client.recv(1024).decode('utf-8') #wl-1001 / fl-1001
		#print(type(data))

		if data[:2] == 'wl':
			#table_order.insert('','end',value=[data[2:]])
			ordernum = data.split('-')[1]
			print(ordernum)
			waiting_list.append(ordernum)

			text = ''
			for wl in waiting_list:
				text += wl + ' | '
			v_waiting.set(text)


		elif data[:2] == 'fl':
			ordernum = data.split('-')[1]
			finish_list.append(ordernum)
			waiting_list.remove(ordernum)
			## replace waiting
			text = ''
			for wl in waiting_list:
				text += wl + ' | '
			v_waiting.set(text)
			## replace finishlist
			text = ''
			for fl in list(reversed(finish_list)):
				text += fl + ' | '
			v_finish.set(text)
		elif data[:2] == 'dl':
			ordernum = data.split('-')[1]
			waiting_list.remove(ordernum)
			## replace waiting
			text = ''
			for wl in waiting_list:
				text += wl + ' | '
			v_waiting.set(text)
			## replace finishlist
			
		else:
			print('<<<< message is not for waiting >>>>')

		print('Message from client: ',data)
		client.send('We received your Message.'.encode('utf-8'))
		client.close()


def ThreadRunServer():
	task = threading.Thread(target=RunServer)
	task.start()


ThreadRunServer()






GUI.mainloop()