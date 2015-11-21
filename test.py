#!/usr/bin/env python	
# import collections
# from collections import defaultdict
from rfid_class import *
import json
import csv
# import sys


RFID_cats = ['EPC','Count','Last Seen Time','Last Seen Date','First Seen Time','First Seen Date', 'Antenna 1 distance', 'Antenna 1 - Last seen time', 'Antenna 1 - First seen time', 'Antenna 2 distance', 'Antenna 2 - Last seen time', 'Antenna 2 - First seen time', 'Antenna 3 distance', 'Antenna 3 - Last seen time', 'Antenna 3 - First seen time', 'Antenna 4 distance', 'Antenna 4 - Last seen time', 'Antenna 4 - First seen time', 'RSSI', 'PC', 'CRC']

def parse(filename):
	# csv_filename = filename[0]
	print "Opening CSV file: ",filename 
	f=open(filename, 'r')
	csv_reader = csv.DictReader(f,RFID_cats)
	return json.dumps([r for r in csv_reader])
	f.close()

def storeAsClass(singleTagChunk):
	data = json.loads(singleTagChunk)
	
	print data[0]['EPC']
	print data[0]['Antenna 1 distance']
	print data[0]['Antenna 2 distance']
	print data[0]['Antenna 3 distance']
	print data[0]['Antenna 4 distance']
	# print data


dump = parse("myCSVfile.json")
storeAsClass(dump)