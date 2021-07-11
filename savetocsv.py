#savetocsv.py
import csv
import os

allfile = os.listdir()

print(allfile)



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

# allip = [['kitchen','192.168.0.133',7000],['waiting','192.168.0.133',8000]]
# Save(allip)

# ipfromcsv = Read()
# print('IP: ',ipfromcsv)
