
##NOTE: python doesnt support private members, 
#       so following convention, any var/func name with leading undersore
#       is to be treated as private.



#######################################
##                                   ##
##          RFID TAG CLASS           ##
##                                   ##
#######################################
class rfid_tags:
	
#######################################
##            constructor            ##
#######################################
	def __init__(self, id, dA, dB, dC, dD, lM):
		self._dist_A = dA
		self._dist_B = dB
		self._dist_C = dC
		self._dist_D = dD
		self._proximity_x = 0
		self._proximity_y = 0
		self._ID = id
		self._lastMoved = lM


#######################################
##             ID getter             ##
#######################################
	def getID(self):
		## [TODO]: write the location algorithm here
		return self._ID

#######################################
##        location algorithm         ##
#######################################
	def locate(self):
		## [TODO]: write the location algorithm here
		pass


##end_class








##Testing it works as expected
# x = rfid_tags(1,2,3,4, '7344245', '0000000')
# print x._dist_A
# print x._dist_B
# print x._dist_C
# print x._dist_D
# print x._proximity_y
# print x._proximity_x
# print x._ID
# print x._lastMoved