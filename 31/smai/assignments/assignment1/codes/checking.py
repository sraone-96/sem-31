a=['<s> i beg you not to return a verdict that may thrust him back into prison and brand him for ever <\\s>\n','<s> i beg you not to return a verdict that may thrust him back into prison and brand him for ever <\s>']
tempo=""
for bis in a:
	tempo+=bis
text2=[]
print tempo
for values in a:
        text2.extend(tempo.split())

print "done"
print text2

