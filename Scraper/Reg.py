file = open("document.txt")
for line in file :
	line=line.rstrip()
	if line.find("Gaurav")>=0 :
		print ("Present")
