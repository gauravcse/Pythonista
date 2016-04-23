import urllib
import re
from BeautifulSoup import BeautifulSoup as BS
serviceUrl="https://en.wikipedia.org/wiki/Robots_exclusion_standard"
#address=raw_input("Enter the Item to be Searched : ")
#mainUrl=serviceUrl+urllib.urlencode({'q':address})
#print mainUrl
url=urllib.urlopen(serviceUrl).read()
soup=BS(url)
#print soup.prettify()
tags=soup('p')
fh=open('Robotic.txt','w')
for tag in tags :
    para=tag.getText()+"\n"
    fh.write(para)
