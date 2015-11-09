#!/usr/bin/env python


#start with dictionary of ids/distances
def solve(distances): 
	pass
	#snapdragon goes
	#

#tell the snapdragons to send signals: need to pass in list of snapdragons we are using

def shoot_snapDragon(dragonList):
	pass


#grab all the data (shit in the todo section) from snapdragon in a storable format (Look up middleware/LLRP language)
#and hold on to all of it (turn em into class instances and store them in a global list maybe?)
def grab_data(dragonLink):
	pass

#parse the big format on snapdragon and put it into individual tag format and into list
#helper that should be called in grab_data
def parse(rfidReturnData):
	pass

#turn each individual format into a class instance and add to list
#helper called from parse
def storeAsClass(singleTagChunk):
	pass

#find  sqrt(number of ids) closest distances (ran on each snapdragon)
def nClosest(nIds, rfidList):
	pass


#compare each two lists and add common elements to dictionary
def compareLists(list1, list2, rfidDict):
	pass

#return midpoint coordinates using proper weights
def findMidpoint(rfidDict):
	pass

#TODO: CREATE A CLASS STRUCTURE {RFID_TAG: CONTAINS ID, DISTANCE1, DISTANCE2,
#DISTANCE3, DISTANCE4    (WILL EVENTUALLY BE TIME1,TIME2,TIME3,TIME4)}