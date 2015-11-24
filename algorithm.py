#!/usr/bin/env python	
import collections
from collections import defaultdict

from rfid_class import *

import copy
from copy import deepcopy

import json
import csv
import sys
RFID_cats = ['EPC','Count','Last Seen Time','Last Seen Date','First Seen Time','First Seen Date', 'Antenna 1 distance', 'Antenna 1 - Last seen time', 'Antenna 1 - First seen time', 'Antenna 2 distance', 'Antenna 2 - Last seen time', 'Antenna 2 - First seen time', 'Antenna 3 distance', 'Antenna 3 - Last seen time', 'Antenna 3 - First seen time', 'Antenna 4 distance', 'Antenna 4 - Last seen time', 'Antenna 4 - First seen time', 'RSSI', 'PC', 'CRC']



#tell the snapdragons to send signals: need to pass in list of snapdragons we are using

def shoot_snapDragon(dragonList):
	pass


#grab all the data (shit in the todo section) from snapdragon in a storable format (Look up middleware/LLRP language)
#and hold on to all of it (turn em into class instances and store them in a global list maybe?)
def grab_data(dragonLink):
	pass

#parse the big format on snapdragon and put it into individual tag format and into list
#helper that should be called in grab_data
def parse(filename):
	# csv_filename = filename[0]
	print "Opening CSV file: ",filename 
	f=open(filename, 'r')
	csv_reader = csv.DictReader(f,RFID_cats)
	data = json.dumps([r for r in csv_reader])
	f.close()
	return data
#turn each individual format into a class instance and add to list
#helper called from parse
def storeAsClass(singleTagChunk):
	data = json.loads(singleTagChunk)
	tags = []
	i = 0
	for tag in data:
		tags.append(Rfid_tag(tag["EPC"]))
		tags[i].initialize(tag["Antenna 1 distance"], tag["Antenna 2 distance"], tag["Antenna 3 distance"], tag["Antenna 4 distance"])
		i = i + 1
	return tags


	#find  sqrt(number of ids) closest distances (ran on each snapdragon)
def nClosest(nSniffers, rfidList, missingID): ##make nSnif = 4 as default 
	


	##assumed: all rfids have locations populated
	##floor of sqrt (number of sniffer) is what should be left
	returnable = int ( len(rfidList) ** (.5) )

	missingDist = missingID.getDistances()
	sniffer_proximity_lists = defaultdict()

	for i in range( 0, nSniffers ): ##each sniffer gets a list of rfid tags
		sniffer_proximity_lists[i] = []
		# sniffer_proximity_lists[i] = deepcopy(rfidList)
		# print sniffer_proximity_lists[i]
		for j, tag in enumerate( rfidList ): ## for each rfid 
			# sniffer_proximity_lists[i].append( tag.getDistances()[i] ) ## get respective tag for each 
			if not tag.getDistances()[i] == -1: 
				sniffer_proximity_lists[i].append( tag ) ## get respective tag for each 	


		## sort the list
	for i, _sniffer_ in enumerate(sniffer_proximity_lists):
		# sniffer_proximity_lists[_sniffer_] = sorted( sniffer_proximity_lists[_sniffer_], key = lambda x: x.getDistances()[i] ,reverse = True )
		sniffer_proximity_lists[_sniffer_].sort( key = lambda x: abs(x.getDistances()[i] - missingDist[i]) ,reverse = False )	
		# del sniffer_proximity_lists[_sniffer_][:returnable] ##truncate past sqrt#sniffers
		del sniffer_proximity_lists[_sniffer_][returnable:] ##truncate past sqrt#sniffers

	return sniffer_proximity_lists


#compare each two lists and add common elements to dictionary
def compareLists(list1, list2):
## NOTE: whatever calls this, must take the returned dictionary and append its changes to the main one.

	if (len(list1) != len(list2)):
		raise ValueError('The two lists have different lengths.')
	matches = defaultdict()

	settit = set() ## for efficient use of "in"
	for rfid in list1:
		settit.add( rfid.getID() )

	for rfid in list2: 
		if rfid.getID() in settit: ## if there is a match
			##add it to the dictionary
			if rfid in matches:
				matches[rfid] += 1
			else:
				matches[rfid] = 1 

	return matches

#return midpoint coordinates using proper weights
def findMidpoint(rfidDict):

	x_avg, y_avg, total_weight = 0, 0, 0
	
	for key in rfidDict: ##key is rfid object, item is weight
		weight = rfidDict[key]
		coordinates = key.get_coordinates()
		
		x_avg += coordinates[0]*weight
		y_avg += coordinates[1]*weight
		total_weight += weight

	x_avg /= total_weight
	y_avg /= total_weight

	return (x_avg,y_avg)



#start with dictionary of ids/distances
def solve(distances): 

	#BLACK BOX: SHOOT SNAPDRAGONS AND ASSUME ALL TAG INFORMATION IS APPENDED INTO A TEXT FILE

	#PUT ALL THE ELEMENTS INTO CLASSES
	tags = storeAsClass(parse("../myCSVfile.txt"))
	nSniffers = 4
	## nClosest call here
	missing_tag = Rfid_tag("5")			###NOTE: WE NEED TO CREATE FUNCTION TO EXTRACT MISSING TAG'S INFORMATION AND DELETE IT FROM LIST###
	missing_tag.initialize("1","4","5","2")
	sniffer_proximity_lists = nClosest(4, tags, missing_tag)
	# below are intermediate steps
	globalDict = defaultdict() 

	for i in range( 0, nSniffers ):
		for j in range( i+1 , nSniffers):
			i_list = sniffer_proximity_lists[i]
			j_list = sniffer_proximity_lists[j]
		
			tempoDict = compareLists(i_list, j_list) ##output dictionary {RFID tag ID: count}

			for key in tempoDict:
				if key in globalDict:
					globalDict[key] += tempoDict[key]
				else:
					globalDict[key] = tempoDict[key]

	foundEm = findMidpoint(globalDict)

	return foundEm
