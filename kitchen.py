#kitchen.py

##############NETWORK CONFIG###############
import csv
import os
allfile = os.listdir()

def Save(data):
	with open('config_kitchen.csv','w',newline='') as file:
		#fw = 'file writer'
		fw = csv.writer(file)
		fw.writerows(data)
		print('Save Done!')


def Read():
	if 'config_kitchen.csv' not in allfile:
		allip = [['kitchen','192.168.0.100',7000],['waiting','192.168.0.100',8000]]
		Save(allip)

	with open('config_kitchen.csv',newline='') as file:
		#fr = 'file reader'
		fr = csv.reader(file)
		data = list(fr)

	return data

readip = Read()
ip_kitchen = readip[0]
ip_waiting = readip[1]

kitchenip = ip_kitchen[1] # '192.168.0.133' #myip
kitchenport = int(ip_kitchen[2]) # 7800 #myport
waitingip = ip_waiting[1] # '192.168.0.133'
waitingport = int(ip_waiting[2]) # 7600

print('IP/PORT (kitchen): ',kitchenip,kitchenport)
print('IP/PORT: (waiting)',waitingip,waitingport)
##############NETWORK CONFIG###############

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import threading

foodlist = {'1001':{'fid':'1001','name':'ไก่ไม่มีกระดูก','price':20},
			'1002':{'fid':'1002','name':'ปลาแซลมอนย่างซีอิ้ว','price':50},
			'1003':{'fid':'1003','name':'ไก่เผ็ด','price':45},
			'1004':{'fid':'1004','name':'ข้าวยำไก่แซ็ป','price':60},
			'1005':{'fid':'1005','name':'มันบด','price':15},
			'1006':{'fid':'1006','name':'ปลากระพงทอด','price':70},
			'1007':{'fid':'1007','name':'ข้าวเปล่า','price':10},
			'1008':{'fid':'1008','name':'น้ำดื่ม','price':7},
			'1009':{'fid':'1009','name':'น้ำส้ม','price':15},
			'1010':{'fid':'1010','name':'น้ำอัดลม','price':25},
			}

GUI = Tk()
GUI.geometry('1000x700')
GUI.title('Kitchen : โปรแกรมในครัว')

FONT = ('Angsana New',15)


def SettingIP(event=None):
	GUI2 = Toplevel()
	GUI2.geometry('500x500')
	GUI2.title('กรุณาตั้งค่า ip ก่อนใช้งาน')

	readip = Read()
	ip_kitchen = readip[0]
	ip_waiting = readip[1]

	########################
	L1 = ttk.Label(GUI2,text='Kitchen IP').pack(pady=10)
	v_kitchenip = StringVar()
	v_kitchenip.set(ip_kitchen[1])
	E1 = ttk.Entry(GUI2,textvariable=v_kitchenip,font=FONT)
	E1.pack(pady=10)

	L2 = ttk.Label(GUI2,text='Kitchen Port').pack(pady=10)
	v_kitchenport = StringVar()
	v_kitchenport.set(ip_kitchen[2])
	E2 = ttk.Entry(GUI2,textvariable=v_kitchenport,font=FONT)
	E2.pack(pady=10)
	########################
	L3 = ttk.Label(GUI2,text='Waiting IP').pack(pady=10)
	v_waitingip = StringVar()
	v_waitingip.set(ip_waiting[1])
	E3 = ttk.Entry(GUI2,textvariable=v_waitingip,font=FONT)
	E3.pack(pady=10)

	L4 = ttk.Label(GUI2,text='Waiting Port').pack(pady=10)
	v_waitingport = StringVar()
	v_waitingport.set(ip_waiting[2])
	E4 = ttk.Entry(GUI2,textvariable=v_waitingport,font=FONT)
	E4.pack(pady=10)
	########################

	def SaveSetting():
		saveip = [['kitchen',v_kitchenip.get(),v_kitchenport.get()],
				  ['waiting',v_waitingip.get(),v_waitingport.get()]]
		Save(saveip)
		
		messagebox.showinfo('บันทึก ip ใหม่','บันทึก ip ใหม่แล้ว!')
		GUI2.withdraw()


	B1 = ttk.Button(GUI2,text='Save',command=SaveSetting)
	B1.pack(ipady=10,ipadx=20)

	GUI2.mainloop()

