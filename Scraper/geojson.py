import json
import urllib

serviceurl="http://maps.googleapis.com/maps/api/geocode/json?"
address=raw_input("Enter the Address :")
request_address=serviceurl+urllib.urlencode({'sensor':'false','address':address})
print request_address
js=urllib.urlopen(request_address).read()
data=json.loads(str(js))
print json.dumps(data,indent=4)
