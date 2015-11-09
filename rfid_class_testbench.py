from rfid_class import rfid_tags

myRFIDS = {}

for line in open("rfid_class.tb", "r"):
	if line[0] == "#":
		continue
	if line == "\n":
		continue
	# print line
	params = line.split()

	x = rfid_tags( params[0], params[1], params[2], params[3], params[4], params[5])

	myRFIDS[ x.getID() ] = x


print myRFIDS



