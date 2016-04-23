import re
def put_num(x) :
	for i in x :
		numbers.append(i);
def sum() :
	s=0
	for num in numbers :
		s=s+int(num)
	return s


fie = open("data.txt")
numbers=[]
for line in fie :
	line=line.rstrip()
	x=re.findall("[0-9]+",line)
	put_num(x)
print (sum())

