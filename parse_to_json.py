#EPC, Count, Last seen time, Last seen date, First seen time, First seen date, Antenna 1 count, Antenna 1 - Last seen time, Antenna 1 - First seen time, Antenna 2 count, Antenna 2 - Last seen time, Antenna 2 - First seen time, Antenna 3 count, Antenna 3 - Last seen time, Antenna 3 - First seen time, Antenna 4 count, Antenna 4 - Last seen time, Antenna 4 - First seen time, RSSI, PC, CRC

#305400B8AC023E0000000022, 25, 14:02:50:8681, Apr-22-2013, 14:02:44:5987, Apr-22-2013, 25, 14:02:50:8681, 14:02:44:5987, 0, , , 0, , , 0, , , -69, 3000, 2A0F
import json
import csv
import sys

RFID_cats = ['EPC','Count','Last Seen Time','Last Seen Date','First Seen Time','First Seen Date', 'Antenna 1 distance', 'Antenna 1 - Last seen time', 'Antenna 1 - First seen time', 'Antenna 2 distance', 'Antenna 2 - Last seen time', 'Antenna 2 - First seen time', 'Antenna 3 distance', 'Antenna 3 - Last seen time', 'Antenna 3 - First seen time', 'Antenna 4 distance', 'Antenna 4 - Last seen time', 'Antenna 4 - First seen time', 'RSSI', 'PC', 'CRC']


def convert(filename):
	csv_filename = filename[0]
	print "Opening CSV file: ",csv_filename 
	f=open(csv_filename, 'r')
	csv_reader = csv.DictReader(f,RFID_cats)
	json_filename = csv_filename.split(".")[0]+".json"
	print "Saving JSON to file: ",json_filename
	jsonf = open(json_filename,'w') 
	data = json.dumps([r for r in csv_reader])
	jsonf.write(data) 
	f.close()
	jsonf.close()

if __name__=="__main__":
	convert(sys.argv[1:])




# RFID_cats = ['EPC','Count','Last Seen Time','Last Seen Date','First Seen Time','First Seen Date', 'Antenna 1 count', 'Antenna 1 - Last seen time', 'Antenna 1 - First seen time', 'Antenna 2 count', 'Antenna 2 - Last seen time', 'Antenna 2 - First seen time', 'Antenna 3 count', 'Antenna 3 - Last seen time', 'Antenna 3 - First seen time', 'Antenna 4 count', 'Antenna 4 - Last seen time', 'Antenna 4 - First seen time', 'RSSI', 'PC', 'CRC']
# data_string = "EPC, Count, Last seen time, Last seen date, First seen time, First seen date, Antenna 1 count, Antenna 1 - Last seen time, Antenna 1 - First seen time, Antenna 2 count, Antenna 2 - Last seen time, Antenna 2 - First seen time, Antenna 3 count, Antenna 3 - Last seen time, Antenna 3 - First seen time, Antenna 4 count, Antenna 4 - Last seen time, Antenna 4 - First seen time, RSSI, PC, CRC"
# data_list = data_string.split(',')
# data = dict(zip(json1, mylist))
# json2 = json.dumps(data)