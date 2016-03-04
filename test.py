#!/usr/bin/env python	
import collections
from collections import defaultdict
# from rfid_class import *
import json
import csv
from heapq import nsmallest
# import sys

d = defaultdict()
d['1'] = 12
d['2'] = 19
d['3'] = 3.5
d['4'] = 11

ss_to_match = 10
# hit_one = min(d, key=d.get - ss_to_match)
proximity_distance = 12
s = [1,2,3,4,5,6,7]
n = 2
 
for i in s:
	if s[i] != 8
	del s[i]
# print nsmallest(n, d.keys(), key=lambda x: abs(d[x]- proximity_distance)) 
# print  min(d.keys(), key=lambda if x!= '2' x:abs(d[x]-float(ss_to_match)))

# hit_one = min(d.keys(), key=lambda x:abs(d[x]-float(ss_to_match)))
# print d[hit_one]


# RFID_cats = ['EPC','Count','Last Seen Time','Last Seen Date','First Seen Time','First Seen Date', 'Antenna 1 distance', 'Antenna 1 - Last seen time', 'Antenna 1 - First seen time', 'Antenna 2 distance', 'Antenna 2 - Last seen time', 'Antenna 2 - First seen time', 'Antenna 3 distance', 'Antenna 3 - Last seen time', 'Antenna 3 - First seen time', 'Antenna 4 distance', 'Antenna 4 - Last seen time', 'Antenna 4 - First seen time', 'RSSI', 'PC', 'CRC']

# def parse(filename):
# 	# csv_filename = filename[0]
# 	print "Opening CSV file: ",filename 
# 	f=open(filename, 'r')
# 	csv_reader = csv.DictReader(f,RFID_cats)
# 	return json.dumps([r for r in csv_reader])
# 	f.close()

# def storeAsClass(singleTagChunk):
# 	data = json.loads(singleTagChunk)
	
# 	print data[0]['EPC']
# 	print data[0]['Antenna 1 distance']
# 	print data[0]['Antenna 2 distance']
# 	print data[0]['Antenna 3 distance']
# 	print data[0]['Antenna 4 distance']
# 	# print data


# dump = parse("myCSVfile.json")
# storeAsClass(dump)