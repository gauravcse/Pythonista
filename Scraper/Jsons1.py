import urllib
import json
import re
import machine_info
url=raw_input("Enter the Url : ")
sum=0
file=urllib.urlopen(url).read()
data=json.loads(file)
new_data=data["comments"]
for i in new_data :
    sum+=int(i["count"])
print sum
    

