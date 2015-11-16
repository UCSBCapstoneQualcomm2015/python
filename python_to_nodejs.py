import zerorpc
import json
import requests

#url = 'localhost://3000'

class PythonScript(object):
    def hello(self):
        return "What's Gucci!"

    def AuthenticateSelf(self):
    	Self = '{"username": "elgutierrez@umail.ucsb.edu", "password": "password"}'
    	return Self

    def ActivateReaders(self):
    	#Activate the readers
    	#magical code
    	return 0

    def PostNewRFID(self):
    	r = requests.post("localhost://3000/api/RFID",data={'@RFID':1222})
    	return r.reason

    def GetDistance(self,target):
    	#Get distance to target tag
    	#ALAKAZAM!
    	return distanceAlgorithm(target)



s = zerorpc.Server(PythonScript())
s.bind("tcp://0.0.0.0:4242")
s.run()