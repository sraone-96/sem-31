import csv
import json
x="./Musical_Instruments_5.json"
x = json.loads(x)

f = csv.writer(open("test.csv", "wb+"))
f.writerow(["pk", "model", "codename", "name", "content_type"])
for x in x:
        f.writerow([x["pk"],x["model"],x["fields"]["codename"],x["fields"]["name"],x["fields"]["content_type"]])

