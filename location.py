import json

fh = open("LocationHistory.json")
data = fh.read()
print 'Retrieved',len(data),'characters'
js = json.loads(data)

location = js["locations"]
tp=[]
for loc in location:
    if "activitys" in loc:
        acti = loc["activitys"]
        for act in acti:
            if "activities" in act:
                types = act["activities"]
                for typ in types:
                    #if typ["confidence"] ==100:
                    tp.append(typ["type"])

#print tp
counts = {}
for i in tp:
    counts[i]=counts.get(i,0)+1
print counts
