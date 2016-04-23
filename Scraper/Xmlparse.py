import urllib
import re
s=raw_input("Enter the Url : ")
url=urllib.urlopen(s)
numbers=[]
for line in url :
    line=line.rstrip()
    num=re.findall("[0-9]+",line)
    for item in num :
        numbers.append(int(item))
sum=0
for item in numbers :
    sum+=item
print sum
