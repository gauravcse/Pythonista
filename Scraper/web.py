import urllib
import re
from BeautifulSoup import BeautifulSoup
url = urllib.urlopen("http://python-data.dr-chuck.net/comments_209753.html").read()
soup = BeautifulSoup(url)
tags = soup('span')
print tags
numbers=[]
for line in tags :
    num=re.findall("[0-9]+",str(line))
    for item in num :
        numbers.append(int(item))
sum=0
for item in numbers :
    sum+=item
print sum



