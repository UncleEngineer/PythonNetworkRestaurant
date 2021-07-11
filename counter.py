#counter.py

##############NETWORK CONFIG###############
import csv
import os
allfile = os.listdir()

def Save(data):
	with open('config_counter.csv','w',newline='') as file:
		#fw = 'file writer'
		fw = csv.writer(file)
		fw.writerows(data)
		print('Save Done!')


def Read():
	if 'config_counter.csv' not in allfile:
		allip = [['kitchen','192.168.0.100',7000]]
		Save(allip)
	with open('config_counter.csv',newline='') as file:
		#fr = 'file reader'
		fr = csv.reader(file)
		data = list(fr)

	return data
#kitchen ip:
readip = Read()
ip_kitchen = readip[0]

kitchenip = ip_kitchen[1] # '192.168.0.133' #myip
kitchenport = int(ip_kitchen[2]) # 7800 #myport
print('IP/PORT: ',kitchenip,kitchenport)
##############NETWORK CONFIG###############

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import socket
import threading


GUI = Tk()
GUI.geometry('1000x700')
GUI.title('Counter : โปรแกรมหน้าร้าน')

FONT = ('Angsana New',15)

###########config ip############

def SettingIP(event=None):

	GUI2 = Toplevel()
	GUI2.geometry('500x300')
	GUI2.title('กรุณาตั้งค่า ip ก่อนใช้งาน')

	readip = Read()
	ip_kitchen = readip[0]

	L1 = ttk.Label(GUI2,text='Kitchen IP').pack(pady=10)
	v_kitchenip = StringVar()
	v_kitchenip.set(ip_kitchen[1])
	E1 = ttk.Entry(GUI2,textvariable=v_kitchenip,font=FONT)
	E1.pack(pady=10)

	L2 = ttk.Label(GUI2,text='Kitchen Port').pack(pady=10)
	v_kitchenport = StringVar()
	v_kitchenport.set(int(ip_kitchen[2]))
	E2 = ttk.Entry(GUI2,textvariable=v_kitchenport,font=FONT)
	E2.pack(pady=10)
	def SaveSetting():
		saveip = [['kitchen',v_kitchenip.get(),v_kitchenport.get()]]
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
F2.place(x=500,y=20)


L11 = ttk.Label(F1,text='เลือกรายการ',font=FONT,foreground='green').pack()

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

global buffer_tablefood
buffer_tablefood = {}

global order_state 
order_state = False

global order_no
order_no = 1000

def InsertFood(fid):
	global buffer_tablefood
	global order_state
	global order_no

	if order_state == False:
		order_no += 1
		v_orderno.set(order_no)
		order_state = True

	if fid not in buffer_tablefood:
		flist = foodlist[fid]
		#print(flist.values())
		flist = list(flist.values()) #['1001','ไก่ไม่มีกระดูก',20]
		print(flist)
		print(type(flist))
		print('---')
		quan = 1
		total = flist[2] * quan
		flist.append(quan)
		flist.append(total)

		buffer_tablefood[fid] = flist
	else:
		flist = buffer_tablefood[fid] #['1001','ไก่ไม่มีกระดูก',20,1,20]
		flist[-2] = flist[-2] + 1 #เพิ่มค่าเข้าไปอีก 1
		flist[-1] = flist[-3] * flist[-2]
		buffer_tablefood[fid] = flist

	print('Current Table: ',buffer_tablefood)
	table_food.delete(*table_food.get_children()) #clear data in table

	for vl in buffer_tablefood.values():
		table_food.insert('','end',value=vl)

	#total
	total = sum([ vl[-1] for vl in buffer_tablefood.values()])
	v_total.set(f'{total:,.2f} บาท')

	#table_food.insert('','end',value=flist)

Ftable = Frame(F1)
Ftable.pack()

rowcount = 0
bcount = 0
for k,v in foodlist.items():
	print('KEY:',k)
	print('VALUE:',v)
	B1 = ttk.Button(Ftable,text=v['name'],width=15)
	B1.configure(command=lambda x=k: InsertFood(x))

	if bcount % 3 == 0:
		rowcount = rowcount + 1 # rowcount += 1
		cl = 0
	elif bcount % 3 == 1:
		cl = 1
	elif bcount % 3 == 2:
		cl = 2
	else:
		pass
	
	B1.grid(row=rowcount,column=cl ,padx=10,pady=10,ipady=10)

	bcount = bcount + 1


# B1 = ttk.Button(F1,text=foodlist['1001']['name'])
# B1.configure(command=lambda x='1001': InsertFood(x))
# B1.pack(ipadx=20,ipady=10,padx=10,pady=10)


L21 = ttk.Label(F2,text='รายการอาหาร',font=FONT,foreground='green').pack()

header = ['ID','Food Name','Price','Quantity','Total']
hw = [70,150,70,70,70] # |  ID  |   Foodname   | Price |xxxx

table_food = ttk.Treeview(F2,height=15,column=header,show='headings')
table_food.pack()

for hd,w in zip(header,hw):
	table_food.heading(hd,text=hd)
	table_food.column(hd,width=w)



### Total
v_total = StringVar() #ตัวแปรที่ใช้สำหรับเก็บยอดรวม
Ltotal = ttk.Label(GUI,text='Total: ',font=('Angsana New',30),foreground='green').place(x=500,y=450)
total = ttk.Label(GUI,textvariable=v_total)
total.configure(font=('Angsana New',30,'bold'))
total.configure(foreground='green')
total.place(x=600,y=450)


v_orderno = StringVar() #ตัวแปรที่ใช้สำหรับเก็บออร์เดอร์
Lorderno = ttk.Label(GUI,text='Order No. ',font=('Angsana New',30),foreground='green').place(x=500,y=400)
orderno = ttk.Label(GUI,textvariable=v_orderno)
orderno.configure(font=('Angsana New',30,'bold'))
orderno.configure(foreground='green')
orderno.place(x=650,y=400)



########Send Data to Server########
def ConverttoNetwork(data):
	text = ''
	for d in data.values():
		text += '{}={},'.format(d[0],d[-2])
	print(text)
	text = text[:-1]
	#print('k|' + text)
	return text

def SendtoKitchen():
	global buffer_tablefood

	data = 'k|' + 'FSX' + v_orderno.get() + '|'

	#clear order no.
	v_orderno.set('-')
	v_total.set('0.00 บาท')
	#clear state
	global order_state
	order_state = False
	#clear data in table

	table_food.delete(*table_food.get_children()) #clear data in treeview

	data = data + ConverttoNetwork(buffer_tablefood)
	print('DATA:',data)

	serverip =  kitchenip #'192.168.1.30'
	port = kitchenport #7000
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	server.connect((serverip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')
	print('Data from Server: ', data_server)
	server.close()

	buffer_tablefood = {}

def ThreadSendtoKitchen():
	task = threading.Thread(target=SendtoKitchen)
	task.start()

########Button########

FB = Frame(GUI)
FB.place(x=650,y=500)

B1 = ttk.Button(FB,text='ทำรายการสำเร็จ',command=ThreadSendtoKitchen)
B1.grid(row=0,column=0,ipadx=20,ipady=10,padx=10)

B2 = ttk.Button(FB,text='เคลียร์')
B2.grid(row=0,column=1,ipadx=20,ipady=10,padx=10)

GUI.mainloop()