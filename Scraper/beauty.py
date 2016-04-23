import urllib
from BeautifulSoup import *
string=raw_input("Give me the Url : ")
html=urllib.urlopen(string).read()
soup=BeautifulSoup(html)
tags=soup('a')
for tag in tags :
    print(tag.get('href',None))
