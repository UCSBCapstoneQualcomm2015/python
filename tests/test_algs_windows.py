import sys
sys.path.append('C:/Users/Nader/Videos/capstone/algorithm_python/python')
from algorithm import *
from rfid_class import Rfid_tag

tag_a = Rfid_tag(1)
tag_b = Rfid_tag(2)
tag_c = Rfid_tag(3)
tag_d = Rfid_tag(4)
tag_e = Rfid_tag(5)
tag_f = Rfid_tag(6)
tag_g = Rfid_tag(7)
tag_h = Rfid_tag(8)
tag_i = Rfid_tag(9)
tag_j = Rfid_tag(10)
 

##############COMPARE LISTS TESTS###################

#test to see if lists are different lengths
def test_compare_1():
	a = [tag_a, tag_b]
	b = [tag_a, tag_c, tag_b]
	try:
		compareLists(a,b)
	except ValueError:
		print "\n\ncompareLists()_TEST1: PASS :)"
 
test_compare_1()
#error should be raised if multiple of same tag in a list
def test_compare_2(): 
	a = [tag_a, tag_b, tag_c]
	b = [tag_a, tag_a, tag_c]

	zahersDesire = compareLists(a,b)

	print zahersDesire

	for sniffer in zahersDesire:
		print zahersDesire[sniffer]

	# assert err.value.message == 'n_closest algorithm incorrect: one of the lists repeats a value'	
	# print "\n\ncompareLists()_TEST2: PASS :)"
test_compare_2()
#none of values in lists are the same
def test_compare_3():
	a = [tag_a, tag_b, tag_c]
	b = [tag_d, tag_e, tag_f]
	c = dict()
	answer = compareLists(a,b)
	assert answer == {}

#simple working test
def test_compare_4():
	a = [tag_a, tag_b, tag_c, tag_d]
	b = [tag_c, tag_b, tag_f, tag_g]
	answer = compareLists(a,b)
	assert len(answer) == 2
	assert answer[2] == 1 and answer[3] == 1 and len(answer) == 2

#simple working test 2
def test_compare_5():
	a = [tag_a, tag_b, tag_c, tag_d, tag_e, tag_f]
	b = [tag_b, tag_d, tag_f, tag_h, tag_i, tag_j]
	answer = compareLists(a,b)
	assert  answer[2] == 1 and answer[4] == 1 and answer[6] == 1 and len(answer) == 3

########### NEED TO CREATE INTEGRATION TESTS FOR NCLOSEST AND COMPARE #################



##############  N CLOSEST VALUES TESTS  ###################
#find  sqrt(number of ids) closest distances (ran on each snapdragon)

#simple passing test: 9 tags
def test_nClosest_1():
	tag_a.initialize(1,3,9,7)
	tag_b.initialize(2,4,2,6)
	tag_c.initialize(2,9,6,1)
	tag_d.initialize(4,2,5,12)
	tag_e.initialize(3,6,2,1)
	tag_f.initialize(2,4,2,5)
	tag_g.initialize(9,8,5,2)
	tag_h.initialize(1,3,1,9)
	tag_i.initialize(4,2,3,1)
	missing = Rfid_tag(11)
	missing.initialize(5,5,5,5)
	myList = [tag_a, tag_b, tag_c, tag_d, tag_e, tag_f, tag_g, tag_h, tag_i]
	solutionDict = nClosest(4, myList, missing)
	assert len(solutionDict) == 4 
	# assert solutionDict[0] == [tag_d, tag_i, tag_e] 
	assert solutionDict[1] == [tag_b,tag_e, tag_f] 
	assert solutionDict[2] == [tag_d, tag_g, tag_c] 
	assert solutionDict[3] == [tag_f, tag_b, tag_a]
	print "\n\nnClosest_TEST1: PASS :)"
	#dictionary(id: list of objects)

#simple passing test: 4 tags
def test_nClosest_2():
	tag_a.initialize(1,3,9,7)
	tag_b.initialize(2,4,2,6)
	tag_c.initialize(3,9,6,1)
	tag_d.initialize(4,2,5,12)
	missing = Rfid_tag(11)
	missing.initialize(5,5,5,5)
	myList = [tag_a, tag_b, tag_c, tag_d]
	answer = nClosest(4, myList, missing)
	assert answer[0] == [tag_d, tag_c]
	assert answer[1] == [tag_b, tag_a] 
	assert answer[2] == [tag_d, tag_c] 
	assert answer[3] == [tag_b, tag_a]
	print "\n\nnClosest_TEST2: PASS :)"

#should not take in the -1
def test_nClosest_3():
	tag_a.initialize(1,3,9,-1)
	tag_b.initialize(2,4,2,6)
	tag_c.initialize(3,9,6,1)
	tag_d.initialize(4,2,5,12)
	missing = Rfid_tag(11)
	missing.initialize(5,5,5,1)
	myList = [tag_a, tag_b, tag_c, tag_d]
	answer = nClosest(4, myList, missing)
	assert answer[3][1].getID() == 2
	assert answer[3] == [tag_c, tag_b]
	print "\n\nnClosest_TEST3: PASS :)"

test_nClosest_1()
test_nClosest_2()
test_nClosest_3()

################  PARSE ##################### NEEDS TO TURN TEXT FILE INTO LIST OF JSON: PLAY WITH SAMPLE DATA TO LOOK LIKE WHAT WE WANT



################   STORE AS CLASS ############### GIVEN A CHUNK OF JSON: TURN DATA INTO AN INSTANCE OF A CLASS AND ADD TO GLOBAL LIST

