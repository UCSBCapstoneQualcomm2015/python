import collections
from collections import OrderedDict
#!/usr/bin/env python


#start with dictionary of ids/distances
def solve(distances): 
	pass
	#snapdragon goes
	#

	## nClosest call here
	# below are intermediate steps: 
	# for i in range( 0, nSniffers ):
	# for j in range( i+1 , nSniffers):
	# 	i_list = sniffer_proximity_lists[i]
	# 	j_list = sniffer_proximity_lists[j]
		
	# 	compareLists(i, j, rd)

	## compareLIsts call here


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
def nClosest(nSniffers, rfidList, missingID): ##make nSnif = 4 as default
	
	##assumed: all rfids have locations populated

	sniffer_proximity_lists = defaultdict()

	for i in range( 0, nSniffers ): ##for each sniffer
		sniffer_proximity_lists[i] = []
		for j, tag in enumerate( rfidList ): ## for each rfid 
			sniffer_proximity_lists[i].append( tag.getDistances()[i] ) ## get respective tag for each 
		## sort the list
	for _sniffer_ in sniffer_proximity_lists:
		sniffer_proximity_lists[_sniffer_] = sorted( sniffer_proximity_lists[_sniffer_], reverse = True )

	return sniffer_proximity_lists



#compare each two lists and add common elements to dictionary
 def compareLists(list1, list2, rfidDict):
## NOTE: whatever calls this, must take the returned dictionary and append its changes to the main one.
## [todo]: ask sohan what rfidDict is for, should it take the place of matches?


	matches = defaultdict()

	settit = set() ## for efficient use of "in"
	for rfid in list1:
		settit.add( rfid.getID() )

	for rfid in list2: 
		if rfid.getID() in settit: ## if there is a match
			##add it to the dictionary
			if rfid.getID() in matches:
				matches[rfid.getID()] += 1
			else:
				matches[rfid.getID()] = 1 

	return matches

#return midpoint coordinates using proper weights
def findMidpoint(rfidDict):
	pass

#TODO: CREATE A CLASS STRUCTURE {RFID_TAG: CONTAINS ID, DISTANCE1, DISTANCE2,
#DISTANCE3, DISTANCE4    (WILL EVENTUALLY BE TIME1,TIME2,TIME3,TIME4)}