GUI.bind('<F10>',SettingIP)



F1 = Frame(GUI)
F2 = Frame(GUI)
F3 = Frame(GUI)
F1.place(x=20,y=120)
F2.place(x=220,y=120)
F3.place(x=680,y=120)

################Zone1################
L11 = ttk.Label(F1,text='รายการคิว',font=FONT,foreground='green').pack()

header = ['Food Order No.','Quantity']
hw = [100,70]

table_order = ttk.Treeview(F1,height=25,column=header,show='headings')
table_order.pack()

for hd,w in zip(header,hw):
	table_order.heading(hd,text=hd)
	table_order.column(hd,width=w)

################Zone2################
L21 = ttk.Label(F2,text='รายการอาหาร',font=FONT,foreground='green').pack()


header = ['ID','Food Name','Price','Quantity','Total']
hw = [70,150,70,70,70] # |  ID  |   Foodname   | Price |xxxx

table_food = ttk.Treeview(F2,height=25,column=header,show='headings')
table_food.pack()

for hd,w in zip(header,hw):
	table_food.heading(hd,text=hd)
	table_food.column(hd,width=w)

################Zone3################
L31 = ttk.Label(F3,text='รายการคิวที่เสร็จแล้ว',font=FONT,foreground='green').pack()

header = ['Food Order No.','Quantity']
hw = [100,70]

table_finish = ttk.Treeview(F3,height=25,column=header,show='headings')
table_finish.pack()

for hd,w in zip(header,hw):
	table_finish.heading(hd,text=hd)
	table_finish.column(hd,width=w)

##########Button############
################Zone4################

FB = Frame(GUI)
FB.place(x=50,y=50)

B1 = ttk.Button(FB,text='อาหารเสร็จแล้ว')
B1.grid(row=0,column=0,ipadx=20,ipady=10,padx=10)

B2 = ttk.Button(FB,text='เคลียร์')
B2.grid(row=0,column=1,ipadx=20,ipady=10,padx=10)


###############SERVER##################



def ConverttoTable(data):
	# data =  'k|1001=3,1002=2,1003=2'
	# convert to = ['ID','Food Name','Price','Quantity','Total']
	data = data.split('|')[2]
	#print('Data:',data)
	food = data.split(',')
	#print('Food:',food)
	allfood = []
	for f in food:
		fs = f.split('=')
		fid = fs[0]
		quan = fs[1]
		dt = [fid,
			  foodlist[fid]['name'],
			  foodlist[fid]['price'],
			  quan,
			  int(foodlist[fid]['price']) * int(quan)]
		allfood.append(dt)
	print(allfood)
	return allfood


global food_cooking
food_cooking = {}

global chef_cooking
chef_cooking = []

#chef_cooking = [1001,1002,1003]


def RunServer():
	global chef_cooking
	my_ip = kitchenip #'192.168.1.30'
	port = kitchenport #7000

	while True:
		server = socket.socket()
		server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

		server.bind((my_ip,port))
		server.listen(1)
		print('Waiting for client...')

		client, addr = server.accept()
		print('Connected from: ',str(addr))
		data = client.recv(1024).decode('utf-8') #k-Q1001-1001=3-1002=1-1007
		#print(type(data))

		if data[0] == 'k':
			#table_order.insert('','end',value=[data[2:]])
			ordernum = data.split('|')[1]
			
			food_cooking[ordernum] = ConverttoTable(data) #add result to dictionary

			if len(chef_cooking) == 0:
				#หากไม่มีออร์เดอร์
				
				ThreadSendtoWaiting('wl-'+ordernum)
				v_current.set('#' + ordernum)

				sumquan = []
				for fc in food_cooking[ordernum]:
					table_food.insert('','end',value=fc)
					print('FC: ',fc)
					sumquan.append(int(fc[3]))

				print('ORDER NO.',ordernum,type(ordernum))
				table_order.insert('','end',value=[ordernum,sum(sumquan)])
				chef_cooking.append([ordernum,sum(sumquan)])

			else:
				sumquan = []
				for fc in food_cooking[ordernum]:
					print('FC: ',fc)
					sumquan.append(int(fc[3]))

				chef_cooking.append([ordernum,sum(sumquan)])
				ThreadSendtoWaiting('wl-'+ordernum)
				table_order.insert('','end',value=[ordernum,sum(sumquan)])
		else:
			print('<<<< message is not for kitchen >>>>')

		print('Message from client: ',data)
		client.send('We received your Message.'.encode('utf-8'))
		client.close()
		print('ALL FOOD COOKING: ',food_cooking)



