#convertdict.py



def ConverttoNetwork(data):
	text = ''
	for d in data.values():
		text += '{}={},'.format(d[0],d[-2])
	print(text)
	text = text[:-1]
	print('k|' + text)
	return text

current = {'1001': ['1001', 'ไก่ไม่มีกระดูก', 20, 3, 60],
		   '1002': ['1002', 'ปลาแซลมอนย่างซีอิ้ว', 50, 2, 100],
		   '1003': ['1003', 'ปลา', 50, 2, 100]}

#ConverttoNetwork(current)

###########################

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


print('------convert to table-------')
datafromcounter = 'k|2001|1001=3,1002=2,1003=2'
ConverttoTable(datafromcounter)






