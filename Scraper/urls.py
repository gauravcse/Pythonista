import urllib
import re
import BeautifulSoup
fhand=urllib.urlopen("http://www.dr-chuck.com/page1.htm")
link=""
lines=[]
for line in fhand :
    lines.append(line.rstrip().decode('ascii'))
for item in lines :
    new_link=re.findall("http\S+htm",item)
    if(len(new_link)>0) :
        link=new_link[0]
fhand=urllib.urlopen(link)
for line in fhand :
    print(line.rstrip().decode('ascii'))
print_machine_info()
