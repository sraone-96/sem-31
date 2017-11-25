import json
import csv
import sys
filename=sys.argv[1]
data = []
with open(filename) as f:
        for line in f:
                    data.append(json.loads(line))

#print data[1]["helpful"]

f = csv.writer(open("test.csv", "wb+"))
for x in data:
   try:         
        f.writerow([x["helpful"][0],x["helpful"][1],x["reviewText"]])
   except: 
        pass

