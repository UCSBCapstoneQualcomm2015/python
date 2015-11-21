##test

class myClass:
	def __init__(self, val1, val2):
		self.vals = [val1, val2]

	def getVals(self):
		return self.vals



mc1 = myClass(5,2)
mc2 = myClass(1,2)
mc3 = myClass(10, 4)

myList = [mc1,mc2,mc3]


myList.sort( key = lambda x: abs(5-x.getVals()[0]) ,reverse = True )	