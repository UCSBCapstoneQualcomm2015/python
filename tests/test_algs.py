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
	c = dict()
	with pytest.raises(ValueError) as err:
		compareLists(a,b,c)
	assert err.value.message == 'The two lists have different lengths.'

#error should be raised if multiple of same tag in a list
def test_compare_2(): 
	a = [tag_a, tag_b, tag_c]
	b = [tag_a, tag_a, tag_c]
	c = dict()
	with pytest.raises(ValueError) as err:
		compareLists(a,b,c)
	assert err.value.message == 'n_closest algorithm incorrect: one of the lists repeats a value'

#none of values in lists are the same
def test_compare_3():
	a = [tag_a, tag_b, tag_c]
	b = [tag_d, tag_e, tag_f]
	c = dict()
	compareLists(a,b,c)
	assert c == {}

#simple working test
def test_compare_4():
	a = [tag_a, tag_b, tag_c, tag_d]
	b = [tag_c, tag_b, tag_f, tag_g]
	c = dict()
	compareLists(a,b,c)
	assert c[tag_b] == 1 and c[tag_c] == 1 and len(c) == 2

#simple working test 2
def test_compare_5():
	a = [tag_a, tag_b, tag_c, tag_d, tag_e, tag_f]
	b = [tag_b, tag_d, tag_f, tag_h, tag_i, tag_j]
	c = {tag_a:3, tag_b: 2, tag_d: 4}
	compareLists(a,b,c)
	assert c[tag_a] == 3 and c[tag_b] == 3 and c[tag_d] == 5 and c[tag_f] == 1 and len(c) == 4


##############  N CLOSEST VALUES TESTS  ###################



























