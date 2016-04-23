import urllib
from BeautifulSoup import BeautifulSoup
import re
url=raw_input()
number,position=map(int,raw_input().split())
for i in range(0,number) :
    html=urllib.urlopen(url).read()
    soup=BeautifulSoup(html)
    links=soup('a')
    url=links[position-1].get('href',None)
line=links[position-1]
line=str(line)
line=line.rstrip()
name=re.findall('>([A-Za-z]+)<',line)
print name[0]
    


