from algorithm import *
import pytest

 #pretty empty right now, need to fill it with tests evenutally though
 
########COMPARE LISTS: parameter 2 lists & a dict/ updates the dict
###cases: 1 of lists is blank, different lists, a non-dictionary passed in

 #######COMPARE LISTS TESTS########

 	#lists have different lengths
 	def test_compare_1():
 		a = [3,2,5]
 		b = [2,1,6]
 		c = dict()
 		with pytest.raises(ValueError) as err:
 			compareLists(a,b,c)
 		assert err.value.message == 'The two lists have different lengths.'

 	#a list has repeated values
 	def test_compare_2(): 
 		a = [1,2,4]
 		b = [2, 2, 5]
 		c = dict()
 		with pytest.raises(ValueError) as err:
 			compareLists(a,b,c)
 		assert err.value.message == 'n_closest algorithm incorrect: one of the lists repeats a value'

 	#no similar objects
    def test_compare_3():
        a = [1,32,4]
        b = [2,3,6]
        c = dict()
        compareLists(a,b,c)
        assert c == {}


    #similar objects
    def test_compare_4():
    	a = [1,3,5,2]
    	b = [1,3, 8, 4]
    	c = dict()
    	compareLists(a,b,c)
    	assert c[1] == 1 && c[3] == 1 && len(c) == 2

    #bigger example
    def test_compare_5():
    	a = [1,3,5,2,4,9,23]
    	b = [2,4,5,8,1,9,12]
    	c = {1:3, 4:2, 7: 4}
    	compareLists(a,b,c)
    	assert c[7] == 4 && c[1] == 4 && c[9] == 1 && c[2] == 1 && c[4] == 3 && len(c) == 6









