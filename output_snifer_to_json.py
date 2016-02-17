#puython module popen allows you to launch command as if done from terminal
import json
from subprocess import Popen, PIPE

#inputChar = 'i'     #inventory               [0x31, 0x034, 0x01]
inputChar = 'r'     # inventory RSSI   [0x43, 0x034, 0x01]

process = Popen(['./a.out', inputChar], stdout=PIPE, stderr=PIPE)
stdout, stderr = process.communicate()


hexvals = []
for elem in stdout.split():
	if elem[0] == '0':
		hexvals.append( elem )

the_bits = hexvals.split()

ss = 0
id = ""
snapdragon_name = "snapple"


the_signal_strengths = []
the_i_ds = []

while not len(the_bits) == 0:
	myList = the_bits[:22]
	the_bits = the_bits[22:]

	elem = myList[4]
	q = ( int(elem,0) >> 4 ) * 2
	i = ( int(elem,0) & int("0x0F",0) ) * 2
	q = int(q)**2
	i = int(i)**2	
	if i+q == 0:
		print key, "\t", elem, "\tuh-oh"
		continue
	# raw_input("")
	ss = 10 *log10( (i+q) )

	myList = myList[10:]

	myList = map(str, myList)
	id = id.join(myList)

	the_signal_strengths.append(ss)
	the_i_ds.append(id)




return json.dumps({"ids":the_i_ds, "sig_strength":the_signal_strengths})
