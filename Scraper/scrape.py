import urllib
html=urllib.urlopen("https://raw.githubusercontent.com/venthur/gscholar/master/gscholar/gscholar.py")
file=open('gscholar.py','w+')
file.write(html.read())
file.close()
    
