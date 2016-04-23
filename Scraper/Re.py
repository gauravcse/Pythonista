import re
file = open("document.txt")
for line in file :
	line=line.rstrip()
	if re.search("^G.rav",line) :
		print("Present")
                

