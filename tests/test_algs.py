from ..algorithm import *
from ..rfid_class import *
import pytest

tag_a = rfid_tag(1)
tag_b = rfid_tag(2)
tag_c = rfid_tag(3)
tag_d = rfid_tag(4)
tag_e = rfid_tag(5)
tag_f = rfid_tag(6)
tag_g = rfid_tag(7)
tag_h = rfid_tag(8)
tag_i = rfid_tag(9)
tag_j = rfid_tag(10)


##############COMPARE LISTS TESTS###################

#test to see if lists are different lengths
def test_compare_1():
	a = [tag_a, tag_b]
	b = [tag_a, tag_c, tag_b]
	with pytest.raises(ValueError) as err:
		compareLists(a,b)
	assert err.value.message == 'The two lists have different lengths.'

#error should be raised if multiple of same tag in a list
def test_compare_2(): 
	a = [tag_a, tag_b, tag_c]
	b = [tag_a, tag_a, tag_c]
	with pytest.raises(ValueError) as err:
		compareLists(a,b)
	assert err.value.message == 'n_closest algorithm incorrect: one of the lists repeats a value'

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
	c = dict()
	answer = compareLists(a,b)
	assert answer[tag_b] == 1 and answer[tag_c] == 1 and len(answer) == 2

#simple working test 2
def test_compare_5():
	a = [tag_a, tag_b, tag_c, tag_d, tag_e, tag_f]
	b = [tag_b, tag_d, tag_f, tag_h, tag_i, tag_j]
	c = {tag_a:3, tag_b: 2, tag_d: 4}
	answer = compareLists(a,b)
	assert  answer[tag_b] == 1 and answer[tag_d] == 1 and answer[tag_f] == 1 and len(c) == 3

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
	missing = rfid_tag(11)
	missing.initialize(5,5,5,5)
	myList = [tag_a, tag_b, tag_c, tag_d, tag_e, tag_f, tag_g, tag_h, tag_i]
	solutionDict = nClosest(4, myList, missing)
	assert len(solutionDict) == 4 and solutionDict[1] == [tag_d, tag_i, tag_e] and solutionDict[2] == [tag_b,tag_e, tag_f] and solutionDict[3] == [tag_d, tag_g, tag_c] and solutionDict[4] == [tag_f, tag_b, tag_a]
	#dictionary(id: list of objects)

#simple passing test: 4 tags
def test_nClosest_2():
	tag_a.initialize(1,3,9,7)
	tag_b.initialize(2,4,2,6)
	tag_c.initialize(3,9,6,1)
	tag_d.initialize(4,2,5,12)
	missing = rfid_tag(11)
	missing.initialize(5,5,5,5)
	myList = [tag_a, tag_b, tag_c, tag_d]
	answer = nClosest(4, myList, missing)
	assert answer[1] == [tag_c, tag_d] and answer[2] == [tag_b, tag_a] and answer[3] == [tag_d, tag_c] and answer[4] == [tag_b, tag_a]


#should not take in the -1
def test_nClosest_3():
	tag_a.initialize(1,3,9,-1)
	tag_b.initialize(2,4,2,6)
	tag_c.initialize(3,9,6,1)
	tag_d.initialize(4,2,5,12)
	missing = rfid_tag(11)
	missing.initialize(5,5,5,1)
	myList = [tag_a, tag_b, tag_c, tag_d]
	l1, l2, l3, l4 = nClosest(4, myList, missing)
	assert answer[4] == [tag_c, tag_b]



################  PARSE ##################### NEEDS TO TURN TEXT FILE INTO LIST OF JSON: PLAY WITH SAMPLE DATA TO LOOK LIKE WHAT WE WANT



################   STORE AS CLASS ############### GIVEN A CHUNK OF JSON: TURN DATA INTO AN INSTANCE OF A CLASS AND ADD TO GLOBAL LIST


















