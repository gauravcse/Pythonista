import urllib
from BeautifulSoup import BeautifulSoup
main_url='https://google.co.in/#'
query=raw_input("The Query : ")
address=main_url+urllib.urlencode({'q':query})
print address
url=urllib.urlopen(address).read()
soup=BeautifulSoup(url)
tags=soup("div")
for tag in tags :
    print tag

