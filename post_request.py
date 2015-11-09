import httplib2
import urllib
import urllib2
import re

# URL
url = 'http://localhost:3000/rfid_tags'

# Define the information posted
body = {
	'tagId' : 'Phone',
	'readerId' : 'Living Room 4',
	'reference' : 'false',
	'location' : 'Bathroom',
}

headers = {'Content-type': 'application/x-www-form-urlencoded'}

# Make connection with the server
http = httplib2.Http()

# URL encode the information in parameters
http.request(url, 'POST', headers=headers, body=urllib.urlencode(body))
