#puython module popen allows you to launch command as if done from terminal
import json
from subprocess import Popen, PIPE
from math import log10
from collections import OrderedDict
from collections import defaultdict
import collections
import numpy as np
from scipy import stats
import binascii

#inputChar = 'i'     #inventory               [0x31, 0x034, 0x01]
inputChar = 'r'     # inventory RSSI   [0x43, 0x034, 0x01]


# snapdragon_name = "snapple"
x = 0

###########################################################################
##                 FIRST LOOP: run each sniffer 4 times.                 ##
##                             convert raw data, aggregate               ##
###########################################################################

all_ss = defaultdict() ## intermediate representation, ID: [val_1, ... , val_x]
the_final_dict = defaultdict() ##final representation, ID: val_aggregated, converted
num_of_iters = 4

for x in range(0,num_of_iters): # x is iterator
	# all_ss[x] = [] # dictionary key:RFID ID, item: list of signal strenghts
 	
	process = Popen(['./a.out', inputChar], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()

	hexvals = []
	for elem in stdout.split():
		if elem[0] == '0':
			hexvals.append( elem )

	the_bits = hexvals
	theVal = hexvals[3]

	while not len(the_bits) == 0:
		myList = the_bits[:22]
		id = ""
		the_bits = the_bits[22:]
		elem = myList[3]
		q = ( int(elem,0) >> 4 ) * 2
		i = ( int(elem,0) & int("0x0F",0) ) * 2
		q = int(q)**2
		i = int(i)**2	
		if i+q == 0:
			continue
		ss = 10 *log10( (i+q) )

		my_temp_ss = ss

		myList = myList[10:]
		myList = map(str,myList)
		id = id.join(myList)
		id_ir = id.split("0x")
		# id_ascii = binascii.a2b_hex(id_r)
		id = ""
		id = id.join(id_ir)
		id = binascii.a2b_hex(id)
		
		if not id in all_ss:
			all_ss[id] = []
		all_ss[id].append(ss)



###########################################################################
##                 SECOND LOOP: calculating median values and storing    ##
##                                                                       ##
###########################################################################
list_of_ss = all_ss.values() ## gets values from dict
list_of_ids = all_ss.keys()  ## gets keys from dict

# for i in list_of_ss:
# 	if not len(i)== num_of_iters:  ##ensure all list are of same length (-1 is a sentinel)
# 		i.append(-1)


median_val = []

##median val is in // to listofss and listofids
for list in list_of_ss:
	median_val.append(np.median(np.array(list)))

for ident,sigstren in zip(list_of_ids, median_val):
	# print str(ident) + ": " + str(sigstren)
	print json.dumps({"ids": ident, "sig_strength":sigstren})

# for i in median_val:
	# print json.dumps({"ids":the_i_ds[0][0], "sig_strength":i})

# chill = 0
# nlvlchill = -1
# for i in list_of_ss:
# 	chill += 1
# 	# yee = np.array(i)
# 	for j in i:
# 		nlvlchill +=1
# 		# median_val
# 		# yee = np.array(s)
# 		# median_val = np.median(np.array(list_of_ss[]))
# 		# print median_val
# 		print json.dumps({"ids":the_i_ds[chill][nlvlchill], "sig_strength":median_val})