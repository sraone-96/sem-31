import re
f=open('a','r')
ls=[]
for line in f:
	line=line[0:len(line)-1]
	line=re.sub('[^a-zA-Z\ ]+','',line)
	ls.append(line)
print ls