# เชฟกำลังทำอะไรอยู่ให้เช็ค chef_cooking
# มีรายการอาหารอะไรบ้างให้เช็ค food_cooking
def Finish(event=None):
	print('CHEF:',chef_cooking)
	if len(chef_cooking) != 0:
		del food_cooking[chef_cooking[0][0]] #[1001,3]
		table_finish.insert('',0,value=chef_cooking[0]) # chef_cooking[0] = ['1001',3]
		ThreadSendtoWaiting('fl-'+chef_cooking[0][0])
		del chef_cooking[0]
		table_food.delete(*table_food.get_children())
		table_order.delete(*table_order.get_children())
	
		for c in chef_cooking:
			table_order.insert('','end',value=c)

		#insert current food
		if len(chef_cooking) > 0:
			ordernum = chef_cooking[0][0]
			v_current.set('#' + ordernum)
			for fc in food_cooking[ordernum]:
				table_food.insert('','end',value=fc)
		if len(chef_cooking) == 0:
			v_current.set('----ORDER NO.----')

	else:
		v_current.set('----ORDER NO.----')


GUI.bind('<F1>',Finish)

v_current = StringVar()
v_current.set('----ORDER NO.----')
currentorder = ttk.Label(GUI,textvariable=v_current)
currentorder.configure(font=(None,30,'bold'))
currentorder.configure(foreground='green')
currentorder.place(x=400,y=50)



def ShowFood(event=None):
	select = table_order.selection() #เช็คว่าเราดับเบิลคลิกเลือกรายการไหน
	data = table_order.item(select) #ดึงข้อมูลของรายการนั้นมา
	v_current.set('#' + data['values'][0])
	print('DATA:',data)
	table_food.delete(*table_food.get_children())
	for fc in food_cooking[data['values'][0]]:
		table_food.insert('','end',value=fc)


def DeleteFood(event=None):
	print('TEST DELETE')
	select = table_order.selection() #เช็คว่าเราดับเบิลคลิกเลือกรายการไหน
	data = table_order.item(select) #ดึงข้อมูลของรายการนั้นมา
	print('DATA:',data)
	for i,f in enumerate(chef_cooking):
		#f = ['1001',3]
		if f[0] == data['values'][0]:
			del chef_cooking[i]
	table_order.delete(*table_order.get_children())
	ThreadSendtoWaiting('dl-' + data['values'][0])
	try:
		for c in chef_cooking:
			table_order.insert('','end',value=c)

		v_current.set('#' + chef_cooking[0][0])
		
		table_food.delete(*table_food.get_children())
		for fc in food_cooking[chef_cooking[0][0]]:
			table_food.insert('','end',value=fc)
		
	except:
		v_current.set('----ORDER NO.----')
		table_food.delete(*table_food.get_children())


table_order.bind('<Double-1>',ShowFood)
table_order.bind('<Delete>',DeleteFood)


def SendtoWaiting(data):
	serverip = waitingip #'192.168.1.30'
	port = waitingport #7500
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))
	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ', data_server)
	server.close()

def ThreadSendtoWaiting(data):
	task = threading.Thread(target=SendtoWaiting,args=(data,))
	task.start()

def ThreadRunServer():
	task = threading.Thread(target=RunServer)
	task.start()

ThreadRunServer()

GUI.mainloop()